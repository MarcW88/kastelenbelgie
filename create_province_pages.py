#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script pour créer les pages provinces avec tous les châteaux organisés par province
"""

import os
import glob
import re

# Définition des provinces et leurs châteaux
PROVINCES = {
    'antwerpen': {
        'name': 'Antwerpen',
        'description': 'De provincie Antwerpen herbergt een rijke collectie kastelen die de evolutie van de Vlaamse architectuur illustreren, van middeleeuwse burchten tot elegante 19e-eeuwse landhuizen.',
        'places': ['edegem', 'mortsel', 'merksem', 'deurne', 'kontich', 'aartselaar', 'schoten', 'brasschaat', 'kapellen', 'zandhoven', 'lier', 'bonheiden', 'heist-op-den-berg', 'vorselaar', 'berlaar', 'laakdal', 'retie', 'westerlo', 'hoboken', 'wilrijk', 'ekeren', 'oelegem']
    },
    'oost-vlaanderen': {
        'name': 'Oost-Vlaanderen',
        'description': 'Oost-Vlaanderen biedt een fascinerende mix van middeleeuwse kastelen en renaissanceresidencies, getuigen van de rijke handelsgeschiedenis van de regio.',
        'places': ['beervelde', 'berlare', 'gavere', 'gent', 'gentbrugge', 'drongen', 'mariakerke', 'sint-denijs-westrem', 'destelbergen', 'lovendegem', 'vinderhoute', 'aalst', 'ninove', 'zottegem', 'kruishoutem', 'zulte', 'waasmunster', 'beveren-waas', 'oostakker', 'beerlegem', 'meulebeke', 'nokere', 'olsene', 'regelsbrugge', 'wedergrate', 'wippelgem']
    },
    'west-vlaanderen': {
        'name': 'West-Vlaanderen',
        'description': 'West-Vlaanderen toont de verfijnde architectuur van de Vlaamse adel met prachtige kastelen die de invloed van de Bourgondische cultuur weerspiegelen.',
        'places': ['beernem', 'tillegem', 'sint-michiels', 'brugge', 'varsenare', 'boekhoute', 'sint-andries', 'ieper', 'elverdinge', 'diksmuide', 'torhout', 'izegem', 'waregem', 'deerlijk', 'kortrijk', 'meulebeke', 'spiere', 'templeuve', 'wakken', 'vichte', 'moere']
    },
    'limburg': {
        'name': 'Limburg',
        'description': 'Limburg combineert middeleeuwse commanderijen met elegante kastelen, vaak gelegen in pittoreske natuurdomeinen die de rust van het Limburgse landschap uitstralen.',
        'places': ['bokrijk', 'genk', 'sint-pieters-voeren', 'voeren', 'rekem', 'lanaken', 'dilsen', 'bilzen', 'munsterbilzen', 'sint-truiden', 'borgloon', 'tongeren', 'hasselt', 'heusden-zolder', 'houthalen', 'achel', 'alken', 'diepenbeek', 'meer', 'nieuwerkerken', 'wimmertingen', 'rotem']
    },
    'vlaams-brabant': {
        'name': 'Vlaams-Brabant',
        'description': 'Vlaams-Brabant herbergt kastelen die de nabijheid van Brussel weerspiegelen, met een mix van historische residenties en moderne restauraties in groene omgevingen.',
        'places': ['bouchout', 'meise', 'coloma', 'sint-pieters-leeuw', 'grimbergen', 'aarschot', 'elewijt', 'zaventem', 'overijse', 'dilbeek', 'leuven', 'sterrebeek', 'heikruis', 'westmeerbeek', 'duffel', 'loksbergen', 'strijtem', 'schoonhoven']
    },
    'namen': {
        'name': 'Namen',
        'description': 'De provincie Namen biedt spectaculaire kastelen langs de Maas en in de Ardennen, elk met een unieke geschiedenis en architecturale pracht.',
        'places': ['freyr', 'hastiere', 'spontin', 'yvoir', 'dinant', 'celles', 'falaen', 'natoye', 'sombreffe', 'haltinne', 'serinchamps', 'fronville', 'deulin']
    },
    'luik': {
        'name': 'Luik',
        'description': 'Luik combineert indrukwekkende citadellen met elegante kastelen, getuigen van de strategische betekenis van deze provincie in de Europese geschiedenis.',
        'places': ['hoei', 'huy', 'modave', 'awans', 'alleur', 'engis', 'hermalle-sous-huy', 'esneux', 'aywaille', 'stoumont', 'weismes', 'soumagne', 'blegny', 'voeren', 'tilff', 'oteppe', 'hergenrath', 'sippenaeken', 'remersdaal']
    },
    'luxemburg': {
        'name': 'Luxemburg',
        'description': 'De provincie Luxemburg toont kastelen in het hart van de Ardennen, omgeven door bossen en rivieren, perfect geïntegreerd in het natuurlijke landschap.',
        'places': ['durbuy', 'la-roche-en-ardenne', 'mirwart', 'saint-hubert', 'longchamps', 'bertogne', 'bastogne', 'houffalize', 'tavigny', 'neufchateau', 'daverdisse', 'porcheresse', 'villers-devant-orval', 'orval', 'houyet', 'ciergnon', 'beauraing', 'sohier', 'veves', 'baronville', 'seraing-le-chateau']
    },
    'henegouwen': {
        'name': 'Henegouwen',
        'description': 'Henegouwen presenteert kastelen die de Franse invloed op de Belgische architectuur tonen, met elegante châteaux en historische vestingen.',
        'places': ['seneffe', 'boussu', 'doornik', 'tournai', 'peruwelz', 'biez', 'attre', 'manage', 'houtaing', 'froyennes', 'templeuve']
    },
    'waals-brabant': {
        'name': 'Waals-Brabant',
        'description': 'Waals-Brabant biedt kastelen die de overgang vormen tussen de Vlaamse en Waalse architectuurtraditie, in een groene en heuvelachtige omgeving.',
        'places': ['rixensart', 'genval', 'ceroux-mousty', 'kasteelbrakel', 'braine-le-chateau', 'nijvel', 'geldenaken']
    }
}

def find_castles_by_province():
    """Vind alle kastelen georganiseerd per provincie"""
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
    
    # Organiseer per provincie
    province_castles = {province: [] for province in PROVINCES.keys()}
    
    for file_path in castle_files:
        filename = os.path.basename(file_path)
        filename_lower = filename.lower()
        
        # Bepaal provincie
        assigned = False
        for province, data in PROVINCES.items():
            for place in data['places']:
                if place in filename_lower:
                    # Extraheer kastelnaam
                    castle_name = filename.replace('.html', '').replace('-', ' ').title()
                    castle_name = re.sub(r'^(Kasteel|Chateau|Citadel|Burcht|Hof|Het|De|Sint)\s+', '', castle_name)
                    
                    province_castles[province].append({
                        'name': castle_name,
                        'file': filename,
                        'place': place
                    })
                    assigned = True
                    break
            if assigned:
                break
    
    return province_castles

def create_provinces_overview():
    """Creëer de hoofdpagina met overzicht van alle provincies"""
    html = '''<!doctype html>
<html lang="nl">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Kastelen per Provincie | kastelenbelgie.be</title>
  <meta name="description" content="Ontdek de mooiste kastelen van België georganiseerd per provincie. Van Antwerpen tot Luxemburg, elk met hun unieke architecturale schatten.">
  <link rel="stylesheet" href="./css/style.css">
</head>
<body>
  <header class="site-header">
    <div class="container header-inner">
      <a class="brand" href="./">kastelenbelgie.be</a>
      <nav class="nav">
        <a href="./provinces.html">Kastelen per provincie</a>
        <a href="./index.html#blog">Blog</a>
      </nav>
    </div>
  </header>
  
  <main>
    <section class="hero">
      <div class="container">
        <h1>Kastelen per Provincie</h1>
        <p class="lead">Ontdek de rijke kasteelcollectie van België, georganiseerd per provincie. Elke regio heeft zijn eigen architecturale tradities en historische verhalen.</p>
      </div>
    </section>
    
    <section class="section">
      <div class="container">
        <div class="province-grid">'''
    
    province_castles = find_castles_by_province()
    
    for province_id, province_data in PROVINCES.items():
        castle_count = len(province_castles[province_id])
        
        html += f'''
          <a class="province-card" href="{province_id}.html">
            <div class="province-header">
              <h3>{province_data['name']}</h3>
              <span class="castle-count">{castle_count} kastelen</span>
            </div>
            <p>{province_data['description']}</p>
            <span class="province-link">Ontdek kastelen →</span>
          </a>'''
    
    html += '''
        </div>
      </div>
    </section>
  </main>
  
  <footer class="site-footer">
    <div class="container footer-grid">
      <div class="footer-col">
        <h4>Contact</h4>
        <p><a href="./index.html#">Contacteer ons</a></p>
      </div>
      <div class="footer-col">
        <h4>Populaire kastelen</h4>
        <ul>
          <li><a href="kasteel-van-freyr-freyr.html">Kasteel van Freÿr</a></li>
          <li><a href="kasteel-van-durbuy-durbuy.html">Kasteel van Durbuy</a></li>
          <li><a href="citadel-van-hoei-hoei.html">Citadel van Hoei</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Handige links</h4>
        <ul>
          <li><a href="#">Privacy Policy</a></li>
          <li><a href="#">Facebook</a></li>
          <li><a href="#">Twitter</a></li>
        </ul>
      </div>
    </div>
    <div class="container footer-bottom">
      <p>© 2024 kastelenbelgie.be. Alle rechten voorbehouden</p>
    </div>
  </footer>
</body>
</html>'''
    
    return html

def create_province_page(province_id, province_data, castles):
    """Creëer een individuele provinciepagina"""
    castle_count = len(castles)
    
    html = f'''<!doctype html>
<html lang="nl">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Kastelen in {province_data['name']} | kastelenbelgie.be</title>
  <meta name="description" content="Ontdek alle {castle_count} kastelen in de provincie {province_data['name']}. {province_data['description']}">
  <link rel="stylesheet" href="./css/style.css">
</head>
<body>
  <header class="site-header">
    <div class="container header-inner">
      <a class="brand" href="./">kastelenbelgie.be</a>
      <nav class="nav">
        <a href="./provinces.html">Kastelen per provincie</a>
        <a href="./index.html#blog">Blog</a>
      </nav>
    </div>
  </header>
  
  <main>
    <section class="hero">
      <div class="container">
        <nav class="breadcrumb">
          <a href="provinces.html">Provincies</a> → <span>{province_data['name']}</span>
        </nav>
        <h1>Kastelen in {province_data['name']}</h1>
        <p class="lead">{province_data['description']}</p>
        <div class="stats">
          <span class="stat"><strong>{castle_count}</strong> kastelen</span>
        </div>
      </div>
    </section>
    
    <section class="section">
      <div class="container">
        <div class="castle-grid">'''
    
    for castle in sorted(castles, key=lambda x: x['name']):
        html += f'''
          <a class="castle-card" href="{castle['file']}">
            <div class="castle-media gradient-1"></div>
            <div class="castle-info">
              <h3>{castle['name']}</h3>
              <p class="castle-location">{castle['place'].title()}</p>
            </div>
          </a>'''
    
    html += f'''
        </div>
      </div>
    </section>
  </main>
  
  <footer class="site-footer">
    <div class="container footer-grid">
      <div class="footer-col">
        <h4>Contact</h4>
        <p><a href="./index.html#">Contacteer ons</a></p>
      </div>
      <div class="footer-col">
        <h4>Andere provincies</h4>
        <ul>'''
    
    # Voeg links naar andere provincies toe
    other_provinces = [(k, v) for k, v in PROVINCES.items() if k != province_id][:4]
    for other_id, other_data in other_provinces:
        html += f'          <li><a href="{other_id}.html">{other_data["name"]}</a></li>\n'
    
    html += '''        </ul>
      </div>
      <div class="footer-col">
        <h4>Handige links</h4>
        <ul>
          <li><a href="#">Privacy Policy</a></li>
          <li><a href="#">Facebook</a></li>
          <li><a href="#">Twitter</a></li>
        </ul>
      </div>
    </div>
    <div class="container footer-bottom">
      <p>© 2024 kastelenbelgie.be. Alle rechten voorbehouden</p>
    </div>
  </footer>
</body>
</html>'''
    
    return html

def add_province_css():
    """Voeg CSS toe voor provincie-paginas"""
    css_code = '''
/* Province Pages Styles */
.province-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 2rem;
  margin-top: 2rem;
}

.province-card {
  background: white;
  border-radius: 12px;
  padding: 2rem;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
  text-decoration: none;
  color: inherit;
  transition: transform 0.2s, box-shadow 0.2s;
  border: 1px solid #e5e7eb;
}

.province-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 25px rgba(0,0,0,0.15);
  text-decoration: none;
  color: inherit;
}

.province-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.province-header h3 {
  margin: 0;
  color: #1f2937;
  font-size: 1.5rem;
}

.castle-count {
  background: #3b82f6;
  color: white;
  padding: 0.25rem 0.75rem;
  border-radius: 20px;
  font-size: 0.875rem;
  font-weight: 500;
}

.province-card p {
  color: #6b7280;
  line-height: 1.6;
  margin-bottom: 1.5rem;
}

.province-link {
  color: #3b82f6;
  font-weight: 500;
  font-size: 0.875rem;
}

.breadcrumb {
  margin-bottom: 1rem;
  font-size: 0.875rem;
}

.breadcrumb a {
  color: #6b7280;
  text-decoration: none;
}

.breadcrumb a:hover {
  color: #3b82f6;
}

.stats {
  margin-top: 1rem;
}

.stat {
  background: #f3f4f6;
  padding: 0.5rem 1rem;
  border-radius: 8px;
  font-size: 0.875rem;
  color: #374151;
}

.castle-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1.5rem;
  margin-top: 2rem;
}

.castle-card {
  background: white;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  text-decoration: none;
  color: inherit;
  transition: transform 0.2s;
}

.castle-card:hover {
  transform: translateY(-2px);
  text-decoration: none;
  color: inherit;
}

.castle-media {
  height: 200px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.castle-info {
  padding: 1.5rem;
}

.castle-info h3 {
  margin: 0 0 0.5rem 0;
  color: #1f2937;
  font-size: 1.125rem;
}

.castle-location {
  margin: 0;
  color: #6b7280;
  font-size: 0.875rem;
}

@media (max-width: 768px) {
  .province-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
  }
  
  .province-card {
    padding: 1.5rem;
  }
  
  .castle-grid {
    grid-template-columns: 1fr;
  }
}'''
    
    css_file = '/Users/marc/Desktop/kastelenbelgie/css/style.css'
    
    try:
        with open(css_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if '/* Province Pages Styles */' not in content:
            with open(css_file, 'a', encoding='utf-8') as f:
                f.write(css_code)
            return True
        
        return False
        
    except Exception as e:
        print(f"Fout bij CSS toevoegen: {e}")
        return False

def main():
    """Hoofdfunctie"""
    print("=== CREATIE PROVINCIE PAGINAS ===")
    
    # Voeg CSS toe
    print("CSS toevoegen...")
    if add_province_css():
        print("  ✓ Province CSS toegevoegd")
    else:
        print("  ○ Province CSS al aanwezig")
    
    # Analyseer kastelen per provincie
    print("\nAnalyseren kastelen per provincie...")
    province_castles = find_castles_by_province()
    
    total_castles = sum(len(castles) for castles in province_castles.values())
    print(f"  Totaal kastelen gevonden: {total_castles}")
    
    for province, castles in province_castles.items():
        print(f"  {PROVINCES[province]['name']}: {len(castles)} kastelen")
    
    # Creëer hoofdpagina provincies
    print("\nCreëren hoofdpagina provincies...")
    provinces_html = create_provinces_overview()
    
    with open('/Users/marc/Desktop/kastelenbelgie/provinces.html', 'w', encoding='utf-8') as f:
        f.write(provinces_html)
    print("  ✓ provinces.html aangemaakt")
    
    # Creëer individuele provinciepaginas
    print("\nCreëren individuele provinciepaginas...")
    created_pages = 0
    
    for province_id, province_data in PROVINCES.items():
        castles = province_castles[province_id]
        
        if castles:  # Alleen paginas maken voor provincies met kastelen
            province_html = create_province_page(province_id, province_data, castles)
            
            filename = f'/Users/marc/Desktop/kastelenbelgie/{province_id}.html'
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(province_html)
            
            print(f"  ✓ {province_id}.html aangemaakt ({len(castles)} kastelen)")
            created_pages += 1
        else:
            print(f"  ○ Geen kastelen gevonden voor {province_data['name']}")
    
    print(f"\n=== RESULTAAT ===")
    print(f"Hoofdpagina aangemaakt: provinces.html")
    print(f"Provinciepaginas aangemaakt: {created_pages}")
    print(f"Totaal kastelen georganiseerd: {total_castles}")

if __name__ == "__main__":
    main()
