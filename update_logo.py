#!/usr/bin/env python3
"""
Script pour mettre à jour le favicon et le logo dans le header de toutes les pages
"""

import os
import re
from pathlib import Path

def update_logo_and_favicon(html_file):
    """Met à jour le favicon et le logo dans un fichier HTML"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # 1. Mettre à jour le favicon (remplacer favicon.svg par favicon.png)
    content = re.sub(
        r'<link[^>]*href="favicon\.svg"[^>]*type="image/svg\+xml"[^>]*/?>',
        '<link href="favicon.png" rel="icon" type="image/png"/>',
        content
    )
    content = re.sub(
        r'<link[^>]*rel="icon"[^>]*href="favicon\.svg"[^>]*/?>',
        '<link href="favicon.png" rel="icon" type="image/png"/>',
        content
    )
    
    # 2. Mettre à jour le logo dans le header (remplacer emoji par image)
    # Pattern: <div class="logo-icon">🏰</div>
    content = re.sub(
        r'<div class="logo-icon">🏰</div>',
        '<img src="logo_kastelenbelgie.png" alt="Kastelen België" class="logo-img" style="height: 40px; width: auto;"/>',
        content
    )
    
    # Pattern alternatif pour le footer emoji
    # On garde l'emoji dans le footer car c'est du texte
    
    if content != original_content:
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    
    return False

def main():
    base_path = Path('/Users/marc/Desktop/kastelenbelgie')
    
    # Trouver tous les fichiers HTML
    html_files = list(base_path.glob('*.html'))
    
    updated = 0
    skipped = 0
    
    for html_file in sorted(html_files):
        # Ignorer les fichiers backup/old
        if '-old' in html_file.name or '-backup' in html_file.name:
            continue
            
        try:
            if update_logo_and_favicon(html_file):
                print(f"✓ {html_file.name}")
                updated += 1
            else:
                skipped += 1
        except Exception as e:
            print(f"✗ {html_file.name}: {e}")
    
    print(f"\nTotal: {updated} fichiers mis à jour, {skipped} ignorés")

if __name__ == '__main__':
    main()
