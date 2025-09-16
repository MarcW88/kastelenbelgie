#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script pour utiliser les images déjà présentes dans assets/img
et les assigner aux pages correspondantes
"""

import os
import re
import glob

def update_html_with_image(file_path, image_filename, castle_name):
    """Mettre à jour le fichier HTML avec l'image existante"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        img_tag = f'<img src="assets/img/{image_filename}" alt="{castle_name}" loading="lazy" class="castle-main-image">'
        
        # Chercher le placeholder d'image
        image_placeholder = '<!-- Image placeholder: will be replaced with actual castle image -->'
        
        if image_placeholder in content:
            content = content.replace(image_placeholder, img_tag)
            content = content.replace('class="detail-media detail-media-hidden"', 'class="detail-media"')
        else:
            # Chercher la section detail-media et ajouter l'image
            detail_media_pattern = r'<div class="detail-media[^"]*"[^>]*>'
            match = re.search(detail_media_pattern, content)
            
            if match:
                content = re.sub(r'class="detail-media detail-media-hidden"', 'class="detail-media"', content)
                insert_pos = match.end()
                content = content[:insert_pos] + '\n        ' + img_tag + content[insert_pos:]
            else:
                return False
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
        
    except Exception as e:
        print(f"  ✗ Erreur mise à jour HTML: {e}")
        return False

def extract_castle_name(filename):
    """Extraire le nom du château depuis le nom de fichier"""
    name = filename.replace('.html', '').replace('-', ' ')
    return ' '.join(word.capitalize() for word in name.split())

def main():
    """Fonction principale"""
    print("=== UTILISATION DES IMAGES EXISTANTES ===")
    
    # Répertoire des images
    img_dir = "/Users/marc/Desktop/kastelenbelgie/assets/img"
    
    # Lister toutes les images disponibles
    available_images = []
    for img_file in os.listdir(img_dir):
        if img_file.endswith('.jpg'):
            available_images.append(img_file)
    
    print(f"Images disponibles: {len(available_images)}")
    
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
    
    castle_files = sorted(list(set(castle_files)))
    
    print(f"Pages de châteaux trouvées: {len(castle_files)}")
    
    success_count = 0
    
    for file_path in castle_files:
        filename = os.path.basename(file_path)
        castle_name = extract_castle_name(filename)
        
        # Chercher l'image correspondante
        expected_image = filename.replace('.html', '.jpg')
        
        if expected_image in available_images:
            print(f"Traitement: {filename}")
            print(f"  Image trouvée: {expected_image}")
            
            # Mettre à jour le HTML
            if update_html_with_image(file_path, expected_image, castle_name):
                print(f"  ✓ Succès: {filename}")
                success_count += 1
            else:
                print(f"  ✗ Échec mise à jour HTML: {filename}")
        else:
            print(f"○ Pas d'image pour: {filename}")
    
    print(f"\n=== RÉSUMÉ ===")
    print(f"Pages traitées: {len(castle_files)}")
    print(f"Images ajoutées avec succès: {success_count}")
    print(f"Taux de succès: {success_count/len(castle_files)*100:.1f}%")

if __name__ == "__main__":
    main()
