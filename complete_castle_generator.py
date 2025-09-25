#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
GÉNÉRATEUR COMPLET DE PAGES CHÂTEAUX
Intègre Wikipedia, images, GPS et related castles
"""

import os
import csv
import time
from urllib.parse import quote
from advanced_wikipedia_scraper import AdvancedWikipediaScraper
from image_matcher import CastleImageMatcher
from gps_coordinates_manager import GPSCoordinatesManager
from castle_activities_data import get_activities_for_province

class CompleteCastleGenerator:
    def __init__(self):
        # Initialiser les composants
        self.wikipedia_scraper = AdvancedWikipediaScraper()
        self.image_matcher = CastleImageMatcher("/Users/marc/Desktop/kastelenbelgie/chateaux_images_update-2")
        self.gps_manager = GPSCoordinatesManager("/Users/marc/Desktop/kastelenbelgie/chateaux_coord.csv")
        
        # Statistiques
        self.stats = {
            'total_processed': 0,
            'wikipedia_found': 0,
            'images_found': 0,
            'coordinates_found': 0,
            'errors': []
        }
    
    def should_skip_entry(self, row):
        """Détermine si une entrée doit être ignorée"""
        skip_keywords = [
            "kastelen per provincie", "kastelen in", "kastelen-", 
            "kaart", "home", "belgië"
        ]
        
        title = row.get('Title', '').lower()
        return any(keyword in title for keyword in skip_keywords)
    
    def get_filename_from_url(self, url):
        """Extraire le nom du fichier de l'URL"""
        from urllib.parse import urlparse
        url_path = urlparse(url).path
        filename = url_path.split('/')[-2] if url_path.endswith('/') else url_path.split('/')[-1]
        return filename if filename else "kasteel"
    
    def generate_related_castles_section(self, province, current_castle_name, max_castles=3):
        """Génère la section des châteaux reliés avec images et descriptions Wikipedia"""
        print(f"  🔗 Recherche châteaux reliés en {province}")
        
        # Obtenir des images de châteaux de la même province
        related_images = self.image_matcher.get_related_castle_images(
            province, 
            exclude_castle=current_castle_name, 
            max_images=max_castles
        )
        
        related_castles_html = ""
        
        for i, image_info in enumerate(related_images):
            # Extraire le nom du château depuis le nom de l'image
            castle_name = image_info['base_name'].replace('_', ' ').title()
            castle_name = castle_name.replace('Kasteel ', '').replace('Château ', '')
            
            # Obtenir une description courte depuis Wikipedia
            wiki_result = self.wikipedia_scraper.scrape_castle_info(
                f"Kasteel {castle_name}", province
            )
            
            if wiki_result and wiki_result['paragraphs']:
                # Prendre les 20 premiers mots du premier paragraphe
                description = ' '.join(wiki_result['paragraphs'][0].split()[:20]) + "..."
            else:
                description = f"Découvrez ce magnifique château historique situé en {province}, témoin du riche patrimoine architectural belge."
            
            related_castles_html += f'''
                <div class="castle-card">
                    <div class="castle-image">
                        <img src="chateaux_images_update-2/{image_info['filename']}" 
                             alt="{castle_name}" 
                             loading="lazy">
                    </div>
                    <div class="castle-card-content">
                        <h3>{castle_name}</h3>
                        <p class="card-description">{description}</p>
                        <a href="provinces.html#{province.lower().replace(' ', '-').replace('ë', 'e')}" class="btn-primary">Découvrir</a>
                    </div>
                </div>'''
            
            time.sleep(1)  # Pause pour respecter Wikipedia
        
        # Si pas assez de châteaux trouvés, ajouter une carte générique
        if len(related_images) < max_castles:
            related_castles_html += f'''
                <div class="castle-card">
                    <div class="castle-image-placeholder">
                        <span>🏰</span>
                    </div>
                    <div class="castle-card-content">
                        <h3>Découvrez plus de châteaux</h3>
                        <p class="card-description">Explorez d'autres châteaux historiques en {province} et découvrez leurs histoires fascinantes.</p>
                        <a href="{province.lower().replace(' ', '-').replace('ë', 'e')}.html" class="btn-primary">Voir tous les châteaux</a>
                    </div>
                </div>'''
        
        return related_castles_html
    
    def create_complete_castle_page(self, row):
        """Crée une page château complète avec tous les éléments"""
        # Extraire les données de base
        title = row.get('Title', '')
        url = row.get('URL', '')
        province = row.get('Provincie', '')
        address = row.get('FORMATTED_ADDRESS', '')
        opening_hours = row.get('OPENING_HOURS_TEXT', '')
        can_visit = row.get('CAN_VISIT', '').lower() == 'yes'
        
        if self.should_skip_entry(row) or not title or not url:
            return None
        
        filename = self.get_filename_from_url(url)
        self.stats['total_processed'] += 1
        
        print(f"\n🏰 [{self.stats['total_processed']}] Création: {filename}.html")
        print(f"  📝 Titre: {title}")
        print(f"  🗺️ Province: {province}")
        
        # 1. SCRAPER WIKIPEDIA (300+ mots)
        wiki_result = self.wikipedia_scraper.scrape_castle_info(title, province)
        if wiki_result:
            paragraphs = wiki_result['paragraphs']
            self.stats['wikipedia_found'] += 1
            print(f"  ✅ Wikipedia: {wiki_result['word_count']} mots trouvés")
        else:
            # Contenu par défaut enrichi
            paragraphs = [
                f"{title} est un château historique emblématique situé en {province}, représentant un patrimoine architectural exceptionnel. Ce monument témoigne de siècles d'histoire belge et constitue un exemple remarquable de l'évolution des techniques de construction et des styles architecturaux à travers les époques. L'édifice a joué un rôle important dans l'histoire locale et régionale.",
                f"L'architecture du château reflète les influences stylistiques de différentes périodes historiques, combinant des éléments médiévaux, Renaissance ou classiques selon son époque de construction. Les matériaux utilisés, souvent issus de la région, témoignent du savoir-faire local et des ressources disponibles. Chaque élément architectural raconte une partie de l'histoire du château et de ses occupants successifs.",
                f"Aujourd'hui, {title} continue d'attirer les visiteurs par son charme historique et son importance culturelle. Il représente un maillon essentiel du patrimoine castral de {province} et offre aux visiteurs une plongée authentique dans l'histoire architecturale et sociale de la Belgique. Ce château contribue à préserver et transmettre la richesse du patrimoine belge aux générations futures."
            ]
            print(f"  ⚠️ Wikipedia: Contenu par défaut utilisé")
        
        # 2. TROUVER IMAGES
        best_image = self.image_matcher.get_best_image(title, url, 0.5)
        if best_image:
            main_image_html = f'''
                <div class="castle-image">
                    <img src="chateaux_images_update-2/{best_image['filename']}" 
                         alt="{title}" 
                         loading="lazy">
                </div>'''
            self.stats['images_found'] += 1
        else:
            main_image_html = '''
                <div class="castle-image">
                    <div class="image-placeholder">
                        <h2>📸 ''' + title + '''</h2>
                        <p>Afbeelding wordt binnenkort toegevoegd</p>
                    </div>
                </div>'''
        
        # 3. COORDONNÉES GPS ET CARTES
        maps_data = self.gps_manager.generate_google_maps_embed(title, url, address)
        if maps_data['has_precise_location']:
            self.stats['coordinates_found'] += 1
            print(f"  📍 GPS: Coordonnées précises trouvées")
        else:
            print(f"  📍 GPS: Utilisation de l'adresse")
        
        # 4. ACTIVITÉS PAR PROVINCE
        activities = get_activities_for_province(province)
        
        # 5. CHÂTEAUX RELIÉS
        related_castles_html = self.generate_related_castles_section(province, title, 3)
        
        # 6. FORMULAIRE DE RÉSERVATION
        has_opening_hours = bool(opening_hours and opening_hours.strip() and opening_hours != "Info volgt")
        
        # 7. LIENS AVEC ANCRES SPÉCIFIQUES
        province_link = f"provincie {province}"
        
        # GÉNÉRATION DU HTML COMPLET
        html_content = f'''<!DOCTYPE html>
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
            <a href="{province.lower().replace(' ', '-').replace('ë', 'e')}.html">{province_link}</a>
            <span>›</span>
            <span>{title}</span>
        </div>
    </div>

    <!-- Section 1: Hero avec image et info box -->
    <section class="castle-hero">
        <div class="container">
            <div class="castle-hero-content">
                {main_image_html}
                <div class="castle-info-box">
                    <h1>{title}</h1>
                    <div class="castle-details">
                        <div class="detail-item">
                            <strong>Provincie:</strong> 
                            <span class="meta-value">{province}</span>
                        </div>
                        {'<div class="detail-item"><strong>Adres:</strong> <span class="meta-value">' + maps_data["address"] + '</span></div>' if maps_data["address"] else ''}
                        {'<div class="detail-item"><strong>Openingsuren:</strong><div class="opening-hours">' + opening_hours.replace(' | ', '<br>') + '</div></div>' if has_opening_hours else '<div class="detail-item"><strong>Openingsuren:</strong> <span class="meta-value">Contacteer het kasteel voor actuele openingsuren</span></div>'}
                        <div class="detail-item">
                            <strong>Bezoekbaar:</strong> 
                            <span class="meta-value">{'Ja' if can_visit else 'Neem contact op'}</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Section 2: Introductie tekst (Wikipedia content 300+ mots) -->
    <section class="castle-intro">
        <div class="container">
            <div class="content-wrapper">
                <p>{paragraphs[0]} <a href="index.html">Kastelen in België</a> bieden een unieke kijk op onze geschiedenis.</p>
                
                <p>{paragraphs[1]} De <a href="{province.lower().replace(' ', '-').replace('ë', 'e')}.html">kastelen in {province_link}</a> zijn bijzonder rijk aan geschiedenis en architectuur.</p>
                
                <p>{paragraphs[2]} Dit kasteel is een prachtig voorbeeld van het culturele erfgoed dat <a href="provinces.html">kastelen per provincie</a> te bieden hebben.</p>
            </div>
        </div>
    </section>

    <!-- Section 3: Activiteiten in de regio -->
    <section class="castle-activities">
        <div class="container">
            <h2>Activiteiten in {province}</h2>
            <div class="activities-content">
                <p>De {province_link} biedt naast het bezoek aan {title} nog vele andere interessante activiteiten en bezienswaardigheden die uw bezoek compleet maken.</p>
                
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
                {related_castles_html}
            </div>
        </div>
    </section>

    <!-- Section 5: Kaart met GPS coordonnées -->
    <section class="castle-map">
        <div class="container">
            <div class="map-container">
                <div class="map-header">
                    <h3>📍 Locatie van {title}</h3>
                    <p><strong>Adres:</strong> {maps_data['address'] if maps_data['address'] else f'{title}, {province}'}</p>
                    {f'<p><strong>Coördinaten:</strong> {maps_data["coordinates"]["lat"]:.6f}, {maps_data["coordinates"]["lng"]:.6f}</p>' if maps_data['coordinates'] else ''}
                </div>
                <div class="google-map">
                    <iframe 
                        src="{maps_data['embed_url']}"
                        width="100%" 
                        height="400" 
                        style="border:0;" 
                        allowfullscreen="" 
                        loading="lazy" 
                        referrerpolicy="no-referrer-when-downgrade">
                    </iframe>
                </div>
                <div class="map-actions">
                    <a href="{maps_data['search_url']}" target="_blank" class="btn-secondary">
                        🗺️ Open in Google Maps
                    </a>
                    <a href="{maps_data['directions_url']}" target="_blank" class="btn-secondary">
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
</html>'''

        # Sauvegarder le fichier
        filepath = f"/Users/marc/Desktop/kastelenbelgie/{filename}.html"
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        total_words = sum(len(p.split()) for p in paragraphs)
        print(f"  ✅ Page créée: {filename}.html ({total_words} mots)")
        
        return filename
