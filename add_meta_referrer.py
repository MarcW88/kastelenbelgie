#!/usr/bin/env python3
"""
Script pour ajouter la balise meta referrer à toutes les pages HTML.
"""

import os
from pathlib import Path

DIRECTORY = "/Users/marc/Desktop/kastelenbelgie"

def add_meta_referrer(filepath):
    """Ajoute une balise meta referrer à un fichier HTML."""
    
    filename = os.path.basename(filepath)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Vérifier si la balise meta referrer existe déjà
    if 'name="referrer"' in content or "name='referrer'" in content:
        print(f"⏭️  Meta referrer déjà présent: {filename}")
        return False
    
    # Créer la balise meta referrer
    meta_tag = '<meta name="referrer" content="strict-origin-when-cross-origin"/>'
    
    # Insérer après la balise <meta charset> ou après <meta name="viewport">
    if '<meta content="width=device-width' in content:
        content = content.replace(
            '<meta content="width=device-width, initial-scale=1.0" name="viewport"/>',
            '<meta content="width=device-width, initial-scale=1.0" name="viewport"/>\n' + meta_tag,
            1
        )
    elif '<meta charset' in content:
        # Chercher la fin de la balise charset
        import re
        content = re.sub(
            r'(<meta charset="utf-8"\s*/>)',
            r'\1\n' + meta_tag,
            content,
            count=1
        )
    else:
        print(f"⚠️  Structure HTML non standard: {filename}")
        return False
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Meta referrer ajouté: {filename}")
    return True

def main():
    """Parcourt tous les fichiers HTML et ajoute les balises meta referrer."""
    
    html_files = list(Path(DIRECTORY).glob("*.html"))
    
    print(f"\n🔍 Trouvé {len(html_files)} fichiers HTML\n")
    print("=" * 60)
    
    added = 0
    skipped = 0
    errors = 0
    
    for filepath in sorted(html_files):
        try:
            result = add_meta_referrer(str(filepath))
            if result:
                added += 1
            else:
                skipped += 1
        except Exception as e:
            print(f"❌ Erreur: {filepath.name} - {e}")
            errors += 1
    
    print("=" * 60)
    print(f"\n📊 Résumé:")
    print(f"   ✅ Meta referrer ajoutés: {added}")
    print(f"   ⏭️  Déjà présents: {skipped}")
    print(f"   ❌ Erreurs: {errors}")
    print(f"   📁 Total fichiers: {len(html_files)}")

if __name__ == "__main__":
    main()
