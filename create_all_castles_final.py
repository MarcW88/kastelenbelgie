#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CRÉATION COMPLÈTE DE TOUS LES CHÂTEAUX
Script final pour créer toutes les pages avec Wikipedia scraping
"""

import os
import re
import json
import requests
import time
from urllib.parse import quote, urlparse

# Configuration
WIKIPEDIA_SEARCH_API = "https://fr.wikipedia.org/w/api.php"

# Activités par province
PROVINCE_ACTIVITIES = {
    "Antwerpen": [
        {"title": "🏛️ Rubenshuis Antwerpen", "description": "Bezoek het voormalige huis en atelier van Peter Paul Rubens"},
        {"title": "⛪ Onze-Lieve-Vrouwekathedraal", "description": "Bewonder de gotische architectuur en Rubens' meesterwerken"},
        {"title": "🌳 Rivierenhof Park", "description": "Wandel door een van de mooiste parken van Antwerpen"},
        {"title": "🏰 Het Steen Museum", "description": "Ontdek de geschiedenis van Antwerpen in dit historische kasteel"}
    ],
    "Limburg": [
        {"title": "🌲 Nationaal Park Hoge Kempen", "description": "Verken de unieke heide- en boslandschappen"},
        {"title": "⛏️ Mijnmuseum Beringen", "description": "Ontdek de rijke mijnbouwgeschiedenis van Limburg"},
        {"title": "🍎 Fruitstreek Borgloon", "description": "Geniet van de bloesems en fruitboomgaarden"},
        {"title": "🏞️ Voerstreek", "description": "Wandel door de glooiende heuvels van Voeren"}
    ],
    "Luik": [
        {"title": "🏛️ Paleis der Prinsbisschoppen", "description": "Bewonder de gotische architectuur in Luik"},
        {"title": "⛪ Sint-Pauluskathedraal", "description": "Bezoek deze prachtige barokke kathedraal"},
        {"title": "🌊 Maas Promenade", "description": "Wandel langs de rivier door het stadscentrum"},
        {"title": "🎭 Opéra Royal de Wallonie", "description": "Geniet van cultuur in dit historische operagebouw"}
    ],
    "Luxemburg": [
        {"title": "🏰 Kasteel van Bouillon", "description": "Verken een van Europa's oudste burchten"},
        {"title": "🌲 Semois Vallei", "description": "Ontdek de meanderende rivier en bossen"},
        {"title": "🍺 Abdij van Orval", "description": "Proef het beroemde Trappistenbier"},
        {"title": "🦌 Natuurpark Haute-Sûre", "description": "Spot wilde dieren in hun natuurlijke habitat"}
    ]
}

def search_wikipedia(castle_name, location=""):
    """Recherche un château sur Wikipedia"""
    try:
        search_terms = [
            castle_name,
            castle_name.replace("Kasteel", "Château"),
            castle_name.replace("van", "de"),
            f"{castle_name} {location}",
            f"Château {castle_name.replace('Kasteel', '').strip()}"
        ]
        
        for term in search_terms:
            params = {
                'action': 'query',
                'format': 'json',
                'list': 'search',
                'srsearch': term,
                'srlimit': 3
            }
            
            response = requests.get(WIKIPEDIA_SEARCH_API, params=params, timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data.get('query', {}).get('search'):
                    return data['query']['search'][0]['title']
            
            time.sleep(0.5)
        
        return None
    except Exception as e:
        print(f"Erreur recherche Wikipedia pour {castle_name}: {e}")
        return None

def get_wikipedia_content(page_title):
    """Récupère le contenu Wikipedia d'une page"""
    try:
        params = {
            'action': 'query',
            'format': 'json',
            'titles': page_title,
            'prop': 'extracts',
            'exintro': True,
            'explaintext': True,
            'exsectionformat': 'plain'
        }
        
        response = requests.get(WIKIPEDIA_SEARCH_API, params=params, timeout=10)
        if response.status_code == 200:
            data = response.json()
            pages = data.get('query', {}).get('pages', {})
            for page_id, page_info in pages.items():
                if 'extract' in page_info:
                    return page_info['extract']
        
        return None
    except Exception as e:
        print(f"Erreur récupération contenu Wikipedia: {e}")
        return None

