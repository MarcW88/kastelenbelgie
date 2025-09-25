#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
AJOUT DE LA FONCTIONNALITÉ DE RECHERCHE À TOUTES LES PAGES
Ajoute le script search.js à toutes les pages HTML
"""

import os
import glob
import re

def add_search_script_to_page(file_path):
    """Ajoute le script de recherche à une page"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Vérifier si le script est déjà présent
        if 'js/search.js' in content:
            return False
        
        # Ajouter le script avant </body>
        if '</body>' in content:
            content = content.replace('</body>', '    <script src="js/search.js"></script>\n</body>')
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        
        return False
        
    except Exception as e:
        print(f"Erreur avec {file_path}: {e}")
        return False

def main():
    """Fonction principale"""
    print("🔍 AJOUT DE LA RECHERCHE À TOUTES LES PAGES")
    print("=" * 50)
    
    # Trouver tous les fichiers HTML
    html_files = glob.glob("/Users/marc/Desktop/kastelenbelgie/*.html")
    
    print(f"📄 {len(html_files)} fichiers HTML trouvés")
    
    updated_count = 0
    
    for file_path in html_files:
        filename = os.path.basename(file_path)
        
        if add_search_script_to_page(file_path):
            updated_count += 1
            print(f"  ✅ {filename}")
        else:
            print(f"  ⏭️  {filename} (déjà à jour)")
    
    print(f"\n🎯 {updated_count} pages mises à jour avec la recherche")
    print("✅ Fonctionnalité de recherche ajoutée !")

if __name__ == "__main__":
    main()
