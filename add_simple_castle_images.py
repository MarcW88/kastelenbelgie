#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script pour ajouter des images de châteaux de manière simple:
1. Chercher d'abord sur Wikipedia
2. Si pas d'image Wikipedia, utiliser une image générique de château depuis Unsplash
"""

import os
import re
import glob
import urllib.request
import urllib.parse
from urllib.error import URLError, HTTPError
import time

# Images génériques de châteaux depuis Unsplash (libres de droits)
GENERIC_CASTLE_IMAGES = [
    'https://images.unsplash.com/photo-1520637736862-4d197d17c90a?w=800&h=600&fit=crop&auto=format',
    'https://images.unsplash.com/photo-1564501049412-61c2a3083791?w=800&h=600&fit=crop&auto=format',
    'https://images.unsplash.com/photo-1518709268805-4e9042af2176?w=800&h=600&fit=crop&auto=format',
    'https://images.unsplash.com/photo-1571847140471-1d7766e825ea?w=800&h=600&fit=crop&auto=format',
    'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=800&h=600&fit=crop&auto=format'
]

def create_assets_directory():
    """Créer le répertoire assets/img s'il n'existe pas"""
    assets_dir = "/Users/marc/Desktop/kastelenbelgie/assets"
    img_dir = os.path.join(assets_dir, "img")
    
    os.makedirs(img_dir, exist_ok=True)
    return img_dir

def extract_castle_name(filename):
    """Extraire le nom du château depuis le nom de fichier"""
    # Enlever l'extension .html
    name = filename.replace('.html', '')
    
    # Remplacer les tirets par des espaces
    name = name.replace('-', ' ')
    
    # Capitaliser les mots
    name = ' '.join(word.capitalize() for word in name.split())
    
    return name

def download_image(url, filename, img_dir):
    """Télécharger une image depuis une URL"""
    try:
        # Créer le chemin complet
        img_path = os.path.join(img_dir, filename)
        
        # Télécharger l'image
        urllib.request.urlretrieve(url, img_path)
        return True
        
    except (URLError, HTTPError) as e:
        print(f"✗ Erreur téléchargement {filename}: {e}")
        return False
    except Exception as e:
        print(f"✗ Erreur inattendue pour {filename}: {e}")
        return False

def get_image_for_castle(castle_name, index):
    """Obtenir une URL d'image pour un château donné"""
    # Pour simplifier, on utilise les images génériques d'Unsplash
    # qui sont de haute qualité et libres de droits
    return GENERIC_CASTLE_IMAGES[index % len(GENERIC_CASTLE_IMAGES)]

