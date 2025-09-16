# Kastelen België - Reservatieplatform

Een complete website en reservatieplatform voor de kastelen van België met gebruikersbeheer, reserveringssysteem en admin interface.

## 🏰 Functionaliteiten

### Frontend
- **Homepage** met moderne design en kasteel overzicht
- **Kasteel pagina's** met gedetailleerde informatie en reserveringsformulieren
- **Blog sectie** met artikelen over kastelen
- **Gebruikersauthenticatie** (login/registratie)
- **Dashboard** voor gebruikers om reserveringen te beheren
- **Admin interface** voor beheer van reserveringen
- **Responsive design** voor alle apparaten

### Backend
- **Node.js/Express** API server
- **SQLite** database voor gebruikers en reserveringen
- **JWT authenticatie** voor veilige sessies
- **Email notificaties** voor reserveringsbevestigingen
- **RESTful API** voor alle functionaliteiten

## 🚀 Installatie & Setup

### Vereisten
- Node.js (versie 16 of hoger)
- npm of yarn package manager

### Stap 1: Dependencies installeren
```bash
npm install
```

### Stap 2: Environment configureren
```bash
# Kopieer het voorbeeld bestand
cp .env.example .env

# Bewerk .env met uw configuratie
# - Wijzig JWT_SECRET naar een veilige sleutel
# - Configureer SMTP instellingen voor emails (optioneel)
```

### Stap 3: Database initialiseren
```bash
# De database wordt automatisch aangemaakt bij eerste start
npm start
```

### Stap 4: Server starten
```bash
# Development mode (met auto-restart)
npm run dev

# Production mode
npm start
```

De website is nu beschikbaar op `http://localhost:3000`

## 📁 Project Structuur

```
kastelenbelgie/
├── server.js              # Backend API server
├── package.json           # Dependencies en scripts
├── .env.example           # Environment variabelen voorbeeld
├── kastelenbelgie.db      # SQLite database (wordt automatisch aangemaakt)
│
├── Frontend Pages:
├── index.html             # Homepage
├── login.html             # Inlog pagina
├── register.html          # Registratie pagina
├── dashboard.html         # Gebruiker dashboard
├── admin.html             # Admin interface
├── kasteel-*.html         # Individuele kasteel pagina's
├── blog-*.html            # Blog artikelen
├── privacybeleid.html     # Privacy policy
├── algemene-voorwaarden.html # Terms & conditions
│
├── Assets:
├── css/
│   ├── style.css          # Originele styles
│   └── style-new.css      # Nieuwe homepage styles
├── js/
│   └── booking.js         # Enhanced booking functionality
├── assets/img/            # Algemene afbeeldingen
└── chateaux_images/       # Kasteel foto's
```

## 🔧 API Endpoints

### Authenticatie
- `POST /api/auth/register` - Gebruiker registratie
- `POST /api/auth/login` - Gebruiker login

### Gebruiker
- `GET /api/user/profile` - Gebruikersprofiel ophalen
- `PUT /api/user/profile` - Gebruikersprofiel bijwerken

### Reserveringen
- `POST /api/reservations` - Nieuwe reservering aanmaken
- `GET /api/reservations/user` - Gebruiker reserveringen
- `GET /api/reservations/:id` - Specifieke reservering
- `POST /api/reservations/:id/cancel` - Reservering annuleren

### Admin (vereist admin rechten)
- `GET /api/admin/reservations` - Alle reserveringen
- `PUT /api/admin/reservations/:id/status` - Reservering status wijzigen

### Favorieten
- `POST /api/favorites` - Kasteel aan favorieten toevoegen
- `DELETE /api/favorites/:castleSlug` - Kasteel uit favorieten verwijderen
- `GET /api/favorites` - Gebruiker favorieten

## 👤 Gebruikersrollen

### Bezoekers (niet ingelogd)
- Kastelen bekijken
- Blog lezen
- Reserveringsaanvragen indienen
- Account aanmaken

### Geregistreerde gebruikers
- Alle bezoeker functionaliteiten
- Reserveringen beheren via dashboard
- Profiel bewerken
- Favoriete kastelen opslaan
- Reserveringsgeschiedenis bekijken

### Administrators
- Alle gebruiker functionaliteiten
- Reserveringen beheren en bevestigen
- Gebruikers beheren
- Analytics en rapporten bekijken

## 📧 Email Configuratie

Voor email notificaties, configureer de SMTP instellingen in `.env`:

```env
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASS=your-app-password
```

## 🔒 Beveiliging

- Wachtwoorden worden gehashed met bcrypt
- JWT tokens voor sessie beheer
- Input validatie op frontend en backend
- CORS configuratie voor API beveiliging
- SQL injection preventie met prepared statements

## 🚀 Deployment

### Lokale Development
```bash
npm run dev
```

### Production Deployment
1. Configureer production environment variabelen
2. Build en start de applicatie:
```bash
npm start
```

### Database Backup
```bash
# Backup SQLite database
cp kastelenbelgie.db kastelenbelgie-backup-$(date +%Y%m%d).db
```

## 🛠️ Troubleshooting

### Database Issues
Als de database corrupt raakt, verwijder `kastelenbelgie.db` en herstart de server.

### Email Issues
Controleer SMTP configuratie in `.env` bestand. Gmail vereist app-specific passwords.

### Port Conflicts
Wijzig de PORT variabele in `.env` als poort 3000 al in gebruik is.

## 📝 Changelog

### Versie 1.0.0
- ✅ Complete gebruikersauthenticatie
- ✅ Reserveringssysteem met email bevestigingen
- ✅ Admin dashboard voor reserveringsbeheer
- ✅ Enhanced booking formulieren met validatie
- ✅ Responsive design voor alle pagina's
- ✅ SQLite database met complete schema
- ✅ RESTful API met JWT authenticatie

## 🤝 Support

Voor vragen of problemen, neem contact op via de admin interface of check de console logs voor technische details.