#!/usr/bin/env python3
"""
Script pour appliquer le design sobre sur les pages château.
- Hero avec badge sobre, tagline, heures lisibles
- Section Waarom bezoeken sobre
- Carte tickets sobre
- Sans emojis excessifs, couleurs cohérentes avec la charte
"""

import os
import re

SITE_DIR = "/Users/marc/Desktop/kastelenbelgie"

# Châteaux avec données personnalisées
CASTLE_DATA = {
    'kasteel-van-freyr-freyr.html': {
        'name': 'Kasteel van Freÿr',
        'badge': 'Populair kasteel in de Maasvallei',
        'tagline': 'Historisch renaissancekasteel met prachtige Franse tuinen, uitzicht op de Maas en een van de oudste oranjerieën van de Lage Landen.',
        'reasons': [
            {'title': 'Unieke ligging aan de Maas', 'desc': 'Geniet van het adembenemende uitzicht op de Maasvallei en de indrukwekkende rotsformaties rond het kasteel.'},
            {'title': 'Historisch interieur en tuinen', 'desc': 'Ontdek de stijlvolle salons, symmetrische Franse tuinen en de meer dan 300 jaar oude oranjerie.'},
            {'title': 'Ideaal voor een daguitstap', 'desc': 'Combineer je bezoek met Dinant, een boottocht op de Maas of een wandeling in de omgeving.'},
        ],
        'highlight': 'Dit kasteel staat in onze selectie <a href="blog-mooiste-kastelen-belgie.html">mooiste kastelen van België</a>.',
        'province': 'Namen',
        'address': 'Freyr 12, 5540 Hastière',
        'visit': 'Kasteel en tuinen bezoekbaar',
    },
    'kasteel-van-bouchout-te-meise.html': {
        'name': 'Kasteel van Bouchout',
        'badge': 'Iconisch kasteel in de Plantentuin',
        'tagline': 'Middeleeuws kasteel gelegen in een van de grootste botanische tuinen van de wereld, perfect voor natuur- en geschiedenisliefhebbers.',
        'reasons': [
            {'title': 'Plantentuin van Meise', 'desc': 'Bezoek het kasteel én ontdek 18.000 plantensoorten in de prachtige Nationale Plantentuin.'},
            {'title': 'Rijke geschiedenis', 'desc': 'Ontdek de verhalen van keizerin Charlotte en de middeleeuwse oorsprong van dit imposante kasteel.'},
            {'title': 'Wandelen in de natuur', 'desc': 'Combineer cultuur met een ontspannende wandeling door 92 hectare tuinen en bossen.'},
        ],
        'highlight': 'Ideaal voor een familieuitstap nabij Brussel.',
        'province': 'Vlaams-Brabant',
        'address': 'Nieuwelaan 38, 1860 Meise',
        'visit': 'Kasteel en tuinen bezoekbaar',
    },
    'kasteel-reinhardstein-burg-metternich-te-weismes.html': {
        'name': 'Kasteel Reinhardstein',
        'badge': 'Spectaculair middeleeuws kasteel',
        'tagline': 'Indrukwekkende burcht op een rots in de Warche-vallei, volledig gerestaureerd met authentiek middeleeuws interieur.',
        'reasons': [
            {'title': 'Adembenemende locatie', 'desc': 'Gelegen op een rots boven de Warche-vallei, met spectaculair uitzicht op de Ardennen.'},
            {'title': 'Authentiek middeleeuws', 'desc': 'Ontdek wapens, harnassen, tapijten en meubels uit de 14e-17e eeuw.'},
            {'title': 'Combineer met wandelen', 'desc': 'Start je wandeling naar de waterval van Reinhardstein direct bij het kasteel.'},
        ],
        'highlight': 'Een van de best bewaarde middeleeuwse kastelen van België.',
        'province': 'Luik',
        'address': 'Chemin du Cheneux 50, 4950 Waimes',
        'visit': 'Rondleidingen op afspraak',
    },
    'kasteel-van-veves-te-celles.html': {
        'name': 'Kasteel van Vêves',
        'badge': 'Sprookjeskasteel uit de 15e eeuw',
        'tagline': 'Pittoresk middeleeuws kasteel met vijf torens, prachtig bewaard en nog steeds bewoond door dezelfde familie sinds 1410.',
        'reasons': [
            {'title': 'Authentiek sprookjeskasteel', 'desc': 'Met vijf ronde torens en een slotgracht lijkt dit kasteel recht uit een sprookje te komen.'},
            {'title': '600 jaar familiegeschiedenis', 'desc': 'Nog steeds bewoond door de familie Liedekerke-Beaufort, die het sinds 1410 bezit.'},
            {'title': 'Interactieve rondleidingen', 'desc': 'Ontdek het kasteel met boeiende verhalen over ridders, edelen en het dagelijks leven.'},
        ],
        'highlight': 'Regelmatig gebruikt als filmlocatie dankzij de sprookjesachtige uitstraling.',
        'province': 'Namen',
        'address': 'Rue de Furfooz 3, 5561 Celles',
        'visit': 'Kasteel bezoekbaar met rondleiding',
    },
    'kasteel-van-la-roche-en-ardenne-la-roche-en-ardenne.html': {
        'name': 'Kasteel van La Roche-en-Ardenne',
        'badge': 'Imposante kasteelruïne',
        'tagline': 'Middeleeuwse ruïne met panoramisch uitzicht over La Roche en de Ourthe-vallei, ideaal startpunt voor Ardennen-avonturen.',
        'reasons': [
            {'title': 'Panoramisch uitzicht', 'desc': 'Geniet van een adembenemend uitzicht over het stadje La Roche en de groene Ourthe-vallei.'},
            {'title': 'Middeleeuwse geschiedenis', 'desc': 'Ontdek de rijke geschiedenis van deze 9e-eeuwse burcht en zijn rol in de regio.'},
            {'title': 'Avontuur in de Ardennen', 'desc': 'Combineer met kayakken, mountainbiken of wandelen in de prachtige omgeving.'},
        ],
        'highlight': 'Perfecte stop tijdens een weekend in de Ardennen.',
        'province': 'Luxemburg',
        'address': 'Rue du Vieux Château 4, 6980 La Roche-en-Ardenne',
        'visit': 'Ruïne vrij toegankelijk',
    },
    'citadel-van-hoei-hoei.html': {
        'name': 'Citadel van Hoei',
        'badge': 'Historische citadel met 373 trappen',
        'tagline': 'Imposante citadel boven de Maas met een bewogen geschiedenis en spectaculair uitzicht over Hoei en de Maasvallei.',
        'reasons': [
            {'title': 'De beroemde 373 trappen', 'desc': 'Beklim de iconische trap of neem de kabelbaan voor een onvergetelijk uitzicht.'},
            {'title': 'Rijke oorlogsgeschiedenis', 'desc': 'Ontdek het verleden als gevangenis tijdens WOII en de verhalen van het verzet.'},
            {'title': 'Panoramisch uitzicht', 'desc': 'Geniet van een spectaculair uitzicht over de Maas, Hoei en de omliggende heuvels.'},
        ],
        'highlight': 'Gratis toegang tot de citadel en het museum.',
        'province': 'Luik',
        'address': 'Rue des Coteaux, 4500 Huy',
        'visit': 'Citadel en museum bezoekbaar',
    },
    'kasteel-van-durbuy-durbuy.html': {
        'name': 'Kasteel van Durbuy',
        'badge': 'Kasteel in het kleinste stadje',
        'tagline': 'Middeleeuws kasteel in het pittoreske Durbuy, de perfecte combinatie van geschiedenis, gastronomie en Ardense charme.',
        'reasons': [
            {'title': 'Kleinste stadje ter wereld', 'desc': 'Ontdek het charmante Durbuy met zijn kasseien, vakwerkhuizen en gezellige terrassen.'},
            {'title': 'Gastronomische hotspot', 'desc': 'Combineer je bezoek met een lunch in een van de vele uitstekende restaurants.'},
            {'title': 'Natuur en avontuur', 'desc': 'Wandel, kayak of bezoek het labyrint en de topiary-tuin in de buurt.'},
        ],
        'highlight': 'Ideaal voor een romantisch weekend of daguitstap.',
        'province': 'Luxemburg',
        'address': 'Rue Comte d\'Ursel, 6940 Durbuy',
        'visit': 'Buitenzijde vrij toegankelijk',
    },
    'kasteel-de-merode-westerlo.html': {
        'name': 'Kasteel de Merode',
        'badge': 'Imposant waterkasteel',
        'tagline': 'Prachtig waterkasteel omgeven door een slotgracht, al eeuwenlang in bezit van de adellijke familie de Merode.',
        'reasons': [
            {'title': 'Romantisch waterkasteel', 'desc': 'Bewonder het kasteel omringd door water, met zijn karakteristieke torens en bruggen.'},
            {'title': 'Adellijke geschiedenis', 'desc': 'Ontdek de verhalen van de familie de Merode, een van de oudste adellijke families van België.'},
            {'title': 'Kasteeldomein en park', 'desc': 'Wandel door het uitgestrekte kasteeldomein met oude bomen en pittoreske vijvers.'},
        ],
        'highlight': 'Regelmatig open voor evenementen en speciale gelegenheden.',
        'province': 'Antwerpen',
        'address': 'Kasteelpark convergentiecentrum, 2260 Westerlo',
        'visit': 'Park toegankelijk, kasteel op afspraak',
    },
    'kasteel-van-seneffe-seneffe.html': {
        'name': 'Kasteel van Seneffe',
        'badge': 'Meesterwerk 18e-eeuwse architectuur',
        'tagline': 'Schitterend neoklassiek kasteel met een museum voor zilverwerk en een van de mooiste Engelse tuinen van België.',
        'reasons': [
            {'title': 'Neoklassieke pracht', 'desc': 'Bewonder de elegante architectuur en de rijke interieurs van dit 18e-eeuwse meesterwerk.'},
            {'title': 'Museum voor zilverwerk', 'desc': 'Ontdek een unieke collectie zilverwerk uit de 17e tot 20e eeuw.'},
            {'title': 'Prachtige Engelse tuinen', 'desc': 'Wandel door 22 hectare tuinen met vijvers, bruggen en romantische paviljoens.'},
        ],
        'highlight': 'Gratis toegang tot het park, ideaal voor een ontspannende wandeling.',
        'province': 'Henegouwen',
        'address': 'Rue Lucien Plasman 7-9, 7180 Seneffe',
        'visit': 'Kasteel en park bezoekbaar',
    },
    'kasteel-van-montaigle-falaen.html': {
        'name': 'Kasteel van Montaigle',
        'badge': 'Indrukwekkende kasteelruïne',
        'tagline': 'Romantische ruïne van een middeleeuws kasteel op een rots, met prachtig uitzicht over de groene Molignée-vallei.',
        'reasons': [
            {'title': 'Romantische ruïne', 'desc': 'Verken de imposante overblijfselen van dit 14e-eeuwse kasteel op een rotsachtige heuvel.'},
            {'title': 'Prachtig uitzicht', 'desc': 'Geniet van een spectaculair panorama over de groene Molignée-vallei.'},
            {'title': 'RAVeL en fietsen', 'desc': 'Combineer je bezoek met een fietstocht langs de oude spoorlijn door de vallei.'},
        ],
        'highlight': 'Perfecte stop tijdens een fietstocht door de Molignée-vallei.',
        'province': 'Namen',
        'address': 'Rue de Montaigle, 5522 Falaën',
        'visit': 'Ruïne bezoekbaar',
    },
    'kasteel-van-spontin-spontin.html': {
        'name': 'Kasteel van Spontin',
        'badge': 'Middeleeuws waterkasteel',
        'tagline': 'Pittoresk waterkasteel met torens en een slotgracht, prachtig gelegen aan de oevers van de Bocq.',
        'reasons': [
            {'title': 'Authentiek waterkasteel', 'desc': 'Bewonder dit goed bewaarde kasteel omringd door water en groen.'},
            {'title': 'Middeleeuwse charme', 'desc': 'Ontdek de torens, de slotgracht en de sfeer van een echt ridderkasteel.'},
            {'title': 'Wandelen langs de Bocq', 'desc': 'Combineer je bezoek met een wandeling langs de pittoreske Bocq-vallei.'},
        ],
        'highlight': 'Een van de mooiste waterkastelen van Wallonië.',
        'province': 'Namen',
        'address': 'Rue du Château 6, 5530 Spontin',
        'visit': 'Kasteel bezoekbaar op afspraak',
    },
}

