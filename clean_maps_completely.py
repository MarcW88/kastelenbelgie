#!/usr/bin/env python3
"""
Script pour nettoyer complètement toutes les références aux cartes Google Maps
et les remplacer par des iframes fonctionnelles sans API
"""

import os
import re
from pathlib import Path
import urllib.parse

def clean_maps_completely():
    """Nettoyage complet des cartes Google Maps"""
    
    base_dir = Path("/Users/marc/Desktop/kastelenbelgie")
    
    print("🧹 NETTOYAGE COMPLET DES CARTES GOOGLE MAPS")
    print("=" * 50)
    
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
            
            # 1. Remplacer TOUTES les iframes Google Maps par une version simple
            # Pattern très large pour capturer toutes les variantes
            iframe_patterns = [
                r'<iframe[^>]*src="https://www\.google\.com/maps/embed/v1/[^"]*"[^>]*></iframe>',
                r'<iframe[^>]*src="https://maps\.google\.com/maps[^"]*"[^>]*></iframe>',
                r'<iframe[^>]*google\.com/maps[^>]*></iframe>'
            ]
            
            # Extraire la localisation depuis le titre de la page
            title_match = re.search(r'<title>([^|]+)', content)
            castle_name = "België"
            if title_match:
                castle_name = title_match.group(1).strip()
            
            # Créer une iframe simple et fonctionnelle
            simple_iframe = f'''<iframe 
                        src="https://maps.google.com/maps?q={urllib.parse.quote(castle_name + ", België")}&t=&z=15&ie=UTF8&iwloc=&output=embed"
                        width="100%" 
                        height="400" 
                        style="border:0;" 
                        allowfullscreen="" 
                        loading="lazy">
                    </iframe>'''
            
            # Remplacer toutes les iframes
            for pattern in iframe_patterns:
                content = re.sub(pattern, simple_iframe, content, flags=re.DOTALL)
            
            # 2. Nettoyer toute référence à l'API key
            content = content.replace('AIzaSyAvyQt1-zQB1bzIX3N8KnYKgPCs-8d328s', '')
            content = re.sub(r'key=[^&"]*&?', '', content)
            content = re.sub(r'\?&', '?', content)
            content = re.sub(r'&&', '&', content)
            
            # 3. Corriger les liens Maps
            # Extraire l'adresse depuis les métadonnées si possible
            address_match = re.search(r'<p><strong>Adres:</strong>\s*([^<]+)</p>', content)
            location = castle_name + ", België"
            if address_match:
                location = address_match.group(1).strip() + ", België"
            
            encoded_location = urllib.parse.quote(location)
            
            # Corriger les liens "Open in Google Maps"
            content = re.sub(
                r'<a href="https://www\.google\.com/maps/search/[^"]*"',
                f'<a href="https://www.google.com/maps/search/{encoded_location}"',
                content
            )
            
            # Corriger les liens "Routebeschrijving"
            content = re.sub(
                r'<a href="https://www\.google\.com/maps/dir//[^"]*"',
                f'<a href="https://www.google.com/maps/dir//{encoded_location}"',
                content
            )
            
            if content != original_content:
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                files_modified += 1
                print(f"✅ {html_file.name} - Carte nettoyée complètement")
        
        except Exception as e:
            print(f"❌ Erreur avec {html_file.name}: {e}")
    
    print(f"\n📊 RÉSULTATS:")
    print(f"   Fichiers traités: {files_processed}")
    print(f"   Fichiers modifiés: {files_modified}")
    
    if files_modified > 0:
        print(f"\n🎉 Cartes Google Maps complètement nettoyées!")
        print("   - Toutes les références API supprimées")
        print("   - Iframes simples et fonctionnelles")
        print("   - Plus d'erreur d'autorisation")
        print("   - Cartes affichées correctement")
    else:
        print("\n✨ Toutes les cartes sont déjà propres!")

if __name__ == "__main__":
    clean_maps_completely()
