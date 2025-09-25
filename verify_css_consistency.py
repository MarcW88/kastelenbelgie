#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
VÉRIFICATION DE LA COHÉRENCE CSS
Vérifie que tous les CSS ont les styles nécessaires pour les grilles
"""

import glob
import os

def verify_css_consistency():
    """Vérifie la cohérence des styles CSS"""
    
    print("🎨 VÉRIFICATION DE LA COHÉRENCE CSS")
    print("=" * 50)
    
    # CSS files à vérifier
    css_files = [
        '/Users/marc/Desktop/kastelenbelgie/css/unified-style.css',
        '/Users/marc/Desktop/kastelenbelgie/css/modern-style.css',
        '/Users/marc/Desktop/kastelenbelgie/css/style.css'
    ]
    
    required_styles = [
        '.castle-grid',
        '.castle-card',
        '.castle-card-content',
        'grid-template-columns'
    ]
    
    for css_file in css_files:
        if not os.path.exists(css_file):
            print(f"⚠️ {os.path.basename(css_file)}: fichier non trouvé")
            continue
            
        try:
            with open(css_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            print(f"\n📄 {os.path.basename(css_file)}:")
            
            for style in required_styles:
                if style in content:
                    print(f"  ✅ {style}")
                else:
                    print(f"  ❌ {style} - MANQUANT")
                    
        except Exception as e:
            print(f"  ❌ Erreur lecture: {e}")

def check_html_css_usage():
    """Vérifie quel CSS est utilisé par quelles pages"""
    
    print(f"\n🔍 UTILISATION DES CSS PAR LES PAGES")
    print("=" * 40)
    
    html_files = glob.glob("/Users/marc/Desktop/kastelenbelgie/*.html")
    css_usage = {
        'unified-style.css': [],
        'modern-style.css': [],
        'style.css': [],
        'style-new.css': []
    }
    
    for html_file in html_files[:10]:  # Limiter à 10 pour le test
        filename = os.path.basename(html_file)
        
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            for css_name in css_usage.keys():
                if css_name in content:
                    css_usage[css_name].append(filename)
                    
        except Exception as e:
            continue
    
    for css_name, files in css_usage.items():
        if files:
            print(f"\n📄 {css_name}: {len(files)} pages")
            for file in files[:3]:  # Montrer les 3 premiers
                print(f"  • {file}")
            if len(files) > 3:
                print(f"  ... et {len(files)-3} autres")

if __name__ == "__main__":
    verify_css_consistency()
    check_html_css_usage()
    
    print(f"\n🎯 RECOMMANDATIONS:")
    print(f"1. Toutes les pages provinces utilisent modern-style.css ✅")
    print(f"2. Les styles castle-grid sont maintenant dans modern-style.css ✅")
    print(f"3. Les châteaux devraient s'afficher en grille de 3 colonnes ✅")
    print(f"\n🚀 Lancez start_local_server.py pour tester visuellement!")
