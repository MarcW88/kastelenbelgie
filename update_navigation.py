#!/usr/bin/env python3
"""
Script pour mettre à jour la navigation sur toutes les pages:
1. Renommer "A–Z" en "Alle Kastelen" 
2. S'assurer que le lien est présent dans tous les menus
3. Ajouter lien "Over ons" dans le footer
"""

import re
from pathlib import Path

BASE_DIR = Path(__file__).parent

def update_navigation(filepath: Path) -> bool:
    """Met à jour la navigation d'une page HTML"""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    original = content
    changes_made = False
    
    # 1. Remplacer "A–Z" par "Alle Kastelen" dans le menu nav
    # Pattern: <a href="alle-kastelen.html" class="nav-link">A–Z</a>
    old_patterns = [
        r'(<a[^>]*href="alle-kastelen\.html"[^>]*>)A–Z(</a>)',
        r'(<a[^>]*href="alle-kastelen\.html"[^>]*>)A-Z(</a>)',
        r'(<a[^>]*class="nav-link"[^>]*href="alle-kastelen\.html"[^>]*>)A–Z(</a>)',
        r'(<a[^>]*class="nav-link"[^>]*href="alle-kastelen\.html"[^>]*>)A-Z(</a>)',
    ]
    
    for pattern in old_patterns:
        content = re.sub(pattern, r'\1Alle Kastelen\2', content)
    
    # 2. Si le menu n'a pas "Alle Kastelen", l'ajouter après "Provincies" ou "Kastelen"
    if 'alle-kastelen.html' not in content and '<nav class="navbar">' in content:
        # Ajouter le lien après Provincies ou Kastelen
        patterns_to_add_after = [
            (r'(<a[^>]*href="provinces\.html"[^>]*>Provincies</a>)', 
             r'\1\n                    <a href="alle-kastelen.html" class="nav-link">Alle Kastelen</a>'),
            (r'(<a[^>]*href="provinces\.html"[^>]*>Kastelen</a>)',
             r'\1\n                    <a href="alle-kastelen.html" class="nav-link">Alle Kastelen</a>'),
        ]
        for pattern, replacement in patterns_to_add_after:
            if re.search(pattern, content):
                content = re.sub(pattern, replacement, content)
                break
    
    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    
    return False


def process_all_pages():
    """Traite toutes les pages HTML"""
    print("🔄 Mise à jour de la navigation...\n")
    
    updated = 0
    skipped = 0
    
    for filepath in BASE_DIR.glob("*.html"):
        if update_navigation(filepath):
            print(f"✅ {filepath.name}")
            updated += 1
        else:
            skipped += 1
    
    print(f"\n📊 Résultat: {updated} mises à jour, {skipped} inchangées")


if __name__ == "__main__":
    process_all_pages()
