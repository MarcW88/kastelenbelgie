#!/usr/bin/env python3
"""
Script pour améliorer l'UX des pages château style Booking/TripAdvisor.
1. Badge + tagline + CTA dans le hero (above the fold)
2. Section "Waarom bezoeken?" avec 3 cartes avantages
3. Section Tickets transformée en carte de réservation
"""

import os
import re
import glob

SITE_DIR = "/Users/marc/Desktop/kastelenbelgie"

# Châteaux prioritaires avec données personnalisées
CASTLE_DATA = {
    'kasteel-van-freyr-freyr.html': {
        'name': 'Kasteel van Freÿr',
        'badge': '⭐ Populair kasteel in de Maasvallei • Ideaal voor een daguitstap',
        'tagline': 'Historisch renaissancekasteel met prachtige Franse tuinen, uitzicht op de Maas en een van de oudste oranjerieën van de Lage Landen.',
        'reasons': [
            {'icon': '🌳', 'title': 'Unieke ligging aan de Maas', 'desc': 'Geniet van het adembenemende uitzicht op de Maasvallei en de indrukwekkende rotsformaties rond het kasteel.'},
            {'icon': '🏰', 'title': 'Historisch interieur & tuinen', 'desc': 'Ontdek de stijlvolle salons, symmetrische Franse tuinen en de meer dan 300 jaar oude oranjerie.'},
            {'icon': '👨‍👩‍👧‍👦', 'title': 'Ideaal voor een daguitstap', 'desc': 'Combineer je bezoek met Dinant, een boottocht op de Maas of een wandeling in de omgeving.'},
        ],
        'highlight': 'Dit kasteel staat in onze selectie <a href="blog-mooiste-kastelen-belgie.html" style="color: #C89A3B;">mooiste kastelen van België</a>.',
    },
    'kasteel-van-bouchout-te-meise.html': {
        'name': 'Kasteel van Bouchout',
        'badge': '⭐ Iconisch kasteel in de Plantentuin van Meise',
        'tagline': 'Middeleeuws kasteel gelegen in een van de grootste botanische tuinen van de wereld, perfect voor natuur- en geschiedenisliefhebbers.',
        'reasons': [
            {'icon': '🌺', 'title': 'Plantentuin van Meise', 'desc': 'Bezoek het kasteel én ontdek 18.000 plantensoorten in de prachtige Nationale Plantentuin.'},
            {'icon': '🏰', 'title': 'Rijke geschiedenis', 'desc': 'Ontdek de verhalen van keizerin Charlotte en de middeleeuwse oorsprong van dit imposante kasteel.'},
            {'icon': '🚶', 'title': 'Wandelen in de natuur', 'desc': 'Combineer cultuur met een ontspannende wandeling door 92 hectare tuinen en bossen.'},
        ],
        'highlight': 'Ideaal voor een familieuitstap nabij Brussel.',
    },
    'kasteel-reinhardstein-burg-metternich-te-weismes.html': {
        'name': 'Kasteel Reinhardstein',
        'badge': '⭐ Spectaculair middeleeuws kasteel in de Ardennen',
        'tagline': 'Indrukwekkende burcht op een rots in de Warche-vallei, volledig gerestaureerd met authentiek middeleeuws interieur.',
        'reasons': [
            {'icon': '🏔️', 'title': 'Adembenemende locatie', 'desc': 'Gelegen op een rots boven de Warche-vallei, met spectaculair uitzicht op de Ardennen.'},
            {'icon': '⚔️', 'title': 'Authentiek middeleeuws', 'desc': 'Ontdek wapens, harnassen, tapijten en meubels uit de 14e-17e eeuw.'},
            {'icon': '🥾', 'title': 'Combineer met wandelen', 'desc': 'Start je wandeling naar de waterval van Reinhardstein direct bij het kasteel.'},
        ],
        'highlight': 'Een van de best bewaarde middeleeuwse kastelen van België.',
    },
    'kasteel-van-veves-te-celles.html': {
        'name': 'Kasteel van Vêves',
        'badge': '⭐ Sprookjeskasteel uit de 15e eeuw',
        'tagline': 'Pittoresk middeleeuws kasteel met vijf torens, prachtig bewaard en nog steeds bewoond door dezelfde familie sinds 1410.',
        'reasons': [
            {'icon': '🏰', 'title': 'Authentiek sprookjeskasteel', 'desc': 'Met vijf ronde torens en een slotgracht lijkt dit kasteel recht uit een sprookje te komen.'},
            {'icon': '👑', 'title': '600 jaar familiegeschiedenis', 'desc': 'Nog steeds bewoond door de familie Liedekerke-Beaufort, die het sinds 1410 bezit.'},
            {'icon': '🎭', 'title': 'Interactieve rondleidingen', 'desc': 'Ontdek het kasteel met boeiende verhalen over ridders, edelen en het dagelijks leven.'},
        ],
        'highlight': 'Regelmatig gebruikt als filmlocatie dankzij de sprookjesachtige uitstraling.',
    },
    'kasteel-van-la-roche-en-ardenne-la-roche-en-ardenne.html': {
        'name': 'Kasteel van La Roche-en-Ardenne',
        'badge': '⭐ Imposante kasteelruïne in het hart van de Ardennen',
        'tagline': 'Middeleeuwse ruïne met panoramisch uitzicht over La Roche en de Ourthe-vallei, ideaal startpunt voor Ardennen-avonturen.',
        'reasons': [
            {'icon': '🏔️', 'title': 'Panoramisch uitzicht', 'desc': 'Geniet van een adembenemend uitzicht over het stadje La Roche en de groene Ourthe-vallei.'},
            {'icon': '⚔️', 'title': 'Middeleeuwse geschiedenis', 'desc': 'Ontdek de rijke geschiedenis van deze 9e-eeuwse burcht en zijn rol in de regio.'},
            {'icon': '🚣', 'title': 'Avontuur in de Ardennen', 'desc': 'Combineer met kayakken, mountainbiken of wandelen in de prachtige omgeving.'},
        ],
        'highlight': 'Perfecte stop tijdens een weekend in de Ardennen.',
    },
    'citadel-van-hoei-hoei.html': {
        'name': 'Citadel van Hoei',
        'badge': '⭐ Historische citadel met 373 trappen',
        'tagline': 'Imposante citadel boven de Maas met een bewogen geschiedenis en spectaculair uitzicht over Hoei en de Maasvallei.',
        'reasons': [
            {'icon': '🪜', 'title': 'De beroemde 373 trappen', 'desc': 'Beklim de iconische trap of neem de kabelbaan voor een onvergetelijk uitzicht.'},
            {'icon': '📜', 'title': 'Rijke oorlogsgeschiedenis', 'desc': 'Ontdek het verleden als gevangenis tijdens WOII en de verhalen van het verzet.'},
            {'icon': '🌅', 'title': 'Panoramisch uitzicht', 'desc': 'Geniet van een spectaculair uitzicht over de Maas, Hoei en de omliggende heuvels.'},
        ],
        'highlight': 'Gratis toegang tot de citadel en het museum.',
    },
    'kasteel-van-durbuy-durbuy.html': {
        'name': 'Kasteel van Durbuy',
        'badge': '⭐ Kasteel in het kleinste stadje ter wereld',
        'tagline': 'Middeleeuws kasteel in het pittoreske Durbuy, de perfecte combinatie van geschiedenis, gastronomie en Ardense charme.',
        'reasons': [
            {'icon': '🏘️', 'title': 'Kleinste stadje ter wereld', 'desc': 'Ontdek het charmante Durbuy met zijn kasseien, vakwerkhuizen en gezellige terrassen.'},
            {'icon': '🍽️', 'title': 'Gastronomische hotspot', 'desc': 'Combineer je bezoek met een lunch in een van de vele uitstekende restaurants.'},
            {'icon': '🌲', 'title': 'Natuur & avontuur', 'desc': 'Wandel, kayak of bezoek het labyrint en de topiary-tuin in de buurt.'},
        ],
        'highlight': 'Ideaal voor een romantisch weekend of daguitstap.',
    },
    'kasteel-de-merode-westerlo.html': {
        'name': 'Kasteel de Merode',
        'badge': '⭐ Imposant waterkasteel in de Kempen',
        'tagline': 'Prachtig waterkasteel omgeven door een slotgracht, al eeuwenlang in bezit van de adellijke familie de Merode.',
        'reasons': [
            {'icon': '💧', 'title': 'Romantisch waterkasteel', 'desc': 'Bewonder het kasteel omringd door water, met zijn karakteristieke torens en bruggen.'},
            {'icon': '👑', 'title': 'Adellijke geschiedenis', 'desc': 'Ontdek de verhalen van de familie de Merode, een van de oudste adellijke families van België.'},
            {'icon': '🌳', 'title': 'Kasteeldomein & park', 'desc': 'Wandel door het uitgestrekte kasteeldomein met oude bomen en pittoreske vijvers.'},
        ],
        'highlight': 'Regelmatig open voor evenementen en speciale gelegenheden.',
    },
    'kasteel-van-seneffe-seneffe.html': {
        'name': 'Kasteel van Seneffe',
        'badge': '⭐ Meesterwerk van 18e-eeuwse architectuur',
        'tagline': 'Schitterend neoklassiek kasteel met een museum voor zilverwerk en een van de mooiste Engelse tuinen van België.',
        'reasons': [
            {'icon': '🏛️', 'title': 'Neoklassieke pracht', 'desc': 'Bewonder de elegante architectuur en de rijke interieurs van dit 18e-eeuwse meesterwerk.'},
            {'icon': '🥈', 'title': 'Museum voor zilverwerk', 'desc': 'Ontdek een unieke collectie zilverwerk uit de 17e tot 20e eeuw.'},
            {'icon': '🌳', 'title': 'Prachtige Engelse tuinen', 'desc': 'Wandel door 22 hectare tuinen met vijvers, bruggen en romantische paviljoens.'},
        ],
        'highlight': 'Gratis toegang tot het park, ideaal voor een ontspannende wandeling.',
    },
    'kasteel-van-montaigle-falaen.html': {
        'name': 'Kasteel van Montaigle',
        'badge': '⭐ Indrukwekkende kasteelruïne in de Molignée-vallei',
        'tagline': 'Romantische ruïne van een middeleeuws kasteel op een rots, met prachtig uitzicht over de groene Molignée-vallei.',
        'reasons': [
            {'icon': '🏚️', 'title': 'Romantische ruïne', 'desc': 'Verken de imposante overblijfselen van dit 14e-eeuwse kasteel op een rotsachtige heuvel.'},
            {'icon': '🌄', 'title': 'Prachtig uitzicht', 'desc': 'Geniet van een spectaculair panorama over de groene Molignée-vallei.'},
            {'icon': '🚴', 'title': 'RAVeL & fietsen', 'desc': 'Combineer je bezoek met een fietstocht langs de oude spoorlijn door de vallei.'},
        ],
        'highlight': 'Perfecte stop tijdens een fietstocht door de Molignée-vallei.',
    },
    'kasteel-van-spontin-spontin.html': {
        'name': 'Kasteel van Spontin',
        'badge': '⭐ Middeleeuws waterkasteel in de Bocq-vallei',
        'tagline': 'Pittoresk waterkasteel met torens en een slotgracht, prachtig gelegen aan de oevers van de Bocq.',
        'reasons': [
            {'icon': '💧', 'title': 'Authentiek waterkasteel', 'desc': 'Bewonder dit goed bewaarde kasteel omringd door water en groen.'},
            {'icon': '🏰', 'title': 'Middeleeuwse charme', 'desc': 'Ontdek de torens, de slotgracht en de sfeer van een echt ridderkasteel.'},
            {'icon': '🥾', 'title': 'Wandelen langs de Bocq', 'desc': 'Combineer je bezoek met een wandeling langs de pittoreske Bocq-vallei.'},
        ],
        'highlight': 'Een van de mooiste waterkastelen van Wallonië.',
    },
}

