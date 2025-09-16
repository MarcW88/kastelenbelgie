const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const cors = require('cors');
const path = require('path');
const nodemailer = require('nodemailer');

const app = express();
const PORT = process.env.PORT || 3000;
const JWT_SECRET = process.env.JWT_SECRET || 'your-secret-key-change-in-production';

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.static('.'));

// Database setup
const db = new sqlite3.Database('./kastelenbelgie.db');

// Initialize database tables
db.serialize(() => {
  // Users table
  db.run(`
    CREATE TABLE IF NOT EXISTS users (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      firstName TEXT NOT NULL,
      lastName TEXT NOT NULL,
      email TEXT UNIQUE NOT NULL,
      phone TEXT,
      password TEXT NOT NULL,
      newsletter BOOLEAN DEFAULT 0,
      createdAt DATETIME DEFAULT CURRENT_TIMESTAMP,
      updatedAt DATETIME DEFAULT CURRENT_TIMESTAMP
    )
  `);

  // Reservations table
  db.run(`
    CREATE TABLE IF NOT EXISTS reservations (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      userId INTEGER,
      castleName TEXT NOT NULL,
      castleSlug TEXT NOT NULL,
      date DATE NOT NULL,
      time TIME,
      visitors INTEGER NOT NULL,
      visitType TEXT NOT NULL,
      language TEXT NOT NULL,
      name TEXT NOT NULL,
      email TEXT NOT NULL,
      phone TEXT,
      message TEXT,
      status TEXT DEFAULT 'pending',
      createdAt DATETIME DEFAULT CURRENT_TIMESTAMP,
      updatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,
      FOREIGN KEY (userId) REFERENCES users (id)
    )
  `);

  // Favorites table
  db.run(`
    CREATE TABLE IF NOT EXISTS favorites (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      userId INTEGER NOT NULL,
      castleSlug TEXT NOT NULL,
      castleName TEXT NOT NULL,
      createdAt DATETIME DEFAULT CURRENT_TIMESTAMP,
      FOREIGN KEY (userId) REFERENCES users (id),
      UNIQUE(userId, castleSlug)
    )
  `);
});

// Email configuration (configure with your SMTP settings)
const transporter = nodemailer.createTransport({
  host: process.env.SMTP_HOST || 'smtp.gmail.com',
  port: process.env.SMTP_PORT || 587,
  secure: false,
  auth: {
    user: process.env.SMTP_USER,
    pass: process.env.SMTP_PASS
  }
});

// Middleware to verify JWT token
const authenticateToken = (req, res, next) => {
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1];

  if (!token) {
    return res.status(401).json({ message: 'Access token required' });
  }

  jwt.verify(token, JWT_SECRET, (err, user) => {
    if (err) {
      return res.status(403).json({ message: 'Invalid or expired token' });
    }
    req.user = user;
    next();
  });
};

// Auth Routes
app.post('/api/auth/register', async (req, res) => {
  try {
    const { firstName, lastName, email, phone, password, newsletter } = req.body;

    // Check if user already exists
    db.get('SELECT email FROM users WHERE email = ?', [email], async (err, row) => {
      if (err) {
        return res.status(500).json({ message: 'Database error' });
      }
      
      if (row) {
        return res.status(400).json({ message: 'Email already registered' });
      }

      // Hash password
      const hashedPassword = await bcrypt.hash(password, 10);

      // Insert new user
      db.run(
        'INSERT INTO users (firstName, lastName, email, phone, password, newsletter) VALUES (?, ?, ?, ?, ?, ?)',
        [firstName, lastName, email, phone, hashedPassword, newsletter ? 1 : 0],
        function(err) {
          if (err) {
            return res.status(500).json({ message: 'Error creating user' });
          }

          // Send welcome email
          if (process.env.SMTP_USER) {
            const mailOptions = {
              from: process.env.SMTP_USER,
              to: email,
              subject: 'Welkom bij kastelenbelgie.be!',
              html: `
                <h2>Welkom ${firstName}!</h2>
                <p>Bedankt voor het aanmaken van uw account bij kastelenbelgie.be.</p>
                <p>U kunt nu kastelen reserveren en uw bezoeken beheren via uw dashboard.</p>
                <p><a href="${process.env.BASE_URL || 'http://localhost:3000'}/dashboard.html">Ga naar uw dashboard</a></p>
              `
            };
            
            transporter.sendMail(mailOptions).catch(console.error);
          }

          res.status(201).json({ 
            message: 'User created successfully',
            userId: this.lastID 
          });
        }
      );
    });
  } catch (error) {
    res.status(500).json({ message: 'Server error' });
  }
});

