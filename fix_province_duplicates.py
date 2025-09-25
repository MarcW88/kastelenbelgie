#!/usr/bin/env python3
"""
Script pour supprimer les doublons de titre/intro sur les pages provinces
"""

import os
import re
from pathlib import Path

def fix_province_duplicates():
    """Supprime les sections hero-modern dupliquées sur les pages provinces"""
    
    base_dir = Path("/Users/marc/Desktop/kastelenbelgie")
    
    # Pages provinces à traiter
    province_pages = [
        'antwerpen.html', 'limburg.html', 'oost-vlaanderen.html', 
        'west-vlaanderen.html', 'vlaams-brabant.html', 'namen.html',
        'luxemburg.html', 'luik.html', 'henegouwen.html', 'waals-brabant.html'
    ]
    
    print("🗑️  SUPPRESSION DES DOUBLONS TITRE/INTRO PROVINCES")
    print("=" * 55)
    
    files_processed = 0
    files_modified = 0
    
    for page_name in province_pages:
        page_file = base_dir / page_name
        
        if not page_file.exists():
            print(f"⚠️  {page_name} non trouvé")
            continue
        
        files_processed += 1
        
        try:
            with open(page_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Supprimer la section hero-modern complète (première section avec titre/intro)
            # Pattern pour capturer toute la section hero-modern
            hero_pattern = r'<!-- Hero -->\s*<section class="hero-modern">.*?</section>'
            content = re.sub(hero_pattern, '', content, flags=re.DOTALL)
            
            # Alternative si le pattern ci-dessus ne fonctionne pas
            hero_pattern2 = r'<section class="hero-modern">.*?</section>'
            content = re.sub(hero_pattern2, '', content, flags=re.DOTALL)
            
            # Nettoyer les espaces multiples créés
            content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
            
            # Vérifier si on a bien supprimé le doublon
            if content != original_content:
                with open(page_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                files_modified += 1
                print(f"✅ {page_name} - Section hero dupliquée supprimée")
            else:
                print(f"ℹ️  {page_name} - Aucun doublon détecté")
        
        except Exception as e:
            print(f"❌ Erreur avec {page_name}: {e}")
    
    print(f"\n📊 RÉSULTATS:")
    print(f"   Fichiers traités: {files_processed}")
    print(f"   Fichiers modifiés: {files_modified}")
    
    if files_modified > 0:
        print(f"\n🎉 Doublons supprimés!")
        print("   - Plus de titres dupliqués")
        print("   - Espacement réduit en haut de page")
        print("   - Structure plus propre")
    else:
        print("\n✨ Aucun doublon trouvé!")

if __name__ == "__main__":
    fix_province_duplicates()
