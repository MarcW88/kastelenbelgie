#!/usr/bin/env python3
"""
Script pour ajouter le lien "Over ons" dans le footer de toutes les pages
"""

import re
from pathlib import Path

BASE_DIR = Path(__file__).parent


def add_over_ons_link(filepath: Path) -> bool:
    """Ajoute le lien Over ons dans le footer"""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    original = content
    
    # Si le lien existe déjà, ne rien faire
    if 'over-ons.html' in content:
        return False
    
    # Pattern 1: Ajouter après "Algemene voorwaarden" dans le footer
    pattern1 = r'(<li[^>]*><a[^>]*href="algemene-voorwaarden\.html"[^>]*>Algemene voorwaarden</a></li>)'
    replacement1 = r'\1\n<li style="margin-bottom: 0.6rem;"><a href="over-ons.html" style="color: #D4C7B4; text-decoration: none; font-size: 0.9rem;">Over ons</a></li>'
    
    if re.search(pattern1, content):
        content = re.sub(pattern1, replacement1, content)
    
    # Pattern 2: Ajouter dans la section "Blog & Informatie" si elle existe
    pattern2 = r'(Blog &amp; Informatie</h4>.*?<ul[^>]*>)'
    
    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    
    return False


def process_all_pages():
    """Traite toutes les pages HTML"""
    print("🔄 Ajout du lien 'Over ons' dans les footers...\n")
    
    updated = 0
    skipped = 0
    
    for filepath in BASE_DIR.glob("*.html"):
        if filepath.name == "over-ons.html":
            continue
        if add_over_ons_link(filepath):
            print(f"✅ {filepath.name}")
            updated += 1
        else:
            skipped += 1
    
    print(f"\n📊 Résultat: {updated} mises à jour, {skipped} inchangées/déjà présent")


if __name__ == "__main__":
    process_all_pages()
