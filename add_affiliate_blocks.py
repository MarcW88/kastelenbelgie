#!/usr/bin/env python3
"""
Script pour ajouter des blocs d'affiliation sur les fiches château.
1. Remplace le formulaire de réservation par un bloc "Tickets en bezoeken" affilié
2. Corrige les incohérences de province/activités si détectées
"""

import os
import re
import glob

SITE_DIR = "/Users/marc/Desktop/kastelenbelgie"

# Liste des châteaux prioritaires pour l'affiliation (très touristiques)
PRIORITY_CASTLES = [
    'kasteel-van-freyr-freyr.html',
    'kasteel-van-bouchout-te-meise.html',
    'kasteel-reinhardstein-burg-metternich-te-weismes.html',
    'kasteel-van-veves-te-celles.html',
    'kasteel-van-la-roche-en-ardenne-la-roche-en-ardenne.html',
    'citadel-van-hoei-hoei.html',
    'kasteel-van-durbuy-durbuy.html',
    'kasteel-de-merode-westerlo.html',
    'kasteel-van-gaasbeek-lennik.html',
    'kasteel-van-seneffe-seneffe.html',
    'kasteel-van-bouillon-bouillon.html',
    'kasteel-van-montaigle-falaen.html',
    'kasteel-van-spontin-spontin.html',
    'kasteel-van-annevoie-annevoie.html',
]

# Coordonnées GPS correctes pour certains châteaux
GPS_CORRECTIONS = {
    'kasteel-van-freyr-freyr.html': {
        'lat': 50.2283,
        'lon': 4.8983,
        'address': 'Freyr 12, 5540 Hastière',
        'province': 'Namen'
    },
}

# Activités par province
PROVINCE_ACTIVITIES = {
    'Namen': [
        {'icon': '⛪', 'title': 'Citadel van Namen', 'desc': 'Bezoek de imposante citadel met panoramisch uitzicht'},
        {'icon': '🚤', 'title': 'Boottocht op de Maas', 'desc': 'Ontdek de Maasvallei vanaf het water'},
        {'icon': '🏰', 'title': 'Kasteel van Vêves', 'desc': 'Een van de mooiste middeleeuwse kastelen van België'},
        {'icon': '🌳', 'title': 'Tuinen van Annevoie', 'desc': 'Prachtige watertuinen in Franse stijl'},
    ],
    'Luik': [
        {'icon': '🏛️', 'title': 'Citadel van Luik', 'desc': 'Historische citadel met 373 trappen'},
        {'icon': '⛪', 'title': 'Kathedraal van Luik', 'desc': 'Bewonder de gotische architectuur'},
        {'icon': '🌳', 'title': 'Parc de la Boverie', 'desc': 'Wandel door dit prachtige stadspark'},
        {'icon': '🏰', 'title': 'Kasteel van Jehay', 'desc': 'Uniek schaakbordpatroon kasteel'},
    ],
    'Antwerpen': [
        {'icon': '🏛️', 'title': 'Rubenshuis Antwerpen', 'desc': 'Bezoek het voormalige huis en atelier van Rubens'},
        {'icon': '⛪', 'title': 'Onze-Lieve-Vrouwekathedraal', 'desc': 'Bewonder de gotische architectuur'},
        {'icon': '🌳', 'title': 'Rivierenhof Park', 'desc': 'Wandel door een van de mooiste parken'},
        {'icon': '🏰', 'title': 'Het Steen Museum', 'desc': 'Ontdek de geschiedenis van Antwerpen'},
    ],
}

def extract_castle_name(content):
    """Extrait le nom du château depuis le H1"""
    match = re.search(r'<h1>([^<]+)</h1>', content)
    if match:
        return match.group(1).strip()
    return None

def extract_province_from_breadcrumb(content):
    """Extrait la province depuis le breadcrumb"""
    match = re.search(r'<a href="([^"]+)\.html">([^<]+)</a>\s*<span class="breadcrumbs-separator">›</span>\s*<span class="breadcrumbs-current">', content)
    if match:
        return match.group(2).strip()
    return None

def generate_affiliate_block(castle_name):
    """Génère le bloc d'affiliation pour remplacer le formulaire"""
    return f'''<!-- Section 6: Tickets en bezoeken (Affiliate) -->
<section class="reservation-form">
<div class="container">
<h2>🎟️ Tickets en bezoeken voor {castle_name}</h2>
<div class="form-intro">
<p>Wil je {castle_name} bezoeken? Raadpleeg de officiële ticketpagina's van onze partners voor actuele openingsuren, tarieven en rondleidingen.</p>
</div>
<div class="ticket-links" style="display: flex; flex-direction: column; gap: 1rem; max-width: 400px; margin: 2rem auto;">
<a class="btn-modern btn-primary-modern" href="https://www.tripadvisor.com/Search?q={castle_name.replace(' ', '+')}" target="_blank" rel="nofollow sponsored" style="text-align: center; padding: 1rem 2rem;">
🎟️ Bekijk tickets en bezoeken op Tripadvisor
</a>
<a class="btn-modern btn-secondary-modern" href="https://www.viator.com/searchResults/all?text={castle_name.replace(' ', '+')}" target="_blank" rel="nofollow sponsored" style="text-align: center; padding: 1rem 2rem;">
👣 Bekijk rondleidingen op Viator
</a>
</div>
<p class="form-note" style="text-align: center; margin-top: 1.5rem; color: #666; font-size: 0.9rem;">
Je reserveert rechtstreeks via onze partners. Kastelenbelgie.be verkoopt zelf geen tickets, maar helpt je op weg met informatie en links.
</p>
</div>
</section>'''

