#!/usr/bin/env python3
"""
Script pour ajouter le lien 'A–Z' dans le menu de navigation de toutes les pages
"""

import os
import re
from pathlib import Path

def update_navigation(html_file):
    """Ajoute le lien A-Z dans le menu de navigation"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Vérifier si le lien A-Z existe déjà
    if 'alle-kastelen.html' in content:
        return False
    
    # Pattern pour trouver le menu de navigation et ajouter le lien A-Z
    # On cherche le lien "Provincies" ou "Kastelen" et on ajoute A-Z après
    
    # Pattern 1: <a href="provinces.html" class="nav-link">Provincies</a>
    pattern1 = r'(<a[^>]*href="provinces\.html"[^>]*class="nav-link"[^>]*>Provincies</a>)'
    replacement1 = r'\1\n                    <a href="alle-kastelen.html" class="nav-link">A–Z</a>'
    
    if re.search(pattern1, content):
        content = re.sub(pattern1, replacement1, content)
    else:
        # Pattern 2: <a class="nav-link" href="provinces.html">Kastelen</a>
        pattern2 = r'(<a[^>]*class="nav-link"[^>]*href="provinces\.html"[^>]*>Kastelen</a>)'
        replacement2 = r'\1\n<a class="nav-link" href="alle-kastelen.html">A–Z</a>'
        
        if re.search(pattern2, content):
            content = re.sub(pattern2, replacement2, content)
        else:
            return False
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def main():
    base_path = Path('/Users/marc/Desktop/kastelenbelgie')
    
    # Trouver tous les fichiers HTML
    html_files = list(base_path.glob('*.html'))
    
    updated = 0
    skipped = 0
    
    for html_file in html_files:
        # Ignorer les fichiers backup/old
        if '-old' in html_file.name or '-backup' in html_file.name:
            continue
            
        try:
            if update_navigation(html_file):
                print(f"✓ {html_file.name}")
                updated += 1
            else:
                skipped += 1
        except Exception as e:
            print(f"✗ {html_file.name}: {e}")
    
    print(f"\nTotal: {updated} fichiers mis à jour, {skipped} ignorés (déjà à jour ou structure différente)")

if __name__ == '__main__':
    main()
