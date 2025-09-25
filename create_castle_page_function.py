#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
FONCTION DE CRÉATION DE PAGE CHÂTEAU
"""

from urllib.parse import quote
from castle_activities_data import get_activities_for_province

def create_castle_page_from_csv_row(row, search_wikipedia_func, get_wikipedia_content_func, generate_rich_content_func, get_filename_from_url_func):
    """Crée une page château à partir d'une ligne CSV"""
    import time
    
    # Extraire les données
    title = row.get('Title', '')
    url = row.get('URL', '')
    province = row.get('Provincie', '')
    address = row.get('FORMATTED_ADDRESS', '')
    opening_hours = row.get('OPENING_HOURS_TEXT', '')
    can_visit = row.get('CAN_VISIT', '').lower() == 'yes'
    
    filename = get_filename_from_url_func(url)
    
    print(f"Création de la page: {filename}.html pour {title}")
    
    # Rechercher sur Wikipedia
    wiki_title, wiki_lang = search_wikipedia_func(title, province)
    wiki_content = None
    
    if wiki_title:
        print(f"  Trouvé sur Wikipedia ({wiki_lang}): {wiki_title}")
        wiki_content = get_wikipedia_content_func(wiki_title, wiki_lang)
        time.sleep(2)  # Respecter les limites de l'API
    else:
        print(f"  Pas trouvé sur Wikipedia, utilisation contenu par défaut")
    
    # Générer le contenu
    paragraphs = generate_rich_content_func(title, province, wiki_content)
    
    # Vérifier la longueur totale
    total_words = sum(len(p.split()) for p in paragraphs)
    print(f"  Contenu généré: {total_words} mots")
    
    # Déterminer si on a besoin d'un formulaire de réservation
    has_opening_hours = bool(opening_hours and opening_hours.strip() and opening_hours != "Info volgt")
    
    # Obtenir les activités pour cette province
    activities = get_activities_for_province(province)
    
    # Template de la page complète
    html_content = f"""<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | kastelenbelgie.be</title>
    <meta name="description" content="Bezoek {title} in {province}. Ontdek de geschiedenis, openingsuren en praktische informatie voor je bezoek aan dit prachtige kasteel.">
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
                <a href="index.html" class="logo">
                    <img src="assets/castle-icon.svg" alt="Kasteel icoon" style="width: 24px; height: 24px; margin-right: 0.5rem; vertical-align: middle;">
                    kastelenbelgie
                </a>
                <div class="nav-menu">
                    <a href="provinces.html" class="nav-link">Kastelen</a>
                    <a href="blog.html" class="nav-link">Blog</a>
                    <a href="contact.html" class="nav-link">Contact</a>
                    <div class="search-box">
                        <input type="text" placeholder="Zoek kasteel..." class="search-input" id="search-input">
                        <div class="search-results" id="search-results"></div>
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
            <a href="provinces.html">Kastelen</a>
            <span>›</span>
            <a href="{province.lower().replace(' ', '-').replace('ë', 'e')}.html">{province}</a>
            <span>›</span>
            <span>{title}</span>
        </div>
    </div>

    <!-- Section 1: Hero avec image et info box -->
    <section class="castle-hero">
        <div class="container">
            <div class="castle-hero-content">
                <div class="castle-image">
                    <div class="image-placeholder">
                        <h2>📸 {title}</h2>
                        <p>Afbeelding wordt binnenkort toegevoegd</p>
                    </div>
                </div>
                <div class="castle-info-box">
                    <h1>{title}</h1>
                    <div class="castle-details">
                        <div class="detail-item">
                            <strong>Provincie:</strong> 
                            <span class="meta-value">{province}</span>
                        </div>
                        {f'<div class="detail-item"><strong>Adres:</strong> <span class="meta-value">{address}</span></div>' if address else ''}
                        {f'''<div class="detail-item">
                            <strong>Openingsuren:</strong>
                            <div class="opening-hours">
                                {opening_hours.replace(' | ', '<br>')}
                            </div>
                        </div>''' if has_opening_hours else '<div class="detail-item"><strong>Openingsuren:</strong> <span class="meta-value">Contacteer het kasteel voor actuele openingsuren</span></div>'}
                        <div class="detail-item">
                            <strong>Bezoekbaar:</strong> 
                            <span class="meta-value">{'Ja' if can_visit else 'Neem contact op'}</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Section 2: Introductie tekst (Wikipedia content) -->
    <section class="castle-intro">
        <div class="container">
            <div class="content-wrapper">
                <p>{paragraphs[0]} <a href="index.html">Kastelen in België</a> bieden een unieke kijk op onze geschiedenis.</p>
                
                <p>{paragraphs[1]} De <a href="{province.lower().replace(' ', '-').replace('ë', 'e')}.html">kastelen in {province}</a> zijn bijzonder rijk aan geschiedenis en architectuur.</p>
                
                <p>{paragraphs[2]} Dit kasteel is een prachtig voorbeeld van het culturele erfgoed dat <a href="provinces.html">kastelen per provincie</a> te bieden hebben.</p>
            </div>
        </div>
    </section>

    <!-- Section 3: Activiteiten in de regio -->
    <section class="castle-activities">
        <div class="container">
            <h2>Activiteiten in {province}</h2>
            <div class="activities-content">
                <p>De provincie {province} biedt naast het bezoek aan {title} nog vele andere interessante activiteiten en bezienswaardigheden die uw bezoek compleet maken.</p>
                
                <div class="activities-grid">
                    {''.join([f'<div class="activity-item"><h3>{activity["title"]}</h3><p>{activity["description"]}</p></div>' for activity in activities])}
                </div>
            </div>
        </div>
    </section>

    <!-- Section 4: Gerelateerde kastelen -->
    <section class="related-castles">
        <div class="container">
            <h2>Andere Kastelen in {province}</h2>
            <div class="castles-grid">
                <div class="castle-card">
                    <div class="castle-image-placeholder">
                        <span>🏰</span>
                    </div>
                    <div class="castle-card-content">
                        <h3>Ontdek meer kastelen</h3>
                        <p class="card-description">Verken andere historische kastelen in {province} en ontdek hun unieke verhalen en architectuur.</p>
                        <a href="{province.lower().replace(' ', '-').replace('ë', 'e')}.html" class="btn-primary">Bekijk alle kastelen</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Section 5: Kaart -->
    <section class="castle-map">
        <div class="container">
            <div class="map-container">
                <div class="map-header">
                    <h3>📍 Locatie van {title}</h3>
                    <p><strong>Adres:</strong> {address if address else f'{title}, {province}'}</p>
                </div>
                <div class="google-map">
                    <iframe 
                        src="https://www.google.com/maps/embed/v1/place?key=YOUR_API_KEY&q={quote(f'{title}, {address if address else province}, Belgium')}"
                        width="100%" 
                        height="400" 
                        style="border:0;" 
                        allowfullscreen="" 
                        loading="lazy" 
                        referrerpolicy="no-referrer-when-downgrade">
                    </iframe>
                </div>
                <div class="map-actions">
                    <a href="https://www.google.com/maps/search/{quote(f'{title}, {address if address else province}, Belgium')}" target="_blank" class="btn-secondary">
                        🗺️ Open in Google Maps
                    </a>
                    <a href="https://www.google.com/maps/dir//{quote(f'{title}, {address if address else province}, Belgium')}" target="_blank" class="btn-secondary">
                        🚗 Routebeschrijving
                    </a>
                </div>
            </div>
        </div>
    </section>

    {f'''<!-- Section 6: Reservatieformulier -->
    <section class="reservation-form">
        <div class="container">
            <h2>Reserveer je bezoek aan {title}</h2>
            <div class="form-intro">
                <p>Plan uw bezoek aan {title} en reserveer uw tickets online. Vul onderstaand formulier in en wij nemen zo spoedig mogelijk contact met u op.</p>
            </div>
            <form class="contact-form" action="mailto:ninjas.of.seo@gmail.com" method="post" enctype="text/plain">
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
                <div class="form-row">
                    <div class="form-group">
                        <label for="phone">Telefoon</label>
                        <input type="tel" id="phone" name="phone">
                    </div>
                    <div class="form-group">
                        <label for="date">Gewenste datum</label>
                        <input type="date" id="date" name="date">
                    </div>
                </div>
                <div class="form-group">
                    <label for="visitors">Aantal bezoekers</label>
                    <select id="visitors" name="visitors">
                        <option value="1">1 persoon</option>
                        <option value="2">2 personen</option>
                        <option value="3-5">3-5 personen</option>
                        <option value="6-10">6-10 personen</option>
                        <option value="10+">Meer dan 10 personen</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="message">Bericht</label>
                    <textarea id="message" name="message" rows="4" placeholder="Eventuele opmerkingen, vragen of speciale wensen voor uw bezoek..."></textarea>
                </div>
                <button type="submit" class="btn-primary">Verstuur reservatie</button>
                <p class="form-note">* Verplichte velden. Uw gegevens worden vertrouwelijk behandeld.</p>
            </form>
        </div>
    </section>''' if has_opening_hours else ''}

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-brand">
                    <h3>kastelenbelgie.be</h3>
                    <p>Ontdek de mooiste kastelen van België</p>
                    <div class="social-links">
                        <a href="#">Facebook</a>
                        <a href="#">Instagram</a>
                        <a href="#">Twitter</a>
                    </div>
                </div>
                <div class="footer-links">
                    <div class="link-group">
                        <h4>Kastelen</h4>
                        <ul>
                            <li><a href="antwerpen.html">Antwerpen</a></li>
                            <li><a href="limburg.html">Limburg</a></li>
                            <li><a href="oost-vlaanderen.html">Oost-Vlaanderen</a></li>
                            <li><a href="west-vlaanderen.html">West-Vlaanderen</a></li>
                        </ul>
                    </div>
                    <div class="link-group">
                        <h4>Informatie</h4>
                        <ul>
                            <li><a href="blog.html">Blog</a></li>
                            <li><a href="contact.html">Contact</a></li>
                            <li><a href="privacybeleid.html">Privacy</a></li>
                            <li><a href="algemene-voorwaarden.html">Voorwaarden</a></li>
                        </ul>
                    </div>
                    <div class="link-group">
                        <h4>Service</h4>
                        <ul>
                            <li><a href="index.html">Homepage</a></li>
                            <li><a href="provinces.html">Alle provincies</a></li>
                            <li><a href="blog.html">Alle artikelen</a></li>
                            <li><a href="contact.html">Contact</a></li>
                        </ul>
                    </div>
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

    # Sauvegarder le fichier
    filepath = f"/Users/marc/Desktop/kastelenbelgie/{filename}.html"
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"  ✅ Page créée: {filename}.html ({total_words} mots)")
    return filename
