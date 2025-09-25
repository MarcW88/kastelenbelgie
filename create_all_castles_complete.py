#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CRÉATION COMPLÈTE DE TOUTES LES PAGES CHÂTEAUX
Génère toutes les pages avec contenu Wikipedia scraped
"""

import os
import re
import json
import requests
import time
import csv
from urllib.parse import quote, urlparse
from io import StringIO

# Configuration Wikipedia
WIKIPEDIA_API_BASE = "https://fr.wikipedia.org/api/rest_v1/page/summary/"
WIKIPEDIA_SEARCH_API = "https://fr.wikipedia.org/w/api.php"

# Données des châteaux (format CSV)
CASTLES_DATA_CSV = """Title,URL,Provincie,PLACE_ID,NAME_FOUND,FORMATTED_ADDRESS,TYPES,BUSINESS_STATUS,OPEN_NOW,OPENING_HOURS_TEXT,MON,TUE,WED,THU,FRI,SAT,SUN,CAN_VISIT
Kasteel engelhof,https://kastelenbelgie.be/nl/kasteel-engelhof-houthalen/,Luik,ChIJ4YgVpIfYwEcROLY6-aVZxVg,Kasteel Engelhof,"Hengelhoefdreef 2, 3530 Houthalen-Helchteren","establishment,point_of_interest",OPERATIONAL,yes,,,,,,,,yes
Kasteel Beauregard,https://kastelenbelgie.be/nl/kasteel-beauregard-froyennes/,Luik,ChIJg32qFBI9wkcRnH8JNQ_K-SU,Château Beauregard,"Beauregard, 6530 Thuin","establishment,point_of_interest",OPERATIONAL,yes,,,,,,,,yes
Kasteel karreveld,https://kastelenbelgie.be/nl/kasteel-karreveld-te-sint-jans-molenbeek/,Luik,ChIJpxgMN-PDw0cRudiYpvhfQOg,Kasteelhoeve Karreveld,"Jean de la Hoeselaan 32, 1080 Sint-Jans-Molenbeek","establishment,point_of_interest,tourist_attraction",OPERATIONAL,FALSE,"maandag: 08:30–17:00 | dinsdag: 08:30–17:00 | woensdag: 08:30–18:00 | donderdag: 08:30–18:00 | vrijdag: 08:30–18:00 | zaterdag: 08:30–18:00 | zondag: 08:30–18:00",08:30–17:00,08:30–17:00,08:30–18:00,08:30–18:00,08:30–18:00,08:30–18:00,08:30–18:00,yes
Kasteel van wegimont,https://kastelenbelgie.be/nl/kasteel-van-wegimont-ayeneux-soumagne/,Luik,ChIJV9ZMwIX0wEcRkqSleNQDFfE,Château de Wégimont,4630 Liège,"establishment,point_of_interest",OPERATIONAL,FALSE,"maandag: 09:00–17:00 | dinsdag: 09:00–17:00 | woensdag: 09:00–17:00 | donderdag: 09:00–17:00 | vrijdag: 09:00–17:00 | zaterdag: 09:00–17:00 | zondag: 09:00–17:00",09:00–17:00,09:00–17:00,09:00–17:00,09:00–17:00,09:00–17:00,09:00–17:00,09:00–17:00,yes"""

def parse_csv_data():
    """Parse les données CSV des châteaux"""
    reader = csv.DictReader(StringIO(CASTLES_DATA_CSV))
    castles = []
    for row in reader:
        if row['Title'] and row['URL']:
            castles.append(row)
    return castles

