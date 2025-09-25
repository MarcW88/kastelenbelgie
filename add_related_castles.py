#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
AJOUT DE CHÂTEAUX RELIÉS AVEC DESCRIPTIONS
Remplace les châteaux génériques par de vrais châteaux de la même région
"""

import os
import re
import glob
import random

# Base de données des châteaux par province
CASTLES_BY_PROVINCE = {
    "Antwerpen": [
        {"name": "Kasteel van Brasschaat", "description": "Prachtig neoclassicistisch kasteel uit de 19e eeuw, omgeven door een uitgestrekt park.", "url": "kasteel-van-brasschaat.html"},
        {"name": "Kasteel van Bouchout", "description": "Romantisch kasteel in Meise, bekend om zijn botanische tuinen en rijke geschiedenis.", "url": "kasteel-van-bouchout-te-meise.html"},
        {"name": "Kasteel Cleydael", "description": "Waterslot uit de 16e eeuw in Aartselaar, omringd door grachten en eeuwenoude bomen.", "url": "waterslot-cleydael.html"},
        {"name": "Kasteel van Zellaer", "description": "Imposant kasteel in Bonheiden met een rijke geschiedenis en prachtige architectuur.", "url": "kasteel-van-zellaer.html"},
        {"name": "Kasteel Arendsnest", "description": "Charmant kasteel in Edegem, bekend om zijn pittoreske ligging en historische waarde.", "url": "kasteel-arendsnest.html"}
    ],
    "Limburg": [
        {"name": "Kasteel van Hex", "description": "Middeleeuws kasteel met imposante torens en een fascinerende geschiedenis.", "url": "kasteel-van-hex.html"},
        {"name": "Kasteel van Rijckholt", "description": "Historisch kasteel aan de Maas met prachtige tuinen en authentieke architectuur.", "url": "kasteel-van-rijckholt.html"},
        {"name": "Kasteel Ter Dolen", "description": "Elegant kasteel in Houthalen-Helchteren, omgeven door natuur en geschiedenis.", "url": "kasteel-ter-dolen.html"},
        {"name": "Kasteel van Vogelsanck", "description": "Romantisch kasteel in Zolder met een unieke architecturale stijl.", "url": "kasteel-van-vogelsanck.html"}
    ],
    "Oost-Vlaanderen": [
        {"name": "Kasteel van Laarne", "description": "Middeleeuws waterslot met een indrukwekkende collectie zilverwerk en tapijten.", "url": "kasteel-van-laarne.html"},
        {"name": "Kasteel van Ooidonk", "description": "Sprookjesachtig kasteel uit de 16e eeuw met prachtige Franse tuinen.", "url": "kasteel-van-ooidonk.html"},
        {"name": "Kasteel van Beervelde", "description": "Neoclassicistisch kasteel bekend om zijn magnolia's en azalea's in het voorjaar.", "url": "kasteel-van-beervelde.html"},
        {"name": "Gravensteen", "description": "Iconische middeleeuwse burcht in het hart van Gent, symbool van de stad.", "url": "gravensteen-gent.html"}
    ],
    "West-Vlaanderen": [
        {"name": "Kasteel van Tillegem", "description": "Historisch kasteel in Brugge met prachtige tuinen en een rijke geschiedenis.", "url": "kasteel-van-tillegem.html"},
        {"name": "Kasteel van Wijnendale", "description": "Middeleeuws kasteel waar Maria van Bourgondië overleed, vol geschiedenis.", "url": "kasteel-van-wijnendale.html"},
        {"name": "Kasteel van Loppem", "description": "Neo-gotisch kasteel met een indrukwekkende collectie kunst en antiek.", "url": "kasteel-van-loppem.html"},
        {"name": "Kasteel van Beauvoorde", "description": "Charmant kasteel in de Westhoek met authentieke interieurs.", "url": "kasteel-van-beauvoorde.html"}
    ],
    "Vlaams-Brabant": [
        {"name": "Kasteel van Gaasbeek", "description": "Imposant kasteel met een rijke collectie kunst en historische voorwerpen.", "url": "kasteel-van-gaasbeek.html"},
        {"name": "Kasteel van Horst", "description": "Renaissance kasteel in Holsbeek met prachtige tuinen en architectuur.", "url": "kasteel-van-horst.html"},
        {"name": "Kasteel van Arenberg", "description": "Historisch kasteel in Leuven, nu deel van de universiteit.", "url": "kasteel-van-arenberg.html"},
        {"name": "Kasteel van Beersel", "description": "Middeleeuws waterslot met drie ronde torens, perfect bewaard gebleven.", "url": "kasteel-van-beersel.html"}
    ],
    "Namen": [
        {"name": "Kasteel van Freÿr", "description": "Prachtig kasteel aan de Maas met beroemde tuinen in Franse stijl.", "url": "kasteel-van-freyr-freyr.html"},
        {"name": "Citadel van Namen", "description": "Imposante vesting op een rots boven de Maas, symbool van de stad.", "url": "citadel-van-namen.html"},
        {"name": "Kasteel van Annevoie", "description": "Bekend om zijn watertuinen en cascades, een uniek erfgoed.", "url": "kasteel-van-annevoie.html"},
        {"name": "Kasteel van Spontin", "description": "Middeleeuws kasteel met een donjon uit de 14e eeuw.", "url": "kasteel-van-spontin.html"}
    ],
    "Luik": [
        {"name": "Kasteel van Jehay", "description": "Uniek dambordkasteel uit de 16e eeuw met schaakbordpatroon.", "url": "kasteel-van-jehay.html"},
        {"name": "Citadel van Hoei", "description": "Strategische vesting op 100 meter hoogte boven de Maas.", "url": "citadel-van-hoei-hoei.html"},
        {"name": "Kasteel van Modave", "description": "Elegant kasteel uit de 17e eeuw met prachtige interieurs.", "url": "kasteel-van-modave.html"},
        {"name": "Kasteel van Warfusée", "description": "Historisch kasteel met een rijke geschiedenis en mooie architectuur.", "url": "kasteel-van-warfusee.html"}
    ],
    "Luxemburg": [
        {"name": "Kasteel van Durbuy", "description": "Privé kasteel in de kleinste stad van België, vol charme en geschiedenis.", "url": "kasteel-van-durbuy-durbuy.html"},
        {"name": "Kasteel van La Roche-en-Ardenne", "description": "Ruïnes van een middeleeuws kasteel op een rots boven de Ourthe.", "url": "kasteel-van-la-roche-en-ardenne.html"},
        {"name": "Kasteel van Mirwart", "description": "Romantisch kasteel in de Ardennen met prachtige natuur rondom.", "url": "kasteel-van-mirwart.html"},
        {"name": "Kasteel van Bouillon", "description": "Een van de oudste burchten van Europa, vol middeleeuwse geschiedenis.", "url": "kasteel-van-bouillon.html"}
    ],
    "Henegouwen": [
        {"name": "Kasteel van Beloeil", "description": "Het 'Versailles van België' met prachtige tuinen en rijke collecties.", "url": "kasteel-van-beloeil.html"},
        {"name": "Kasteel van Seneffe", "description": "18e-eeuws kasteel met een indrukwekkende collectie zilverwerk.", "url": "kasteel-van-seneffe.html"},
        {"name": "Kasteel van Attre", "description": "Rococo kasteel met authentieke interieurs en prachtige tuinen.", "url": "kasteel-van-attre.html"},
        {"name": "Kasteel van Chimay", "description": "Historisch kasteel van de prinsen van Chimay met rijke geschiedenis.", "url": "kasteel-van-chimay.html"}
    ],
    "Waals-Brabant": [
        {"name": "Kasteel van Rixensart", "description": "Elegant kasteel met prachtige tuinen en historische waarde.", "url": "kasteel-van-rixensart.html"},
        {"name": "Kasteel van Hélécine", "description": "Charmant kasteel in een groene omgeving met rijke geschiedenis.", "url": "kasteel-van-helecine.html"},
        {"name": "Kasteel van Bois-Seigneur-Isaac", "description": "Historisch kasteel met een fascinerende geschiedenis.", "url": "kasteel-van-bois-seigneur-isaac.html"},
        {"name": "Kasteel van Walhain", "description": "Pittoresk kasteel in een landelijke omgeving.", "url": "kasteel-van-walhain.html"}
    ]
}

def get_province_from_page(content):
    """Extrait la province d'une page château"""
    province_match = re.search(r'<span class="meta-value">([^<]+)</span>', content)
    if province_match:
        return province_match.group(1).strip()
    
    # Essayer dans les breadcrumbs
    breadcrumb_match = re.search(r'<a href="([^"]+)\.html"[^>]*>([^<]+)</a>\s*<span[^>]*>›</span>\s*<span[^>]*>[^<]*</span>', content)
    if breadcrumb_match:
        return breadcrumb_match.group(2).strip()
    
    return None

