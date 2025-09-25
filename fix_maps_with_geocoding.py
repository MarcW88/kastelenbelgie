#!/usr/bin/env python3
"""
Script pour corriger les cartes Google Maps en utilisant l'API Geocoding
(comme dans votre script qui fonctionne) pour obtenir les coordonnées
puis créer des cartes fonctionnelles
"""

import os
import re
import requests
import time
from pathlib import Path
from bs4 import BeautifulSoup
import urllib.parse

# Configuration basée sur votre script qui fonctionne
API_KEY = "AIzaSyAvyQt1-zQB1bzIX3N8KnYKgPCs-8d328s"
LANG = "nl"
REGION = "BE"
SLEEP_S = 0.2

def geocode_address(query: str):
    """Fonction identique à votre script qui fonctionne"""
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "address": query,
        "key": API_KEY,
        "language": LANG,
        "region": REGION,
        "components": "country:BE"
    }
    
    try:
        r = requests.get(url, params=params, timeout=20)
        if r.status_code != 200:
            return None, None, f"HTTP_{r.status_code}", None
        
        data = r.json()
        status = data.get("status", "UNKNOWN")
        err = data.get("error_message")
        
        if status != "OK":
            return None, None, status, err
        
        results = data.get("results", [])
        if not results:
            return None, None, "NO_RESULTS", None
        
        # Prendre le premier résultat
        result = results[0]
        location = result.get("geometry", {}).get("location", {})
        lat = location.get("lat")
        lng = location.get("lng")
        formatted_address = result.get("formatted_address")
        
        return lat, lng, status, formatted_address
    
    except Exception as e:
        return None, None, "ERROR", str(e)

def extract_castle_info(html_file):
    """Extrait le nom du château et la province"""
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
        
        # Extraire la province depuis les métadonnées
        province = ""
        meta_values = soup.find_all('span', class_='meta-value')
        for meta in meta_values:
            text = meta.get_text().strip()
            # Chercher une province belge
            provinces = ['Antwerpen', 'Limburg', 'Oost-Vlaanderen', 'West-Vlaanderen', 
                        'Vlaams-Brabant', 'Namen', 'Luxemburg', 'Luik', 'Henegouwen', 'Waals-Brabant']
            if text in provinces:
                province = text
                break
        
        return castle_name, province
    
    except Exception as e:
        return "", ""

def create_functional_map_iframe(lat, lng, castle_name, address):
    """Crée une iframe de carte fonctionnelle avec les coordonnées"""
    
    # Option 1: Google Maps avec coordonnées (fonctionne sans API key)
    google_url = f"https://maps.google.com/maps?q={lat},{lng}&t=&z=15&ie=UTF8&iwloc=&output=embed"
    
    # Option 2: OpenStreetMap en fallback
    osm_url = f"https://www.openstreetmap.org/export/embed.html?bbox={lng-0.01},{lat-0.01},{lng+0.01},{lat+0.01}&layer=mapnik&marker={lat},{lng}"
    
    iframe = f'''<iframe 
                        src="{google_url}"
                        width="100%" 
                        height="400" 
                        style="border:0;" 
                        allowfullscreen="" 
                        loading="lazy"
                        onerror="this.src='{osm_url}'">
                    </iframe>'''
    
    return iframe

def fix_maps_with_geocoding():
    """Corrige les cartes en utilisant l'API Geocoding comme votre script"""
    
    base_dir = Path("/Users/marc/Desktop/kastelenbelgie")
    
    print("🗺️  CORRECTION DES CARTES AVEC API GEOCODING")
    print("=" * 50)
    print(f"Utilisation de la clé API: {API_KEY[:20]}...")
    
    files_processed = 0
    files_modified = 0
    geocoding_success = 0
    geocoding_failed = 0
    
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
            castle_name, province = extract_castle_info(html_file)
            
            if not castle_name:
                print(f"⚠️  {html_file.name} - Nom du château non trouvé")
                continue
            
            # Créer la query comme dans votre script
            query = f"{castle_name}, {province}, België" if province else f"{castle_name}, België"
            
            # Utiliser l'API Geocoding (comme votre script)
            print(f"🔍 Géocodage: {query}")
            lat, lng, status, address = geocode_address(query)
            
            if status == "OK" and lat and lng:
                geocoding_success += 1
                print(f"✅ {castle_name} → {lat}, {lng}")
                
                # Créer l'iframe fonctionnelle avec les coordonnées
                new_iframe = create_functional_map_iframe(lat, lng, castle_name, address)
                
                # Remplacer toutes les iframes Google Maps
                iframe_patterns = [
                    r'<iframe[^>]*src="https://www\.google\.com/maps/embed[^"]*"[^>]*></iframe>',
                    r'<iframe[^>]*src="https://maps\.google\.com/maps[^"]*"[^>]*></iframe>',
                    r'<iframe[^>]*google\.com/maps[^>]*></iframe>'
                ]
                
                for pattern in iframe_patterns:
                    content = re.sub(pattern, new_iframe, content, flags=re.DOTALL)
                
                # Mettre à jour les liens Maps avec les coordonnées
                maps_link = f"https://www.google.com/maps/search/{lat},{lng}"
                directions_link = f"https://www.google.com/maps/dir//{lat},{lng}"
                
                content = re.sub(
                    r'<a href="https://www\.google\.com/maps/search/[^"]*"',
                    f'<a href="{maps_link}"',
                    content
                )
                
                content = re.sub(
                    r'<a href="https://www\.google\.com/maps/dir//[^"]*"',
                    f'<a href="{directions_link}"',
                    content
                )
                
                # Mettre à jour le titre et l'adresse
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
                
            else:
                geocoding_failed += 1
                print(f"❌ {castle_name} → {status}")
                # Garder l'iframe existante ou créer une iframe basique
                encoded_query = urllib.parse.quote(query)
                fallback_iframe = f'''<iframe 
                        src="https://maps.google.com/maps?q={encoded_query}&t=&z=15&ie=UTF8&iwloc=&output=embed"
                        width="100%" 
                        height="400" 
                        style="border:0;" 
                        allowfullscreen="" 
                        loading="lazy">
                    </iframe>'''
                
                iframe_patterns = [
                    r'<iframe[^>]*src="https://www\.google\.com/maps/embed[^"]*"[^>]*></iframe>',
                    r'<iframe[^>]*src="https://maps\.google\.com/maps[^"]*"[^>]*></iframe>'
                ]
                
                for pattern in iframe_patterns:
                    content = re.sub(pattern, fallback_iframe, content, flags=re.DOTALL)
            
            if content != original_content:
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                files_modified += 1
            
            # Respecter le délai comme dans votre script
            time.sleep(SLEEP_S)
        
        except Exception as e:
            print(f"❌ Erreur avec {html_file.name}: {e}")
    
    print(f"\n📊 RÉSULTATS:")
    print(f"   Fichiers traités: {files_processed}")
    print(f"   Fichiers modifiés: {files_modified}")
    print(f"   Géocodage réussi: {geocoding_success}")
    print(f"   Géocodage échoué: {geocoding_failed}")
    print(f"   Clé API utilisée: {API_KEY[:20]}...")
    
    if files_modified > 0:
        print(f"\n🎉 Cartes mises à jour avec l'API Geocoding!")
        print("   - Coordonnées précises obtenues via API")
        print("   - Cartes fonctionnelles avec coordonnées")
        print("   - Même méthode que votre script qui fonctionne")
    else:
        print("\n✨ Toutes les cartes sont déjà à jour!")

if __name__ == "__main__":
    fix_maps_with_geocoding()
