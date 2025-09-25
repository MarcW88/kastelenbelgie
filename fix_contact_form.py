#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CORRECTION DU FORMULAIRE DE CONTACT
Assure que le formulaire pointe vers ninjas.of.seo@gmail.com
"""

import os
import re
import glob

def fix_contact_form():
    """Corrige le formulaire de contact sur toutes les pages"""
    
    # Vérifier si contact.html existe
    contact_file = "/Users/marc/Desktop/kastelenbelgie/contact.html"
    
    if os.path.exists(contact_file):
        print("📧 CORRECTION DU FORMULAIRE DE CONTACT")
        print("=" * 50)
        
        with open(contact_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Vérifier si l'email est déjà correct
        if 'ninjas.of.seo@gmail.com' in content:
            print("✅ Le formulaire de contact pointe déjà vers ninjas.of.seo@gmail.com")
        else:
            # Corriger l'action du formulaire
            content = re.sub(
                r'action="[^"]*"',
                'action="mailto:ninjas.of.seo@gmail.com"',
                content
            )
            
            # Sauvegarder
            with open(contact_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print("✅ Formulaire de contact corrigé vers ninjas.of.seo@gmail.com")
    
    else:
        print("❌ Fichier contact.html non trouvé")
        
        # Créer une page de contact complète
        contact_html = """<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact | kastelenbelgie.be</title>
    <meta name="description" content="Neem contact op met kastelenbelgie.be voor vragen over Belgische kastelen, bezoeken en meer informatie.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/modern-style.css">
    <link rel="icon" type="image/svg+xml" href="favicon.svg">
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar">
        <div class="container">
            <div class="nav-container">
                <a href="index.html" class="logo">kastelenbelgie</a>
                <div class="nav-menu">
                    <a href="provinces.html" class="nav-link">Kastelen</a>
                    <a href="blog.html" class="nav-link">Blog</a>
                    <a href="contact.html" class="nav-link active">Contact</a>
                    <div class="search-box">
                        <input type="text" placeholder="Zoek kasteel..." class="search-input" id="search-input">
                    </div>
                </div>
            </div>
        </div>
    </nav>

    <!-- Breadcrumbs -->
    <div class="breadcrumbs">
        <div class="container">
            <a href="index.html">Home</a>
            <span>›</span>
            <span>Contact</span>
        </div>
    </div>

    <!-- Hero Section -->
    <section class="contact-hero">
        <div class="container">
            <h1>Contact</h1>
            <p>Heeft u vragen over Belgische kastelen? Neem gerust contact met ons op!</p>
        </div>
    </section>

    <!-- Contact Section -->
    <section class="contact-section">
        <div class="container">
            <div class="contact-grid">
                <!-- Contact Info -->
                <div class="contact-info">
                    <h2>Neem contact op</h2>
                    <p>We helpen u graag met al uw vragen over Belgische kastelen, bezoeken, geschiedenis en meer.</p>
                    
                    <div class="contact-items">
                        <div class="contact-item">
                            <div class="contact-icon">📧</div>
                            <div class="contact-details">
                                <h3>E-mail</h3>
                                <p>ninjas.of.seo@gmail.com</p>
                            </div>
                        </div>
                        
                        <div class="contact-item">
                            <div class="contact-icon">🏰</div>
                            <div class="contact-details">
                                <h3>Kastelen Informatie</h3>
                                <p>Vragen over bezoeken, geschiedenis en praktische info</p>
                            </div>
                        </div>
                        
                        <div class="contact-item">
                            <div class="contact-icon">📱</div>
                            <div class="contact-details">
                                <h3>Sociale Media</h3>
                                <p>Volg ons voor de laatste updates</p>
                            </div>
                        </div>
                        
                        <div class="contact-item">
                            <div class="contact-icon">⏰</div>
                            <div class="contact-details">
                                <h3>Reactietijd</h3>
                                <p>We reageren binnen 24 uur</p>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Contact Form -->
                <div class="contact-form-container">
                    <form class="contact-form" action="mailto:ninjas.of.seo@gmail.com" method="post" enctype="text/plain">
                        <h2>Stuur ons een bericht</h2>
                        
                        <div class="form-row">
                            <div class="form-group">
                                <label for="name">Naam *</label>
                                <input type="text" id="name" name="name" required>
                            </div>
                            <div class="form-group">
                                <label for="email">E-mail *</label>
                                <input type="email" id="email" name="email" required>
                            </div>
                        </div>
                        
                        <div class="form-group">
                            <label for="phone">Telefoon</label>
                            <input type="tel" id="phone" name="phone">
                        </div>
                        
                        <div class="form-group">
                            <label for="subject">Onderwerp</label>
                            <select id="subject" name="subject">
                                <option value="">Selecteer een onderwerp</option>
                                <option value="kasteel-info">Informatie over een kasteel</option>
                                <option value="bezoek-plannen">Bezoek plannen</option>
                                <option value="geschiedenis">Geschiedenis vragen</option>
                                <option value="website">Website feedback</option>
                                <option value="anders">Anders</option>
                            </select>
                        </div>
                        
                        <div class="form-group">
                            <label for="message">Bericht *</label>
                            <textarea id="message" name="message" rows="6" placeholder="Vertel ons hoe we u kunnen helpen..." required></textarea>
                        </div>
                        
                        <button type="submit" class="btn-primary">Verstuur bericht</button>
                        <p class="form-note">* Verplichte velden. Uw gegevens worden vertrouwelijk behandeld.</p>
                    </form>
                </div>
            </div>
        </div>
    </section>

    <!-- FAQ Section -->
    <section class="faq-section">
        <div class="container">
            <h2>Veelgestelde vragen</h2>
            <div class="faq-grid">
                <div class="faq-item">
                    <h3>Kan ik alle kastelen bezoeken?</h3>
                    <p>Niet alle kastelen zijn opengesteld voor het publiek. Controleer altijd de openingsuren en toegankelijkheid voordat u een bezoek plant.</p>
                </div>
                
                <div class="faq-item">
                    <h3>Zijn er rondleidingen beschikbaar?</h3>
                    <p>Veel kastelen bieden gidsen rondleidingen aan. Neem contact op met het kasteel voor meer informatie over beschikbare tours.</p>
                </div>
                
                <div class="faq-item">
                    <h3>Wat zijn de toegangsprijzen?</h3>
                    <p>Toegangsprijzen variëren per kasteel. Bekijk de individuele kasteelpagina's voor actuele prijsinformatie.</p>
                </div>
                
                <div class="faq-item">
                    <h3>Kan ik foto's maken?</h3>
                    <p>Fotografiebeleid verschilt per kasteel. Sommige staan fotografie toe, andere hebben beperkingen. Informeer vooraf.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h3>kastelenbelgie</h3>
                    <p>Ontdek de mooiste kastelen van België</p>
                    <div class="social-links">
                        <a href="#">Facebook</a>
                        <a href="#">Instagram</a>
                        <a href="#">Twitter</a>
                    </div>
                </div>
                <div class="footer-section">
                    <h4>Kastelen</h4>
                    <ul>
                        <li><a href="antwerpen.html">Antwerpen</a></li>
                        <li><a href="limburg.html">Limburg</a></li>
                        <li><a href="oost-vlaanderen.html">Oost-Vlaanderen</a></li>
                        <li><a href="west-vlaanderen.html">West-Vlaanderen</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4>Informatie</h4>
                    <ul>
                        <li><a href="blog.html">Blog</a></li>
                        <li><a href="contact.html">Contact</a></li>
                        <li><a href="privacybeleid.html">Privacy</a></li>
                        <li><a href="algemene-voorwaarden.html">Voorwaarden</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2024 kastelenbelgie.be - Alle rechten voorbehouden</p>
            </div>
        </div>
    </footer>

    <script src="js/search.js"></script>
</body>
</html>"""
        
        with open(contact_file, 'w', encoding='utf-8') as f:
            f.write(contact_html)
        
        print("✅ Page de contact créée avec formulaire vers ninjas.of.seo@gmail.com")

def main():
    """Fonction principale"""
    fix_contact_form()

if __name__ == "__main__":
    main()
