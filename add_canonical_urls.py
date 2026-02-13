#!/usr/bin/env python3
"""
Script pour ajouter des balises canoniques self-referencing à toutes les pages HTML.
Les URLs canoniques pointent vers https://kastelenbelgie.be/[nom-du-fichier].html
"""

import os
import re
from pathlib import Path

# Configuration
BASE_URL = "https://kastelenbelgie.be"
DIRECTORY = "/Users/marc/Desktop/kastelenbelgie"

def add_canonical_to_file(filepath):
    """Ajoute une balise canonical self-referencing à un fichier HTML."""
    
    filename = os.path.basename(filepath)
    canonical_url = f"{BASE_URL}/{filename}"
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Vérifier si une balise canonical existe déjà
    if 'rel="canonical"' in content or "rel='canonical'" in content:
        print(f"⏭️  Canonical déjà présent: {filename}")
        return False
    
    # Créer la balise canonical
    canonical_tag = f'<link rel="canonical" href="{canonical_url}"/>'
    
    # Insérer après la balise </title> ou avant </head>
    if '</title>' in content:
        # Insérer après </title>
        content = content.replace('</title>', f'</title>\n{canonical_tag}', 1)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Canonical ajouté: {filename}")
        return True
    elif '</head>' in content:
        # Insérer avant </head>
        content = content.replace('</head>', f'{canonical_tag}\n</head>', 1)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Canonical ajouté: {filename}")
        return True
    else:
        print(f"⚠️  Structure HTML non standard: {filename}")
        return False

def main():
    """Parcourt tous les fichiers HTML et ajoute les balises canoniques."""
    
    html_files = list(Path(DIRECTORY).glob("*.html"))
    
    print(f"\n🔍 Trouvé {len(html_files)} fichiers HTML\n")
    print("=" * 60)
    
    added = 0
    skipped = 0
    errors = 0
    
    for filepath in sorted(html_files):
        try:
            result = add_canonical_to_file(str(filepath))
            if result:
                added += 1
            else:
                skipped += 1
        except Exception as e:
            print(f"❌ Erreur: {filepath.name} - {e}")
            errors += 1
    
    print("=" * 60)
    print(f"\n📊 Résumé:")
    print(f"   ✅ Canonicals ajoutés: {added}")
    print(f"   ⏭️  Déjà présents: {skipped}")
    print(f"   ❌ Erreurs: {errors}")
    print(f"   📁 Total fichiers: {len(html_files)}")

if __name__ == "__main__":
    main()
