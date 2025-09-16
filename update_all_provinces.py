#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script pour mettre à jour toutes les pages provinces avec des liens
"""

import os
import re

def update_province_page(file_path, province_name):
    """Met à jour une page province avec des liens"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Trouve le paragraphe de description (le deuxième <p>)
        pattern = r'(<p class="lead">[^<]+</p>\s*<p>)([^<]+)(</p>)'
        match = re.search(pattern, content)
        
        if not match:
            return False, "Pattern non trouvé"
        
        lead_part = match.group(1)
        description_part = match.group(2)
        end_part = match.group(3)
        
        # Vérifie si les liens existent déjà
        if 'href="provinces.html"' in description_part and 'href="index.html"' in description_part:
            return False, "Liens déjà présents"
        
        # Ajoute les liens à la fin de la description
        enhanced_description = description_part.rstrip('.')
        enhanced_description += '. Ontdek ook <a href="provinces.html">alle provincies van België</a> en hun unieke kasteelcollecties, of bezoek onze <a href="index.html">homepage</a> voor meer informatie over kastelen in België.'
        
        # Remplace le contenu
        new_content = content.replace(
            match.group(0),
            lead_part + enhanced_description + end_part
        )
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True, "Liens ajoutés"
        
    except Exception as e:
        return False, f"Erreur: {e}"

def main():
    """Fonction principale"""
    province_files = [
        ('/Users/marc/Desktop/kastelenbelgie/henegouwen.html', 'Henegouwen'),
        ('/Users/marc/Desktop/kastelenbelgie/oost-vlaanderen.html', 'Oost-Vlaanderen'),
        ('/Users/marc/Desktop/kastelenbelgie/west-vlaanderen.html', 'West-Vlaanderen'),
        ('/Users/marc/Desktop/kastelenbelgie/limburg.html', 'Limburg'),
        ('/Users/marc/Desktop/kastelenbelgie/vlaams-brabant.html', 'Vlaams-Brabant'),
        ('/Users/marc/Desktop/kastelenbelgie/namen.html', 'Namen'),
        ('/Users/marc/Desktop/kastelenbelgie/luik.html', 'Luik'),
        ('/Users/marc/Desktop/kastelenbelgie/luxemburg.html', 'Luxemburg'),
        ('/Users/marc/Desktop/kastelenbelgie/waals-brabant.html', 'Waals-Brabant'),
        ('/Users/marc/Desktop/kastelenbelgie/brussel.html', 'Brussel')
    ]
    
    print("=== MISE À JOUR DES PAGES PROVINCES ===")
    
    updated_count = 0
    
    for file_path, province_name in province_files:
        if not os.path.exists(file_path):
            print(f"  ○ {province_name}: Fichier non trouvé")
            continue
        
        success, message = update_province_page(file_path, province_name)
        
        if success:
            print(f"  ✓ {province_name}: {message}")
            updated_count += 1
        else:
            print(f"  ○ {province_name}: {message}")
    
    print(f"\nRésultat: {updated_count} pages provinces mises à jour")

if __name__ == "__main__":
    main()