def generate_sober_hero(castle_data):
    """Génère le hero sobre avec badge, tagline et heures lisibles"""
    return f'''<section class="castle-hero">
<div class="container">
<div class="castle-hero-content">
<div class="castle-image">
<img alt="{castle_data['name']}" loading="lazy" src="CASTLE_IMAGE_SRC"/>
</div>
<div class="castle-info-box">
<span class="castle-badge-sober">{castle_data['badge']}</span>
<h1>{castle_data['name']}</h1>
<p class="castle-tagline-sober">{castle_data['tagline']}</p>

<div class="castle-details-grid">
<div class="detail-column">
<div class="detail-item-sober">
<span class="detail-label">Provincie</span>
<span class="detail-value">{castle_data['province']}</span>
</div>
<div class="detail-item-sober">
<span class="detail-label">Adres</span>
<span class="detail-value">{castle_data['address']}</span>
</div>
<div class="detail-item-sober">
<span class="detail-label">Bezoek</span>
<span class="detail-value">{castle_data['visit']}</span>
</div>
</div>
<div class="detail-column">
<span class="detail-label">Openingsuren (indicatief)</span>
<ul class="opening-hours-list">
OPENING_HOURS_PLACEHOLDER
</ul>
</div>
</div>

<div class="castle-cta-sober">
<a class="btn-primary-hero" href="https://www.tripadvisor.com/Search?q={castle_data['name'].replace(' ', '+')}" target="_blank" rel="nofollow sponsored">
Tickets en bezoeken bekijken op Tripadvisor
</a>
<p class="cta-note-sober">Je reserveert rechtstreeks via onze partner.</p>
</div>
</div>
</div>
</div>
</section>'''

