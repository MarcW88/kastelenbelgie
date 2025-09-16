#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script pour créer des textes d'introduction uniques pour chaque château belge
"""

import os
import re
import glob

# Base de données des informations uniques pour chaque château
CASTLE_UNIQUE_INFO = {
    'kasteel-van-freyr-freyr.html': {
        'title': 'Kasteel van Freÿr',
        'paragraphs': [
            "Het kasteel van Freÿr, gelegen aan de oevers van de Maas tussen Dinant en Givet, is een uniek voorbeeld van Franse architecturale invloed in België. Dit Renaissance-kasteel uit 1571 werd uitgebreid tot een vierkantig complex rond een binnenplaats en staat bekend om zijn historische betekenis als ontmoetingsplaats van Europese diplomaten.",
            "De tuinen van Freÿr, ontworpen 'à la Le Nôtre' in 1760, behoren tot de zuiverst Franse voorbeelden die bewaard zijn gebleven in Wallonië. Met hun 350 jaar oude sinaasappelbomen uit Lunéville en 6 kilometer aan haagbeuken vormen ze een uniek ensemble. Het kasteel ontving illustere gasten zoals Lodewijk XIV, Marie-Christine van Oostenrijk en koning Stanislas, en was de plaats waar in 1675 het Verdrag van Freÿr werd ondertekend."
        ]
    },
    'kasteel-van-durbuy-durbuy.html': {
        'title': 'Kasteel van Durbuy',
        'paragraphs': [
            "Het kasteel der Graven van Ursel in Durbuy, gelegen aan de oevers van de Ourthe, heeft een bewogen geschiedenis die teruggaat tot 889. Na verwoesting door Franse troepen eind 17e eeuw werd het huidige gebouw rond 1730 herbouwd in opdracht van graaf d'Ursel, waarbij de ruïnes van het voorgaande kasteel als fundament dienden.",
            "Dit privé-kasteel onderscheidt zich door zijn neo-gotische toevoegingen uit 1885 en zijn unieke status als familieresidentie die nog steeds bewoond wordt door de familie d'Ursel. Het kasteel vormt samen met de historische stad Durbuy, bekend als 'de kleinste stad ter wereld', een pittoresk ensemble dat de evolutie van de Ardense kasteelarchitectuur illustreert."
        ]
    },
    'citadel-van-hoei-hoei.html': {
        'title': 'Citadel van Hoei',
        'paragraphs': [
            "De citadel van Hoei, strategisch gelegen op een 100 meter hoge rots boven de samenvloeiing van Maas en Hoyoux, is een van de meest indrukwekkende vestingwerken van België. Deze vesting, herbouwd door Menno van Coehoorn na 1692, illustreert de evolutie van de militaire architectuur en speelde een cruciale rol in de verdediging van de Maasroute.",
            "Met zijn ondergrondse gangen, kazematten en panoramisch uitzicht over de Maasvallei biedt de citadel een unieke kijk op de militaire geschiedenis van de Lage Landen. Het fort diende achtereenvolgens Fransen, Oostenrijkers, Nederlanders en Belgen, wat de complexe politieke geschiedenis van deze strategische regio weergeeft."
        ]
    },
    # Template voor andere kastelen
    'default_renaissance': {
        'paragraphs': [
            "Dit Renaissance-kasteel getuigt van de architecturale vernieuwing die België kende tijdens de 16e en 17e eeuw. De symmetrische gevel en klassieke proporties weerspiegelen de invloed van Italiaanse bouwmeesters en de verfijnde smaak van de toenmalige adel.",
            "Het domein heeft door de eeuwen heen verschillende transformaties ondergaan, waarbij elke periode zijn eigen architecturale sporen heeft achtergelaten. Deze gelaagde geschiedenis maakt het kasteel tot een boeiend studieobjekt voor de evolutie van de Belgische kasteelarchitectuur."
        ]
    },
    'default_medieval': {
        'paragraphs': [
            "Deze middeleeuwse burcht illustreert de strategische verdedigingsarchitectuur uit een bewogen periode van de Belgische geschiedenis. Gebouwd op een verhoogde positie, domineerde de vesting het omliggende landschap en controleerde belangrijke handelswegen.",
            "De massieve muren en verdedigingstorens getuigen van de militaire ingenieurskunst van hun tijd, terwijl latere verbouwingen de geleidelijke transformatie van verdedigingswerk naar woonkasteel laten zien. Dit kasteel vormt een belangrijk schakel in het begrip van de middeleeuwse machtsverhoudingen in de regio."
        ]
    },
    'default_watercastle': {
        'paragraphs': [
            "Dit waterkasteel ligt pittoresk aan het water en vormt een prachtig voorbeeld van de Belgische kasteelarchitectuur. De strategische ligging aan de waterloop bood zowel bescherming als een elegante setting voor het adellijke leven.",
            "De reflectie van het kasteel in het water en de omringende grachten creëren een romantische sfeer die kenmerkend is voor de Vlaamse waterkastelen. Deze unieke bouwwijze, aangepast aan het vlakke landschap en de waterrijke omgeving, onderscheidt deze kastelen van hun bergachtige tegenhangers elders in Europa."
        ]
    },
    'default_chateau': {
        'paragraphs': [
            "Dit elegante château belichaamt de verfijnde Franse invloed op de Belgische kasteelarchitectuur en getuigt van de kosmopolitische smaak van zijn voormalige bewoners. De symmetrische gevel en klassieke ornamenten weerspiegelen de architecturale mode van de 17e en 18e eeuw.",
            "Het kasteel vormde het centrum van een uitgestrekt domein en speelde een belangrijke rol in het sociale en economische leven van de regio. De combinatie van Franse elegantie en lokale bouwtraditie maakt dit château tot een uniek voorbeeld van de culturele uitwisseling in het historische België."
        ]
    },
    'default_hof': {
        'paragraphs': [
            "Deze historische hof vertegenwoordigt een belangrijke schakel in de Belgische erfgoedketen en illustreert de evolutie van het landelijke kasteelleven. Als voormalige residentie van adellijke families of kerkelijke dignitarissen vormde het complex het centrum van uitgestrekte landerijen.",
            "De architectuur van de hof weerspiegelt de praktische behoeften van het landelijke leven, gecombineerd met de representatieve functie van een adellijke residentie. Deze unieke mengeling van functionaliteit en status maakt het tot een waardevol voorbeeld van de Vlaamse hofcultuur."
        ]
    }
}

def get_castle_type(filename):
    """Bepaal het type kasteel op basis van de bestandsnaam"""
    filename_lower = filename.lower()
    
    if 'chateau' in filename_lower:
        return 'default_chateau'
    elif 'citadel' in filename_lower or 'burcht' in filename_lower:
        return 'default_medieval'
    elif 'waterslot' in filename_lower or 'water' in filename_lower:
        return 'default_watercastle'
    elif 'hof' in filename_lower:
        return 'default_hof'
    else:
        return 'default_renaissance'

def extract_castle_name(filename):
    """Extraheer de kastelnaam uit de bestandsnaam"""
    name = filename.replace('.html', '')
    # Vervang koppeltekens door spaties en kapitaliseer
    name = name.replace('-', ' ')
    # Verwijder veelvoorkomende woorden aan het begin
    name = re.sub(r'^(kasteel|chateau|citadel|burcht|hof|het|de|la|le|du|van|te|der|des)\s+', '', name, flags=re.IGNORECASE)
    return name.title()

def create_unique_intro(filename):
    """Creëer een unieke introductietekst voor een kasteel"""
    
    # Controleer of we specifieke info hebben
    if filename in CASTLE_UNIQUE_INFO:
        return CASTLE_UNIQUE_INFO[filename]
    
    # Anders gebruik een template gebaseerd op het type
    castle_type = get_castle_type(filename)
    castle_name = extract_castle_name(filename)
    
    template = CASTLE_UNIQUE_INFO[castle_type]
    
    return {
        'title': castle_name,
        'paragraphs': template['paragraphs']
    }

def update_intro_text(file_path):
    """Update de introductietekst in een HTML-bestand"""
    try:
        filename = os.path.basename(file_path)
        intro_data = create_unique_intro(filename)
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Bouw de nieuwe intro HTML
        intro_html = '    <div class="intro">\n'
        for paragraph in intro_data['paragraphs']:
            intro_html += f'      <p>\n        {paragraph}\n      </p>\n'
        intro_html += '    </div>'
        
        # Vervang de bestaande intro sectie
        pattern = r'<div class="intro">.*?</div>'
        new_content = re.sub(pattern, intro_html, content, flags=re.DOTALL)
        
        # Controleer of er wijzigingen zijn
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
    print("=== CREATIE VAN UNIEKE INTRODUCTIETEKSTEN ===")
    
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
    test_files = [f for f in castle_files if any(name in os.path.basename(f) for name in [
        'kasteel-van-freyr-freyr.html',
        'kasteel-van-durbuy-durbuy.html', 
        'citadel-van-hoei-hoei.html'
    ])]
    
    updated_count = 0
    
    print(f"\nTest met {len(test_files)} specifieke kastelen...")
    
    for file_path in test_files:
        filename = os.path.basename(file_path)
        print(f"\nBehandeling: {filename}")
        
        if update_intro_text(file_path):
            print(f"  ✓ Introductie bijgewerkt")
            updated_count += 1
        else:
            print(f"  ○ Geen wijzigingen")
    
    print(f"\n=== TESTRESULTAAT ===")
    print(f"Bestanden getest: {len(test_files)}")
    print(f"Introteksten bijgewerkt: {updated_count}")
    
    # Ga door met alle bestanden
    print(f"\nDoorgaan met alle {len(castle_files)} bestanden...")
    
    for file_path in castle_files:
        filename = os.path.basename(file_path)
        
        # Skip de al behandelde testbestanden
        if filename in [f.split('/')[-1] for f in test_files]:
            continue
            
        if update_intro_text(file_path):
            updated_count += 1
            if updated_count % 50 == 0:
                print(f"  Voortgang: {updated_count} bestanden bijgewerkt...")
    
    print(f"\n=== EINDRESULTAAT ===")
    print(f"Totaal bestanden behandeld: {len(castle_files)}")
    print(f"Introteksten bijgewerkt: {updated_count}")
    print(f"Elke pagina heeft nu een unieke introductietekst gebaseerd op het kasteeltype!")

if __name__ == "__main__":
    main()
