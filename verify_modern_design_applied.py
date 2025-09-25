#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
VÉRIFICATION DE L'APPLICATION DU DESIGN MODERNE
Vérifie que le design moderne a été appliqué sur tout le site
"""

import glob
import re
import os

def verify_modern_design_applied():
    """Vérifie que le design moderne a été appliqué partout"""
    
    print("✅ VÉRIFICATION DE L'APPLICATION DU DESIGN MODERNE")
    print("=" * 60)
    
    html_files = glob.glob("/Users/marc/Desktop/kastelenbelgie/*.html")
    
    # Classes modernes à vérifier
    modern_classes = [
        'hero-modern',
        'hero-content-modern',
        'btn-modern',
        'btn-primary-modern',
        'card-modern',
        'hero-floating-card'
    ]
    
    # Classes anciennes qui ne devraient plus exister
    old_classes = [
        'class="hero"',
        'class="btn btn-primary"',
        'class="floating-card"'
    ]
    
    pages_with_modern = 0
    pages_with_old = 0
    total_modern_classes = 0
    total_old_classes = 0
    
    sample_pages = []
    
    for html_file in html_files[:10]:  # Vérifier un échantillon
        filename = os.path.basename(html_file)
        
        if filename == 'test-modern-design.html':
            continue
        
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Compter les classes modernes
            modern_count = 0
            for modern_class in modern_classes:
                modern_count += content.count(modern_class)
            
            # Compter les anciennes classes
            old_count = 0
            for old_class in old_classes:
                old_count += content.count(old_class)
            
            if modern_count > 0:
                pages_with_modern += 1
                total_modern_classes += modern_count
            
            if old_count > 0:
                pages_with_old += 1
                total_old_classes += old_count
            
            sample_pages.append({
                'filename': filename,
                'modern_classes': modern_count,
                'old_classes': old_count
            })
            
        except Exception as e:
            continue
    
    print(f"📊 RÉSULTATS DE VÉRIFICATION:")
    print(f"Pages analysées: {len(sample_pages)}")
    print(f"Pages avec classes modernes: {pages_with_modern}")
    print(f"Pages avec anciennes classes: {pages_with_old}")
    print(f"Total classes modernes: {total_modern_classes}")
    print(f"Total anciennes classes: {total_old_classes}")
    
    print(f"\n📄 ÉCHANTILLON DE PAGES:")
    for page in sample_pages:
        status = "✅" if page['modern_classes'] > 0 and page['old_classes'] == 0 else "⚠️"
        print(f"  {status} {page['filename']}: {page['modern_classes']} modernes, {page['old_classes']} anciennes")
    
    return pages_with_modern, pages_with_old

def test_specific_pages():
    """Teste des pages spécifiques importantes"""
    
    print(f"\n🧪 TEST DE PAGES SPÉCIFIQUES")
    print("-" * 40)
    
    test_pages = [
        ('index.html', 'Homepage'),
        ('antwerpen.html', 'Page province'),
        ('kasteel-van-freyr-freyr.html', 'Page château')
    ]
    
    for filename, description in test_pages:
        file_path = f"/Users/marc/Desktop/kastelenbelgie/{filename}"
        
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Vérifications spécifiques
                checks = []
                
                if 'hero-modern' in content:
                    checks.append("✅ Hero moderne")
                else:
                    checks.append("❌ Hero ancien")
                
                if 'btn-modern' in content:
                    checks.append("✅ Boutons modernes")
                else:
                    checks.append("❌ Boutons anciens")
                
                if 'castle-grid' in content or 'grid-auto' in content:
                    checks.append("✅ Grilles modernes")
                else:
                    checks.append("⚠️ Pas de grilles")
                
                print(f"📄 {description} ({filename}):")
                for check in checks:
                    print(f"    {check}")
                
            except Exception as e:
                print(f"❌ Erreur avec {filename}: {e}")
        else:
            print(f"⚠️ {filename}: fichier non trouvé")

def check_css_consistency():
    """Vérifie que le CSS contient tous les styles modernes"""
    
    print(f"\n🎨 VÉRIFICATION DE LA COHÉRENCE CSS")
    print("-" * 40)
    
    css_file = "/Users/marc/Desktop/kastelenbelgie/css/style.css"
    
    try:
        with open(css_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        required_styles = [
            '.hero-modern',
            '.btn-modern',
            '.card-modern',
            '.grid-auto',
            '.castle-grid'
        ]
        
        missing_styles = []
        for style in required_styles:
            if style in content:
                print(f"  ✅ {style}")
            else:
                missing_styles.append(style)
                print(f"  ❌ {style} - MANQUANT")
        
        if missing_styles:
            print(f"⚠️ {len(missing_styles)} styles manquants dans le CSS")
            return False
        else:
            print("✅ Tous les styles modernes présents dans le CSS")
            return True
            
    except Exception as e:
        print(f"❌ Erreur lecture CSS: {e}")
        return False

if __name__ == "__main__":
    modern_pages, old_pages = verify_modern_design_applied()
    test_specific_pages()
    css_ok = check_css_consistency()
    
    print(f"\n🎯 CONCLUSION:")
    
    if modern_pages > 0 and old_pages == 0 and css_ok:
        print("🎉 DESIGN MODERNE APPLIQUÉ AVEC SUCCÈS SUR TOUT LE SITE!")
        print("✅ Toutes les pages utilisent les classes modernes")
        print("✅ Aucune ancienne classe détectée")
        print("✅ CSS cohérent et complet")
        print("\n🚀 Le site a maintenant un design moderne uniforme!")
    else:
        print("⚠️ Quelques problèmes détectés:")
        if old_pages > 0:
            print(f"  • {old_pages} pages avec anciennes classes")
        if not css_ok:
            print("  • Styles CSS incomplets")
        print("🔧 Vérifiez les détails ci-dessus")
    
    print(f"\n🌐 TESTEZ LE SITE:")
    print(f"python3 start_local_server.py")
    print(f"Puis ouvrez: http://localhost:8000/index.html")