app.post('/api/auth/login', (req, res) => {
  const { email, password } = req.body;

  db.get('SELECT * FROM users WHERE email = ?', [email], async (err, user) => {
    if (err) {
      return res.status(500).json({ message: 'Database error' });
    }

    if (!user) {
      return res.status(400).json({ message: 'Invalid credentials' });
    }

    const validPassword = await bcrypt.compare(password, user.password);
    if (!validPassword) {
      return res.status(400).json({ message: 'Invalid credentials' });
    }

    const token = jwt.sign(
      { userId: user.id, email: user.email },
      JWT_SECRET,
      { expiresIn: '24h' }
    );

    res.json({
      token,
      user: {
        id: user.id,
        firstName: user.firstName,
        lastName: user.lastName,
        email: user.email
      }
    });
  });
});

// User Routes
app.get('/api/user/profile', authenticateToken, (req, res) => {
  db.get('SELECT id, firstName, lastName, email, phone, newsletter FROM users WHERE id = ?', 
    [req.user.userId], (err, user) => {
    if (err) {
      return res.status(500).json({ message: 'Database error' });
    }
    
    if (!user) {
      return res.status(404).json({ message: 'User not found' });
    }
    
    res.json(user);
  });
});

app.put('/api/user/profile', authenticateToken, (req, res) => {
  const { firstName, lastName, phone, newsletter } = req.body;
  
  db.run(
    'UPDATE users SET firstName = ?, lastName = ?, phone = ?, newsletter = ?, updatedAt = CURRENT_TIMESTAMP WHERE id = ?',
    [firstName, lastName, phone, newsletter ? 1 : 0, req.user.userId],
    function(err) {
      if (err) {
        return res.status(500).json({ message: 'Error updating profile' });
      }
      
      res.json({ message: 'Profile updated successfully' });
    }
  );
});

// Reservation Routes
app.post('/api/reservations', (req, res) => {
  const {
    castleName, castleSlug, date, time, visitors, visitType, language,
    name, email, phone, message, userId
  } = req.body;

  db.run(`
    INSERT INTO reservations 
    (userId, castleName, castleSlug, date, time, visitors, visitType, language, name, email, phone, message)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
  `, [userId, castleName, castleSlug, date, time, visitors, visitType, language, name, email, phone, message],
  function(err) {
    if (err) {
      return res.status(500).json({ message: 'Error creating reservation' });
    }

    // Send confirmation email
    if (process.env.SMTP_USER) {
      const mailOptions = {
        from: process.env.SMTP_USER,
        to: email,
        subject: `Reservering bevestiging - ${castleName}`,
        html: `
          <h2>Reservering ontvangen</h2>
          <p>Beste ${name},</p>
          <p>We hebben uw reservering voor <strong>${castleName}</strong> ontvangen.</p>
          <h3>Details:</h3>
          <ul>
            <li><strong>Datum:</strong> ${date}</li>
            <li><strong>Tijd:</strong> ${time || 'Hele dag'}</li>
            <li><strong>Aantal bezoekers:</strong> ${visitors}</li>
            <li><strong>Type bezoek:</strong> ${visitType}</li>
            <li><strong>Taal:</strong> ${language}</li>
          </ul>
          <p>We nemen binnen 24 uur contact met u op voor bevestiging.</p>
          <p>Reserveringsnummer: #${this.lastID}</p>
        `
      };
      
      transporter.sendMail(mailOptions).catch(console.error);
    }

    res.status(201).json({ 
      message: 'Reservation created successfully',
      reservationId: this.lastID 
    });
  });
});

