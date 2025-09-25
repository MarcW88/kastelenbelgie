#!/usr/bin/env python3
"""
Script pour corriger les cartes Google Maps en utilisant correctement l'API key
avec l'API Maps Embed (différente de l'API Geocoding)
"""

import os
import re
from pathlib import Path
from bs4 import BeautifulSoup
import urllib.parse

def extract_castle_info(html_file):
    """Extrait le nom du château et l'adresse"""
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
            # Chercher une adresse (avec des chiffres et pas "België")
            if any(char.isdigit() for char in text) and len(text) > 5 and 'België' not in text:
                address = text
                break
        
        return castle_name, address
    
    except Exception as e:
        return "", ""

def fix_maps_with_working_api():
    """Corrige les cartes en utilisant l'API key correctement"""
    
    base_dir = Path("/Users/marc/Desktop/kastelenbelgie")
    
    # Votre clé API
    API_KEY = "AIzaSyAvyQt1-zQB1bzIX3N8KnYKgPCs-8d328s"
    
    print("🗺️  CORRECTION DES CARTES AVEC API KEY FONCTIONNELLE")
    print("=" * 55)
    
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
            castle_name, address = extract_castle_info(html_file)
            
            # Créer la query pour la carte
            if address:
                map_query = f"{address}, België"
            else:
                map_query = f"{castle_name}, België"
            
            # URL encoder la query
            encoded_query = urllib.parse.quote(map_query)
            
            # OPTION 1: Utiliser l'API Maps Embed (nécessite que l'API soit activée)
            embed_url = f"https://www.google.com/maps/embed/v1/place?key={API_KEY}&q={encoded_query}&zoom=15"
            
            # OPTION 2: Si l'API Embed ne fonctionne pas, utiliser l'iframe standard
            standard_url = f"https://maps.google.com/maps?q={encoded_query}&t=&z=15&ie=UTF8&iwloc=&output=embed"
            
            # Créer l'iframe avec l'API key d'abord, puis fallback
            new_iframe = f'''<iframe 
                        src="{embed_url}"
                        width="100%" 
                        height="400" 
                        style="border:0;" 
                        allowfullscreen="" 
                        loading="lazy" 
                        referrerpolicy="no-referrer-when-downgrade"
                        onerror="this.src='{standard_url}'">
                    </iframe>'''
            
            # Remplacer toutes les iframes Google Maps
            iframe_patterns = [
                r'<iframe[^>]*src="https://www\.google\.com/maps/embed[^"]*"[^>]*></iframe>',
                r'<iframe[^>]*src="https://maps\.google\.com/maps[^"]*"[^>]*></iframe>',
                r'<iframe[^>]*google\.com/maps[^>]*></iframe>'
            ]
            
            for pattern in iframe_patterns:
                content = re.sub(pattern, new_iframe, content, flags=re.DOTALL)
            
            # Corriger les liens Maps
            content = re.sub(
                r'<a href="https://www\.google\.com/maps/search/[^"]*"',
                f'<a href="https://www.google.com/maps/search/{encoded_query}"',
                content
            )
            
            content = re.sub(
                r'<a href="https://www\.google\.com/maps/dir//[^"]*"',
                f'<a href="https://www.google.com/maps/dir//{encoded_query}"',
                content
            )
            
            # Mettre à jour le titre et l'adresse
            if castle_name:
                content = re.sub(
                    r'<h3>📍 Locatie van [^<]*</h3>',
                    f'<h3>📍 Locatie van {castle_name}</h3>',
                    content
                )
            
            if address:
                content = re.sub(
                    r'<p><strong>Adres:</strong> [^<]*</p>',
                    f'<p><strong>Adres:</strong> {address}</p>',
                    content
                )
            
            if content != original_content:
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                files_modified += 1
                print(f"✅ {html_file.name} - Carte mise à jour: {castle_name}")
        
        except Exception as e:
            print(f"❌ Erreur avec {html_file.name}: {e}")
    
    print(f"\n📊 RÉSULTATS:")
    print(f"   Fichiers traités: {files_processed}")
    print(f"   Fichiers modifiés: {files_modified}")
    print(f"   Clé API utilisée: {API_KEY[:20]}...")
    
    if files_modified > 0:
        print(f"\n🎉 Cartes mises à jour avec votre clé API!")
        print("   - API Maps Embed utilisée en priorité")
        print("   - Fallback vers iframe standard si nécessaire")
        print("   - Localisation précise par château")
        print("\n⚠️  Si vous voyez encore des erreurs:")
        print("   1. Activez l'API 'Maps Embed' dans Google Cloud Console")
        print("   2. Ajoutez votre domaine aux restrictions")
        print("   3. Vérifiez que la facturation est activée")
    else:
        print("\n✨ Toutes les cartes sont déjà à jour!")

if __name__ == "__main__":
    fix_maps_with_working_api()
