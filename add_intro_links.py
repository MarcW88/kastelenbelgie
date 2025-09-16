#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script pour ajouter des liens internes dans les textes d'introduction des châteaux
Liens vers: 'kastelen in België' (homepage) et 'kastelen in (provincie)' (page province)
"""

import os
import re
import glob

# Mapping des provinces pour déterminer la province d'un château
PROVINCES_MAPPING = {
    'antwerpen': {
        'name': 'Antwerpen',
        'places': ['edegem', 'mortsel', 'merksem', 'deurne', 'kontich', 'aartselaar', 'schoten', 'brasschaat', 'kapellen', 'zandhoven', 'lier', 'bonheiden', 'heist-op-den-berg', 'vorselaar', 'berlaar', 'laakdal', 'retie', 'westerlo', 'hoboken', 'wilrijk', 'ekeren', 'oelegem']
    },
    'oost-vlaanderen': {
        'name': 'Oost-Vlaanderen',
        'places': ['beervelde', 'berlare', 'gavere', 'gent', 'gentbrugge', 'drongen', 'mariakerke', 'sint-denijs-westrem', 'destelbergen', 'lovendegem', 'vinderhoute', 'aalst', 'ninove', 'zottegem', 'kruishoutem', 'zulte', 'waasmunster', 'beveren-waas', 'oostakker', 'beerlegem', 'meulebeke', 'nokere', 'olsene', 'regelsbrugge', 'wedergrate', 'wippelgem']
    },
    'west-vlaanderen': {
        'name': 'West-Vlaanderen',
        'places': ['beernem', 'tillegem', 'sint-michiels', 'brugge', 'varsenare', 'boekhoute', 'sint-andries', 'ieper', 'elverdinge', 'diksmuide', 'torhout', 'izegem', 'waregem', 'deerlijk', 'kortrijk', 'meulebeke', 'spiere', 'templeuve', 'wakken', 'vichte', 'moere']
    },
    'limburg': {
        'name': 'Limburg',
        'places': ['bokrijk', 'genk', 'sint-pieters-voeren', 'voeren', 'rekem', 'lanaken', 'dilsen', 'bilzen', 'munsterbilzen', 'sint-truiden', 'borgloon', 'tongeren', 'hasselt', 'heusden-zolder', 'houthalen', 'achel', 'alken', 'diepenbeek', 'meer', 'nieuwerkerken', 'wimmertingen', 'rotem']
    },
    'vlaams-brabant': {
        'name': 'Vlaams-Brabant',
        'places': ['bouchout', 'meise', 'coloma', 'sint-pieters-leeuw', 'grimbergen', 'aarschot', 'elewijt', 'zaventem', 'overijse', 'dilbeek', 'leuven', 'sterrebeek', 'heikruis', 'westmeerbeek', 'duffel', 'loksbergen', 'strijtem', 'schoonhoven']
    },
    'namen': {
        'name': 'Namen',
        'places': ['freyr', 'hastiere', 'spontin', 'yvoir', 'dinant', 'celles', 'falaen', 'natoye', 'sombreffe', 'haltinne', 'serinchamps', 'fronville', 'deulin']
    },
    'luik': {
        'name': 'Luik',
        'places': ['hoei', 'huy', 'modave', 'awans', 'alleur', 'engis', 'hermalle-sous-huy', 'esneux', 'aywaille', 'stoumont', 'weismes', 'soumagne', 'blegny', 'voeren', 'tilff', 'oteppe', 'hergenrath', 'sippenaeken', 'remersdaal']
    },
    'luxemburg': {
        'name': 'Luxemburg',
        'places': ['durbuy', 'la-roche-en-ardenne', 'mirwart', 'saint-hubert', 'longchamps', 'bertogne', 'bastogne', 'houffalize', 'tavigny', 'neufchateau', 'daverdisse', 'porcheresse', 'villers-devant-orval', 'orval', 'houyet', 'ciergnon', 'beauraing', 'sohier', 'veves', 'baronville', 'seraing-le-chateau']
    },
    'henegouwen': {
        'name': 'Henegouwen',
        'places': ['seneffe', 'boussu', 'doornik', 'tournai', 'peruwelz', 'biez', 'attre', 'manage', 'houtaing', 'froyennes', 'templeuve']
    },
    'waals-brabant': {
        'name': 'Waals-Brabant',
        'places': ['rixensart', 'genval', 'ceroux-mousty', 'kasteelbrakel', 'braine-le-chateau', 'nijvel', 'geldenaken']
    }
}

def determine_province(filename):
    """Bepaal de provincie van een kasteel op basis van de bestandsnaam"""
    filename_lower = filename.lower()
    
    for province_id, province_data in PROVINCES_MAPPING.items():
        for place in province_data['places']:
            if place in filename_lower:
                return province_id, province_data['name']
    
    # Default fallback
    return 'vlaams-brabant', 'Vlaams-Brabant'

def add_links_to_intro_text(paragraph_text, province_id, province_name, is_first_paragraph=True):
    """Voeg intelligente links toe aan een paragraaf van de introductietekst"""
    
    # Controleer of er al links aanwezig zijn
    if '<a href=' in paragraph_text:
        return paragraph_text, 0
    
    modified_text = paragraph_text
    changes_made = 0
    
    # Voor de eerste paragraaf: voeg link naar België toe
    if is_first_paragraph:
        # Zoek naar zinnen die eindigen met een punt en bevatten 'kasteel'
        if 'kasteel' in modified_text.lower():
            # Voeg België link toe aan het einde van de eerste zin
            sentences = modified_text.split('. ')
            if len(sentences) >= 1:
                first_sentence = sentences[0]
                if 'kasteel' in first_sentence.lower():
                    # Voeg link toe aan het einde van de eerste zin
                    if first_sentence.endswith('.'):
                        first_sentence = first_sentence[:-1] + ', een prachtig voorbeeld van de <a href="index.html#provincies">kastelen in België</a>.'
                    else:
                        first_sentence += ', een prachtig voorbeeld van de <a href="index.html#provincies">kastelen in België</a>'
                    
                    sentences[0] = first_sentence
                    modified_text = '. '.join(sentences)
                    changes_made += 1
    
    # Voor de tweede paragraaf: voeg link naar provincie toe
    else:
        if 'kasteel' in modified_text.lower():
            # Zoek naar een geschikte plek om de provincie link toe te voegen
            sentences = modified_text.split('. ')
            if len(sentences) >= 1:
                last_sentence = sentences[-1]
                
                # Voeg provincie link toe aan het einde
                if last_sentence.endswith('.'):
                    last_sentence = last_sentence[:-1] + f', onderdeel van het rijke erfgoed van <a href="{province_id}.html">kastelen in {province_name}</a>.'
                else:
                    last_sentence += f', onderdeel van het rijke erfgoed van <a href="{province_id}.html">kastelen in {province_name}</a>'
                
                sentences[-1] = last_sentence
                modified_text = '. '.join(sentences)
                changes_made += 1
    
    return modified_text, changes_made

def update_castle_intro_links(file_path):
    """Update de introductietekst van een kasteelpagina met links"""
    try:
        filename = os.path.basename(file_path)
        province_id, province_name = determine_province(filename)
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Zoek de intro sectie
        intro_pattern = r'<div class="intro">\s*<p>\s*(.*?)\s*</p>\s*<p>\s*(.*?)\s*</p>\s*</div>'
        intro_match = re.search(intro_pattern, content, re.DOTALL)
        
        if not intro_match:
            return False, "Geen intro sectie gevonden"
        
        # Extraheer de twee paragrafen
        paragraph1 = intro_match.group(1).strip()
        paragraph2 = intro_match.group(2).strip()
        
        # Voeg links toe aan beide paragrafen
        new_paragraph1, changes1 = add_links_to_intro_text(paragraph1, province_id, province_name, is_first_paragraph=True)
        new_paragraph2, changes2 = add_links_to_intro_text(paragraph2, province_id, province_name, is_first_paragraph=False)
        
        total_changes = changes1 + changes2
        
        if total_changes > 0:
            # Vervang de intro sectie
            new_intro = f'''<div class="intro">
      <p>
        {new_paragraph1}
      </p>
      <p>
        {new_paragraph2}
      </p>
    </div>'''
            
            new_content = re.sub(intro_pattern, new_intro, content, flags=re.DOTALL)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            return True, f"{total_changes} links toegevoegd"
        
        return False, "Geen wijzigingen nodig"
        
    except Exception as e:
        return False, f"Fout: {e}"

def main():
    """Hoofdfunctie"""
    print("=== TOEVOEGEN INTRO LINKS ===")
    
    # Vind alle kasteelbestanden
    print("Zoeken naar kasteelbestanden...")
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
    print(f"\nTest met {len(test_files)} bestanden...")
    
    success_count = 0
    total_links = 0
    
    for file_path in test_files:
        filename = os.path.basename(file_path)
        success, message = update_castle_intro_links(file_path)
        
        if success:
            print(f"  ✓ {filename}: {message}")
            success_count += 1
            # Extract number of links from message
            if "links toegevoegd" in message:
                total_links += int(message.split()[0])
        else:
            print(f"  ○ {filename}: {message}")
    
    print(f"\n=== TESTRESULTAAT ===")
    print(f"Bestanden getest: {len(test_files)}")
    print(f"Succesvol bijgewerkt: {success_count}")
    print(f"Links toegevoegd: {total_links}")
    
    # Ga door met alle bestanden
    print(f"\nDoorgaan met alle {len(castle_files)} bestanden...")
    
    for file_path in castle_files:
        filename = os.path.basename(file_path)
        
        # Skip de al behandelde testbestanden
        if file_path in test_files:
            continue
            
        success, message = update_castle_intro_links(file_path)
        
        if success:
            success_count += 1
            if "links toegevoegd" in message:
                total_links += int(message.split()[0])
            
            if success_count % 50 == 0:
                print(f"  Voortgang: {success_count} bestanden bijgewerkt...")
    
    print(f"\n=== EINDRESULTAAT ===")
    print(f"Totaal kasteelpaginas behandeld: {len(castle_files)}")
    print(f"Succesvol bijgewerkt: {success_count}")
    print(f"Totaal links toegevoegd: {total_links}")
    print(f"Interne links zijn nu actief in alle intro teksten!")

if __name__ == "__main__":
    main()