def extract_castle_name(content):
    """Extrait le nom du château depuis le H1"""
    match = re.search(r'<h1>([^<]+)</h1>', content)
    if match:
        return match.group(1).strip()
    return None

def generate_hero_upgrade(castle_data):
    """Génère le badge, tagline et CTA pour le hero"""
    return f'''
<!-- Badge & Tagline -->
<div class="castle-badge" style="background: linear-gradient(135deg, #C89A3B 0%, #A67C2E 100%); color: white; padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.85rem; font-weight: 600; display: inline-block; margin-bottom: 1rem;">
{castle_data['badge']}
</div>

<p class="castle-tagline" style="color: #666; font-size: 1rem; line-height: 1.6; margin-bottom: 1.5rem; font-style: italic;">
{castle_data['tagline']}
</p>
'''

def generate_hero_cta(castle_name):
    """Génère le CTA principal dans le hero"""
    return f'''
<!-- CTA Principal dans Hero -->
<div class="castle-cta" style="margin-top: 1.5rem; padding-top: 1.5rem; border-top: 1px solid #eee;">
<a class="btn-modern btn-primary-modern" href="https://www.tripadvisor.com/Search?q={castle_name.replace(' ', '+')}" target="_blank" rel="nofollow sponsored" style="display: block; text-align: center; padding: 1rem 2rem; font-size: 1.1rem; background: linear-gradient(135deg, #00aa6c 0%, #008f5a 100%); border: none; box-shadow: 0 4px 15px rgba(0,170,108,0.3);">
🎟️ Bekijk tickets & bezoeken op Tripadvisor
</a>
<p class="cta-note" style="text-align: center; margin-top: 0.75rem; color: #888; font-size: 0.8rem;">
Je boekt veilig via onze partner. Kastelenbelgie.be helpt je met info en inspiratie.
</p>
</div>
'''

