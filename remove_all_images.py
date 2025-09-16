#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script pour supprimer toutes les images des pages de châteaux
et restaurer le placeholder d'image à gauche avec les heures d'ouverture à droite
"""

import os
import re
import glob

def remove_images_and_restore_placeholder(file_path):
    """Supprimer les images et restaurer le placeholder"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Supprimer toutes les balises img dans la section detail-media
        content = re.sub(r'<img src="assets/img/[^"]+\.jpg"[^>]*>', '', content)
        
        # Restaurer la classe detail-media-hidden si elle n'est pas présente
        content = re.sub(r'class="detail-media"', 'class="detail-media detail-media-hidden"', content)
        
        # Ajouter le placeholder d'image s'il n'est pas présent
        placeholder_comment = '<!-- Image placeholder: will be replaced with actual castle image -->'
        
        # Chercher la section detail-media et s'assurer qu'elle contient le placeholder
        detail_media_pattern = r'(<div class="detail-media detail-media-hidden"[^>]*>)(.*?)(</div>)'
        
        def replace_detail_media(match):
            opening_tag = match.group(1)
            content_inside = match.group(2).strip()
            closing_tag = match.group(3)
            
            # Si le placeholder n'est pas déjà présent, l'ajouter
            if placeholder_comment not in content_inside:
                return f'{opening_tag}\n        {placeholder_comment}\n      {closing_tag}'
            else:
                return f'{opening_tag}\n        {placeholder_comment}\n      {closing_tag}'
        
        content = re.sub(detail_media_pattern, replace_detail_media, content, flags=re.DOTALL)
        
        # Écrire le fichier modifié
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
        
    except Exception as e:
        print(f"  ✗ Erreur: {e}")
        return False

def main():
    """Fonction principale"""
    print("=== SUPPRESSION DE TOUTES LES IMAGES ===")
    
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
        
        if remove_images_and_restore_placeholder(file_path):
            print(f"✓ Images supprimées: {filename}")
            success_count += 1
        else:
            print(f"✗ Échec: {filename}")
    
    print(f"\n=== RÉSUMÉ ===")
    print(f"Pages traitées: {len(castle_files)}")
    print(f"Pages nettoyées: {success_count}")
    
    # Supprimer aussi toutes les images du répertoire assets/img
    img_dir = "/Users/marc/Desktop/kastelenbelgie/assets/img"
    if os.path.exists(img_dir):
        print(f"\nSuppression des images dans {img_dir}...")
        for img_file in os.listdir(img_dir):
            if img_file.endswith('.jpg'):
                img_path = os.path.join(img_dir, img_file)
                try:
                    os.remove(img_path)
                    print(f"✓ Supprimé: {img_file}")
                except Exception as e:
                    print(f"✗ Erreur suppression {img_file}: {e}")

if __name__ == "__main__":
    main()
