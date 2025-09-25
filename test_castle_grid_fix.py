#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
TEST DE LA CORRECTION DES GRILLES DE CHÂTEAUX
Vérifie que les grilles s'affichent correctement
"""

def test_castle_grid_fix():
    """Teste la correction des grilles de châteaux"""
    
    print("🧪 TEST DE LA CORRECTION DES GRILLES DE CHÂTEAUX")
    print("=" * 60)
    
    # Vérifier qu'Antwerpen a bien les styles CSS
    antwerpen_file = "/Users/marc/Desktop/kastelenbelgie/antwerpen.html"
    
    try:
        with open(antwerpen_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print("✅ Fichier Antwerpen lu avec succès")
        
        # Vérifications
        checks = [
            ('modern-style.css', 'CSS moderne chargé'),
            ('castle-grid', 'Classe castle-grid présente'),
            ('castle-card', 'Classes castle-card présentes'),
            ('castle-card-content', 'Classes castle-card-content présentes'),
            ('castle-image', 'Classes castle-image présentes')
        ]
        
        for check, description in checks:
            if check in content:
                print(f"✅ {description}")
            else:
                print(f"❌ {description} - MANQUANT")
        
        # Compter les châteaux
        castle_count = content.count('<div class="castle-card">')
        print(f"🏰 Nombre de châteaux trouvés: {castle_count}")
        
        if castle_count > 0:
            print("✅ Les châteaux devraient maintenant s'afficher en grille de 3 colonnes")
        else:
            print("❌ Aucun château trouvé dans la grille")
            
    except Exception as e:
        print(f"❌ Erreur: {e}")

def check_modern_css():
    """Vérifie que modern-style.css contient les styles nécessaires"""
    
    print("\n🎨 VÉRIFICATION DU CSS MODERNE")
    print("=" * 40)
    
    css_file = "/Users/marc/Desktop/kastelenbelgie/css/modern-style.css"
    
    try:
        with open(css_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        css_checks = [
            ('.castle-grid', 'Grille châteaux définie'),
            ('grid-template-columns: repeat(auto-fit, minmax(300px, 1fr))', 'Colonnes responsive'),
            ('.castle-card', 'Styles cards châteaux'),
            ('.castle-card:hover', 'Effets hover'),
            ('transform: translateY(-5px)', 'Animation hover'),
            ('.castle-image', 'Styles images'),
            ('object-fit: cover', 'Images responsive')
        ]
        
        for check, description in css_checks:
            if check in content:
                print(f"✅ {description}")
            else:
                print(f"❌ {description} - MANQUANT")
                
    except Exception as e:
        print(f"❌ Erreur CSS: {e}")

if __name__ == "__main__":
    test_castle_grid_fix()
    check_modern_css()
    
    print("\n🎯 RÉSULTAT:")
    print("Les châteaux devraient maintenant s'afficher correctement")
    print("en grille de 3 colonnes côte à côte sur les pages provinces!")
    print("\nPour tester: ouvrez antwerpen.html dans votre navigateur")