def generate_reasons_section(castle_name, castle_data):
    """Génère la section 'Waarom bezoeken?'"""
    reasons_html = ''
    for reason in castle_data['reasons']:
        reasons_html += f'''
<div class="reason-card" style="background: white; padding: 1.5rem; border-radius: 12px; box-shadow: 0 2px 10px rgba(0,0,0,0.08); transition: transform 0.2s, box-shadow 0.2s;">
<div style="font-size: 2rem; margin-bottom: 0.75rem;">{reason['icon']}</div>
<h3 style="font-size: 1.1rem; font-weight: 700; color: #1E2523; margin-bottom: 0.5rem;">{reason['title']}</h3>
<p style="color: #666; font-size: 0.95rem; line-height: 1.5; margin: 0;">{reason['desc']}</p>
</div>'''
    
    highlight_html = ''
    if 'highlight' in castle_data:
        highlight_html = f'''
<div style="text-align: center; margin-top: 2rem;">
<p style="display: inline-block; background: #FFF8E7; padding: 0.75rem 1.5rem; border-radius: 8px; color: #1E2523; font-size: 0.95rem;">
🌟 {castle_data['highlight']}
</p>
</div>'''
    
    return f'''
<!-- Section: Waarom bezoeken? -->
<section class="castle-reasons" style="background: #F8F9FA; padding: 3rem 0;">
<div class="container">
<h2 style="text-align: center; font-size: 1.75rem; font-weight: 700; color: #1E2523; margin-bottom: 0.5rem;">Waarom {castle_name} bezoeken?</h2>
<p style="text-align: center; color: #666; margin-bottom: 2rem;">Ontdek wat dit kasteel zo bijzonder maakt</p>
<div class="reasons-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem;">
{reasons_html}
</div>
{highlight_html}
</div>
</section>
'''