def generate_sober_reasons(castle_data):
    """Génère la section Waarom bezoeken sobre"""
    reasons_html = ''
    for reason in castle_data['reasons']:
        reasons_html += f'''
<div class="reason-card-sober">
<h3>{reason['title']}</h3>
<p>{reason['desc']}</p>
</div>'''
    
    highlight_html = ''
    if 'highlight' in castle_data:
        highlight_html = f'''
<div class="castle-highlight-sober">
<p>{castle_data['highlight']}</p>
</div>'''
    
    return f'''
<section class="castle-reasons-sober">
<div class="container">
<h2>Waarom {castle_data['name']} bezoeken?</h2>
<p class="section-subtitle">Ontdek wat dit kasteel zo bijzonder maakt</p>
<div class="reasons-grid-sober">
{reasons_html}
</div>
{highlight_html}
</div>
</section>
'''

def generate_sober_ticket_card(castle_data):
    """Génère la carte tickets sobre"""
    return f'''<section class="reservation-form" style="padding: 3rem 0;">
<div class="container">
<div class="ticket-card-sober">
<div class="ticket-card-header">
<h2>Tickets en rondleidingen</h2>
<p>Boek je bezoek aan {castle_data['name']}</p>
</div>
<div class="ticket-card-body">
<ul class="ticket-checklist">
<li><span class="check-icon">✓</span> Online tickets met actuele openingsuren</li>
<li><span class="check-icon">✓</span> Rondleidingen en combinaties met activiteiten</li>
<li><span class="check-icon">✓</span> Veilig reserveren via vertrouwde partners</li>
<li><span class="check-icon">✓</span> Gratis annulering bij veel opties</li>
</ul>
<div class="ticket-buttons">
<a class="btn-ticket-primary" href="https://www.tripadvisor.com/Search?q={castle_data['name'].replace(' ', '+')}" target="_blank" rel="nofollow sponsored">
Bekijk tickets op Tripadvisor
</a>
<a class="btn-ticket-secondary" href="https://www.viator.com/searchResults/all?text={castle_data['name'].replace(' ', '+')}" target="_blank" rel="nofollow sponsored">
Bekijk rondleidingen op Viator
</a>
</div>
<p class="ticket-note">Je reserveert rechtstreeks via onze partners. Kastelenbelgie.be verkoopt zelf geen tickets.</p>
</div>
</div>
</div>
</section>'''