def get_related_castles(province, current_castle_name, count=3):
    """Obtient des châteaux reliés pour une province"""
    if province not in CASTLES_BY_PROVINCE:
        # Utiliser Antwerpen par défaut
        province = "Antwerpen"
    
    available_castles = CASTLES_BY_PROVINCE[province].copy()
    
    # Retirer le château actuel de la liste
    available_castles = [c for c in available_castles if c['name'].lower() not in current_castle_name.lower()]
    
    # Sélectionner aléatoirement
    if len(available_castles) >= count:
        return random.sample(available_castles, count)
    else:
        return available_castles

def update_related_castles_section(content, province, castle_name):
    """Met à jour la section châteaux reliés"""
    related_castles = get_related_castles(province, castle_name, 3)
    
    if not related_castles:
        return content
    
    # Créer le HTML pour les châteaux reliés
    related_html = ""
    for castle in related_castles:
        related_html += f'''
                <div class="castle-card">
                    <div class="castle-image-placeholder">
                        <span>🏰</span>
                    </div>
                    <div class="castle-card-content">
                        <h3>{castle['name']}</h3>
                        <p class="card-description">{castle['description']}</p>
                        <a href="{castle['url']}" class="btn-primary">Meer info</a>
                    </div>
                </div>'''
    
    # Chercher et remplacer la section related castles
    pattern = r'(<section class="related-castles">.*?<div class="castles-grid">)(.*?)(</div>\s*</div>\s*</section>)'
    
    replacement = f'''\\1{related_html}
            \\3'''
    
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    return new_content

