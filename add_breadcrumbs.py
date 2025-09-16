#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script pour ajouter des breadcrumbs sur toutes les pages du site kastelenbelgie.be
Structure: Home > Provinces > Province > Château
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

def extract_castle_name(filename):
    """Extraheer de kastelnaam uit de bestandsnaam"""
    name = filename.replace('.html', '')
    name = name.replace('-', ' ')
    # Verwijder veelvoorkomende prefixen
    name = re.sub(r'^(kasteel|chateau|citadel|burcht|hof|het|de|la|le|du|van|te|der|des)\s+', '', name, flags=re.IGNORECASE)
    return name.title()

def create_breadcrumb_html(level, castle_name=None, province_id=None, province_name=None):
    """Genereer breadcrumb HTML voor verschillende niveaus"""
    
    if level == 'home':
        # Niveau 0: Home page - geen breadcrumb
        return ''
    
    elif level == 'provinces':
        # Niveau 1: Provinces overview
        return '''        <nav class="breadcrumb">
          <a href="index.html">Home</a>
          <span class="breadcrumb-separator">›</span>
          <span class="breadcrumb-current">Provincies</span>
        </nav>'''
    
    elif level == 'province':
        # Niveau 2: Specifieke provincie
        return f'''        <nav class="breadcrumb">
          <a href="index.html">Home</a>
          <span class="breadcrumb-separator">›</span>
          <a href="provinces.html">Provincies</a>
          <span class="breadcrumb-separator">›</span>
          <span class="breadcrumb-current">{province_name}</span>
        </nav>'''
    
    elif level == 'castle':
        # Niveau 3: Specifiek kasteel
        return f'''        <nav class="breadcrumb">
          <a href="index.html">Home</a>
          <span class="breadcrumb-separator">›</span>
          <a href="provinces.html">Provincies</a>
          <span class="breadcrumb-separator">›</span>
          <a href="{province_id}.html">{province_name}</a>
          <span class="breadcrumb-separator">›</span>
          <span class="breadcrumb-current">{castle_name}</span>
        </nav>'''
    
    return ''

def add_breadcrumb_to_castle_page(file_path):
    """Voeg breadcrumb toe aan een kasteelpagina"""
    try:
        filename = os.path.basename(file_path)
        province_id, province_name = determine_province(filename)
        castle_name = extract_castle_name(filename)
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Controleer of breadcrumb al bestaat
        if 'class="breadcrumb"' in content:
            return False
        
        # Genereer breadcrumb HTML
        breadcrumb_html = create_breadcrumb_html('castle', castle_name, province_id, province_name)
        
        # Zoek de positie na de hero section opening
        pattern = r'(<section class="detail-header">\s*<div class="container">\s*)'
        
        def add_breadcrumb(match):
            return f'{match.group(1)}{breadcrumb_html}\n        '
        
        new_content = re.sub(pattern, add_breadcrumb, content)
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        
        return False
        
    except Exception as e:
        print(f"  ✗ Fout bij {filename}: {e}")
        return False

def add_breadcrumb_to_provinces_page():
    """Voeg breadcrumb toe aan de provinces hoofdpagina"""
    file_path = '/Users/marc/Desktop/kastelenbelgie/provinces.html'
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Controleer of breadcrumb al bestaat
        if 'class="breadcrumb"' in content:
            return False
        
        # Genereer breadcrumb HTML
        breadcrumb_html = create_breadcrumb_html('provinces')
        
        # Zoek de positie na de hero section opening
        pattern = r'(<section class="hero">\s*<div class="container">\s*)'
        
        def add_breadcrumb(match):
            return f'{match.group(1)}{breadcrumb_html}\n        '
        
        new_content = re.sub(pattern, add_breadcrumb, content)
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        
        return False
        
    except Exception as e:
        print(f"  ✗ Fout bij provinces.html: {e}")
        return False

