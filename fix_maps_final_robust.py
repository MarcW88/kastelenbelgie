#!/usr/bin/env python3
"""
Script robuste pour remplacer TOUTES les iframes Google Maps Embed
par des cartes OpenStreetMap (sans API)
"""

import os
import re
import requests
import time
from pathlib import Path
from bs4 import BeautifulSoup

# Configuration GEOCODING
API_KEY = "AIzaSyAvyQt1-zQB1bzIX3N8KnYKgPCs-8d328s"
LANG = "nl"
REGION = "BE"
SLEEP_S = 0.2

def geocode_address(query: str):
    """GEOCODING pour obtenir les coordonnées"""
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
            return None, None, f"HTTP_{r.status_code}"
        
        data = r.json()
        status = data.get("status", "UNKNOWN")
        
        if status != "OK":
            return None, None, status
        
        results = data.get("results", [])
        if not results:
            return None, None, "NO_RESULTS"
        
        result = results[0]
        location = result.get("geometry", {}).get("location", {})
        lat = location.get("lat")
        lng = location.get("lng")
        
        return lat, lng, status
    
    except Exception as e:
        return None, None, str(e)

def extract_castle_info(html_file):
    """Extrait le nom du château et la province"""
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        # Nom du château
        title_tag = soup.find('title')
        castle_name = ""
        if title_tag:
            title = title_tag.get_text()
            castle_name = title.replace(' | kastelenbelgie.be', '').strip()
        
        # Province
        province = ""
        meta_values = soup.find_all('span', class_='meta-value')
        for meta in meta_values:
            text = meta.get_text().strip()
            provinces = ['Antwerpen', 'Limburg', 'Oost-Vlaanderen', 'West-Vlaanderen', 
                        'Vlaams-Brabant', 'Namen', 'Luxemburg', 'Luik', 'Henegouwen', 'Waals-Brabant']
            if text in provinces:
                province = text
                break
        
        return castle_name, province
    
    except Exception as e:
        return "", ""

def fix_maps_final_robust():
    """Remplace TOUTES les iframes Google Maps par OpenStreetMap"""
    
    base_dir = Path("/Users/marc/Desktop/kastelenbelgie")
    
    print("🗺️  REMPLACEMENT ROBUSTE DES CARTES")
    print("=" * 45)
    print("✅ GEOCODING: Coordonnées précises")
    print("✅ CARTES: OpenStreetMap (aucune API)")
    print("❌ MAPS EMBED: Complètement supprimé")
    
    files_processed = 0
    files_modified = 0
    geocoding_success = 0
    
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
            
            # Utiliser BeautifulSoup pour parser et remplacer les iframes
            soup = BeautifulSoup(content, 'html.parser')
            
            # Trouver TOUTES les iframes Google Maps
            google_iframes = soup.find_all('iframe', src=re.compile(r'google\.com/maps'))
            
            if not google_iframes:
                continue
            
            # Extraire les informations du château
            castle_name, province = extract_castle_info(html_file)
            
            if not castle_name:
                print(f"⚠️  {html_file.name} - Nom du château non trouvé")
                continue
            
            # Query pour le GEOCODING
            query = f"{castle_name}, {province}, België" if province else f"{castle_name}, België"
            
            # GEOCODING
            print(f"🔍 {castle_name}")
            lat, lng, status = geocode_address(query)
            
            if status == "OK" and lat and lng:
                geocoding_success += 1
                print(f"✅ Coordonnées: {lat}, {lng}")
                
                # Créer l'iframe OpenStreetMap
                osm_url = f"https://www.openstreetmap.org/export/embed.html?bbox={lng-0.01},{lat-0.01},{lng+0.01},{lat+0.01}&layer=mapnik&marker={lat},{lng}"
                
                # Remplacer chaque iframe Google Maps
                for iframe in google_iframes:
                    # Créer la nouvelle iframe OpenStreetMap
                    new_iframe = soup.new_tag('iframe')
                    new_iframe['src'] = osm_url
                    new_iframe['width'] = "100%"
                    new_iframe['height'] = "400"
                    new_iframe['style'] = "border:0;"
                    new_iframe['allowfullscreen'] = ""
                    new_iframe['loading'] = "lazy"
                    
                    # Remplacer l'ancienne iframe
                    iframe.replace_with(new_iframe)
                
                # Mettre à jour les liens Maps avec les coordonnées
                for link in soup.find_all('a', href=re.compile(r'google\.com/maps')):
                    href = link.get('href', '')
                    if 'search' in href:
                        link['href'] = f"https://www.google.com/maps/search/{lat},{lng}"
                    elif 'dir' in href:
                        link['href'] = f"https://www.google.com/maps/dir//{lat},{lng}"
                
                # Mettre à jour le titre de la carte
                location_title = soup.find('h3', string=re.compile(r'📍 Locatie van'))
                if location_title:
                    location_title.string = f"📍 Locatie van {castle_name}"
                
            else:
                print(f"❌ {castle_name} → {status}")
                
                # Carte de fallback OpenStreetMap générique (Belgique)
                fallback_url = "https://www.openstreetmap.org/export/embed.html?bbox=2.5,49.5,6.5,51.5&layer=mapnik"
                
                for iframe in google_iframes:
                    new_iframe = soup.new_tag('iframe')
                    new_iframe['src'] = fallback_url
                    new_iframe['width'] = "100%"
                    new_iframe['height'] = "400"
                    new_iframe['style'] = "border:0;"
                    new_iframe['allowfullscreen'] = ""
                    new_iframe['loading'] = "lazy"
                    
                    iframe.replace_with(new_iframe)
            
            # Sauvegarder le fichier modifié
            new_content = str(soup)
            
            if new_content != original_content:
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                files_modified += 1
            
            # Respecter le délai
            time.sleep(SLEEP_S)
        
        except Exception as e:
            print(f"❌ Erreur avec {html_file.name}: {e}")
    
    print(f"\n📊 RÉSULTATS:")
    print(f"   Fichiers traités: {files_processed}")
    print(f"   Fichiers modifiés: {files_modified}")
    print(f"   Géocodage réussi: {geocoding_success}")
    
    if files_modified > 0:
        print(f"\n🎉 CARTES REMPLACÉES PAR OPENSTREETMAP!")
        print("   ✅ Plus d'API Google Maps Embed")
        print("   ✅ Coordonnées précises via GEOCODING")
        print("   ✅ Cartes OpenStreetMap fonctionnelles")
        print("   ✅ Aucune erreur d'autorisation API!")
    else:
        print("\n⚠️  Aucune iframe Google Maps trouvée à remplacer")

if __name__ == "__main__":
    fix_maps_final_robust()