def add_related_castles_to_all_pages():
    """Ajoute des châteaux reliés à toutes les pages"""
    castle_files = []
    
    # Chercher tous les fichiers de châteaux
    patterns = ['kasteel-*.html', 'chateau-*.html', 'citadel-*.html', 'burcht-*.html']
    for pattern in patterns:
        castle_files.extend(glob.glob(f"/Users/marc/Desktop/kastelenbelgie/{pattern}"))
    
    print(f"🏰 AJOUT DE CHÂTEAUX RELIÉS À {len(castle_files)} PAGES")
    print("=" * 60)
    
    updated_count = 0
    
    for i, filepath in enumerate(castle_files, 1):
        filename = os.path.basename(filepath)
        print(f"\n[{i}/{len(castle_files)}] Traitement de {filename}")
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extraire le nom du château et la province
            title_match = re.search(r'<title>([^|]+)', content)
            if not title_match:
                print(f"  ⚠️ Titre non trouvé")
                continue
                
            castle_name = title_match.group(1).strip()
            province = get_province_from_page(content)
            
            if not province:
                print(f"  ⚠️ Province non trouvée")
                continue
            
            print(f"  Château: {castle_name}")
            print(f"  Province: {province}")
            
            # Vérifier si la section related castles existe
            if 'related-castles' not in content:
                print(f"  ⚠️ Section related-castles non trouvée")
                continue
            
            # Mettre à jour la section
            new_content = update_related_castles_section(content, province, castle_name)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                updated_count += 1
                print(f"  ✅ Châteaux reliés ajoutés")
            else:
                print(f"  ⚠️ Aucune modification")
                
        except Exception as e:
            print(f"  ❌ Erreur: {e}")
    
    print(f"\n✅ TERMINÉ: {updated_count} pages mises à jour avec des châteaux reliés")

def add_css_for_card_descriptions():
    """Ajoute le CSS pour les descriptions des cartes"""
    css_file = "/Users/marc/Desktop/kastelenbelgie/css/modern-style.css"
    
    css_to_add = """
/* Descriptions des cartes châteaux */
.card-description {
    font-size: 0.9rem;
    color: #64748b;
    line-height: 1.5;
    margin: 0.5rem 0 1rem 0;
}

.castle-card-content .card-description {
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
    text-overflow: ellipsis;
}
"""
    
    try:
        if os.path.exists(css_file):
            with open(css_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if 'card-description' not in content:
                with open(css_file, 'a', encoding='utf-8') as f:
                    f.write(css_to_add)
                print("✅ CSS ajouté pour les descriptions des cartes")
            else:
                print("✅ CSS déjà présent")
        else:
            print("⚠️ Fichier CSS non trouvé")
    except Exception as e:
        print(f"❌ Erreur ajout CSS: {e}")

def main():
    """Fonction principale"""
    print("🏰 AMÉLIORATION DES CHÂTEAUX RELIÉS")
    print("=" * 50)
    
    # Ajouter le CSS nécessaire
    add_css_for_card_descriptions()
    
    # Ajouter les châteaux reliés
    add_related_castles_to_all_pages()

if __name__ == "__main__":
    main()
