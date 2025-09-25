#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CRÉATION DES PAGES CHÂTEAUX
Génère toutes les pages châteaux avec contenu Wikipedia
"""

import os
import re
import json
import requests
from urllib.parse import quote
import time

# Template HTML pour les pages châteaux
CASTLE_PAGE_TEMPLATE = """<!DOCTYPE html>
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
                        <input type="text" placeholder="Zoek kasteel..." class="search-input">
                    </div>
                </div>
            </div>
        </div>
    </nav>

    <!-- Breadcrumbs -->
    <div style="background: var(--bg-light); padding: 1rem 0; border-bottom: 1px solid var(--border);">
        <div class="container">
            <nav style="font-size: 0.875rem; color: var(--text-light);">
                <a href="index.html" style="color: var(--text-light); text-decoration: none;">Home</a>
                <span style="margin: 0 0.5rem;">›</span>
                <a href="provinces.html" style="color: var(--text-light); text-decoration: none;">Provincies</a>
                <span style="margin: 0 0.5rem;">›</span>
                <a href="{province_slug}.html" style="color: var(--text-light); text-decoration: none;">{province}</a>
                <span style="margin: 0 0.5rem;">›</span>
                <span style="color: var(--text);">{title}</span>
            </nav>
        </div>
    </div>

    <!-- Section 1: Image + Info -->
    <section class="section">
        <div class="container">
            <div style="display: grid; grid-template-columns: 1fr 350px; gap: 3rem; align-items: start;">
                <div>
                    <img src="{main_image}" alt="{title}" style="width: 100%; height: 400px; object-fit: cover; border-radius: var(--radius); box-shadow: var(--shadow-lg);">
                </div>
                <div style="background: var(--white); padding: 2rem; border-radius: var(--radius); box-shadow: var(--shadow); border: 1px solid var(--border);">
                    <h1 style="font-size: 2rem; font-weight: 800; margin-bottom: 1rem; color: var(--text);">{title}</h1>
                    <div style="margin-bottom: 1rem;">
                        <strong style="color: var(--text);">Provincie:</strong>
                        <span style="color: var(--text-light);">{province}</span>
                    </div>
                    {address_section}
                    {opening_hours_section}
                </div>
            </div>
        </div>
    </section>

    <!-- Section 2: Intro tekst -->
    <section class="section" style="background: var(--bg-light);">
        <div class="container">
            <div style="max-width: 800px; margin: 0 auto;">
                <h2 style="font-size: 2rem; font-weight: 700; margin-bottom: 2rem; text-align: center;">Over {title}</h2>
                <div style="font-size: 1.125rem; line-height: 1.8; color: var(--text);">
                    {intro_content}
                </div>
            </div>
        </div>
    </section>

    <!-- Section 3: Activiteiten -->
    <section class="section">
        <div class="container">
            <h2 style="font-size: 2rem; font-weight: 700; margin-bottom: 2rem; text-align: center;">Activiteiten in de buurt</h2>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 3rem;">
                <div>
                    <h3 style="font-size: 1.5rem; font-weight: 600; margin-bottom: 1rem;">Ontdek de omgeving</h3>
                    <p style="color: var(--text-light); line-height: 1.6; margin-bottom: 1.5rem;">
                        De regio rond {title} biedt talloze mogelijkheden voor een onvergetelijke dag uit. 
                        Van culturele bezienswaardigheden tot natuurwandelingen, er is voor elk wat wils.
                    </p>
                    <p style="color: var(--text-light); line-height: 1.6;">
                        Plan je bezoek en combineer je kasteelbezoek met andere attracties in {province} 
                        voor een complete ervaring van de Belgische geschiedenis en cultuur.
                    </p>
                </div>
                <div>
                    <h4 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 1rem;">Aanbevolen activiteiten</h4>
                    {activities_content}
                </div>
            </div>
        </div>
    </section>

    {gallery_section}

    <!-- Section 5: Meer kastelen -->
    <section class="section" style="background: var(--bg-light);">
        <div class="container">
            <h2 style="font-size: 2rem; font-weight: 700; margin-bottom: 2rem; text-align: center;">Ontdek meer kastelen in {province}</h2>
            <div class="cards-grid">
                {related_castles}
            </div>
        </div>
    </section>

    <!-- Section 6: Kaart -->
    <section class="section">
        <div class="container">
            <h2 style="font-size: 2rem; font-weight: 700; margin-bottom: 2rem; text-align: center;">Locatie</h2>
            <div style="background: var(--bg-light); padding: 3rem; border-radius: var(--radius); text-align: center;">
                <p style="color: var(--text-light); margin-bottom: 1rem;">📍 {address}</p>
                <p style="color: var(--text-light);">Interactieve kaart wordt binnenkort toegevoegd</p>
            </div>
        </div>
    </section>

    {reservation_section}

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h4>Kastelen</h4>
                    <ul>
                        <li><a href="provinces.html">Alle kastelen</a></li>
                        <li><a href="antwerpen.html">Antwerpen</a></li>
                        <li><a href="limburg.html">Limburg</a></li>
                        <li><a href="oost-vlaanderen.html">Oost-Vlaanderen</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4>Informatie</h4>
                    <ul>
                        <li><a href="blog.html">Blog</a></li>
                        <li><a href="contact.html">Contact</a></li>
                        <li><a href="algemene-voorwaarden.html">Algemene voorwaarden</a></li>
                        <li><a href="privacybeleid.html">Privacybeleid</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4>kastelenbelgie.be</h4>
                    <p>Ontdek de mooiste kastelen van België en beleef eeuwenoude geschiedenis.</p>
                </div>
            </div>
            <div class="footer-bottom">
                <p>© 2025 kastelenbelgie.be. Alle rechten voorbehouden.</p>
            </div>
        </div>
    </footer>
