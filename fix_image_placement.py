#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script pour corriger le placement des images dans les pages de châteaux
Les images doivent être à l'intérieur de la div detail-media, pas après
"""

import os
import re
import glob

def fix_image_placement(file_path):
    """Corriger le placement de l'image dans le HTML"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern pour trouver une image mal placée après la div detail-media
        pattern = r'(<div class="detail-media"[^>]*>)\s*\n\s*(<img src="assets/img/[^"]+\.jpg"[^>]*>)'
        
        def replace_func(match):
            div_opening = match.group(1)
            img_tag = match.group(2)
            return f'{div_opening}\n        {img_tag}'
        
        # Remplacer le pattern
        new_content = re.sub(pattern, replace_func, content)
        
        # Vérifier si des changements ont été faits
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        
        return False
        
    except Exception as e:
        print(f"  ✗ Erreur: {e}")
        return False

def main():
    """Fonction principale"""
    print("=== CORRECTION DU PLACEMENT DES IMAGES ===")
    
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
    
    fixed_count = 0
    
    for file_path in castle_files:
        filename = os.path.basename(file_path)
        
        if fix_image_placement(file_path):
            print(f"✓ Corrigé: {filename}")
            fixed_count += 1
        else:
            print(f"○ Pas de correction nécessaire: {filename}")
    
    print(f"\n=== RÉSUMÉ ===")
    print(f"Pages traitées: {len(castle_files)}")
    print(f"Pages corrigées: {fixed_count}")

if __name__ == "__main__":
    main()
