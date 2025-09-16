// Enhanced booking form functionality
class BookingManager {
  constructor() {
    this.init();
  }

  init() {
    this.setupFormHandlers();
    this.setupDateValidation();
    this.setupUserDetection();
  }

  setupFormHandlers() {
    // Find all booking forms on the page
    const bookingForms = document.querySelectorAll('.booking-form');
    
    bookingForms.forEach(form => {
      form.addEventListener('submit', (e) => this.handleFormSubmit(e));
    });
  }

  setupDateValidation() {
    const dateInputs = document.querySelectorAll('input[type="date"]');
    
    dateInputs.forEach(input => {
      // Set minimum date to today
      const today = new Date().toISOString().split('T')[0];
      input.setAttribute('min', today);
      
      // Set maximum date to 1 year from now
      const maxDate = new Date();
      maxDate.setFullYear(maxDate.getFullYear() + 1);
      input.setAttribute('max', maxDate.toISOString().split('T')[0]);
    });
  }

  setupUserDetection() {
    // Check if user is logged in and pre-fill form
    const token = localStorage.getItem('authToken');
    if (token) {
      this.loadUserData(token);
    }
  }

  async loadUserData(token) {
    try {
      const response = await fetch('/api/user/profile', {
        headers: {
          'Authorization': `Bearer ${token}`
        }
      });

      if (response.ok) {
        const userData = await response.json();
        this.prefillUserData(userData);
      }
    } catch (error) {
      console.error('Error loading user data:', error);
    }
  }

  prefillUserData(userData) {
    // Pre-fill name and email fields
    const nameInput = document.querySelector('input[name="name"]');
    const emailInput = document.querySelector('input[name="email"]');
    const phoneInput = document.querySelector('input[name="phone"]');

    if (nameInput && !nameInput.value) {
      nameInput.value = `${userData.firstName} ${userData.lastName}`;
    }
    
    if (emailInput && !emailInput.value) {
      emailInput.value = userData.email;
    }
    
    if (phoneInput && !phoneInput.value && userData.phone) {
      phoneInput.value = userData.phone;
    }
  }

  async handleFormSubmit(e) {
    e.preventDefault();
    
    const form = e.target;
    const formData = new FormData(form);
    const data = Object.fromEntries(formData);
    
    // Add castle information from page
    data.castleName = this.getCastleName();
    data.castleSlug = this.getCastleSlug();
    
    // Add user ID if logged in
    const token = localStorage.getItem('authToken');
    if (token) {
      try {
        const payload = JSON.parse(atob(token.split('.')[1]));
        data.userId = payload.userId;
      } catch (error) {
        console.error('Error parsing token:', error);
      }
    }

    // Show loading state
    const submitButton = form.querySelector('button[type="submit"]');
    const originalText = submitButton.textContent;
    submitButton.textContent = 'Versturen...';
    submitButton.disabled = true;

    try {
      const response = await fetch('/api/reservations', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
      });

      const result = await response.json();

      if (response.ok) {
        this.showSuccess('Reservering succesvol verzonden! We nemen binnen 24 uur contact met u op.');
        form.reset();
        
        // If user is logged in, offer to go to dashboard
        if (token) {
          setTimeout(() => {
            if (confirm('Wilt u naar uw dashboard gaan om de reservering te bekijken?')) {
              window.location.href = 'dashboard.html';
            }
          }, 2000);
        }
      } else {
        this.showError(result.message || 'Er is een fout opgetreden bij het verzenden van uw reservering.');
      }
    } catch (error) {
      this.showError('Er is een netwerkfout opgetreden. Probeer het later opnieuw.');
    } finally {
      // Restore button state
      submitButton.textContent = originalText;
      submitButton.disabled = false;
    }
  }

  getCastleName() {
    // Try to get castle name from page title or heading
    const titleElement = document.querySelector('.detail-title, h1');
    if (titleElement) {
      return titleElement.textContent.trim();
    }
    
    // Fallback to page title
    const pageTitle = document.title;
    return pageTitle.split('|')[0].trim();
  }

  getCastleSlug() {
    // Get slug from current page URL
    const path = window.location.pathname;
    const filename = path.split('/').pop();
    return filename.replace('.html', '');
  }

  showSuccess(message) {
    this.showMessage(message, 'success');
  }

  showError(message) {
    this.showMessage(message, 'error');
  }

  showMessage(message, type) {
    // Remove existing messages
    const existingMessages = document.querySelectorAll('.booking-message');
    existingMessages.forEach(msg => msg.remove());

    // Create message element
    const messageDiv = document.createElement('div');
    messageDiv.className = `booking-message booking-message-${type}`;
    messageDiv.textContent = message;

    // Add styles
    messageDiv.style.cssText = `
      padding: 1rem;
      margin: 1rem 0;
      border-radius: 8px;
      font-weight: 500;
      ${type === 'success' ? 
        'background: #d4edda; color: #155724; border: 1px solid #c3e6cb;' : 
        'background: #f8d7da; color: #721c24; border: 1px solid #f5c6cb;'
      }
    `;

    // Insert message before the form
    const bookingCard = document.querySelector('.booking-card');
    if (bookingCard) {
      bookingCard.insertBefore(messageDiv, bookingCard.firstChild);
    }

    // Auto-remove success messages after 5 seconds
    if (type === 'success') {
      setTimeout(() => {
        messageDiv.remove();
      }, 5000);
    }
  }
}