def generate_ticket_card(castle_name):
    """Génère la carte de réservation style Booking"""
    return f'''<!-- Section: Tickets & Reserveren (Booking-style) -->
<section class="reservation-form" style="padding: 3rem 0;">
<div class="container">
<div class="ticket-card" style="background: white; border-radius: 16px; box-shadow: 0 4px 20px rgba(0,0,0,0.1); overflow: hidden; max-width: 600px; margin: 0 auto;">

<!-- Card Header -->
<div style="background: linear-gradient(135deg, #1E2523 0%, #2D3A36 100%); padding: 1.5rem 2rem; color: white;">
<h2 style="margin: 0; font-size: 1.4rem; font-weight: 700;">🎟️ Tickets & rondleidingen</h2>
<p style="margin: 0.5rem 0 0 0; opacity: 0.9; font-size: 0.95rem;">Boek je bezoek aan {castle_name}</p>
</div>

<!-- Card Body -->
<div style="padding: 2rem;">

<!-- Checklist -->
<ul style="list-style: none; padding: 0; margin: 0 0 1.5rem 0;">
<li style="display: flex; align-items: center; gap: 0.75rem; padding: 0.5rem 0; color: #333;">
<span style="color: #00aa6c; font-size: 1.2rem;">✓</span>
<span>Online tickets met actuele openingsuren</span>
</li>
<li style="display: flex; align-items: center; gap: 0.75rem; padding: 0.5rem 0; color: #333;">
<span style="color: #00aa6c; font-size: 1.2rem;">✓</span>
<span>Rondleidingen en combinaties met activiteiten</span>
</li>
<li style="display: flex; align-items: center; gap: 0.75rem; padding: 0.5rem 0; color: #333;">
<span style="color: #00aa6c; font-size: 1.2rem;">✓</span>
<span>Veilig reserveren via vertrouwde partners</span>
</li>
<li style="display: flex; align-items: center; gap: 0.75rem; padding: 0.5rem 0; color: #333;">
<span style="color: #00aa6c; font-size: 1.2rem;">✓</span>
<span>Gratis annulering bij veel opties</span>
</li>
</ul>

<!-- CTA Buttons -->
<div style="display: flex; flex-direction: column; gap: 0.75rem;">
<a href="https://www.tripadvisor.com/Search?q={castle_name.replace(' ', '+')}" target="_blank" rel="nofollow sponsored" style="display: flex; align-items: center; justify-content: center; gap: 0.5rem; background: linear-gradient(135deg, #00aa6c 0%, #008f5a 100%); color: white; padding: 1rem 2rem; border-radius: 8px; text-decoration: none; font-weight: 600; font-size: 1rem; box-shadow: 0 4px 15px rgba(0,170,108,0.3); transition: transform 0.2s;">
<span style="font-size: 1.2rem;">🎟️</span> Bekijk tickets op Tripadvisor
</a>
<a href="https://www.viator.com/searchResults/all?text={castle_name.replace(' ', '+')}" target="_blank" rel="nofollow sponsored" style="display: flex; align-items: center; justify-content: center; gap: 0.5rem; background: white; color: #1E2523; padding: 1rem 2rem; border-radius: 8px; text-decoration: none; font-weight: 600; font-size: 1rem; border: 2px solid #1E2523; transition: background 0.2s;">
<span style="font-size: 1.2rem;">👣</span> Bekijk rondleidingen op Viator
</a>
</div>

<!-- Trust Note -->
<p style="text-align: center; margin: 1.5rem 0 0 0; color: #888; font-size: 0.85rem; line-height: 1.5;">
Je reserveert rechtstreeks via onze partners.<br/>
Kastelenbelgie.be verkoopt zelf geen tickets, maar helpt je bij het plannen van je bezoek.
</p>

</div>
</div>
</div>
</section>'''

