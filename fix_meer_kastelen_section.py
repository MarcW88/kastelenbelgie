#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CORRECTION SECTION "MEER KASTELEN" 
Remplace les liens vers provinces par des châteaux de la même province
"""

from castle_organizer import CastleOrganizer
import re
import glob

def fix_meer_kastelen_section():
    """Corrige la section Meer kastelen sur toutes les pages châteaux"""
    
    print("🏰 CORRECTION SECTION 'MEER KASTELEN'")
    print("=" * 60)
    
    # Charger les données des châteaux
    organizer = CastleOrganizer()
    organizer.load_castles_data()
    
    # Trouver tous les fichiers de châteaux
    castle_files = []
    patterns = [
        "kasteel-*.html", "hof-*.html", "het-*.html", "de-*.html", 
        "sint-*.html", "chateau-*.html", "burcht-*.html", "paleis-*.html",
        "commanderij-*.html", "waterkasteel-*.html", "waterburcht-*.html",
        "koninklijk-*.html", "gaverkasteel-*.html", "citadel-*.html",
        "domein-*.html", "bisschoppenhof-*.html", "waterslot-*.html",
        "braemkasteel-*.html", "vrieselhof-*.html", "rood-*.html",
        "rentmeesterij-*.html", "oud-*.html"
    ]
    
    for pattern in patterns:
        castle_files.extend(glob.glob(f"/Users/marc/Desktop/kastelenbelgie/{pattern}"))
    
    print(f"📊 {len(castle_files)} fichiers de châteaux trouvés")
    
    updated_count = 0
    
    for castle_file in castle_files:
        try:
            # Lire le fichier
            with open(castle_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extraire le nom du château et la province depuis le contenu
            castle_name = extract_castle_name_from_content(content)
            province = extract_province_from_content(content)
            
            if not castle_name or not province:
                continue
            
            # Obtenir des châteaux liés dans la même province
            related_castles = organizer.get_related_castles_in_province(castle_name, province, 3)
            
            if len(related_castles) < 2:
                continue  # Pas assez de châteaux liés
            
            # Générer le HTML pour les châteaux liés
            related_html = generate_related_castles_html(related_castles)
            
            # Chercher et remplacer la section "Meer kastelen"
            meer_pattern = r'<section[^>]*class="[^"]*related-castles[^"]*"[^>]*>.*?</section>'
            meer_match = re.search(meer_pattern, content, re.DOTALL)
            
            if meer_match:
                new_content = content[:meer_match.start()] + related_html + content[meer_match.end():]
                
                # Sauvegarder
                with open(castle_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                updated_count += 1
                print(f"✅ {castle_name}: {len(related_castles)} châteaux liés ajoutés")
            
        except Exception as e:
            print(f"❌ Erreur avec {castle_file}: {e}")
            continue
    
    print(f"\n📊 RÉSULTATS:")
    print(f"Pages mises à jour: {updated_count}")

def extract_castle_name_from_content(content):
    """Extrait le nom du château depuis le contenu HTML"""
    # Chercher dans le title
    title_match = re.search(r'<title>([^|]+)', content)
    if title_match:
        return title_match.group(1).strip()
    
    # Chercher dans le h1
    h1_match = re.search(r'<h1[^>]*>([^<]+)</h1>', content)
    if h1_match:
        return h1_match.group(1).strip()
    
    return None

def extract_province_from_content(content):
    """Extrait la province depuis le contenu HTML"""
    province_match = re.search(r'<strong>Provincie:</strong>\s*<span[^>]*>([^<]+)</span>', content)
    if province_match:
        return province_match.group(1).strip()
    return None

def generate_related_castles_html(related_castles):
    """Génère le HTML pour les châteaux liés"""
    cards_html = ""
    
    for castle in related_castles:
        image_src = f"chateaux_images_update-2/{castle['image']}" if castle['image'] else "assets/placeholder-castle-card.svg"
        
        cards_html += f'''
                <div class="related-castle-card">
                    <div class="castle-image">
                        <img src="{image_src}" alt="{castle['title']}" loading="lazy">
                    </div>
                    <div class="castle-card-content">
                        <h3>{castle['title']}</h3>
                        <p class="card-description">Ontdek dit prachtige kasteel in {castle['province']}</p>
                        <a href="{castle['filename']}.html" class="btn-primary">Meer info</a>
                    </div>
                </div>
        '''
    
    return f'''
    <!-- Section Meer kastelen -->
    <section class="related-castles-section">
        <div class="container">
            <h2 class="section-title">Meer kastelen in de buurt</h2>
            <p class="section-description">Ontdek andere prachtige kastelen in dezelfde provincie</p>
            <div class="related-castles-grid">
                {cards_html}
            </div>
        </div>
    </section>
'''

if __name__ == "__main__":
    fix_meer_kastelen_section()