def search_wikipedia(castle_name, location=""):
    """Recherche un château sur Wikipedia"""
    try:
        # Nettoyer le nom
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
        # Récupérer le résumé
        summary_url = f"{WIKIPEDIA_API_BASE}{quote(page_title)}"
        response = requests.get(summary_url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            extract = data.get('extract', '')
            
            # Si le résumé est trop court, essayer de récupérer plus de contenu
            if len(extract) < 200:
                # Utiliser l'API de contenu
                content_params = {
                    'action': 'query',
                    'format': 'json',
                    'titles': page_title,
                    'prop': 'extracts',
                    'exintro': True,
                    'explaintext': True,
                    'exsectionformat': 'plain'
                }
                
                content_response = requests.get(WIKIPEDIA_SEARCH_API, params=content_params, timeout=10)
                if content_response.status_code == 200:
                    content_data = content_response.json()
                    pages = content_data.get('query', {}).get('pages', {})
                    for page_id, page_info in pages.items():
                        if 'extract' in page_info:
                            extract = page_info['extract']
                            break
            
            return extract
        
        return None
    except Exception as e:
        print(f"Erreur récupération contenu Wikipedia: {e}")
        return None

def format_wikipedia_content(content, castle_name):
    """Formate le contenu Wikipedia en 3 paragraphes de ~100 mots"""
    if not content:
        return generate_default_content(castle_name)
    
    # Nettoyer le contenu
    content = re.sub(r'\[.*?\]', '', content)  # Supprimer les références
    content = re.sub(r'\s+', ' ', content).strip()
    
    # Diviser en phrases
    sentences = re.split(r'[.!?]+', content)
    sentences = [s.strip() for s in sentences if len(s.strip()) > 20]
    
    # Créer 3 paragraphes
    paragraphs = []
    sentences_per_paragraph = max(1, len(sentences) // 3)
    
    for i in range(0, len(sentences), sentences_per_paragraph):
        paragraph_sentences = sentences[i:i + sentences_per_paragraph]
        paragraph = '. '.join(paragraph_sentences)
        if paragraph and not paragraph.endswith('.'):
            paragraph += '.'
        paragraphs.append(paragraph)
    
    # S'assurer d'avoir exactement 3 paragraphes
    while len(paragraphs) < 3:
        if paragraphs:
            # Diviser le dernier paragraphe
            last = paragraphs[-1]
            mid = len(last) // 2
            split_point = last.find('. ', mid)
            if split_point > 0:
                paragraphs[-1] = last[:split_point + 1]
                paragraphs.append(last[split_point + 2:])
            else:
                paragraphs.append(generate_default_paragraph(castle_name))
        else:
            paragraphs.append(generate_default_paragraph(castle_name))
    
    return paragraphs[:3]

def generate_default_content(castle_name):
    """Génère un contenu par défaut si Wikipedia n'est pas disponible"""
    return [
        f"{castle_name} is een historisch kasteel dat een belangrijke rol heeft gespeeld in de geschiedenis van België. Dit prachtige monument getuigt van eeuwen van architecturale evolutie en cultureel erfgoed.",
        f"Het kasteel heeft door de jaren heen verschillende eigenaren gekend en heeft meerdere renovaties ondergaan. De architectuur weerspiegelt de verschillende bouwperiodes en stijlen die kenmerkend zijn voor de Belgische kastelen.",
        f"Vandaag de dag staat {castle_name} als een symbool van het rijke historische erfgoed van België. Bezoekers kunnen er genieten van de prachtige architectuur en de verhalen die de muren vertellen."
    ]

def generate_default_paragraph(castle_name):
    """Génère un paragraphe par défaut"""
    return f"Dit kasteel vertegenwoordigt een belangrijk onderdeel van het Belgische culturele erfgoed en biedt bezoekers een unieke kijk op de geschiedenis van de regio."

def create_castle_page(castle_data):
    """Crée une page château complète"""
    title = castle_data['Title']
    url = castle_data['URL']
    province = castle_data['Provincie']
    address = castle_data.get('FORMATTED_ADDRESS', '')
    opening_hours = castle_data.get('OPENING_HOURS_TEXT', '')
    
    # Extraire le nom du fichier de l'URL
    url_path = urlparse(url).path
    filename = url_path.split('/')[-2] if url_path.endswith('/') else url_path.split('/')[-1]
    if not filename:
        filename = title.lower().replace(' ', '-').replace('kasteel', 'kasteel')
    
    print(f"Création de la page: {filename}.html pour {title}")
    
    # Rechercher sur Wikipedia
    wiki_title = search_wikipedia(title, province)
    wiki_content = None
    
    if wiki_title:
        print(f"  Trouvé sur Wikipedia: {wiki_title}")
        wiki_content = get_wikipedia_content(wiki_title)
        time.sleep(1)  # Respecter les limites de l'API
    
    # Formater le contenu
    paragraphs = format_wikipedia_content(wiki_content, title)
    
    # Déterminer si on a besoin d'un formulaire de réservation
    has_opening_hours = bool(opening_hours and opening_hours.strip())
    
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
                    <img src="chateaux_images_update-2/{filename}.jpg" alt="{title}" onerror="this.src='chateaux_images_update-2/default-castle.jpg'">
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
                        </div>''' if has_opening_hours else ''}
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
                <p>De provincie {province} biedt naast het bezoek aan {title} nog vele andere interessante activiteiten en bezienswaardigheden.</p>
                
                <div class="activities-grid">
                    <div class="activity-item">
                        <h3>🏰 Andere Kastelen</h3>
                        <p>Ontdek meer historische kastelen in de regio</p>
                    </div>
                    <div class="activity-item">
                        <h3>🌳 Natuurwandelingen</h3>
                        <p>Verken de prachtige natuur rondom het kasteel</p>
                    </div>
                    <div class="activity-item">
                        <h3>🍽️ Lokale Gastronomie</h3>
                        <p>Proef de specialiteiten van {province}</p>
                    </div>
                    <div class="activity-item">
                        <h3>🎨 Cultureel Erfgoed</h3>
                        <p>Bezoek musea en culturele sites in de buurt</p>
                    </div>
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
                    <img src="chateaux_images_update-2/placeholder1.jpg" alt="Gerelateerd kasteel" onerror="this.src='chateaux_images_update-2/default-castle.jpg'">
                    <div class="castle-card-content">
                        <h3>Ontdek meer kastelen</h3>
                        <p>Verken andere historische kastelen in {province}</p>
                        <a href="{province.lower()}.html" class="btn-primary">Bekijk alle kastelen</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Section 5: Kaart -->
    <section class="castle-map">
        <div class="container">
            <h2>Locatie van {title}</h2>
            <div class="map-container">
                <div class="map-placeholder">
                    <p>📍 {address if address else f'{title}, {province}'}</p>
                    <p>Interactieve kaart wordt hier geladen</p>
                </div>
            </div>
        </div>
    </section>

    {f'''<!-- Section 6: Reservatieformulier -->
    <section class="reservation-form">
        <div class="container">
            <h2>Reserveer je bezoek</h2>
            <form class="contact-form">
                <div class="form-group">
                    <label for="name">Naam *</label>
                    <input type="text" id="name" name="name" required>
                </div>
                <div class="form-group">
                    <label for="email">E-mail *</label>
                    <input type="email" id="email" name="email" required>
                </div>
                <div class="form-group">
                    <label for="phone">Telefoon</label>
                    <input type="tel" id="phone" name="phone">
                </div>
                <div class="form-group">
                    <label for="date">Gewenste datum</label>
                    <input type="date" id="date" name="date">
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
                    <textarea id="message" name="message" rows="4" placeholder="Eventuele opmerkingen of vragen..."></textarea>
                </div>
                <button type="submit" class="btn-primary">Verstuur reservatie</button>
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
    
    print(f"  ✅ Page créée: {filename}.html")
    return filename

def main():
    """Fonction principale"""
    print("🏰 CRÉATION COMPLÈTE DE TOUTES LES PAGES CHÂTEAUX")
    print("=" * 60)
    
    # Parser les données
    castles = parse_csv_data()
    print(f"📊 {len(castles)} châteaux trouvés dans les données")
    
    created_pages = []
    
    for i, castle in enumerate(castles, 1):
        print(f"\n[{i}/{len(castles)}] Traitement de {castle['Title']}")
        try:
            filename = create_castle_page(castle)
            created_pages.append(filename)
            time.sleep(2)  # Pause entre les requêtes
        except Exception as e:
            print(f"  ❌ Erreur: {e}")
    
    print(f"\n✅ TERMINÉ: {len(created_pages)} pages créées")
    print("Pages créées:")
    for page in created_pages:
        print(f"  • {page}.html")

if __name__ == "__main__":
    main()