def format_wikipedia_content(content, castle_name):
    """Formate le contenu Wikipedia en 3 paragraphes de ~100 mots"""
    if not content or len(content) < 100:
        return generate_default_content(castle_name)
    
    # Nettoyer le contenu
    content = re.sub(r'\[.*?\]', '', content)  # Supprimer les références
    content = re.sub(r'\s+', ' ', content).strip()
    
    # Diviser en phrases
    sentences = re.split(r'[.!?]+', content)
    sentences = [s.strip() for s in sentences if len(s.strip()) > 20]
    
    # Créer 3 paragraphes d'environ 100 mots chacun
    paragraphs = []
    words_per_paragraph = 100
    current_paragraph = ""
    current_word_count = 0
    
    for sentence in sentences:
        sentence_words = len(sentence.split())
        if current_word_count + sentence_words > words_per_paragraph and current_paragraph:
            paragraphs.append(current_paragraph.strip() + ".")
            current_paragraph = sentence
            current_word_count = sentence_words
        else:
            current_paragraph += (" " if current_paragraph else "") + sentence
            current_word_count += sentence_words
        
        if len(paragraphs) >= 3:
            break
    
    # Ajouter le dernier paragraphe
    if current_paragraph and len(paragraphs) < 3:
        paragraphs.append(current_paragraph.strip() + ".")
    
    # S'assurer d'avoir exactement 3 paragraphes
    while len(paragraphs) < 3:
        paragraphs.append(generate_default_paragraph(castle_name))
    
    return paragraphs[:3]

def generate_default_content(castle_name):
    """Génère un contenu par défaut si Wikipedia n'est pas disponible"""
    return [
        f"{castle_name} is een historisch kasteel dat een belangrijke rol heeft gespeeld in de geschiedenis van België. Dit prachtige monument getuigt van eeuwen van architecturale evolutie en cultureel erfgoed dat kenmerkend is voor de Belgische kastelen. De geschiedenis van dit kasteel weerspiegelt de rijke traditie van de Belgische adel en hun invloed op de lokale gemeenschap.",
        f"Het kasteel heeft door de jaren heen verschillende eigenaren gekend en heeft meerdere renovaties ondergaan die de architecturale stijlen van verschillende periodes weerspiegelen. De structuur combineert elementen uit verschillende bouwperiodes, wat resulteert in een unieke architecturale mix die bezoekers een fascinerende kijk geeft op de evolutie van kasteelbouw in België door de eeuwen heen.",
        f"Vandaag de dag staat {castle_name} als een symbool van het rijke historische erfgoed van België en trekt het bezoekers van over de hele wereld aan. Het kasteel biedt een unieke gelegenheid om de geschiedenis van de regio te ontdekken en de verhalen te horen die de muren vertellen over het leven van vroegere bewoners en hun rol in de Belgische geschiedenis."
    ]

def generate_default_paragraph(castle_name):
    """Génère un paragraphe par défaut"""
    return f"Dit kasteel vertegenwoordigt een belangrijk onderdeel van het Belgische culturele erfgoed en biedt bezoekers een unieke kijk op de geschiedenis van de regio. De architectuur en de verhalen die ermee verbonden zijn, maken het tot een waardevolle bestemming voor iedereen die geïnteresseerd is in de rijke geschiedenis van België."

def get_filename_from_url(url):
    """Extraire le nom du fichier de l'URL"""
    url_path = urlparse(url).path
    filename = url_path.split('/')[-2] if url_path.endswith('/') else url_path.split('/')[-1]
    return filename if filename else "kasteel"

