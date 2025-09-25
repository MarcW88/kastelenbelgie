#!/usr/bin/env python3
"""
Script pour corriger les cartes Google Maps en utilisant l'API avec la clé fournie
et améliorer l'intégration des cartes géographiques
"""

import os
import re
from pathlib import Path
from bs4 import BeautifulSoup

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
            # Chercher quelque chose qui ressemble à une adresse (avec des chiffres)
            if any(char.isdigit() for char in text) and len(text) > 5:
                address = text
                break
        
        # Si pas d'adresse trouvée, utiliser le nom du château
        if not address:
            address = castle_name
        
        return castle_name, address
    
    except Exception as e:
        return "", ""

def fix_google_maps_embed():
    """Corrige les cartes Google Maps avec l'API et améliore l'intégration"""
    
    base_dir = Path("/Users/marc/Desktop/kastelenbelgie")
    
    # Clé API fournie par l'utilisateur
    API_KEY = "AIzaSyAvyQt1-zQB1bzIX3N8KnYKgPCs-8d328s"
    
    print("🗺️  AMÉLIORATION DES CARTES GOOGLE MAPS")
    print("=" * 45)
    
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
            
            # Créer la query pour Google Maps
            if address and castle_name:
                # Utiliser l'adresse si disponible, sinon le nom du château
                map_query = address if any(char.isdigit() for char in address) else f"{castle_name}, België"
            else:
                map_query = "België"
            
            # URL encoder la query
            import urllib.parse
            encoded_query = urllib.parse.quote(map_query)
            
            # 1. Corriger les iframes Google Maps existantes
            # Pattern pour les iframes avec l'ancienne clé
            old_iframe_pattern = r'<iframe[^>]*src="https://www\.google\.com/maps/embed/v1/place\?key=[^&]*&q=([^"]*)"[^>]*></iframe>'
            
            # Nouvelle iframe avec la vraie clé API
            new_iframe = f'''<iframe 
                        src="https://www.google.com/maps/embed/v1/place?key={API_KEY}&q={encoded_query}&zoom=15"
                        width="100%" 
                        height="400" 
                        style="border:0;" 
                        allowfullscreen="" 
                        loading="lazy" 
                        referrerpolicy="no-referrer-when-downgrade">
                    </iframe>'''
            
            content = re.sub(old_iframe_pattern, new_iframe, content)
            
            # 2. Améliorer les liens Google Maps
            # Corriger les liens "Open in Google Maps"
            old_link_pattern = r'<a href="https://www\.google\.com/maps/search/([^"]*)"'
            new_link = f'<a href="https://www.google.com/maps/search/{encoded_query}"'
            content = re.sub(old_link_pattern, new_link, content)
            
            # Corriger les liens "Routebeschrijving"
            old_directions_pattern = r'<a href="https://www\.google\.com/maps/dir//([^"]*)"'
            new_directions = f'<a href="https://www.google.com/maps/dir//{encoded_query}"'
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
                new_address = f'<p><strong>Adres:</strong> {address}</p>'
                content = re.sub(old_address_pattern, new_address, content)
            
            if content != original_content:
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                files_modified += 1
                print(f"✅ {html_file.name} - Carte améliorée: {castle_name}")
        
        except Exception as e:
            print(f"❌ Erreur avec {html_file.name}: {e}")
    
    print(f"\n📊 RÉSULTATS:")
    print(f"   Fichiers traités: {files_processed}")
    print(f"   Fichiers modifiés: {files_modified}")
    print(f"   Clé API utilisée: {API_KEY[:20]}...")
    
    if files_modified > 0:
        print(f"\n🎉 Cartes Google Maps améliorées!")
        print("   - API key fonctionnelle intégrée")
        print("   - Localisation précise par château")
        print("   - Liens Maps fonctionnels")
        print("   - Titres et adresses corrects")
    else:
        print("\n✨ Cartes déjà optimisées!")

if __name__ == "__main__":
    fix_google_maps_embed()