def extract_image_src(content):
    """Extrait le src de l'image du château"""
    match = re.search(r'<div class="castle-image">\s*<img[^>]+src="([^"]+)"', content)
    if match:
        return match.group(1)
    return 'chateaux_images_update-2/default.jpg'

def extract_opening_hours(content):
    """Retourne les heures d'ouverture formatées"""
    # Heures standard pour les châteaux visitables
    return '''<li><span class="opening-hours-day">Maandag</span><span class="opening-hours-time opening-hours-closed">Gesloten</span></li>
<li><span class="opening-hours-day">Dinsdag</span><span class="opening-hours-time">10:00–17:00</span></li>
<li><span class="opening-hours-day">Woensdag</span><span class="opening-hours-time">10:00–17:00</span></li>
<li><span class="opening-hours-day">Donderdag</span><span class="opening-hours-time">10:00–17:00</span></li>
<li><span class="opening-hours-day">Vrijdag</span><span class="opening-hours-time">10:00–17:00</span></li>
<li><span class="opening-hours-day">Zaterdag</span><span class="opening-hours-time">10:00–17:00</span></li>
<li><span class="opening-hours-day">Zondag</span><span class="opening-hours-time">10:00–17:00</span></li>'''

def apply_sober_design(filepath, castle_data):
    """Applique le design sobre sur une page château"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # Extraire l'image et les heures
        image_src = extract_image_src(content)
        opening_hours = extract_opening_hours(content)
        
        # Générer le nouveau hero
        new_hero = generate_sober_hero(castle_data)
        new_hero = new_hero.replace('CASTLE_IMAGE_SRC', image_src)
        new_hero = new_hero.replace('OPENING_HOURS_PLACEHOLDER', opening_hours)
        
        # Remplacer le hero existant
        content = re.sub(
            r'<!-- Section 1: Hero avec image et info box -->.*?</section>',
            new_hero,
            content,
            flags=re.DOTALL
        )
        
        # Remplacer la section Waarom bezoeken
        new_reasons = generate_sober_reasons(castle_data)
        content = re.sub(
            r'<!-- Section: Waarom bezoeken\? -->.*?</section>\s*</section>',
            new_reasons + '\n</section>',
            content,
            flags=re.DOTALL
        )
        
        # Remplacer la section tickets
        new_tickets = generate_sober_ticket_card(castle_data)
        content = re.sub(
            r'<!-- Section: Tickets & Reserveren \(Booking-style\) -->.*?</section>',
            new_tickets,
            content,
            flags=re.DOTALL
        )
        
        # Aussi remplacer l'ancien format si présent
        content = re.sub(
            r'<!-- Section 6: Tickets en bezoeken \(Affiliate\) -->.*?</section>',
            new_tickets,
            content,
            flags=re.DOTALL
        )
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✅ {os.path.basename(filepath)}")
            return True
        else:
            print(f"  ⚠️ Pas de changement: {os.path.basename(filepath)}")
        return False
    except Exception as e:
        print(f"  ❌ Erreur {filepath}: {e}")
        return False

def main():
    print("🎨 Application du design sobre sur les pages château...\n")
    
    updated = 0
    for filename, castle_data in CASTLE_DATA.items():
        filepath = os.path.join(SITE_DIR, filename)
        if os.path.exists(filepath):
            if apply_sober_design(filepath, castle_data):
                updated += 1
        else:
            print(f"  ⚠️ Fichier non trouvé: {filename}")
    
    print(f"\n✅ {updated} pages mises à jour avec le design sobre")

if __name__ == "__main__":
    main()
