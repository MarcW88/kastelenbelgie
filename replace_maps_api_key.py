#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
REMPLACEMENT DE LA CLÉ API GOOGLE MAPS
Remplace YOUR_API_KEY par votre vraie clé API
"""

import os
import glob

def replace_api_key(api_key):
    """Remplace la clé API dans tous les fichiers"""
    if not api_key or api_key == "YOUR_API_KEY":
        print("❌ Veuillez fournir une vraie clé API")
        return
    
    castle_files = []
    patterns = ['kasteel-*.html', 'chateau-*.html', 'citadel-*.html', 'burcht-*.html']
    for pattern in patterns:
        castle_files.extend(glob.glob(f"/Users/marc/Desktop/kastelenbelgie/{pattern}"))
    
    updated_count = 0
    
    for filepath in castle_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if 'YOUR_API_KEY' in content:
                new_content = content.replace('YOUR_API_KEY', api_key)
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                updated_count += 1
        except Exception as e:
            print(f"Erreur avec {filepath}: {e}")
    
    print(f"✅ {updated_count} fichiers mis à jour avec la clé API")

if __name__ == "__main__":
    # Remplacez par votre vraie clé API Google Maps
    API_KEY = "YOUR_GOOGLE_MAPS_API_KEY_HERE"
    replace_api_key(API_KEY)
