#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
RAPPORT FINAL DU SITE KASTELENBELGIE.BE
Vérifie que tous les éléments sont en place
"""

import os
import glob
import json
from collections import defaultdict

def check_file_exists(filepath, description):
    """Vérifie si un fichier existe"""
    exists = os.path.exists(filepath)
    status = "✅" if exists else "❌"
    print(f"  {status} {description}: {os.path.basename(filepath)}")
    return exists

def analyze_html_files():
    """Analyse tous les fichiers HTML"""
    html_files = glob.glob("/Users/marc/Desktop/kastelenbelgie/*.html")
    
    categories = {
        'homepage': [],
        'provinces': [],
        'castles': [],
        'blog': [],
        'legal': [],
        'other': []
    }
    
    for file_path in html_files:
        filename = os.path.basename(file_path)
        
        if filename == 'index.html':
            categories['homepage'].append(filename)
        elif filename == 'provinces.html' or filename in ['antwerpen.html', 'limburg.html', 'oost-vlaanderen.html', 'west-vlaanderen.html', 'vlaams-brabant.html', 'brussel.html', 'waals-brabant.html', 'henegouwen.html', 'namen.html', 'luik.html', 'luxemburg.html']:
            categories['provinces'].append(filename)
        elif filename.startswith('kasteel-') or filename.startswith('chateau-') or filename.startswith('citadel-'):
            categories['castles'].append(filename)
        elif filename.startswith('blog'):
            categories['blog'].append(filename)
        elif filename in ['contact.html', 'privacybeleid.html', 'algemene-voorwaarden.html']:
            categories['legal'].append(filename)
        else:
            categories['other'].append(filename)
    
    return categories, len(html_files)

def check_css_structure():
    """Vérifie la structure CSS"""
    css_files = glob.glob("/Users/marc/Desktop/kastelenbelgie/css/*.css")
    return len(css_files), css_files

def check_js_structure():
    """Vérifie la structure JavaScript"""
    js_files = glob.glob("/Users/marc/Desktop/kastelenbelgie/js/*.js")
    return len(js_files), js_files

def check_images_structure():
    """Vérifie la structure des images"""
    images_dir = "/Users/marc/Desktop/kastelenbelgie/chateaux_images_update-2"
    if os.path.exists(images_dir):
        images = glob.glob(f"{images_dir}/*.jpg")
        return len(images), True
    return 0, False

def check_search_functionality():
    """Vérifie que la recherche est implémentée"""
    search_js = "/Users/marc/Desktop/kastelenbelgie/js/search.js"
    if not os.path.exists(search_js):
        return False, "Fichier search.js manquant"
    
    # Vérifier quelques pages pour le script
    test_files = ['index.html', 'provinces.html', 'contact.html']
    pages_with_search = 0
    
    for filename in test_files:
        filepath = f"/Users/marc/Desktop/kastelenbelgie/{filename}"
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                if 'js/search.js' in content:
                    pages_with_search += 1
    
    return pages_with_search == len(test_files), f"{pages_with_search}/{len(test_files)} pages testées"

def main():
    """Fonction principale"""
    print("🏰 RAPPORT FINAL - KASTELENBELGIE.BE")
    print("=" * 60)
    
    # 1. Fichiers essentiels
    print("\n📄 FICHIERS ESSENTIELS:")
    essential_files = [
        ("/Users/marc/Desktop/kastelenbelgie/index.html", "Homepage"),
        ("/Users/marc/Desktop/kastelenbelgie/provinces.html", "Page provinces"),
        ("/Users/marc/Desktop/kastelenbelgie/contact.html", "Page contact"),
        ("/Users/marc/Desktop/kastelenbelgie/blog.html", "Page blog"),
        ("/Users/marc/Desktop/kastelenbelgie/css/modern-style.css", "CSS principal"),
        ("/Users/marc/Desktop/kastelenbelgie/js/search.js", "JavaScript recherche"),
        ("/Users/marc/Desktop/kastelenbelgie/favicon.svg", "Favicon")
    ]
    
    essential_count = 0
    for filepath, description in essential_files:
        if check_file_exists(filepath, description):
            essential_count += 1
    
    # 2. Analyse des pages HTML
    print(f"\n📊 ANALYSE DES PAGES HTML:")
    categories, total_html = analyze_html_files()
    
    print(f"  📈 Total pages HTML: {total_html}")
    for category, files in categories.items():
        if files:
            print(f"    • {category.title()}: {len(files)} pages")
            if category == 'castles' and len(files) > 0:
                print(f"      Exemples: {', '.join(files[:3])}{'...' if len(files) > 3 else ''}")
    
    # 3. Structure des assets
    print(f"\n🎨 ASSETS ET RESSOURCES:")
    css_count, css_files = check_css_structure()
    js_count, js_files = check_js_structure()
    images_count, images_exist = check_images_structure()
    
    print(f"  ✅ CSS: {css_count} fichiers")
    for css_file in css_files:
        print(f"    • {os.path.basename(css_file)}")
    
    print(f"  ✅ JavaScript: {js_count} fichiers")
    for js_file in js_files:
        print(f"    • {os.path.basename(js_file)}")
    
    if images_exist:
        print(f"  ✅ Images: {images_count} images de châteaux")
    else:
        print(f"  ⚠️  Images: Dossier d'images non trouvé")
    
    # 4. Fonctionnalités
    print(f"\n⚙️  FONCTIONNALITÉS:")
    search_ok, search_details = check_search_functionality()
    search_status = "✅" if search_ok else "❌"
    print(f"  {search_status} Recherche: {search_details}")
    
    # 5. Pages légales
    print(f"\n📋 PAGES LÉGALES:")
    legal_pages = ['privacybeleid.html', 'algemene-voorwaarden.html']
    legal_count = 0
    for page in legal_pages:
        if check_file_exists(f"/Users/marc/Desktop/kastelenbelgie/{page}", page.replace('.html', '').title()):
            legal_count += 1
    
    # 6. Résumé final
    print(f"\n🎯 RÉSUMÉ FINAL:")
    print(f"  📄 Pages HTML créées: {total_html}")
    print(f"  🏰 Pages châteaux: {len(categories['castles'])}")
    print(f"  🏛️  Pages provinces: {len(categories['provinces'])}")
    print(f"  📝 Articles blog: {len(categories['blog'])}")
    print(f"  ⚖️  Pages légales: {legal_count}/2")
    print(f"  🔧 Fichiers essentiels: {essential_count}/{len(essential_files)}")
    
    # 7. Statut global
    print(f"\n🚀 STATUT GLOBAL:")
    if essential_count == len(essential_files) and search_ok and legal_count == 2:
        print("  ✅ SITE COMPLET ET FONCTIONNEL!")
        print("  🎉 Prêt pour la mise en ligne")
    else:
        print("  ⚠️  Quelques éléments à vérifier")
        if essential_count < len(essential_files):
            print("    • Fichiers essentiels manquants")
        if not search_ok:
            print("    • Fonctionnalité de recherche à corriger")
        if legal_count < 2:
            print("    • Pages légales incomplètes")
    
    print(f"\n📅 Rapport généré le: {os.popen('date').read().strip()}")
    print("=" * 60)

if __name__ == "__main__":
    main()
