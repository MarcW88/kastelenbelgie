#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script pour uniformiser les titres des châteaux dans les blocs des pages provinces
"""

import os
import re
import glob

def clean_castle_title(title):
    """Nettoie et uniformise le titre d'un château"""
    title = title.strip()
    
    # Patterns à nettoyer - enlève les localisations à la fin
    patterns_to_remove = [
        r'\s+[A-Z][a-z]+$',  # Enlève le dernier mot s'il commence par une majuscule (ville)
        r'\s+te\s+\w+$',     # Enlève "te [ville]"
        r'\s+in\s+\w+$',     # Enlève "in [ville]"
    ]
    
    # Applique les patterns de nettoyage
    cleaned = title
    for pattern in patterns_to_remove:
        test_result = re.sub(pattern, '', cleaned, flags=re.IGNORECASE).strip()
        if len(test_result) > 5:  # Garde au moins 5 caractères
            cleaned = test_result
    
    # Capitalise correctement
    words = cleaned.split()
    capitalized_words = []
    
    for i, word in enumerate(words):
        word_lower = word.lower()
        
        # Mots qui restent en minuscules (sauf en début de titre)
        if i > 0 and word_lower in ['van', 'de', 'het', 'der', 'des', 'du', 'la', 'le', 'te', 'op', 'aan', 'in']:
            capitalized_words.append(word_lower)
        else:
            # Capitalise la première lettre
            capitalized_words.append(word_lower.capitalize())
    
    return ' '.join(capitalized_words)

def update_province_castle_titles(file_path):
    """Met à jour les titres des châteaux dans une page province"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Trouve tous les titres de châteaux dans les blocs
        title_pattern = r'<h3>([^<]+)</h3>'
        matches = re.findall(title_pattern, content)
        
        if not matches:
            return False, "Aucun titre trouvé"
        
        updated_content = content
        changes_made = 0
        
        for old_title in matches:
            new_title = clean_castle_title(old_title)
            
            if old_title != new_title:
                # Remplace le titre dans le contenu
                updated_content = updated_content.replace(
                    f'<h3>{old_title}</h3>',
                    f'<h3>{new_title}</h3>'
                )
                changes_made += 1
        
        if changes_made > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            return True, f"{changes_made} titres mis à jour"
        else:
            return False, "Aucun changement nécessaire"
        
    except Exception as e:
        return False, f"Erreur: {e}"

def main():
    """Fonction principale"""
    print("=== UNIFORMISATION DES TITRES DANS LES PAGES PROVINCES ===")
    
    # Liste des pages provinces
    province_files = [
        '/Users/marc/Desktop/kastelenbelgie/antwerpen.html',
        '/Users/marc/Desktop/kastelenbelgie/henegouwen.html',
        '/Users/marc/Desktop/kastelenbelgie/oost-vlaanderen.html',
        '/Users/marc/Desktop/kastelenbelgie/west-vlaanderen.html',
        '/Users/marc/Desktop/kastelenbelgie/limburg.html',
        '/Users/marc/Desktop/kastelenbelgie/vlaams-brabant.html',
        '/Users/marc/Desktop/kastelenbelgie/namen.html',
        '/Users/marc/Desktop/kastelenbelgie/luik.html',
        '/Users/marc/Desktop/kastelenbelgie/luxemburg.html',
        '/Users/marc/Desktop/kastelenbelgie/waals-brabant.html'
    ]
    
    total_updated = 0
    
    for file_path in province_files:
        if not os.path.exists(file_path):
            province_name = os.path.basename(file_path).replace('.html', '').title()
            print(f"  ○ {province_name}: Fichier non trouvé")
            continue
        
        province_name = os.path.basename(file_path).replace('.html', '').title()
        success, message = update_province_castle_titles(file_path)
        
        if success:
            print(f"  ✓ {province_name}: {message}")
            total_updated += 1
        else:
            print(f"  ○ {province_name}: {message}")
    
    print(f"\n=== RÉSULTAT FINAL ===")
    print(f"Pages provinces mises à jour: {total_updated}")
    print("Uniformisation des titres terminée!")

if __name__ == "__main__":
    main()
