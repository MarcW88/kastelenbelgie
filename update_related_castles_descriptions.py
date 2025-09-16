#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script pour mettre à jour les descriptions des châteaux dans la section "related castles"
avec des textes plus détaillés (2+ phrases)
"""

import os
import re
import glob

# Base de données étendue des châteaux avec descriptions détaillées
CASTLES_DATABASE = {
    # Province d'Anvers
    'kasteel-arendsnest-edegem.html': {
        'name': 'Kasteel Arendsnest',
        'description': 'Dit 19e-eeuwse kasteel in Edegem combineert neogotische architectuur met romantische parkelementen. Het domein werd ontworpen als een ideale synthese tussen wonen en natuur, met zijn karakteristieke torentjes en uitgestrekte tuinen.'
    },
    'kasteel-cantecroy-mortsel.html': {
        'name': 'Kasteel Cantecroy', 
        'description': 'Een elegant 18e-eeuws kasteel dat de verfijnde levensstijl van de Antwerpse adel illustreert. De symmetrische gevel en de Franse tuinaanleg getuigen van de kosmopolitische invloeden in de regio.'
    },
    'kasteel-groenendaal-merksem.html': {
        'name': 'Kasteel Groenendaal',
        'description': 'Dit waterslot uit de 16e eeuw ligt pittoresk aan de rand van Antwerpen en vormt een uniek voorbeeld van Vlaamse kasteelarchitectuur. De strategische ligging aan de waterloop bood zowel bescherming als handelsmogelijkheden.'
    },

    # Oost-Vlaanderen  
    'kasteel-van-beervelde-beervelde.html': {
        'name': 'Kasteel van Beervelde',
        'description': 'Een imposant neogotisch kasteel uit de 19e eeuw, omgeven door een van de mooiste parken van België. Het domein staat bekend om zijn rododendronverzameling en de jaarlijkse kameliashow die bezoekers van over heel Europa trekt.'
    },
    'kasteel-van-berlare-berlare.html': {
        'name': 'Kasteel van Berlare',
        'description': 'Dit middeleeuwse kasteel aan de Schelde speelde een cruciale rol in de verdediging van de handelswegen naar Gent. De massieve donjon en de omringende grachten getuigen van de strategische betekenis van deze vesting.'
    },
    'kasteel-borgwal-gavere.html': {
        'name': 'Kasteel Borgwal',
        'description': 'Een charmant renaissancekasteel dat de overgang markeert van middeleeuwse vesting naar comfortabele adellijke residentie. De elegante binnenplaats en de decoratieve gevels tonen de invloed van Italiaanse architecten in de 16e eeuw.'
    },

    # West-Vlaanderen
    'kasteel-drie-koningen-beernem.html': {
        'name': 'Kasteel Drie Koningen',
        'description': 'Dit barokke kasteel uit de 17e eeuw dankt zijn naam aan de drie koningen die er zouden hebben gelogeerd. De rijke decoratie en de symmetrische tuinaanleg maken het tot een pareltje van de West-Vlaamse kasteelarchitectuur.'
    },
    'kasteel-van-tillegem-sint-michiels.html': {
        'name': 'Kasteel van Tillegem',
        'description': 'Een middeleeuws kasteel dat uitgroeide tot een elegant herenhuis, gelegen in een uitgestrekt natuurdomein nabij Brugge. Het kasteel combineert gotische elementen met latere classicistische toevoegingen, wat resulteert in een fascinerende architecturale synthese.'
    },

    # Limburg
    'kasteel-van-bokrijk-genk.html': {
        'name': 'Kasteel van Bokrijk',
        'description': 'Het hart van het beroemde openluchtmuseum Bokrijk, dit 18e-eeuwse kasteel illustreert de evolutie van het Limburgse plattelandsleven. Het domein combineert historische architectuur met educatieve functies en vormt een brug tussen verleden en heden.'
    },
    'kasteel-de-commanderij-sint-pieters-voeren.html': {
        'name': 'Kasteel de Commanderij',
        'description': 'Deze voormalige commanderij van de Duitse Orde getuigt van de religieuze en militaire geschiedenis van het Voerstreek. Het complex combineert verdedigingsarchitectuur met kloosterlijke elementen en biedt een uniek inzicht in de middeleeuwse geschiedenis van de grensregio.'
    },

    # Vlaams-Brabant
    'kasteel-van-bouchout-te-meise.html': {
        'name': 'Kasteel van Bouchout',
        'description': 'Dit romantische kasteel in Meise werd de laatste residentie van keizerin Charlotte van Mexico en staat nu in het hart van de Nationale Plantentuin. De neogotische architectuur en de botanische collecties maken het tot een unieke combinatie van cultuur en natuur.'
    },
    'kasteel-van-coloma-te-sint-pieters-leeuw.html': {
        'name': 'Kasteel van Coloma',
        'description': 'Een elegant 18e-eeuws kasteel omgeven door een prachtig rozentuin met meer dan 3000 rozensoorten. Het domein combineert architecturale schoonheid met horticulturele excellentie en vormt een van de mooiste rozentuinen van Europa.'
    },

    # Namen
    'kasteel-van-freyr-freyr.html': {
        'name': 'Kasteel van Freÿr',
        'description': 'Dit Renaissance-kasteel aan de Maas is beroemd om zijn Franse tuinen à la Le Nôtre en zijn rol in de Europese diplomatie. Het kasteel ontving Lodewijk XIV en was de plaats waar het Verdrag van Freÿr werd ondertekend, wat het tot een monument van internationale betekenis maakt.'
    },
    'kasteel-van-spontin-spontin.html': {
        'name': 'Kasteel van Spontin',
        'description': 'Een middeleeuws kasteel dat uitgroeide tot een elegant renaissancecomplex, gelegen aan de samenvloeiing van de Bocq en de Maas. De verschillende bouwfasen zijn nog duidelijk zichtbaar en illustreren de evolutie van de kasteelarchitectuur door de eeuwen heen.'
    },

    # Luik
    'citadel-van-hoei-hoei.html': {
        'name': 'Citadel van Hoei',
        'description': 'Deze indrukwekkende vesting op een 100 meter hoge rots domineert de samenvloeiing van Maas en Hoyoux. De citadel, herbouwd door Menno van Coehoorn, vormt een meesterwerk van militaire architectuur en biedt een panoramisch uitzicht over de Maasvallei.'
    },
    'kasteel-van-modave-modave.html': {
        'name': 'Kasteel van Modave',
        'description': 'Dit 17e-eeuwse kasteel staat bekend om zijn spectaculaire ligging op een rotsuitstulping boven de Hoyoux en zijn rijke interieurinrichting. Het kasteel speelde een pionersrol in de watervoorziening van Versailles en combineert architecturale schoonheid met technische innovatie.'
    },

    # Luxemburg
    'kasteel-van-durbuy-durbuy.html': {
        'name': 'Kasteel van Durbuy',
        'description': 'Het kasteel der Graven van Ursel domineert de kleinste stad ter wereld en heeft een bewogen geschiedenis die teruggaat tot de 9e eeuw. Na verwoesting door Franse troepen werd het in 1730 herbouwd als een elegant lustslot, dat nog steeds bewoond wordt door de familie d\'Ursel.'
    },
    'kasteel-van-la-roche-en-ardenne-la-roche-en-ardenne.html': {
        'name': 'Kasteel van La Roche-en-Ardenne',
        'description': 'Deze middeleeuwse ruïne op een rotsuitstulping boven de Ourthe biedt een dramatisch beeld van de feodale macht in de Ardennen. Het kasteel controleerde de handelswegen door de vallei en vormt nu een romantische ruïne die de verbeelding prikkelt.'
    },
    'kasteel-van-mirwart-mirwart-saint-hubert.html': {
        'name': 'Kasteel van Mirwart',
        'description': 'Een 18e-eeuws kasteel in het hart van de Ardennen, omgeven door uitgestrekte bossen en wildreservaten. Het domein combineert architecturale elegantie met de natuurlijke schoonheid van het Ardense landschap en vormt een ideale uitvalsbasis voor natuurliefhebbers.'
    },
    'kasteel-van-longchamps-longchamps-bertogne.html': {
        'name': 'Kasteel van Longchamps',
        'description': 'Dit kasteel in de streek van Bastogne getuigt van de woelige geschiedenis van de Ardennen tijdens beide wereldoorlogen. Het domein combineert historische architectuur met herdenkingsmonumenten en biedt een uniek perspectief op de militaire geschiedenis van de regio.'
    },

    # Henegouwen
    'kasteel-van-seneffe-seneffe.html': {
        'name': 'Kasteel van Seneffe',
        'description': 'Dit 18e-eeuwse kasteel in neoclassicistische stijl huisvest nu een museum voor zilverwerk en decoratieve kunsten. De symmetrische architectuur en de Franse tuinen maken het tot een perfect voorbeeld van de Verlichtingsarchitectuur in de Zuidelijke Nederlanden.'
    },
    'kasteel-van-boussu-boussu.html': {
        'name': 'Kasteel van Boussu',
        'description': 'Een Renaissance-kasteel dat gold als een van de mooiste van Europa voordat het werd verwoest in de 18e eeuw. De gerestaureerde ruïnes en de reconstructie van delen van het complex geven een indruk van de voormalige grandeur van dit architecturale meesterwerk.'
    },

    # Waals-Brabant
    'kasteel-van-rixensart-rixensart.html': {
        'name': 'Kasteel van Rixensart',
        'description': 'Dit 18e-eeuwse kasteel in Waals-Brabant combineert Franse elegantie met Vlaamse bouwtraditie. Het domein staat bekend om zijn landschapspark in Engelse stijl en zijn rol in de ontwikkeling van de romantische tuinarchitectuur in België.'
    },

    # Brussel
    'kasteel-van-rivieren-te-ganshoren.html': {
        'name': 'Kasteel van Rivieren',
        'description': 'Een 19e-eeuws neogotisch kasteel in het hart van Brussel, dat de stedelijke ontwikkeling van de hoofdstad illustreert. Het kasteel vormt een oase van rust in de stedelijke omgeving en toont hoe de adel zich aanpaste aan het veranderende karakter van Brussel.'
    }
}

def get_castles_by_region(current_castle_file):
    """Bepaal de regio van het huidige kasteel en retourneer gerelateerde kastelen"""
    
    # Regio-indeling op basis van plaatsnamen en provincies
    regions = {
        'antwerpen': ['edegem', 'mortsel', 'merksem', 'deurne', 'kontich', 'aartselaar', 'schoten', 'brasschaat', 'kapellen', 'zandhoven', 'lier', 'bonheiden', 'heist-op-den-berg', 'vorselaar', 'berlaar', 'laakdal', 'retie', 'westerlo'],
        'oost_vlaanderen': ['beervelde', 'berlare', 'gavere', 'gent', 'gentbrugge', 'drongen', 'mariakerke', 'sint-denijs-westrem', 'destelbergen', 'lovendegem', 'vinderhoute', 'aalst', 'ninove', 'zottegem', 'kruishoutem', 'zulte'],
        'west_vlaanderen': ['beernem', 'tillegem', 'sint-michiels', 'brugge', 'varsenare', 'boekhoute', 'sint-andries', 'ieper', 'elverdinge', 'diksmuide', 'torhout', 'izegem', 'waregem', 'deerlijk', 'kortrijk', 'meulebeke', 'spiere', 'templeuve'],
        'limburg': ['bokrijk', 'genk', 'sint-pieters-voeren', 'voeren', 'rekem', 'lanaken', 'dilsen', 'bilzen', 'munsterbilzen', 'sint-truiden', 'borgloon', 'tongeren', 'hasselt', 'heusden-zolder', 'houthalen', 'achel', 'alken'],
        'vlaams_brabant': ['bouchout', 'meise', 'coloma', 'sint-pieters-leeuw', 'grimbergen', 'aarschot', 'elewijt', 'zaventem', 'overijse', 'dilbeek', 'ukkel', 'laken', 'brussel', 'ganshoren', 'strombeek-bever', 'dworp', 'oetingen'],
        'namen': ['freyr', 'hastiere', 'spontin', 'yvoir', 'dinant', 'celles', 'falaen', 'natoye', 'sombreffe', 'haltinne', 'serinchamps'],
        'luik': ['hoei', 'huy', 'modave', 'awans', 'alleur', 'engis', 'hermalle-sous-huy', 'esneux', 'aywaille', 'stoumont', 'weismes', 'soumagne', 'blegny', 'voeren'],
        'luxemburg': ['durbuy', 'la-roche-en-ardenne', 'mirwart', 'saint-hubert', 'longchamps', 'bertogne', 'bastogne', 'houffalize', 'tavigny', 'neufchateau', 'daverdisse', 'porcheresse', 'villers-devant-orval', 'orval', 'houyet', 'ciergnon'],
        'henegouwen': ['seneffe', 'boussu', 'doornik', 'tournai', 'peruwelz', 'biez', 'attre', 'manage', 'houtaing', 'froyennes'],
        'waals_brabant': ['rixensart', 'genval', 'ceroux-mousty', 'kasteelbrakel', 'braine-le-chateau', 'nijvel', 'geldenaken'],
        'brussel': ['ganshoren', 'ukkel', 'laken', 'brussel']
    }
    
    # Bepaal regio van huidig kasteel
    current_region = None
    filename_lower = current_castle_file.lower()
    
    for region, places in regions.items():
        for place in places:
            if place in filename_lower:
                current_region = region
                break
        if current_region:
            break
    
    if not current_region:
        current_region = 'vlaams_brabant'  # default
    
    # Vind kastelen in dezelfde regio
    related_castles = []
    for castle_file, castle_data in CASTLES_DATABASE.items():
        if castle_file == current_castle_file:
            continue
            
        castle_lower = castle_file.lower()
        for place in regions[current_region]:
            if place in castle_lower:
                related_castles.append({
                    'file': castle_file,
                    'name': castle_data['name'],
                    'description': castle_data['description']
                })
                break
    
    # Als er niet genoeg kastelen in dezelfde regio zijn, voeg nabije regio's toe
    if len(related_castles) < 3:
        nearby_regions = {
            'antwerpen': ['vlaams_brabant', 'oost_vlaanderen'],
            'oost_vlaanderen': ['antwerpen', 'west_vlaanderen', 'vlaams_brabant'],
            'west_vlaanderen': ['oost_vlaanderen'],
            'limburg': ['vlaams_brabant', 'luik'],
            'vlaams_brabant': ['antwerpen', 'oost_vlaanderen', 'limburg', 'waals_brabant'],
            'namen': ['luik', 'luxemburg', 'henegouwen'],
            'luik': ['namen', 'luxemburg', 'limburg'],
            'luxemburg': ['namen', 'luik'],
            'henegouwen': ['namen', 'waals_brabant'],
            'waals_brabant': ['vlaams_brabant', 'henegouwen', 'namen'],
            'brussel': ['vlaams_brabant', 'waals_brabant']
        }
        
        for nearby_region in nearby_regions.get(current_region, []):
            for castle_file, castle_data in CASTLES_DATABASE.items():
                if castle_file == current_castle_file or len(related_castles) >= 6:
                    continue
                    
                castle_lower = castle_file.lower()
                for place in regions[nearby_region]:
                    if place in castle_lower:
                        related_castles.append({
                            'file': castle_file,
                            'name': castle_data['name'],
                            'description': castle_data['description']
                        })
                        break
    
    return related_castles[:3]  # Retourneer max 3 kastelen

def update_related_castles_section(file_path):
    """Update de related castles sectie met uitgebreidere beschrijvingen"""
    try:
        filename = os.path.basename(file_path)
        related_castles = get_castles_by_region(filename)
        
        if len(related_castles) < 3:
            # Vul aan met willekeurige kastelen als er niet genoeg zijn
            import random
            available_castles = [
                {'file': 'kasteel-van-freyr-freyr.html', 'name': 'Kasteel van Freÿr', 'description': CASTLES_DATABASE['kasteel-van-freyr-freyr.html']['description']},
                {'file': 'citadel-van-hoei-hoei.html', 'name': 'Citadel van Hoei', 'description': CASTLES_DATABASE['citadel-van-hoei-hoei.html']['description']},
                {'file': 'kasteel-van-durbuy-durbuy.html', 'name': 'Kasteel van Durbuy', 'description': CASTLES_DATABASE['kasteel-van-durbuy-durbuy.html']['description']}
            ]
            
            for castle in available_castles:
                if castle['file'] != filename and len(related_castles) < 3:
                    if not any(rc['file'] == castle['file'] for rc in related_castles):
                        related_castles.append(castle)
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Bouw de nieuwe related castles HTML
        cards_html = []
        gradients = ['gradient-1', 'gradient-2', 'gradient-3']
        
        for i, castle in enumerate(related_castles[:3]):
            card_html = f'''          <a class="card" href="{castle['file']}">
            <div class="card-media {gradients[i]}"></div>
            <div class="card-body">
              <h3>{castle['name']}</h3>
              <p class="card-description">{castle['description']}</p>
            </div>
          </a>'''
            cards_html.append(card_html)
        
        new_cards_section = '\n'.join(cards_html)
        
        # Vervang de bestaande cards
        pattern = r'(<div class="card-grid three">)(.*?)(</div>\s*</div>\s*</section>)'
        
        def replace_cards(match):
            opening = match.group(1)
            closing = match.group(3)
            return f'{opening}\n{new_cards_section}\n        {closing}'
        
        new_content = re.sub(pattern, replace_cards, content, flags=re.DOTALL)
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        
        return False
        
    except Exception as e:
        print(f"  ✗ Fout bij {filename}: {e}")
        return False

def main():
    """Hoofdfunctie"""
    print("=== UPDATE RELATED CASTLES DESCRIPTIONS ===")
    
    # Vind alle kasteelbestanden
    castle_files = []
    patterns = [
        "kasteel-*.html", "chateau-*.html", "citadel-*.html", "burcht-*.html",
        "hof-*.html", "de-*.html", "het-*.html", "sint-*.html", "koninklijk-*.html",
        "waterslot-*.html", "vrieselhof-*.html", "rentmeesterij-*.html",
        "commanderij-*.html", "domein-*.html", "oud-*.html", "bisschoppenhof-*.html",
        "braemkasteel-*.html", "burchtruine-*.html", "gaverkasteel-*.html"
    ]
    
    for pattern in patterns:
        castle_files.extend(glob.glob(f"/Users/marc/Desktop/kastelenbelgie/{pattern}"))
    
    castle_files = sorted(list(set(castle_files)))
    
    print(f"Gevonden kasteelbestanden: {len(castle_files)}")
    
    # Test eerst met een paar bestanden
    test_files = castle_files[:5]
    updated_count = 0
    
    print(f"\nTest met {len(test_files)} bestanden...")
    
    for file_path in test_files:
        filename = os.path.basename(file_path)
        print(f"\nBehandeling: {filename}")
        
        if update_related_castles_section(file_path):
            print(f"  ✓ Related castles bijgewerkt")
            updated_count += 1
        else:
            print(f"  ○ Geen wijzigingen")
    
    print(f"\n=== TESTRESULTAAT ===")
    print(f"Bestanden getest: {len(test_files)}")
    print(f"Related castles bijgewerkt: {updated_count}")
    
    # Ga door met alle bestanden
    print(f"\nDoorgaan met alle {len(castle_files)} bestanden...")
    
    for file_path in castle_files:
        filename = os.path.basename(file_path)
        
        # Skip de al behandelde testbestanden
        if file_path in test_files:
            continue
            
        if update_related_castles_section(file_path):
            updated_count += 1
            if updated_count % 50 == 0:
                print(f"  Voortgang: {updated_count} bestanden bijgewerkt...")
    
    print(f"\n=== EINDRESULTAAT ===")
    print(f"Totaal bestanden behandeld: {len(castle_files)}")
    print(f"Related castles bijgewerkt: {updated_count}")
    print(f"Elke pagina heeft nu uitgebreidere beschrijvingen voor related castles!")

if __name__ == "__main__":
    main()
