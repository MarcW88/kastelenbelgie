#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script pour ajouter un placeholder d'image visible à gauche
au lieu du placeholder caché
"""

import os
import re
import glob

def add_visible_placeholder(file_path):
    """Ajouter un placeholder d'image visible"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remplacer la classe detail-media-hidden par detail-media normale
        content = re.sub(r'class="detail-media detail-media-hidden"', 'class="detail-media"', content)
        
        # Remplacer le commentaire par un div placeholder visible
        placeholder_comment = '<!-- Image placeholder: will be replaced with actual castle image -->'
        visible_placeholder = '<div class="image-placeholder">Afbeelding volgt</div>'
        
        content = content.replace(placeholder_comment, visible_placeholder)
        
        # Écrire le fichier modifié
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
        
    except Exception as e:
        print(f"  ✗ Erreur: {e}")
        return False

def main():
    """Fonction principale"""
    print("=== AJOUT DE PLACEHOLDERS VISIBLES ===")
    
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
        
        if add_visible_placeholder(file_path):
            print(f"✓ Placeholder ajouté: {filename}")
            success_count += 1
        else:
            print(f"✗ Échec: {filename}")
    
    print(f"\n=== RÉSUMÉ ===")
    print(f"Pages traitées: {len(castle_files)}")
    print(f"Placeholders ajoutés: {success_count}")

if __name__ == "__main__":
    main()
