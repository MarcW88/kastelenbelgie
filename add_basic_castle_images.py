#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script simple pour ajouter des images de châteaux:
- Utilise 3 images génériques de châteaux téléchargées localement
- Ajoute les images même si pas de placeholder
"""

import os
import re
import glob
import urllib.request
from urllib.error import URLError, HTTPError

# Images génériques de châteaux (URLs qui fonctionnent)
CASTLE_IMAGES = [
    'https://cdn.pixabay.com/photo/2017/09/12/13/56/castle-2742618_960_720.jpg',
    'https://cdn.pixabay.com/photo/2016/11/29/05/45/architecture-1867187_960_720.jpg',
    'https://cdn.pixabay.com/photo/2017/05/01/11/04/castle-2272559_960_720.jpg'
]

def create_assets_directory():
    """Créer le répertoire assets/img s'il n'existe pas"""
    assets_dir = "/Users/marc/Desktop/kastelenbelgie/assets"
    img_dir = os.path.join(assets_dir, "img")
    os.makedirs(img_dir, exist_ok=True)
    return img_dir

def download_generic_images(img_dir):
    """Télécharger les 3 images génériques"""
    print("Téléchargement des images génériques...")
    
    for i, url in enumerate(CASTLE_IMAGES):
        filename = f"castle-generic-{i+1}.jpg"
        filepath = os.path.join(img_dir, filename)
        
        if os.path.exists(filepath):
            print(f"✓ Image déjà présente: {filename}")
            continue
            
        try:
            urllib.request.urlretrieve(url, filepath)
            print(f"✓ Téléchargé: {filename}")
        except Exception as e:
            print(f"✗ Erreur téléchargement {filename}: {e}")
            return False
    
    return True

def extract_castle_name(filename):
    """Extraire le nom du château depuis le nom de fichier"""
    name = filename.replace('.html', '').replace('-', ' ')
    return ' '.join(word.capitalize() for word in name.split())

def update_html_with_image(file_path, image_filename, castle_name):
    """Mettre à jour le fichier HTML avec l'image"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Chercher le placeholder ou la section detail-media
        image_placeholder = '<!-- Image placeholder: will be replaced with actual castle image -->'
        img_tag = f'<img src="assets/img/{image_filename}" alt="{castle_name}" loading="lazy" class="castle-main-image">'
        
        if image_placeholder in content:
            # Remplacer le placeholder
            content = content.replace(image_placeholder, img_tag)
            # Enlever la classe qui cache la section
            content = content.replace('class="detail-media detail-media-hidden"', 'class="detail-media"')
        else:
            # Chercher la section detail-media et ajouter l'image
            detail_media_pattern = r'<div class="detail-media[^"]*"[^>]*>'
            match = re.search(detail_media_pattern, content)
            
            if match:
                # Remplacer la classe hidden si présente
                content = re.sub(r'class="detail-media detail-media-hidden"', 'class="detail-media"', content)
                
                # Ajouter l'image après l'ouverture de la div detail-media
                insert_pos = match.end()
                content = content[:insert_pos] + '\n        ' + img_tag + content[insert_pos:]
            else:
                print(f"○ Pas de section detail-media trouvée dans {os.path.basename(file_path)}")
                return False
        
        # Écrire le fichier modifié
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
        
    except Exception as e:
        print(f"✗ Erreur mise à jour HTML {os.path.basename(file_path)}: {e}")
        return False

def main():
    """Fonction principale"""
    print("=== AJOUT D'IMAGES DE CHÂTEAUX (APPROCHE BASIQUE) ===")
    
    # Créer le répertoire d'images
    img_dir = create_assets_directory()
    
    # Télécharger les images génériques
    if not download_generic_images(img_dir):
        print("✗ Échec téléchargement des images génériques")
        return
    
    # Trouver tous les fichiers HTML de châteaux
    castle_files = []
    patterns = [
        "kasteel-*.html", "chateau-*.html", "citadel-*.html", "burcht-*.html",
        "hof-*.html", "de-*.html", "het-*.html", "sint-*.html", "koninklijk-*.html",
        "waterslot-*.html", "vrieselhof-*.html", "rentmeesterij-*.html",
        "commanderij-*.html", "domein-*.html", "oud-*.html", "bisschoppenhof-*.html",
        "braemkasteel-*.html", "burchtruine-*.html", "gaverkasteel-*.html"
    ]
    
    for pattern in patterns:
        castle_files.extend(glob.glob(f"/Users/marc/Desktop/kastelenbelgie/{pattern}"))
    
    # Enlever les doublons et trier
    castle_files = sorted(list(set(castle_files)))
    
    print(f"Nombre de pages de châteaux trouvées: {len(castle_files)}")
    
    success_count = 0
    
    for i, file_path in enumerate(castle_files):
        filename = os.path.basename(file_path)
        castle_name = extract_castle_name(filename)
        
        # Utiliser une des 3 images génériques en rotation
        image_filename = f"castle-generic-{(i % 3) + 1}.jpg"
        
        print(f"Traitement: {filename}")
        
        # Mettre à jour le HTML
        if update_html_with_image(file_path, image_filename, castle_name):
            print(f"✓ Image ajoutée: {filename}")
            success_count += 1
        else:
            print(f"✗ Échec: {filename}")
    
    print("\n=== RÉSUMÉ ===")
    print(f"Pages traitées: {len(castle_files)}")
    print(f"Images ajoutées avec succès: {success_count}")
    print(f"Taux de succès: {success_count/len(castle_files)*100:.1f}%")

if __name__ == "__main__":
    main()