app.get('/api/reservations/user', authenticateToken, (req, res) => {
  db.all(
    'SELECT * FROM reservations WHERE userId = ? ORDER BY date DESC',
    [req.user.userId],
    (err, reservations) => {
      if (err) {
        return res.status(500).json({ message: 'Database error' });
      }
      
      res.json(reservations);
    }
  );
});

app.get('/api/reservations/:id', authenticateToken, (req, res) => {
  db.get(
    'SELECT * FROM reservations WHERE id = ? AND userId = ?',
    [req.params.id, req.user.userId],
    (err, reservation) => {
      if (err) {
        return res.status(500).json({ message: 'Database error' });
      }
      
      if (!reservation) {
        return res.status(404).json({ message: 'Reservation not found' });
      }
      
      res.json(reservation);
    }
  );
});

app.post('/api/reservations/:id/cancel', authenticateToken, (req, res) => {
  db.run(
    'UPDATE reservations SET status = ?, updatedAt = CURRENT_TIMESTAMP WHERE id = ? AND userId = ?',
    ['cancelled', req.params.id, req.user.userId],
    function(err) {
      if (err) {
        return res.status(500).json({ message: 'Error cancelling reservation' });
      }
      
      if (this.changes === 0) {
        return res.status(404).json({ message: 'Reservation not found' });
      }
      
      res.json({ message: 'Reservation cancelled successfully' });
    }
  );
});

// Admin Routes (basic implementation)
app.get('/api/admin/reservations', authenticateToken, (req, res) => {
  // In production, add admin role check
  db.all(
    'SELECT r.*, u.firstName, u.lastName FROM reservations r LEFT JOIN users u ON r.userId = u.id ORDER BY r.createdAt DESC',
    (err, reservations) => {
      if (err) {
        return res.status(500).json({ message: 'Database error' });
      }
      
      res.json(reservations);
    }
  );
});

app.put('/api/admin/reservations/:id/status', authenticateToken, (req, res) => {
  const { status } = req.body;
  
  db.run(
    'UPDATE reservations SET status = ?, updatedAt = CURRENT_TIMESTAMP WHERE id = ?',
    [status, req.params.id],
    function(err) {
      if (err) {
        return res.status(500).json({ message: 'Error updating reservation' });
      }
      
      res.json({ message: 'Reservation status updated successfully' });
    }
  );
});

// Favorites Routes
app.post('/api/favorites', authenticateToken, (req, res) => {
  const { castleSlug, castleName } = req.body;
  
  db.run(
    'INSERT OR IGNORE INTO favorites (userId, castleSlug, castleName) VALUES (?, ?, ?)',
    [req.user.userId, castleSlug, castleName],
    function(err) {
      if (err) {
        return res.status(500).json({ message: 'Error adding favorite' });
      }
      
      res.json({ message: 'Added to favorites' });
    }
  );
});

app.delete('/api/favorites/:castleSlug', authenticateToken, (req, res) => {
  db.run(
    'DELETE FROM favorites WHERE userId = ? AND castleSlug = ?',
    [req.user.userId, req.params.castleSlug],
    function(err) {
      if (err) {
        return res.status(500).json({ message: 'Error removing favorite' });
      }
      
      res.json({ message: 'Removed from favorites' });
    }
  );
});

app.get('/api/favorites', authenticateToken, (req, res) => {
  db.all(
    'SELECT * FROM favorites WHERE userId = ? ORDER BY createdAt DESC',
    [req.user.userId],
    (err, favorites) => {
      if (err) {
        return res.status(500).json({ message: 'Database error' });
      }
      
      res.json(favorites);
    }
  );
});

// Serve static files
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ message: 'Something went wrong!' });
});

// Start server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
  console.log(`Visit http://localhost:${PORT} to view your site`);
});

module.exports = app;