def generate_activities_block(castle_name, province):
    """Génère le bloc d'activités locales"""
    activities = PROVINCE_ACTIVITIES.get(province, PROVINCE_ACTIVITIES['Antwerpen'])
    
    activities_html = ''
    for act in activities:
        activities_html += f'<div class="activity-item"><h3>{act["icon"]} {act["title"]}</h3><p>{act["desc"]}</p></div>'
    
    return f'''<section class="castle-activities">
<div class="container">
<h2>Wat doen in de buurt van {castle_name}?</h2>
<div class="activities-content">
<p>Combineer je bezoek aan {castle_name} met andere bezienswaardigheden in de provincie {province}.</p>
<div class="activities-grid">
{activities_html}
</div>
</div>
</div>
</section>'''

def fix_castle_page(filepath):
    """Corrige une page château et ajoute le bloc affilié"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        castle_name = extract_castle_name(content)
        province = extract_province_from_breadcrumb(content)
        
        if not castle_name:
            return False
        
        filename = os.path.basename(filepath)
        
        # Vérifier si c'est un château prioritaire
        if filename not in PRIORITY_CASTLES:
            return False
        
        # Corrections spécifiques pour certains châteaux
        if filename in GPS_CORRECTIONS:
            corrections = GPS_CORRECTIONS[filename]
            
            # Corriger la province dans l'info box
            content = re.sub(
                r'<span class="meta-value">Antwerpen</span>',
                f'<span class="meta-value">{corrections["province"]}</span>',
                content
            )
            
            # Corriger l'adresse dans la carte
            content = re.sub(
                r'<p><strong>Adres:</strong> Antwerpen, België</p>',
                f'<p><strong>Adres:</strong> {corrections["address"]}</p>',
                content
            )
            
            # Corriger les coordonnées OpenStreetMap
            old_osm = r'https://www\.openstreetmap\.org/export/embed\.html\?bbox=[^"]+&amp;layer=mapnik&amp;marker=[^"]+'
            new_osm = f'https://www.openstreetmap.org/export/embed.html?bbox={corrections["lon"]-0.01},{corrections["lat"]-0.01},{corrections["lon"]+0.01},{corrections["lat"]+0.01}&amp;layer=mapnik&amp;marker={corrections["lat"]},{corrections["lon"]}'
            content = re.sub(old_osm, new_osm, content)
            
            # Corriger les liens Google Maps
            content = re.sub(
                r'https://www\.google\.com/maps/search/[0-9.]+,[0-9.]+',
                f'https://www.google.com/maps/search/{corrections["lat"]},{corrections["lon"]}',
                content
            )
            content = re.sub(
                r'https://www\.google\.com/maps/dir//[0-9.]+,[0-9.]+',
                f'https://www.google.com/maps/dir//{corrections["lat"]},{corrections["lon"]}',
                content
            )
            
            province = corrections["province"]
        
        # Remplacer le formulaire par le bloc affilié
        form_pattern = r'<!-- Section 6: Reservatieformulier -->.*?</section>'
        affiliate_block = generate_affiliate_block(castle_name)
        content = re.sub(form_pattern, affiliate_block, content, flags=re.DOTALL)
        
        # Remplacer les activités par des activités locales correctes
        if province:
            activities_pattern = r'<section class="castle-activities">.*?</section>'
            activities_block = generate_activities_block(castle_name, province)
            content = re.sub(activities_pattern, activities_block, content, flags=re.DOTALL)
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✅ {filename}")
            return True
        return False
    except Exception as e:
        print(f"  ❌ Erreur {filepath}: {e}")
        return False

def main():
    print("🏰 Ajout des blocs d'affiliation sur les châteaux prioritaires...\n")
    
    fixed = 0
    for castle_file in PRIORITY_CASTLES:
        filepath = os.path.join(SITE_DIR, castle_file)
        if os.path.exists(filepath):
            if fix_castle_page(filepath):
                fixed += 1
        else:
            print(f"  ⚠️ Fichier non trouvé: {castle_file}")
    
    print(f"\n✅ {fixed} pages modifiées avec blocs d'affiliation")

if __name__ == "__main__":
    main()
