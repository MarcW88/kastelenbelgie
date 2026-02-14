#!/usr/bin/env python3
"""
Script pour restructurer la section praktische informatie:
- Titre en premier
- Image sous le titre
- Grille de blocs en dessous
"""

import re
from pathlib import Path

BASE_DIR = Path(__file__).parent

PAGES = [
    "kasteel-van-deulin-deulin-fronville.html",
    "kasteel-van-mirwart-mirwart-saint-hubert.html",
    "kasteel-van-longchamps-longchamps-bertogne.html",
    "kasteel-van-porcheresse-daverdisse.html",
    "kasteel-van-orval-villers-devant-orval.html",
]


def restructure_practical_section(content: str) -> str:
    """
    Restructure la section praktische informatie:
    Ancien: <div class="practical-layout"><div class="practical-content"><h2>...</h2><div class="practical-grid">...</div></div><div class="practical-image">...</div></div>
    Nouveau: <div class="practical-layout"><h2>...</h2><div class="practical-image">...</div><div class="practical-grid">...</div></div>
    """
    # Pattern pour capturer la structure actuelle
    pattern = r'(<div class="practical-layout">)\s*<div class="practical-content">\s*(<h2>[^<]+</h2>)\s*(<div class="practical-grid">.*?</div>\s*</div>\s*</div>)\s*</div>\s*(<div class="practical-image">.*?</div>)\s*(</div>)'
    
    def replacement(match):
        layout_start = match.group(1)
        h2 = match.group(2)
        grid = match.group(3)
        image = match.group(4)
        layout_end = match.group(5)
        
        # Nettoyer le grid (enlever les </div> en trop)
        grid_clean = re.sub(r'</div>\s*</div>\s*</div>$', '</div>\n</div>', grid)
        
        return f'{layout_start}\n{h2}\n{image}\n{grid_clean}\n{layout_end}'
    
    return re.sub(pattern, replacement, content, flags=re.DOTALL)


def update_pages():
    for page in PAGES:
        page_path = BASE_DIR / page
        
        if not page_path.exists():
            print(f"⚠️  Page non trouvée: {page}")
            continue
        
        with open(page_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        original = content
        
        # Restructurer la section
        content = restructure_practical_section(content)
        
        if content != original:
            with open(page_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"✅ Restructuré: {page}")
        else:
            print(f"⏭️  Pas de changement: {page}")


if __name__ == "__main__":
    print("🔄 Restructuration des sections praktische informatie...\n")
    update_pages()
    print("\n✅ Terminé!")