def upgrade_castle_page(filepath, castle_data):
    """Améliore une page château avec le nouveau design UX"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        castle_name = castle_data['name']
        
        # 1. Ajouter badge + tagline après le H1
        hero_upgrade = generate_hero_upgrade(castle_data)
        content = re.sub(
            r'(<h1>[^<]+</h1>)',
            r'\1' + hero_upgrade,
            content
        )
        
        # 2. Ajouter CTA dans le hero (après castle-details)
        hero_cta = generate_hero_cta(castle_name)
        content = re.sub(
            r'(</div>\s*</div>\s*</div>\s*</div>\s*</section>\s*<!-- Section 2:)',
            hero_cta + r'\n</div>\n</div>\n</div>\n</section>\n<!-- Section 2:',
            content
        )
        
        # 3. Ajouter section "Waarom bezoeken?" après l'intro
        reasons_section = generate_reasons_section(castle_name, castle_data)
        content = re.sub(
            r'(</section>\s*<!-- Section 3: Activiteiten)',
            reasons_section + r'\n</section>\n<!-- Section 3: Activiteiten',
            content
        )
        
        # 4. Remplacer la section tickets par la carte Booking-style
        ticket_card = generate_ticket_card(castle_name)
        content = re.sub(
            r'<!-- Section 6: Tickets en bezoeken \(Affiliate\) -->.*?</section>',
            ticket_card,
            content,
            flags=re.DOTALL
        )
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✅ {os.path.basename(filepath)}")
            return True
        return False
    except Exception as e:
        print(f"  ❌ Erreur {filepath}: {e}")
        return False

def main():
    print("🎨 Amélioration UX des pages château (style Booking/TripAdvisor)...\n")
    
    upgraded = 0
    for filename, castle_data in CASTLE_DATA.items():
        filepath = os.path.join(SITE_DIR, filename)
        if os.path.exists(filepath):
            if upgrade_castle_page(filepath, castle_data):
                upgraded += 1
        else:
            print(f"  ⚠️ Fichier non trouvé: {filename}")
    
    print(f"\n✅ {upgraded} pages améliorées avec le nouveau design UX")

if __name__ == "__main__":
    main()
