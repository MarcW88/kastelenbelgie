#!/usr/bin/env python3
"""
Script final pour s'assurer que toutes les cartes utilisent la bonne URL sans API
"""

import os
import re
from pathlib import Path
import urllib.parse

def final_maps_cleanup():
    """Nettoyage final pour s'assurer que toutes les cartes fonctionnent"""
    
    base_dir = Path("/Users/marc/Desktop/kastelenbelgie")
    
    print("🔧 NETTOYAGE FINAL DES CARTES")
    print("=" * 35)
    
    files_processed = 0
    files_modified = 0
    
    # Parcourir toutes les pages châteaux
    for html_file in base_dir.glob("*.html"):
        # Ignorer les pages non-châteaux
        if html_file.name in ['index.html', 'contact.html', 'blog.html', 'provinces.html', 
                             'antwerpen.html', 'limburg.html', 'oost-vlaanderen.html', 
                             'west-vlaanderen.html', 'vlaams-brabant.html', 'namen.html',
                             'luxemburg.html', 'luik.html', 'henegouwen.html', 'waals-brabant.html']:
            continue
        
        if html_file.name.startswith('blog-'):
            continue
        
        files_processed += 1
        
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Remplacer toute iframe qui utilise encore l'API v1
            if 'maps/embed/v1/' in content:
                # Extraire le nom du château depuis le titre
                title_match = re.search(r'<title>([^|]+)', content)
                castle_name = "België"
                if title_match:
                    castle_name = title_match.group(1).strip()
                
                encoded_name = urllib.parse.quote(castle_name + ", België")
                
                # Remplacer par l'iframe standard
                new_iframe = f'''<iframe 
                        src="https://maps.google.com/maps?q={encoded_name}&t=&z=15&ie=UTF8&iwloc=&output=embed"
                        width="100%" 
                        height="400" 
                        style="border:0;" 
                        allowfullscreen="" 
                        loading="lazy">
                    </iframe>'''
                
                # Pattern pour capturer l'iframe complète
                iframe_pattern = r'<iframe[^>]*src="https://www\.google\.com/maps/embed/v1/[^"]*"[^>]*></iframe>'
                content = re.sub(iframe_pattern, new_iframe, content, flags=re.DOTALL)
            
            if content != original_content:
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                files_modified += 1
                print(f"✅ {html_file.name} - Iframe corrigée")
        
        except Exception as e:
            print(f"❌ Erreur avec {html_file.name}: {e}")
    
    print(f"\n📊 RÉSULTATS:")
    print(f"   Fichiers traités: {files_processed}")
    print(f"   Fichiers modifiés: {files_modified}")
    
    if files_modified > 0:
        print(f"\n🎉 Nettoyage final terminé!")
        print("   - Toutes les cartes utilisent maintenant l'embed standard")
        print("   - Plus d'erreur API")
    else:
        print("\n✨ Toutes les cartes sont déjà correctes!")

if __name__ == "__main__":
    final_maps_cleanup()
