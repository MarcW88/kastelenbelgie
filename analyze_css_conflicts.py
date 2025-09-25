#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ANALYSE COMPLÈTE DES CONFLITS CSS
Identifie tous les CSS utilisés et crée un plan d'unification
"""

import glob
import re
from collections import defaultdict

def analyze_css_usage():
    """Analyse l'utilisation des CSS sur tout le site"""
    
    print("🔍 ANALYSE COMPLÈTE DES CONFLITS CSS")
    print("=" * 60)
    
    html_files = glob.glob("/Users/marc/Desktop/kastelenbelgie/*.html")
    css_usage = defaultdict(list)
    
    for html_file in html_files:
        filename = html_file.split('/')[-1]
        
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Chercher les liens CSS
            css_links = re.findall(r'<link[^>]*href="([^"]*\.css)"', content)
            
            for css_link in css_links:
                css_name = css_link.split('/')[-1]
                css_usage[css_name].append(filename)
                
        except Exception as e:
            continue
    
    print("📊 UTILISATION DES CSS PAR FICHIER:")
    print("-" * 40)
    
    total_files = len(html_files)
    
    for css_name, files in css_usage.items():
        percentage = (len(files) / total_files) * 100
        print(f"{css_name}: {len(files)} pages ({percentage:.1f}%)")
        
        # Montrer quelques exemples
        if len(files) <= 5:
            for file in files:
                print(f"  • {file}")
        else:
            for file in files[:3]:
                print(f"  • {file}")
            print(f"  ... et {len(files)-3} autres")
        print()
    
    return css_usage

def identify_page_types():
    """Identifie les types de pages et leurs CSS"""
    
    print("🏷️ TYPES DE PAGES ET LEURS CSS:")
    print("-" * 40)
    
    page_types = {
        'Homepage': ['index.html'],
        'Pages provinces': ['antwerpen.html', 'limburg.html', 'oost-vlaanderen.html', 'west-vlaanderen.html'],
        'Pages châteaux': [],
        'Pages génériques': ['blog.html', 'contact.html', 'provinces.html', 'kastelen.html'],
        'Pages admin': ['login.html', 'register.html', 'dashboard.html', 'admin.html']
    }
    
    # Identifier les pages châteaux
    html_files = glob.glob("/Users/marc/Desktop/kastelenbelgie/*.html")
    for html_file in html_files:
        filename = html_file.split('/')[-1]
        if any(pattern in filename for pattern in ['kasteel-', 'chateau-', 'hof-', 'burcht-', 'citadel-']):
            page_types['Pages châteaux'].append(filename)
    
    # Analyser le CSS de chaque type
    for page_type, files in page_types.items():
        if not files:
            continue
            
        print(f"\n{page_type} ({len(files)} pages):")
        
        # Prendre le premier fichier comme exemple
        example_file = f"/Users/marc/Desktop/kastelenbelgie/{files[0]}"
        
        try:
            with open(example_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            css_links = re.findall(r'<link[^>]*href="([^"]*\.css)"', content)
            for css_link in css_links:
                css_name = css_link.split('/')[-1]
                print(f"  → {css_name}")
                
        except Exception as e:
            print(f"  → Erreur lecture: {e}")

def create_unification_plan():
    """Crée un plan d'unification CSS"""
    
    print("\n🎯 PLAN D'UNIFICATION CSS:")
    print("=" * 40)
    
    print("OBJECTIF: UN SEUL FICHIER style.css POUR TOUT LE SITE")
    print()
    print("ÉTAPES À SUIVRE:")
    print("1. Fusionner tous les CSS en un seul style.css")
    print("2. Remplacer tous les liens CSS par style.css")
    print("3. Résoudre les conflits de styles")
    print("4. Tester sur toutes les pages")
    print()
    print("FICHIERS CSS À FUSIONNER:")
    print("• unified-style.css")
    print("• modern-style.css") 
    print("• style.css (existant)")
    print("• style-new.css")

if __name__ == "__main__":
    css_usage = analyze_css_usage()
    identify_page_types()
    create_unification_plan()