def add_breadcrumb_to_province_pages():
    """Voeg breadcrumbs toe aan alle individuele provinciepaginas"""
    updated_count = 0
    
    for province_id, province_data in PROVINCES_MAPPING.items():
        file_path = f'/Users/marc/Desktop/kastelenbelgie/{province_id}.html'
        
        if not os.path.exists(file_path):
            continue
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Controleer of breadcrumb al bestaat (anders dan de bestaande)
            if 'href="index.html">Home</a>' in content:
                continue
            
            # Genereer breadcrumb HTML
            breadcrumb_html = create_breadcrumb_html('province', province_name=province_data['name'])
            
            # Vervang de bestaande breadcrumb
            pattern = r'<nav class="breadcrumb">.*?</nav>'
            new_content = re.sub(pattern, breadcrumb_html.strip(), content, flags=re.DOTALL)
            
            if new_content != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                updated_count += 1
                print(f"  ✓ Breadcrumb bijgewerkt: {province_id}.html")
        
        except Exception as e:
            print(f"  ✗ Fout bij {province_id}.html: {e}")
    
    return updated_count

def add_breadcrumb_css():
    """Voeg CSS toe voor breadcrumb styling"""
    css_code = '''
/* Breadcrumb Styles */
.breadcrumb {
  margin-bottom: 1.5rem;
  font-size: 0.875rem;
  color: #6b7280;
}

.breadcrumb a {
  color: #6b7280;
  text-decoration: none;
  transition: color 0.2s;
}

.breadcrumb a:hover {
  color: #3b82f6;
  text-decoration: underline;
}

.breadcrumb-separator {
  margin: 0 0.5rem;
  color: #9ca3af;
}

.breadcrumb-current {
  color: #1f2937;
  font-weight: 500;
}

@media (max-width: 768px) {
  .breadcrumb {
    font-size: 0.75rem;
    margin-bottom: 1rem;
  }
  
  .breadcrumb-separator {
    margin: 0 0.25rem;
  }
}'''
    
    css_file = '/Users/marc/Desktop/kastelenbelgie/css/style.css'
    
    try:
        with open(css_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if '/* Breadcrumb Styles */' not in content:
            with open(css_file, 'a', encoding='utf-8') as f:
                f.write(css_code)
            return True
        
        return False
        
    except Exception as e:
        print(f"Fout bij CSS toevoegen: {e}")
        return False

def main():
    """Hoofdfunctie"""
    print("=== TOEVOEGEN BREADCRUMB NAVIGATIE ===")
    
    # Voeg CSS toe
    print("CSS toevoegen...")
    if add_breadcrumb_css():
        print("  ✓ Breadcrumb CSS toegevoegd")
    else:
        print("  ○ Breadcrumb CSS al aanwezig")
    
    # Update provinces hoofdpagina
    print("\nBreadcrumb toevoegen aan provinces.html...")
    if add_breadcrumb_to_provinces_page():
        print("  ✓ Breadcrumb toegevoegd aan provinces.html")
    else:
        print("  ○ Breadcrumb al aanwezig op provinces.html")
    
    # Update individuele provinciepaginas
    print("\nBreadcrumbs bijwerken op provinciepaginas...")
    province_updated = add_breadcrumb_to_province_pages()
    print(f"  ✓ {province_updated} provinciepaginas bijgewerkt")
    
    # Vind alle kasteelbestanden
    print("\nBreadcrumbs toevoegen aan kasteelpaginas...")
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
        
        if add_breadcrumb_to_castle_page(file_path):
            print(f"  ✓ Breadcrumb toegevoegd: {filename}")
            updated_count += 1
        else:
            print(f"  ○ Breadcrumb al aanwezig: {filename}")
    
    print(f"\n=== TESTRESULTAAT ===")
    print(f"Bestanden getest: {len(test_files)}")
    print(f"Breadcrumbs toegevoegd: {updated_count}")
    
    # Ga door met alle bestanden
    print(f"\nDoorgaan met alle {len(castle_files)} bestanden...")
    
    for file_path in castle_files:
        filename = os.path.basename(file_path)
        
        # Skip de al behandelde testbestanden
        if file_path in test_files:
            continue
            
        if add_breadcrumb_to_castle_page(file_path):
            updated_count += 1
            if updated_count % 50 == 0:
                print(f"  Voortgang: {updated_count} breadcrumbs toegevoegd...")
    
    print(f"\n=== EINDRESULTAAT ===")
    print(f"Totaal kasteelpaginas behandeld: {len(castle_files)}")
    print(f"Breadcrumbs toegevoegd aan kastelen: {updated_count}")
    print(f"Provinciepaginas bijgewerkt: {province_updated}")
    print(f"Breadcrumb navigatie is nu actief op alle paginas!")

if __name__ == "__main__":
    main()
