#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
VÉRIFICATION FINALE DU SITE
Vérifie que tous les éléments sont en place et fonctionnels
"""

import os
import glob
import re
from collections import defaultdict

def check_castle_pages():
    """Vérifie les pages châteaux"""
    castle_files = []
    patterns = ['kasteel-*.html', 'chateau-*.html', 'citadel-*.html', 'burcht-*.html']
    for pattern in patterns:
        castle_files.extend(glob.glob(f"/Users/marc/Desktop/kastelenbelgie/{pattern}"))
    
    print(f"🏰 PAGES CHÂTEAUX: {len(castle_files)} trouvées")
    
    # Vérifier les éléments essentiels
    issues = []
    complete_pages = 0
    
    for filepath in castle_files:
        filename = os.path.basename(filepath)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Vérifications
            has_title = '<title>' in content
            has_meta_desc = 'meta name="description"' in content
            has_breadcrumbs = 'breadcrumbs' in content
            has_hero = 'castle-hero' in content
            has_intro = 'castle-intro' in content
            has_activities = 'castle-activities' in content
            has_related = 'related-castles' in content
            has_map = 'castle-map' in content or 'google-map' in content
            has_footer = 'footer' in content
            has_search = 'search-input' in content
            
            elements_count = sum([has_title, has_meta_desc, has_breadcrumbs, has_hero, 
                                has_intro, has_activities, has_related, has_map, 
                                has_footer, has_search])
            
            if elements_count >= 8:
                complete_pages += 1
            else:
                issues.append(f"  ⚠️ {filename}: {elements_count}/10 éléments")
                
        except Exception as e:
            issues.append(f"  ❌ {filename}: Erreur lecture - {e}")
    
    print(f"  ✅ Pages complètes: {complete_pages}/{len(castle_files)}")
    if issues:
        print("  Issues détectées:")
        for issue in issues[:5]:  # Limiter à 5 pour éviter le spam
            print(issue)
    
    return len(castle_files), complete_pages

def check_essential_files():
    """Vérifie les fichiers essentiels"""
    essential_files = [
        "index.html",
        "contact.html", 
        "blog.html",
        "provinces.html",
        "css/modern-style.css",
        "js/search.js",
        "favicon.svg"
    ]
    
    print(f"\n📄 FICHIERS ESSENTIELS:")
    missing = []
    
    for file in essential_files:
        filepath = f"/Users/marc/Desktop/kastelenbelgie/{file}"
        if os.path.exists(filepath):
            print(f"  ✅ {file}")
        else:
            print(f"  ❌ {file}")
            missing.append(file)
    
    return len(essential_files) - len(missing), len(essential_files)

def check_province_pages():
    """Vérifie les pages provinces"""
    provinces = [
        "antwerpen.html", "limburg.html", "oost-vlaanderen.html", 
        "west-vlaanderen.html", "vlaams-brabant.html", "namen.html",
        "luxemburg.html", "luik.html", "henegouwen.html", "waals-brabant.html"
    ]
    
    print(f"\n🗺️ PAGES PROVINCES:")
    existing = 0
    
    for province in provinces:
        filepath = f"/Users/marc/Desktop/kastelenbelgie/{province}"
        if os.path.exists(filepath):
            print(f"  ✅ {province}")
            existing += 1
        else:
            print(f"  ❌ {province}")
    
    return existing, len(provinces)

def check_scripts():
    """Vérifie les scripts créés"""
    scripts = [
        "create_all_castles_final.py",
        "improve_wikipedia_scraping.py",
        "add_related_castles.py", 
        "add_google_maps.py",
        "fix_contact_form.py",
        "generate_all_remaining_castles.py",
        "replace_maps_api_key.py"
    ]
    
    print(f"\n🛠️ SCRIPTS CRÉÉS:")
    existing = 0
    
    for script in scripts:
        filepath = f"/Users/marc/Desktop/kastelenbelgie/{script}"
        if os.path.exists(filepath):
            print(f"  ✅ {script}")
            existing += 1
        else:
            print(f"  ❌ {script}")
    
    return existing, len(scripts)

def check_css_completeness():
    """Vérifie la complétude du CSS"""
    css_file = "/Users/marc/Desktop/kastelenbelgie/css/modern-style.css"
    
    print(f"\n🎨 CSS MODERNE:")
    
    if not os.path.exists(css_file):
        print("  ❌ Fichier CSS non trouvé")
        return 0, 10
    
    try:
        with open(css_file, 'r', encoding='utf-8') as f:
            css_content = f.read()
        
        # Vérifier les sections importantes
        sections = [
            "castle-hero",
            "castle-intro", 
            "castle-activities",
            "related-castles",
            "castle-map",
            "Google Maps Integration",
            "card-description",
            "activities-grid",
            "reservation-form",
            "footer"
        ]
        
        found_sections = 0
        for section in sections:
            if section in css_content:
                print(f"  ✅ {section}")
                found_sections += 1
            else:
                print(f"  ❌ {section}")
        
        return found_sections, len(sections)
        
    except Exception as e:
        print(f"  ❌ Erreur lecture CSS: {e}")
        return 0, 10

def check_search_functionality():
    """Vérifie la fonctionnalité de recherche"""
    search_js = "/Users/marc/Desktop/kastelenbelgie/js/search.js"
    
    print(f"\n🔍 FONCTIONNALITÉ RECHERCHE:")
    
    if not os.path.exists(search_js):
        print("  ❌ Fichier search.js non trouvé")
        return False
    
    try:
        with open(search_js, 'r', encoding='utf-8') as f:
            js_content = f.read()
        
        # Vérifier les éléments clés
        has_castles_array = 'const castles' in js_content or 'var castles' in js_content
        has_search_function = 'function' in js_content and 'search' in js_content
        has_event_listener = 'addEventListener' in js_content
        
        if has_castles_array and has_search_function and has_event_listener:
            print("  ✅ Recherche fonctionnelle")
            return True
        else:
            print("  ⚠️ Recherche incomplète")
            return False
            
    except Exception as e:
        print(f"  ❌ Erreur lecture JS: {e}")
        return False

def generate_final_score():
    """Génère le score final"""
    print("\n" + "="*70)
    print("📊 SCORE FINAL DE COMPLETION")
    print("="*70)
    
    # Vérifications
    castles_total, castles_complete = check_castle_pages()
    essential_ok, essential_total = check_essential_files()
    provinces_ok, provinces_total = check_province_pages()
    scripts_ok, scripts_total = check_scripts()
    css_ok, css_total = check_css_completeness()
    search_ok = check_search_functionality()
    
    # Calcul du score
    scores = [
        (castles_complete / castles_total * 100, "Pages châteaux"),
        (essential_ok / essential_total * 100, "Fichiers essentiels"),
        (provinces_ok / provinces_total * 100, "Pages provinces"),
        (scripts_ok / scripts_total * 100, "Scripts créés"),
        (css_ok / css_total * 100, "CSS complet"),
        (100 if search_ok else 0, "Recherche fonctionnelle")
    ]
    
    total_score = sum(score for score, _ in scores) / len(scores)
    
    print(f"\n📈 DÉTAIL DES SCORES:")
    for score, category in scores:
        status = "✅" if score >= 80 else "⚠️" if score >= 60 else "❌"
        print(f"  {status} {category}: {score:.1f}%")
    
    print(f"\n🏆 SCORE GLOBAL: {total_score:.1f}%")
    
    if total_score >= 90:
        print("🎉 EXCELLENT! Le site est prêt pour la production")
    elif total_score >= 75:
        print("👍 BIEN! Quelques ajustements mineurs nécessaires")
    elif total_score >= 60:
        print("⚠️ MOYEN! Des améliorations importantes sont nécessaires")
    else:
        print("❌ INSUFFISANT! Beaucoup de travail reste à faire")
    
    return total_score

def main():
    """Fonction principale"""
    print("🔍 VÉRIFICATION FINALE DU SITE KASTELENBELGIE.BE")
    print("=" * 70)
    
    score = generate_final_score()
    
    print(f"\n📋 RECOMMANDATIONS:")
    if score < 100:
        print("  • Compléter les éléments manquants identifiés ci-dessus")
        print("  • Tester toutes les fonctionnalités manuellement")
        print("  • Configurer la clé API Google Maps")
        print("  • Ajouter de vraies images de châteaux")
        print("  • Vérifier les liens internes")
    
    print(f"\n✨ Le site a un score de {score:.1f}% de completion!")

if __name__ == "__main__":
    main()
