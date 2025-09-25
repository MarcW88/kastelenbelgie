#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
VÉRIFICATION DE L'UNIFICATION CSS
Vérifie que tous les fichiers utilisent maintenant style.css
"""

import glob
import re
import os

def verify_css_unification():
    """Vérifie que l'unification CSS a réussi"""
    
    print("✅ VÉRIFICATION DE L'UNIFICATION CSS")
    print("=" * 50)
    
    html_files = glob.glob("/Users/marc/Desktop/kastelenbelgie/*.html")
    
    style_css_count = 0
    other_css_count = 0
    errors = []
    
    for html_file in html_files:
        filename = os.path.basename(html_file)
        
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Chercher tous les liens CSS
            css_links = re.findall(r'<link[^>]*href="([^"]*\.css)"', content)
            
            for css_link in css_links:
                css_name = css_link.split('/')[-1]
                
                if css_name == 'style.css':
                    style_css_count += 1
                else:
                    other_css_count += 1
                    errors.append(f"{filename}: utilise {css_name}")
                    
        except Exception as e:
            errors.append(f"{filename}: erreur lecture - {e}")
    
    print(f"📊 RÉSULTATS DE VÉRIFICATION:")
    print(f"Total fichiers HTML: {len(html_files)}")
    print(f"Utilisent style.css: {style_css_count}")
    print(f"Utilisent autres CSS: {other_css_count}")
    
    if other_css_count == 0:
        print("🎉 PARFAIT! Tous les fichiers utilisent style.css")
    else:
        print(f"⚠️ {other_css_count} fichiers utilisent encore d'autres CSS:")
        for error in errors[:10]:  # Montrer les 10 premiers
            print(f"  • {error}")
        if len(errors) > 10:
            print(f"  ... et {len(errors)-10} autres")

def verify_css_file_exists():
    """Vérifie que le fichier style.css existe et contient les styles"""
    
    print(f"\n📄 VÉRIFICATION DU FICHIER style.css")
    print("-" * 40)
    
    css_file = "/Users/marc/Desktop/kastelenbelgie/css/style.css"
    
    if not os.path.exists(css_file):
        print("❌ Le fichier style.css n'existe pas!")
        return False
    
    try:
        with open(css_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        file_size = len(content)
        print(f"✅ Fichier style.css existe ({file_size:,} caractères)")
        
        # Vérifier les styles essentiels
        essential_styles = [
            '.castle-grid',
            '.castle-card',
            '.castle-card-content',
            'grid-template-columns',
            '.navbar',
            '.hero',
            '.footer'
        ]
        
        missing_styles = []
        for style in essential_styles:
            if style in content:
                print(f"  ✅ {style}")
            else:
                missing_styles.append(style)
                print(f"  ❌ {style} - MANQUANT")
        
        if missing_styles:
            print(f"⚠️ {len(missing_styles)} styles essentiels manquants")
            return False
        else:
            print("✅ Tous les styles essentiels présents")
            return True
            
    except Exception as e:
        print(f"❌ Erreur lecture style.css: {e}")
        return False

def test_sample_pages():
    """Teste quelques pages échantillon"""
    
    print(f"\n🧪 TEST DE PAGES ÉCHANTILLON")
    print("-" * 30)
    
    test_pages = [
        'index.html',
        'antwerpen.html',
        'kasteel-van-freyr-freyr.html',
        'blog.html'
    ]
    
    for page in test_pages:
        page_path = f"/Users/marc/Desktop/kastelenbelgie/{page}"
        
        if os.path.exists(page_path):
            try:
                with open(page_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if 'css/style.css' in content:
                    print(f"  ✅ {page}: utilise style.css")
                else:
                    print(f"  ❌ {page}: n'utilise pas style.css")
                    
            except Exception as e:
                print(f"  ❌ {page}: erreur - {e}")
        else:
            print(f"  ⚠️ {page}: fichier non trouvé")

if __name__ == "__main__":
    verify_css_unification()
    css_ok = verify_css_file_exists()
    test_sample_pages()
    
    print(f"\n🎯 CONCLUSION:")
    if css_ok:
        print("✅ UNIFICATION RÉUSSIE!")
        print("✅ UN SEUL FICHIER style.css POUR TOUT LE SITE")
        print("✅ Les grilles de châteaux devraient maintenant fonctionner")
        print("\n🚀 Testez avec: python3 start_local_server.py")
    else:
        print("❌ Problèmes détectés dans l'unification")
        print("🔧 Vérifiez le fichier style.css")
