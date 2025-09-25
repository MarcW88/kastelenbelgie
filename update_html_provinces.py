#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MISE À JOUR DES PROVINCES DANS LES PAGES HTML EXISTANTES
Corrige les encadrés des pages châteaux avec les bonnes provinces
"""

import os
import csv
import re
from urllib.parse import urlparse

def update_html_provinces():
    """Met à jour les provinces dans les pages HTML existantes"""
    csv_file = "/Users/marc/Desktop/kastelenbelgie/chateaux_opening_hours - chateaux_opening_hours.csv"
    html_dir = "/Users/marc/Desktop/kastelenbelgie"
    
    print("🔧 MISE À JOUR DES PROVINCES DANS LES PAGES HTML")
    print("=" * 60)
    
    # Charger les données corrigées du CSV
    castle_provinces = {}
    
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                title = row.get('Title', '')
                url = row.get('URL', '')
                province = row.get('Provincie', '')
                
                if url and province:
                    # Extraire le nom du fichier HTML depuis l'URL
                    filename = get_filename_from_url(url)
                    if filename:
                        castle_provinces[filename] = {
                            'title': title,
                            'province': province,
                            'url': url
                        }
        
        print(f"📊 {len(castle_provinces)} châteaux chargés depuis le CSV")
        
    except Exception as e:
        print(f"❌ Erreur lecture CSV: {e}")
        return
    
    # Mettre à jour les fichiers HTML
    updated_count = 0
    error_count = 0
    
    for filename, data in castle_provinces.items():
        html_file = os.path.join(html_dir, f"{filename}.html")
        
        if os.path.exists(html_file):
            try:
                # Lire le fichier HTML
                with open(html_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Chercher et remplacer la province dans l'encadré
                # Pattern: <strong>Provincie:</strong> \s*<span class="meta-value">ANCIENNE_PROVINCE</span>
                pattern = r'(<strong>Provincie:</strong>\s*<span class="meta-value">)[^<]+(</span>)'
                replacement = f'\\g<1>{data["province"]}\\g<2>'
                
                new_content = re.sub(pattern, replacement, content)
                
                # Vérifier si une modification a été faite
                if new_content != content:
                    # Sauvegarder le fichier modifié
                    with open(html_file, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    
                    updated_count += 1
                    print(f"✅ {filename}.html → {data['province']}")
                
            except Exception as e:
                print(f"❌ Erreur avec {filename}.html: {e}")
                error_count += 1
        else:
            print(f"⚠️ Fichier non trouvé: {filename}.html")
    
    print(f"\n📊 RÉSULTATS:")
    print(f"Pages mises à jour: {updated_count}")
    print(f"Erreurs: {error_count}")
    print(f"Total traité: {len(castle_provinces)}")

def get_filename_from_url(url):
    """Extrait le nom du fichier depuis l'URL"""
    if not url:
        return None
    
    try:
        parsed = urlparse(url)
        path = parsed.path.strip('/')
        
        if path:
            # Prendre la dernière partie du chemin
            filename = path.split('/')[-1]
            # Supprimer l'extension si présente
            if filename.endswith('.html'):
                filename = filename[:-5]
            return filename
    except:
        pass
    
    return None

if __name__ == "__main__":
    update_html_provinces()
