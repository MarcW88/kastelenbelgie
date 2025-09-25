#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CORRECTION DE L'AFFICHAGE DES GRILLES DE CHÂTEAUX
Corrige les problèmes d'affichage des encadrés de châteaux
"""

import glob
import re

def fix_castle_grid_display():
    """Corrige l'affichage des grilles de châteaux sur les pages provinces"""
    
    print("🏰 CORRECTION DE L'AFFICHAGE DES GRILLES DE CHÂTEAUX")
    print("=" * 60)
    
    # Pages provinces à corriger
    province_files = [
        'antwerpen.html', 'limburg.html', 'oost-vlaanderen.html', 
        'west-vlaanderen.html', 'vlaams-brabant.html', 'namen.html',
        'luik.html', 'henegouwen.html', 'luxemburg.html', 
        'waals-brabant.html', 'brussel.html'
    ]
    
    updated_count = 0
    
    for filename in province_files:
        file_path = f"/Users/marc/Desktop/kastelenbelgie/{filename}"
        
        try:
            # Lire le fichier
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Vérifier si la page utilise le bon CSS
            if 'unified-style.css' not in content:
                print(f"⚠️ {filename}: utilise un autre CSS")
                continue
            
            # Vérifier la structure de la grille
            if 'castle-grid' not in content:
                print(f"⚠️ {filename}: pas de castle-grid trouvée")
                continue
            
            # S'assurer que la structure est correcte
            content_modified = False
            
            # Vérifier que les castle-card ont bien la classe castle-card-content
            if 'castle-card-content' not in content and 'castle-card' in content:
                # Remplacer les anciennes structures
                content = re.sub(
                    r'<div class="card-content">',
                    '<div class="castle-card-content">',
                    content
                )
                content_modified = True
                print(f"  ✅ Corrigé les classes card-content → castle-card-content")
            
            # S'assurer que les boutons ont la bonne classe
            if 'btn-primary' in content and 'btn btn-primary' not in content:
                content = re.sub(
                    r'class="btn-primary"',
                    'class="btn btn-primary"',
                    content
                )
                content_modified = True
                print(f"  ✅ Corrigé les classes boutons")
            
            if content_modified:
                # Sauvegarder
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                updated_count += 1
                print(f"✅ {filename}: structure corrigée")
            else:
                print(f"✅ {filename}: structure déjà correcte")
            
        except Exception as e:
            print(f"❌ Erreur avec {filename}: {e}")
            continue
    
    print(f"\n📊 RÉSULTATS:")
    print(f"Pages corrigées: {updated_count}")
    print(f"Pages vérifiées: {len(province_files)}")

def add_debug_css():
    """Ajoute du CSS de debug pour vérifier l'affichage"""
    css_file = "/Users/marc/Desktop/kastelenbelgie/css/unified-style.css"
    
    debug_css = """
/* DEBUG: Styles de test pour les grilles châteaux */
.castle-grid {
    border: 2px solid red !important;
    background: rgba(255, 0, 0, 0.1) !important;
}

.castle-card {
    border: 1px solid blue !important;
    background: rgba(0, 0, 255, 0.05) !important;
}

.castle-card-content {
    border: 1px solid green !important;
}
"""
    
    try:
        with open(css_file, 'a', encoding='utf-8') as f:
            f.write(debug_css)
        print("✅ CSS de debug ajouté")
    except Exception as e:
        print(f"❌ Erreur ajout debug CSS: {e}")

if __name__ == "__main__":
    fix_castle_grid_display()
    
    print("\n🔧 Ajouter du CSS de debug? (y/n)")
    # add_debug_css()  # Décommentez pour ajouter le debug CSS