// Enhanced form validation
class FormValidator {
  constructor(form) {
    this.form = form;
    this.setupValidation();
  }

  setupValidation() {
    const inputs = this.form.querySelectorAll('input, select, textarea');
    
    inputs.forEach(input => {
      input.addEventListener('blur', () => this.validateField(input));
      input.addEventListener('input', () => this.clearFieldError(input));
    });
  }

  validateField(field) {
    const value = field.value.trim();
    let isValid = true;
    let errorMessage = '';

    // Required field validation
    if (field.hasAttribute('required') && !value) {
      isValid = false;
      errorMessage = 'Dit veld is verplicht';
    }

    // Email validation
    if (field.type === 'email' && value) {
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRegex.test(value)) {
        isValid = false;
        errorMessage = 'Voer een geldig e-mailadres in';
      }
    }

    // Phone validation
    if (field.type === 'tel' && value) {
      const phoneRegex = /^[\+]?[0-9\s\-\(\)]{8,}$/;
      if (!phoneRegex.test(value)) {
        isValid = false;
        errorMessage = 'Voer een geldig telefoonnummer in';
      }
    }

    // Date validation
    if (field.type === 'date' && value) {
      const selectedDate = new Date(value);
      const today = new Date();
      today.setHours(0, 0, 0, 0);
      
      if (selectedDate < today) {
        isValid = false;
        errorMessage = 'Selecteer een datum in de toekomst';
      }
    }

    // Show/hide error
    if (!isValid) {
      this.showFieldError(field, errorMessage);
    } else {
      this.clearFieldError(field);
    }

    return isValid;
  }

  showFieldError(field, message) {
    this.clearFieldError(field);
    
    const errorDiv = document.createElement('div');
    errorDiv.className = 'field-error';
    errorDiv.textContent = message;
    errorDiv.style.cssText = `
      color: #e74c3c;
      font-size: 0.8rem;
      margin-top: 0.25rem;
    `;

    field.style.borderColor = '#e74c3c';
    field.parentNode.appendChild(errorDiv);
  }

  clearFieldError(field) {
    const existingError = field.parentNode.querySelector('.field-error');
    if (existingError) {
      existingError.remove();
    }
    field.style.borderColor = '';
  }

  validateForm() {
    const inputs = this.form.querySelectorAll('input, select, textarea');
    let isFormValid = true;

    inputs.forEach(input => {
      if (!this.validateField(input)) {
        isFormValid = false;
      }
    });

    return isFormValid;
  }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  // Initialize booking manager
  new BookingManager();

  // Initialize form validation for all booking forms
  const bookingForms = document.querySelectorAll('.booking-form');
  bookingForms.forEach(form => {
    new FormValidator(form);
  });

  // Add login prompt for non-logged-in users
  const token = localStorage.getItem('authToken');
  if (!token) {
    addLoginPrompt();
  }
});

function addLoginPrompt() {
  const bookingCards = document.querySelectorAll('.booking-card');
  
  bookingCards.forEach(card => {
    const loginPrompt = document.createElement('div');
    loginPrompt.className = 'login-prompt';
    loginPrompt.innerHTML = `
      <div style="background: #e3f2fd; border: 1px solid #2196f3; border-radius: 8px; padding: 1rem; margin-bottom: 1rem;">
        <p style="margin: 0; color: #1976d2;">
          💡 <strong>Tip:</strong> <a href="login.html" style="color: #1976d2;">Log in</a> of 
          <a href="register.html" style="color: #1976d2;">maak een account aan</a> 
          om uw reserveringen te beheren en sneller te boeken!
        </p>
      </div>
    `;
    
    card.insertBefore(loginPrompt, card.firstChild);
  });
}
