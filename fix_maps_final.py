#!/usr/bin/env python3
"""
Script pour corriger définitivement les cartes Google Maps
en remplaçant TOUTES les iframes avec API key par des iframes standard
"""

import os
import re
from pathlib import Path
from bs4 import BeautifulSoup
import urllib.parse

def extract_location_from_iframe(iframe_src):
    """Extrait la localisation depuis l'URL de l'iframe"""
    try:
        # Extraire le paramètre q= de l'URL
        if 'q=' in iframe_src:
            # Trouver la partie après q=
            q_part = iframe_src.split('q=')[1]
            # Prendre jusqu'au prochain & ou fin de chaîne
            location = q_part.split('&')[0]
            # Décoder l'URL
            location = urllib.parse.unquote(location)
            return location
        return ""
    except:
        return ""

def fix_maps_final():
    """Correction finale des cartes Google Maps"""
    
    base_dir = Path("/Users/marc/Desktop/kastelenbelgie")
    
    print("🗺️  CORRECTION FINALE DES CARTES GOOGLE MAPS")
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
            
            # 1. Trouver TOUTES les iframes Google Maps avec API key
            iframe_pattern = r'<iframe[^>]*src="https://www\.google\.com/maps/embed/v1/place\?key=AIzaSyAvyQt1-zQB1bzIX3N8KnYKgPCs-8d328s&q=([^"]*)"[^>]*></iframe>'
            
            def replace_iframe(match):
                # Extraire la localisation
                location = urllib.parse.unquote(match.group(1))
                encoded_location = urllib.parse.quote(location)
                
                # Créer la nouvelle iframe sans API key
                return f'''<iframe 
                        src="https://maps.google.com/maps?q={encoded_location}&t=&z=15&ie=UTF8&iwloc=&output=embed"
                        width="100%" 
                        height="400" 
                        style="border:0;" 
                        allowfullscreen="" 
                        loading="lazy">
                    </iframe>'''
            
            # Remplacer toutes les iframes
            content = re.sub(iframe_pattern, replace_iframe, content)
            
            # 2. Vérifier s'il reste des références à l'API key
            if 'AIzaSyAvyQt1-zQB1bzIX3N8KnYKgPCs-8d328s' in content:
                # Remplacer toute référence restante
                content = content.replace('AIzaSyAvyQt1-zQB1bzIX3N8KnYKgPCs-8d328s', '')
                
                # Nettoyer les URLs cassées
                content = re.sub(r'key=&', '', content)
                content = re.sub(r'\?key=&', '?', content)
                content = re.sub(r'&key=', '', content)
            
            # 3. Corriger les iframes malformées
            malformed_pattern = r'<iframe[^>]*src="https://www\.google\.com/maps/embed/v1/place\?[^"]*"[^>]*></iframe>'
            
            def fix_malformed_iframe(match):
                iframe_content = match.group(0)
                # Extraire une localisation par défaut
                return '''<iframe 
                        src="https://maps.google.com/maps?q=België&t=&z=10&ie=UTF8&iwloc=&output=embed"
                        width="100%" 
                        height="400" 
                        style="border:0;" 
                        allowfullscreen="" 
                        loading="lazy">
                    </iframe>'''
            
            content = re.sub(malformed_pattern, fix_malformed_iframe, content)
            
            if content != original_content:
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                files_modified += 1
                print(f"✅ {html_file.name} - Carte corrigée définitivement")
        
        except Exception as e:
            print(f"❌ Erreur avec {html_file.name}: {e}")
    
    print(f"\n📊 RÉSULTATS:")
    print(f"   Fichiers traités: {files_processed}")
    print(f"   Fichiers modifiés: {files_modified}")
    
    if files_modified > 0:
        print(f"\n🎉 Cartes Google Maps définitivement corrigées!")
        print("   - Plus d'API key dans les iframes")
        print("   - Cartes fonctionnelles sans authentification")
        print("   - Plus d'erreur 'API project not authorized'")
    else:
        print("\n✨ Toutes les cartes sont déjà fonctionnelles!")

if __name__ == "__main__":
    fix_maps_final()
