#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script pour remplacer les placeholders d'images par les vraies images de châteaux
depuis le dossier chateaux_images
"""

import os
import re
import glob
from pathlib import Path

def normalize_name(name):
    """Normalise un nom pour la comparaison"""
    # Enlève les extensions, tirets, underscores, espaces
    name = name.lower()
    name = re.sub(r'\.(jpg|jpeg|png|gif)$', '', name)
    name = re.sub(r'[_\-\s]+', '', name)
    return name

def find_matching_image(castle_filename, images_dir):
    """Trouve l'image correspondante pour un château"""
    # Normalise le nom du fichier château
    castle_base = os.path.splitext(castle_filename)[0]
    castle_normalized = normalize_name(castle_base)
    
    # Liste toutes les images disponibles
    image_files = []
    for ext in ['*.jpg', '*.jpeg', '*.png', '*.gif']:
        image_files.extend(glob.glob(os.path.join(images_dir, ext)))
    
    # Essaie de trouver une correspondance exacte ou partielle
    best_match = None
    best_score = 0
    
    for image_path in image_files:
        image_name = os.path.basename(image_path)
        image_normalized = normalize_name(image_name)
        
        # Correspondance exacte
        if castle_normalized == image_normalized:
            return image_name
        
        # Correspondance partielle - compte les mots communs
        castle_words = set(re.split(r'[_\-\s]+', castle_base.lower()))
        image_words = set(re.split(r'[_\-\s]+', os.path.splitext(image_name)[0].lower()))
        
        # Enlève les mots très communs
        common_words = {'kasteel', 'chateau', 'van', 'de', 'het', 'le', 'la', 'du', 'des', 'te', 'in', 'op', 'aan'}
        castle_words -= common_words
        image_words -= common_words
        
        if castle_words and image_words:
            intersection = castle_words & image_words
            union = castle_words | image_words
            score = len(intersection) / len(union) if union else 0
            
            if score > best_score and score > 0.3:  # Seuil minimum
                best_score = score
                best_match = image_name
    
    return best_match

def update_castle_page_image(file_path, images_dir):
    """Met à jour une page de château avec son image"""
    try:
        filename = os.path.basename(file_path)
        
        # Trouve l'image correspondante
        matching_image = find_matching_image(filename, images_dir)
        
        if not matching_image:
            return False, "Aucune image correspondante trouvée"
        
        # Lit le contenu du fichier
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Cherche le placeholder d'image actuel
        placeholder_pattern = r'<div class="detail-media"[^>]*>\s*<div class="image-placeholder"[^>]*>.*?</div>\s*</div>'
        
        if not re.search(placeholder_pattern, content, re.DOTALL):
            return False, "Placeholder d'image non trouvé"
        
        # Crée le nouveau HTML avec l'image
        image_html = f'''<div class="detail-media">
            <img src="./chateaux_images/{matching_image}" alt="{filename.replace('.html', '').replace('-', ' ').title()}" class="castle-image">
          </div>'''
        
        # Remplace le placeholder
        new_content = re.sub(placeholder_pattern, image_html, content, flags=re.DOTALL)
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True, f"Image intégrée: {matching_image}"
        
        return False, "Aucun changement nécessaire"
        
    except Exception as e:
        return False, f"Erreur: {e}"

def add_image_css():
    """Ajoute le CSS pour les images de châteaux"""
    css_code = '''
/* Castle Images */
.castle-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 12px;
}

.detail-media {
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}'''
    
    css_file = '/Users/marc/Desktop/kastelenbelgie/css/style.css'
    
    try:
        with open(css_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if '/* Castle Images */' not in content:
            with open(css_file, 'a', encoding='utf-8') as f:
                f.write(css_code)
            return True
        
        return False
        
    except Exception as e:
        print(f"Erreur CSS: {e}")
        return False

def main():
    """Fonction principale"""
    print("=== INTÉGRATION IMAGES CHÂTEAUX ===")
    
    images_dir = '/Users/marc/Desktop/kastelenbelgie/chateaux_images'
    
    # Vérifie que le dossier d'images existe
    if not os.path.exists(images_dir):
        print(f"❌ Dossier d'images non trouvé: {images_dir}")
        return
    
    # Ajoute le CSS
    print("Ajout du CSS pour les images...")
    if add_image_css():
        print("  ✓ CSS ajouté")
    else:
        print("  ○ CSS déjà présent")
    
    # Trouve tous les fichiers de châteaux
    print("\nRecherche des pages de châteaux...")
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
    print(f"Trouvé {len(castle_files)} pages de châteaux")
    
    # Test avec quelques fichiers d'abord
    test_files = castle_files[:5]
    print(f"\nTest avec {len(test_files)} fichiers...")
    
    success_count = 0
    
    for file_path in test_files:
        filename = os.path.basename(file_path)
        success, message = update_castle_page_image(file_path, images_dir)
        
        if success:
            print(f"  ✓ {filename}: {message}")
            success_count += 1
        else:
            print(f"  ○ {filename}: {message}")
    
    print(f"\n=== RÉSULTAT TEST ===")
    print(f"Fichiers testés: {len(test_files)}")
    print(f"Images intégrées: {success_count}")
    
    if success_count > 0:
        print(f"\nContinuation avec tous les {len(castle_files)} fichiers...")
        
        for file_path in castle_files:
            if file_path in test_files:
                continue
                
            filename = os.path.basename(file_path)
            success, message = update_castle_page_image(file_path, images_dir)
            
            if success:
                success_count += 1
                if success_count % 25 == 0:
                    print(f"  Progression: {success_count} images intégrées...")
        
        print(f"\n=== RÉSULTAT FINAL ===")
        print(f"Total pages traitées: {len(castle_files)}")
        print(f"Images intégrées avec succès: {success_count}")
        print("Les images des châteaux sont maintenant visibles!")
    else:
        print("\nAucune image intégrée lors du test. Vérification nécessaire.")

if __name__ == "__main__":
    main()