</body>
</html>"""

def get_wikipedia_content(castle_name, max_retries=3):
    """Scrape Wikipedia content voor een kasteel"""
    print(f"  📖 Zoeken Wikipedia content voor: {castle_name}")
    
    # Verschillende zoektermen proberen
    search_terms = [
        castle_name,
        castle_name.replace("Kasteel van ", "").replace("Château de ", "").replace("Citadel van ", ""),
        castle_name.replace("kasteel-", "").replace("van-", "").replace("-", " ").title()
    ]
    
    for attempt in range(max_retries):
        for term in search_terms:
            try:
                # Wikipedia API search
                search_url = f"https://nl.wikipedia.org/api/rest_v1/page/summary/{quote(term)}"
                response = requests.get(search_url, timeout=10)
                
                if response.status_code == 200:
                    data = response.json()
                    if 'extract' in data and len(data['extract']) > 100:
                        extract = data['extract']
                        
                        # Splits in 3 paragrafen van ~100 woorden
                        words = extract.split()
                        if len(words) > 50:
                            para1 = ' '.join(words[:100])
                            para2 = ' '.join(words[100:200]) if len(words) > 100 else ""
                            para3 = ' '.join(words[200:300]) if len(words) > 200 else ""
                            
                            # Voeg links toe
                            if para1:
                                para1 += f' Meer informatie over <a href="index.html" style="color: var(--primary);">kastelen in België</a> vind je op onze homepage.'
                            if para2:
                                para2 += f' Ontdek ook andere <a href="{get_province_slug(castle_name)}.html" style="color: var(--primary);">kastelen in {get_province_name(castle_name)}</a>.'
                            
                            paragraphs = [p for p in [para1, para2, para3] if p]
                            return paragraphs
                        
                time.sleep(1)  # Rate limiting
                
            except Exception as e:
                print(f"    ⚠️  Fout bij {term}: {e}")
                continue
    
    # Fallback content
    return generate_fallback_content(castle_name)

def generate_fallback_content(castle_name):
    """Genereer fallback content als Wikipedia niet beschikbaar is"""
    return [
        f"{castle_name} is een van de prachtige historische monumenten van België. Dit kasteel getuigt van de rijke geschiedenis en architecturale erfenis van onze regio. Bezoekers kunnen er genieten van de unieke sfeer en het culturele erfgoed dat eeuwen van geschiedenis heeft gevormd. Meer informatie over <a href='index.html' style='color: var(--primary);'>kastelen in België</a> vind je op onze homepage.",
        
        f"De architectuur van {castle_name} toont de evolutie van de bouwstijlen door de eeuwen heen. Van middeleeuwse versterkingen tot renaissance-elementen, elk detail vertelt een verhaal. Het kasteel speelde een belangrijke rol in de lokale geschiedenis en blijft tot op de dag van vandaag een belangrijk cultureel monument. Ontdek ook andere <a href='provinces.html' style='color: var(--primary);'>kastelen in België</a>.",
        
        f"Een bezoek aan {castle_name} biedt een unieke kans om de Belgische geschiedenis van dichtbij te beleven. Het kasteel en zijn omgeving nodigen uit tot ontdekking en contemplatie. Of je nu geïnteresseerd bent in architectuur, geschiedenis of gewoon op zoek bent naar een mooie uitstap, dit kasteel zal je niet teleurstellen."
    ]

def get_province_slug(castle_name):
    """Bepaal province slug op basis van kasteel naam"""
    province_mapping = {
        'antwerpen': 'antwerpen',
        'limburg': 'limburg', 
        'oost-vlaanderen': 'oost-vlaanderen',
        'west-vlaanderen': 'west-vlaanderen',
        'vlaams-brabant': 'vlaams-brabant',
        'brussel': 'brussel',
        'waals-brabant': 'waals-brabant',
        'henegouwen': 'henegouwen',
        'namen': 'namen',
        'luik': 'luik',
        'luxemburg': 'luxemburg'
    }
    return 'provinces'  # Default

def get_province_name(castle_name):
    """Bepaal province naam"""
    return "België"  # Default

def find_castle_images(slug):
    """Vind afbeeldingen voor een kasteel"""
    images_dir = "/Users/marc/Desktop/kastelenbelgie/chateaux_images_update-2"
    
    # Normaliseer slug voor afbeelding zoeken
    base_name = slug.replace('kasteel-', '').replace('chateau-', '').replace('citadel-', '')
    base_name = base_name.replace('van-', '').replace('-', '_')
    
    try:
        all_files = os.listdir(images_dir)
        # Zoek naar bestanden die beginnen met de base naam
        matching_files = []
        
        for file in all_files:
            if file.lower().endswith('.jpg'):
                file_base = file.lower().replace('.jpg', '')
                if base_name.lower() in file_base or any(part in file_base for part in base_name.lower().split('_')):
                    matching_files.append(file)
        
        return matching_files[:6]  # Max 6 afbeeldingen
    except:
        return []

def generate_activities_content(province):
    """Genereer activiteiten content per provincie"""
    activities_by_province = {
        'Antwerpen': [
            'Bezoek de Antwerpse diamantwijk',
            'Wandeling door het historische centrum',
            'Rondvaart op de Schelde',
            'Museum Plantin-Moretus',
            'Wandeling in het Rivierenhof'
        ],
        'Limburg': [
            'Fietsen door het Nationaal Park Hoge Kempen',
            'Bezoek aan de mijnterreinen van Genk',
            'Wandeling in Bokrijk openluchtmuseum',
            'Ontdek de Limburgse wijnroute',
            'Bezoek aan Alden Biesen'
        ],
        'Luik': [
            'Wandeling door het centrum van Luik',
            'Bezoek aan de Citadel van Luik',
            'Ontdek de Ardennen',
            'Thermale baden in Spa',
            'Bezoek aan de grotten van Han'
        ]
    }
    
    activities = activities_by_province.get(province, [
        'Wandeling door de historische binnenstad',
        'Bezoek aan lokale musea',
        'Ontdek de regionale gastronomie',
        'Fietsroutes door het landschap',
        'Bezoek aan andere historische sites'
    ])
    
    html = '<ul style="list-style: none; padding: 0;">'
    for activity in activities:
        html += f'''
        <li style="padding: 0.75rem; margin-bottom: 0.5rem; background: var(--bg-light); border-radius: var(--radius); border-left: 4px solid var(--primary);">
            <span style="color: var(--text);">• {activity}</span>
        </li>'''
    html += '</ul>'
    
    return html

def create_castle_page(castle_data):
    """Creëer een kasteel pagina"""
    print(f"🏰 Creëren pagina voor: {castle_data['title']}")
    
    # Basis informatie
    title = castle_data['title']
    slug = castle_data['slug']
    province = castle_data.get('province', 'België')
    address = castle_data.get('address', 'Adres niet beschikbaar')
    
    # Zoek afbeeldingen
    images = find_castle_images(slug)
    main_image = f"chateaux_images_update-2/{images[0]}" if images else "assets/placeholder-castle-main.svg"
    
    # Wikipedia content
    intro_paragraphs = get_wikipedia_content(title)
    intro_content = ""
    for i, para in enumerate(intro_paragraphs):
        intro_content += f'<p style="margin-bottom: 1.5rem;">{para}</p>'
    
    # Adres sectie
    address_section = f'''
    <div style="margin-bottom: 1rem;">
        <strong style="color: var(--text);">Adres:</strong><br>
        <span style="color: var(--text-light);">{address}</span>
    </div>''' if address != 'Adres niet beschikbaar' else ''
    
    # Openingsuren sectie
    opening_hours_section = ""
    if castle_data.get('has_opening_hours'):
        opening_hours_section = '''
        <div style="margin-bottom: 1rem;">
            <strong style="color: var(--text);">Openingsuren:</strong><br>
            <span style="color: var(--text-light);">Zie website voor actuele openingsuren</span>
        </div>'''
    
    # Galerij sectie
    gallery_section = ""
    if len(images) > 1:
        gallery_section = f'''
    <!-- Section 4: Galerij -->
    <section class="section" style="background: var(--bg-light);">
        <div class="container">
            <h2 style="font-size: 2rem; font-weight: 700; margin-bottom: 2rem; text-align: center;">Galerij</h2>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem;">
                {"".join([f'<img src="chateaux_images_update-2/{img}" alt="{title}" style="width: 100%; height: 200px; object-fit: cover; border-radius: var(--radius);">' for img in images[1:4]])}
            </div>
        </div>
    </section>'''
    
    # Gerelateerde kastelen (placeholder)
    related_castles = '''
    <div class="card">
        <div class="card-content">
            <h3 class="card-title">Meer kastelen binnenkort</h3>
            <p class="card-description">We voegen voortdurend nieuwe kastelen toe aan onze collectie.</p>
        </div>
    </div>'''
    
    # Reservatie sectie
    reservation_section = ""
    if castle_data.get('has_opening_hours'):
        reservation_section = f'''
    <!-- Section 7: Reservatie -->
    <section class="section">
        <div class="container">
            <div style="max-width: 600px; margin: 0 auto; background: var(--white); padding: 2rem; border-radius: var(--radius); box-shadow: var(--shadow); border: 1px solid var(--border);">
                <h2 style="font-size: 2rem; font-weight: 700; margin-bottom: 2rem; text-align: center;">Reserveer je bezoek</h2>
                <form style="display: grid; gap: 1rem;">
                    <div>
                        <label style="display: block; margin-bottom: 0.5rem; font-weight: 600;">Naam</label>
                        <input type="text" style="width: 100%; padding: 0.75rem; border: 1px solid var(--border); border-radius: var(--radius);">
                    </div>
                    <div>
                        <label style="display: block; margin-bottom: 0.5rem; font-weight: 600;">E-mail</label>
                        <input type="email" style="width: 100%; padding: 0.75rem; border: 1px solid var(--border); border-radius: var(--radius);">
                    </div>
                    <div>
                        <label style="display: block; margin-bottom: 0.5rem; font-weight: 600;">Datum bezoek</label>
                        <input type="date" style="width: 100%; padding: 0.75rem; border: 1px solid var(--border); border-radius: var(--radius);">
                    </div>
                    <div>
                        <label style="display: block; margin-bottom: 0.5rem; font-weight: 600;">Aantal personen</label>
                        <select style="width: 100%; padding: 0.75rem; border: 1px solid var(--border); border-radius: var(--radius);">
                            <option>1 persoon</option>
                            <option>2 personen</option>
                            <option>3-5 personen</option>
                            <option>6+ personen</option>
                        </select>
                    </div>
                    <button type="submit" class="btn btn-primary" style="margin-top: 1rem;">Reservatie aanvragen</button>
                </form>
            </div>
        </div>
    </section>'''
    
    # Vul template in
    html_content = CASTLE_PAGE_TEMPLATE.format(
        title=title,
        province=province,
        province_slug=get_province_slug(title),
        main_image=main_image,
        address=address,
        address_section=address_section,
        opening_hours_section=opening_hours_section,
        intro_content=intro_content,
        activities_content=generate_activities_content(province),
        gallery_section=gallery_section,
        related_castles=related_castles,
        reservation_section=reservation_section
    )
    
    # Schrijf bestand
    filename = f"/Users/marc/Desktop/kastelenbelgie/{slug}.html"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"  ✅ Pagina aangemaakt: {slug}.html")
    return filename

def main():
    """Hoofdfunctie"""
    print("🏰 CREËREN KASTEEL PAGINAS")
    print("=" * 50)
    
    # Test met een paar kastelen eerst
    test_castles = [
        {
            'title': 'Kasteel van Freÿr',
            'slug': 'kasteel-van-freyr-freyr',
            'province': 'Namen',
            'address': 'Freyr 12, 5540 Hastière',
            'has_opening_hours': True
        },
        {
            'title': 'Kasteel van Bouchout',
            'slug': 'kasteel-van-bouchout-te-meise',
            'province': 'Vlaams-Brabant',
            'address': '1860 Meise',
            'has_opening_hours': True
        },
        {
            'title': 'Citadel van Hoei',
            'slug': 'citadel-van-hoei-hoei',
            'province': 'Luik',
            'address': 'Chau. de Napoléon, 4500 Huy',
            'has_opening_hours': True
        }
    ]
    
    created_pages = []
    
    for castle in test_castles:
        try:
            filename = create_castle_page(castle)
            created_pages.append(filename)
            time.sleep(2)  # Rate limiting voor Wikipedia
        except Exception as e:
            print(f"❌ Fout bij {castle['title']}: {e}")
    
    print(f"\n✅ {len(created_pages)} kasteel paginas aangemaakt!")
    print("🎯 Test paginas klaar voor review")

if __name__ == "__main__":
    main()
