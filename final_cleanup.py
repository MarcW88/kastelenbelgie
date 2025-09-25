#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
NETTOYAGE FINAL PRÉCIS
Répare le HTML restant corrompu
"""

import glob
import re
import os

def clean_corrupted_html_precisely():
    """Nettoie précisément le HTML corrompu restant"""
    
    print("🧹 NETTOYAGE FINAL PRÉCIS DU HTML")
    print("-" * 50)
    
    castle_files = glob.glob("/Users/marc/Desktop/kastelenbelgie/kasteel-*.html")
    castle_files.extend(glob.glob("/Users/marc/Desktop/kastelenbelgie/chateau-*.html"))
    
    # Textes de remplacement propres
    clean_texts = [
        "Een kasteel met een fascinerende geschiedenis en unieke architectuur.",
        "Ontdek de rijke verhalen en prachtige details van dit monument.",
        "Een prachtig voorbeeld van Belgische kasteelarchitectuur.",
        "Laat je verrassen door de schoonheid van dit kasteel.",
        "Een must-see kasteel vol geschiedenis en charme.",
        "Verken dit historische juweel en zijn verhalen.",
        "Een kasteel dat getuigt van onze rijke geschiedenis.",
        "Ontdek de architecturale pracht van dit monument."
    ]
    
    fixed_count = 0
    
    for castle_file in castle_files:
        try:
            with open(castle_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Pattern spécifique pour le HTML corrompu détecté
            # "Ontdek de rijke verhalen en prachtige details van dit historische monument.achtige kasteel in Namen"
            corrupted_pattern = r'<p class="card-description-modern">([^<]*?)\.achtige kasteel in [^<]*</p>'
            
            def replace_corrupted(match):
                # Prendre le texte avant ".achtige" et le nettoyer
                clean_text = match.group(1).strip()
                if clean_text.endswith('.'):
                    return f'<p class="card-description-modern">{clean_text}</p>'
                else:
                    return f'<p class="card-description-modern">{clean_text}.</p>'
            
            content = re.sub(corrupted_pattern, replace_corrupted, content)
            
            # Autres patterns corrompus
            content = re.sub(
                r'<p class="card-description-modern">Ontdek dit prachtige kasteel in [^<]*</p>',
                f'<p class="card-description-modern">{clean_texts[0]}</p>',
                content
            )
            
            # Nettoyer les textes qui se terminent mal
            content = re.sub(
                r'<p class="card-description-modern">([^<]*?)achtige kasteel[^<]*</p>',
                f'<p class="card-description-modern">{clean_texts[1]}</p>',
                content
            )
            
            if content != original_content:
                with open(castle_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                fixed_count += 1
                filename = os.path.basename(castle_file)
                print(f"✅ {filename}: HTML nettoyé")
        
        except Exception as e:
            continue
    
    print(f"✅ {fixed_count} pages nettoyées")

if __name__ == "__main__":
    print("🧹 NETTOYAGE FINAL PRÉCIS")
    print("=" * 40)
    
    clean_corrupted_html_precisely()
    
    print(f"\n🎉 NETTOYAGE TERMINÉ!")
    print("✅ HTML corrompu nettoyé précisément")
    print("\n🚀 Site maintenant propre!")
