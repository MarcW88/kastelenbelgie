#!/usr/bin/env python3
"""
Script pour corriger les cartes Google Maps sans utiliser l'API
en utilisant les iframes d'embed standard de Google Maps
"""

import os
import re
from pathlib import Path
from bs4 import BeautifulSoup
import urllib.parse

def extract_castle_location(html_file):
    """Extrait le nom du château et l'adresse pour Google Maps"""
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        # Extraire le nom du château depuis le title
        title_tag = soup.find('title')
        castle_name = ""
        if title_tag:
            title = title_tag.get_text()
            castle_name = title.replace(' | kastelenbelgie.be', '').strip()
        
        # Extraire l'adresse depuis les métadonnées
        address = ""
        meta_values = soup.find_all('span', class_='meta-value')
        for meta in meta_values:
            text = meta.get_text().strip()
            # Chercher quelque chose qui ressemble à une adresse
            if any(char.isdigit() for char in text) and len(text) > 5 and 'België' not in text:
                address = text
                break
        
        # Si pas d'adresse trouvée, utiliser le nom du château + België
        if not address:
            address = f"{castle_name}, België"
        else:
            address = f"{address}, België"
        
        return castle_name, address
    
    except Exception as e:
        return "", ""

def fix_maps_without_api():
    """Corrige les cartes Google Maps en utilisant l'embed standard (sans API key)"""
    
    base_dir = Path("/Users/marc/Desktop/kastelenbelgie")
    
    print("🗺️  CORRECTION DES CARTES GOOGLE MAPS (SANS API)")
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
            
            # Extraire les informations du château
            castle_name, address = extract_castle_location(html_file)
            
            # URL encoder l'adresse pour Google Maps
            encoded_address = urllib.parse.quote(address)
            
            # 1. Remplacer les iframes avec API key par des iframes standard
            # Pattern pour les iframes avec clé API
            api_iframe_pattern = r'<iframe[^>]*src="https://www\.google\.com/maps/embed/v1/place\?key=[^"]*"[^>]*></iframe>'
            
            # Nouvelle iframe sans API key (utilise l'embed standard de Google)
            new_iframe = f'''<iframe 
                        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2000!2d0!3d0!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zQ2FzdGxl!5e0!3m2!1sen!2sbe!4v1000000000000!5m2!1sen!2sbe&q={encoded_address}"
                        width="100%" 
                        height="400" 
                        style="border:0;" 
                        allowfullscreen="" 
                        loading="lazy" 
                        referrerpolicy="no-referrer-when-downgrade">
                    </iframe>'''
            
            # Méthode alternative plus simple : utiliser l'URL de recherche Google Maps
            simple_iframe = f'''<iframe 
                        src="https://maps.google.com/maps?q={encoded_address}&t=&z=15&ie=UTF8&iwloc=&output=embed"
                        width="100%" 
                        height="400" 
                        style="border:0;" 
                        allowfullscreen="" 
                        loading="lazy">
                    </iframe>'''
            
            content = re.sub(api_iframe_pattern, simple_iframe, content)
            
            # 2. Corriger les liens Google Maps
            # Corriger les liens "Open in Google Maps"
            old_link_pattern = r'<a href="https://www\.google\.com/maps/search/([^"]*)"'
            new_link = f'<a href="https://www.google.com/maps/search/{encoded_address}"'
            content = re.sub(old_link_pattern, new_link, content)
            
            # Corriger les liens "Routebeschrijving"
            old_directions_pattern = r'<a href="https://www\.google\.com/maps/dir//([^"]*)"'
            new_directions = f'<a href="https://www.google.com/maps/dir//{encoded_address}"'
            content = re.sub(old_directions_pattern, new_directions, content)
            
            # 3. Améliorer le titre de la carte
            if castle_name:
                # Mettre à jour le titre de la carte
                old_title_pattern = r'<h3>📍 Locatie van [^<]*</h3>'
                new_title = f'<h3>📍 Locatie van {castle_name}</h3>'
                content = re.sub(old_title_pattern, new_title, content)
            
            # 4. Mettre à jour l'adresse affichée
            if address:
                old_address_pattern = r'<p><strong>Adres:</strong> [^<]*</p>'
                new_address_display = f'<p><strong>Adres:</strong> {address}</p>'
                content = re.sub(old_address_pattern, new_address_display, content)
            
            if content != original_content:
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                files_modified += 1
                print(f"✅ {html_file.name} - Carte corrigée: {castle_name}")
        
        except Exception as e:
            print(f"❌ Erreur avec {html_file.name}: {e}")
    
    print(f"\n📊 RÉSULTATS:")
    print(f"   Fichiers traités: {files_processed}")
    print(f"   Fichiers modifiés: {files_modified}")
    
    if files_modified > 0:
        print(f"\n🎉 Cartes Google Maps corrigées!")
        print("   - Plus d'erreur API key")
        print("   - Cartes fonctionnelles sans authentification")
        print("   - Localisation précise par château")
        print("   - Liens Maps et directions fonctionnels")
    else:
        print("\n✨ Cartes déjà fonctionnelles!")

if __name__ == "__main__":
    fix_maps_without_api()
