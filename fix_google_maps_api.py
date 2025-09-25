#!/usr/bin/env python3
"""
Script pour remplacer YOUR_API_KEY par la vraie clé API Google Maps
sur toutes les pages de châteaux
"""

import os
import re
from pathlib import Path

def fix_google_maps_api():
    """Remplace YOUR_API_KEY par la vraie clé API Google Maps"""
    
    # Clé API fournie par l'utilisateur
    API_KEY = "AIzaSyAvyQt1-zQB1bzIX3N8KnYKgPCs-8d328s"
    
    # Répertoire de travail
    base_dir = Path("/Users/marc/Desktop/kastelenbelgie")
    
    # Compteurs
    files_processed = 0
    files_modified = 0
    
    print("🗺️  CORRECTION DES GOOGLE MAPS API")
    print("=" * 50)
    
    # Parcourir tous les fichiers HTML
    for html_file in base_dir.glob("*.html"):
        # Ignorer les pages non-châteaux
        if html_file.name in ['index.html', 'contact.html', 'blog.html', 'provinces.html', 
                             'antwerpen.html', 'limburg.html', 'oost-vlaanderen.html', 
                             'west-vlaanderen.html', 'vlaams-brabant.html', 'namen.html',
                             'luxemburg.html', 'luik.html', 'henegouwen.html', 'waals-brabant.html']:
            continue
            
        files_processed += 1
        
        try:
            # Lire le contenu du fichier
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Chercher et remplacer YOUR_API_KEY
            original_content = content
            
            # Pattern pour Google Maps embed avec YOUR_API_KEY
            pattern = r'https://www\.google\.com/maps/embed/v1/place\?key=YOUR_API_KEY'
            replacement = f'https://www.google.com/maps/embed/v1/place?key={API_KEY}'
            
            content = re.sub(pattern, replacement, content)
            
            # Vérifier si des modifications ont été faites
            if content != original_content:
                # Sauvegarder le fichier modifié
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                files_modified += 1
                print(f"✅ {html_file.name} - API key mise à jour")
            
        except Exception as e:
            print(f"❌ Erreur avec {html_file.name}: {e}")
    
    print("\n📊 RÉSULTATS:")
    print(f"   Fichiers traités: {files_processed}")
    print(f"   Fichiers modifiés: {files_modified}")
    print(f"   Clé API utilisée: {API_KEY[:20]}...")
    
    if files_modified > 0:
        print(f"\n🎉 Google Maps maintenant fonctionnelles sur {files_modified} pages!")
    else:
        print("\n⚠️  Aucune page avec YOUR_API_KEY trouvée")

if __name__ == "__main__":
    fix_google_maps_api()