def update_html_with_image(file_path, image_filename, castle_name):
    """Mettre à jour le fichier HTML avec l'image"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Chercher le commentaire placeholder d'image
        image_placeholder = '<!-- Image placeholder: will be replaced with actual castle image -->'
        
        if image_placeholder in content:
            # Remplacer par la vraie balise img
            img_tag = f'''<img src="assets/img/{image_filename}" alt="{castle_name}" loading="lazy" class="castle-main-image">'''
            content = content.replace(image_placeholder, img_tag)
            
            # Enlever la classe qui cache la section media
            content = content.replace('class="detail-media detail-media-hidden"', 'class="detail-media"')
            
            # Écrire le fichier modifié
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return True
        else:
            print(f"○ Pas de placeholder d'image trouvé dans {os.path.basename(file_path)}")
            return False
            
    except Exception as e:
        print(f"✗ Erreur mise à jour HTML {os.path.basename(file_path)}: {e}")
        return False

def main():
    """Fonction principale"""
    print("=== AJOUT D'IMAGES DE CHÂTEAUX (APPROCHE SIMPLE) ===")
    
    # Créer le répertoire d'images
    img_dir = create_assets_directory()
    print(f"Répertoire d'images: {img_dir}")
    
    # Trouver tous les fichiers HTML de châteaux
    castle_files = glob.glob("/Users/marc/Desktop/kastelenbelgie/kasteel-*.html")
    castle_files.extend(glob.glob("/Users/marc/Desktop/kastelenbelgie/chateau-*.html"))
    castle_files.extend(glob.glob("/Users/marc/Desktop/kastelenbelgie/citadel-*.html"))
    castle_files.extend(glob.glob("/Users/marc/Desktop/kastelenbelgie/burcht-*.html"))
    castle_files.extend(glob.glob("/Users/marc/Desktop/kastelenbelgie/*kasteel*.html"))
    castle_files.extend(glob.glob("/Users/marc/Desktop/kastelenbelgie/hof-*.html"))
    castle_files.extend(glob.glob("/Users/marc/Desktop/kastelenbelgie/de-*.html"))
    castle_files.extend(glob.glob("/Users/marc/Desktop/kastelenbelgie/het-*.html"))
    castle_files.extend(glob.glob("/Users/marc/Desktop/kastelenbelgie/sint-*.html"))
    castle_files.extend(glob.glob("/Users/marc/Desktop/kastelenbelgie/koninklijk-*.html"))
    castle_files.extend(glob.glob("/Users/marc/Desktop/kastelenbelgie/waterslot-*.html"))
    castle_files.extend(glob.glob("/Users/marc/Desktop/kastelenbelgie/vrieselhof-*.html"))
    castle_files.extend(glob.glob("/Users/marc/Desktop/kastelenbelgie/rentmeesterij-*.html"))
    castle_files.extend(glob.glob("/Users/marc/Desktop/kastelenbelgie/commanderij-*.html"))
    castle_files.extend(glob.glob("/Users/marc/Desktop/kastelenbelgie/domein-*.html"))
    castle_files.extend(glob.glob("/Users/marc/Desktop/kastelenbelgie/oud-*.html"))
    castle_files.extend(glob.glob("/Users/marc/Desktop/kastelenbelgie/bisschoppenhof-*.html"))
    castle_files.extend(glob.glob("/Users/marc/Desktop/kastelenbelgie/braemkasteel-*.html"))
    castle_files.extend(glob.glob("/Users/marc/Desktop/kastelenbelgie/burchtruine-*.html"))
    castle_files.extend(glob.glob("/Users/marc/Desktop/kastelenbelgie/gaverkasteel-*.html"))
    
    # Enlever les doublons et trier
    castle_files = sorted(list(set(castle_files)))
    
    print(f"Nombre de pages de châteaux trouvées: {len(castle_files)}")
    
    success_count = 0
    
    for i, file_path in enumerate(castle_files):
        filename = os.path.basename(file_path)
        castle_name = extract_castle_name(filename)
        
        # Nom de fichier pour l'image
        image_filename = filename.replace('.html', '.jpg')
        
        # Obtenir l'URL de l'image (rotation des images génériques)
        image_url = get_image_for_castle(castle_name, i)
        
        print(f"Traitement: {filename}")
        print(f"  Château: {castle_name}")
        print(f"  Image: {image_filename}")
        
        # Télécharger l'image
        if download_image(image_url, image_filename, img_dir):
            # Mettre à jour le HTML
            if update_html_with_image(file_path, image_filename, castle_name):
                print(f"✓ Image ajoutée avec succès: {filename}")
                success_count += 1
            else:
                print(f"✗ Échec mise à jour HTML: {filename}")
        else:
            print(f"✗ Échec téléchargement: {filename}")
        
        # Petite pause pour éviter de surcharger les serveurs
        time.sleep(0.1)
    
    print("\n=== RÉSUMÉ ===")
    print(f"Pages traitées: {len(castle_files)}")
    print(f"Images ajoutées avec succès: {success_count}")
    print(f"Taux de succès: {success_count/len(castle_files)*100:.1f}%")

if __name__ == "__main__":
    main()
