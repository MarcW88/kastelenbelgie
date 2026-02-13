#!/usr/bin/env python3
"""
Script pour supprimer les formulaires de réservation des pages châteaux
"""

import os
import re
from pathlib import Path

def remove_reservation_form(html_file):
    """Supprime la section reservation-form d'un fichier HTML"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Vérifier si le formulaire existe
    if 'reservation-form' not in content and 'Reserveer je bezoek' not in content:
        return False
    
    # Pattern pour supprimer la section complète du formulaire de réservation
    # On cherche depuis le commentaire ou la section jusqu'à la fermeture
    patterns = [
        # Pattern 1: Section avec commentaire
        r'<!-- Section \d+: Reservatieformulier -->\s*<section class="reservation-form">.*?</section>',
        # Pattern 2: Section sans commentaire numéroté
        r'<!-- Reservatieformulier -->\s*<section class="reservation-form">.*?</section>',
        # Pattern 3: Section directe
        r'<section class="reservation-form">\s*<div class="container">\s*<h2>Reserveer je bezoek.*?</section>',
    ]
    
    original_content = content
    
    for pattern in patterns:
        content = re.sub(pattern, '', content, flags=re.DOTALL)
    
    # Nettoyer les lignes vides multiples
    content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
    
    if content != original_content:
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    
    return False

def main():
    base_path = Path('/Users/marc/Desktop/kastelenbelgie')
    
    # Trouver tous les fichiers HTML de châteaux
    patterns = ['kasteel-*.html', 'hof-*.html', 'citadel-*.html', 'burcht-*.html', 
                'slot-*.html', 'waterslot-*.html', 'waterkasteel-*.html', 'chateau-*.html']
    
    html_files = []
    for pattern in patterns:
        html_files.extend(base_path.glob(pattern))
    
    # Ajouter aussi les autres fichiers qui pourraient avoir des formulaires
    html_files.extend(base_path.glob('*.html'))
    html_files = list(set(html_files))  # Dédupliquer
    
    updated = 0
    skipped = 0
    
    for html_file in sorted(html_files):
        # Ignorer les fichiers backup/old
        if '-old' in html_file.name or '-backup' in html_file.name:
            continue
            
        try:
            if remove_reservation_form(html_file):
                print(f"✓ {html_file.name}")
                updated += 1
            else:
                skipped += 1
        except Exception as e:
            print(f"✗ {html_file.name}: {e}")
    
    print(f"\nTotal: {updated} formulaires supprimés, {skipped} fichiers sans formulaire")

if __name__ == '__main__':
    main()