def create_castle_page(castle_data):
    """Crée une page château complète"""
    title = castle_data['title']
    url = castle_data['url']
    province = castle_data['province']
    address = castle_data.get('address', '')
    opening_hours = castle_data.get('opening_hours', '')
    
    filename = get_filename_from_url(url)
    
    print(f"Création de la page: {filename}.html pour {title}")
    
    # Rechercher sur Wikipedia
    wiki_title = search_wikipedia(title, province)
    wiki_content = None
    
    if wiki_title:
        print(f"  Trouvé sur Wikipedia: {wiki_title}")
        wiki_content = get_wikipedia_content(wiki_title)
        time.sleep(2)  # Respecter les limites de l'API
    else:
        print(f"  Pas trouvé sur Wikipedia, utilisation contenu par défaut")
    
    # Formater le contenu
    paragraphs = format_wikipedia_content(wiki_content, title)
    
    # Vérifier la longueur totale (minimum 300 mots)
    total_words = sum(len(p.split()) for p in paragraphs)
    print(f"  Contenu généré: {total_words} mots")
    
    # Déterminer si on a besoin d'un formulaire de réservation
    has_opening_hours = bool(opening_hours and opening_hours.strip())
    
    # Obtenir les activités pour cette province
    activities = PROVINCE_ACTIVITIES.get(province, PROVINCE_ACTIVITIES.get("Antwerpen", []))
    
    # Template de la page
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
                <a href="index.html" class="logo">kastelenbelgie</a>
                <div class="nav-menu">
                    <a href="provinces.html" class="nav-link">Kastelen</a>
                    <a href="blog.html" class="nav-link">Blog</a>
                    <a href="contact.html" class="nav-link">Contact</a>
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
            <a href="provinces.html">Kastelen</a>
            <span>›</span>
            <a href="{province.lower()}.html">{province}</a>
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
                            <strong>Provincie:</strong> {province}
                        </div>
                        {f'<div class="detail-item"><strong>Adres:</strong> {address}</div>' if address else ''}
                        {f'''<div class="detail-item">
                            <strong>Openingsuren:</strong>
                            <div class="opening-hours">
                                {opening_hours.replace(' | ', '<br>')}
                            </div>
                        </div>''' if has_opening_hours else '<div class="detail-item"><strong>Openingsuren:</strong> Contacteer het kasteel voor actuele openingsuren</div>'}
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
                
                <p>{paragraphs[1]} De <a href="{province.lower()}.html">kastelen in {province}</a> zijn bijzonder rijk aan geschiedenis en architectuur.</p>
                
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
                        <p>Verken andere historische kastelen in {province} en ontdek hun unieke verhalen en architectuur.</p>
                        <a href="{province.lower()}.html" class="btn-primary">Bekijk alle kastelen</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Section 5: Kaart -->
    <section class="castle-map">
        <div class="container">
            <h2>📍 Locatie van {title}</h2>
            <div class="map-container">
                <div class="map-placeholder">
                    <h3>{title}</h3>
                    <p><strong>Adres:</strong> {address if address else f'{title}, {province}'}</p>
                    <p>Interactieve Google Maps kaart wordt hier geladen</p>
                    <div class="map-actions">
                        <button class="btn-secondary">Routebeschrijving</button>
                        <button class="btn-secondary">Opslaan in Google Maps</button>
                    </div>
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

    # Sauvegarder le fichier
    filepath = f"/Users/marc/Desktop/kastelenbelgie/{filename}.html"
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"  ✅ Page créée: {filename}.html ({total_words} mots)")
    return filename

# Données des châteaux (échantillon pour test)
CASTLES_SAMPLE = [
    {
        "title": "Kasteel van freyr",
        "url": "https://kastelenbelgie.be/nl/kasteel-van-freyr-freyr/",
        "province": "Namen",
        "address": "Freyr 12, 5540 Hastière",
        "opening_hours": "maandag: Gesloten | dinsdag: 11:00–17:00 | woensdag: 11:00–17:00 | donderdag: 11:00–17:00 | vrijdag: 11:00–17:00 | zaterdag: 11:00–17:00 | zondag: 11:00–17:00",
        "can_visit": True
    },
    {
        "title": "Kasteel van bouchout",
        "url": "https://kastelenbelgie.be/nl/kasteel-van-bouchout-te-meise/",
        "province": "Antwerpen",
        "address": "1860 Meise",
        "opening_hours": "maandag: 10:00–17:00 | dinsdag: 10:00–17:00 | woensdag: 10:00–17:00 | donderdag: 10:00–17:00 | vrijdag: 10:00–17:00 | zaterdag: 10:00–17:00 | zondag: 10:00–17:00",
        "can_visit": True
    },
    {
        "title": "Citadel van hoei",
        "url": "https://kastelenbelgie.be/nl/citadel-van-hoei-hoei/",
        "province": "Luik",
        "address": "Chau. de Napoléon, 4500 Huy",
        "opening_hours": "maandag: 13:30–18:00 | dinsdag: 10:30–18:00 | woensdag: 10:30–18:00 | donderdag: 10:30–18:00 | vrijdag: 10:30–18:00 | zaterdag: 10:30–18:00 | zondag: 10:30–18:00",
        "can_visit": True
    }
]

def main():
    """Fonction principale"""
    print("🏰 CRÉATION COMPLÈTE DE TOUS LES CHÂTEAUX")
    print("=" * 60)
    
    created_pages = []
    
    for i, castle in enumerate(CASTLES_SAMPLE, 1):
        print(f"\n[{i}/{len(CASTLES_SAMPLE)}] Traitement de {castle['title']}")
        try:
            filename = create_castle_page(castle)
            created_pages.append(filename)
            time.sleep(3)  # Pause entre les requêtes pour respecter Wikipedia
        except Exception as e:
            print(f"  ❌ Erreur: {e}")
    
    print(f"\n✅ TERMINÉ: {len(created_pages)} pages créées")
    print("Pages créées:")
    for page in created_pages:
        print(f"  • {page}.html")

if __name__ == "__main__":
    main()
