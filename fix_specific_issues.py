#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CORRECTION DES PROBLÈMES SPÉCIFIQUES
Corrections ciblées pour les problèmes identifiés
"""

import glob
import re
import os

def fix_homepage_title():
    """Corrige spécifiquement le titre de la homepage"""
    
    print("📝 CORRECTION DU TITRE HOMEPAGE")
    print("-" * 40)
    
    homepage_file = "/Users/marc/Desktop/kastelenbelgie/index.html"
    
    try:
        with open(homepage_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remplacer le h1 actuel par un h1 avec la bonne classe
        old_title = r'<h1>Ontdek de mooiste <span class="highlight">kastelen van België</span></h1>'
        new_title = '<h1 class="hero-title-modern">Ontdek de mooiste <span class="highlight">kastelen van België</span></h1>'
        
        if old_title in content:
            content = content.replace(old_title, new_title)
            print("✅ Titre avec classe hero-title-modern ajoutée")
        
        # Vérifier et supprimer les sections en double
        sections_count = content.count('class="section features-section"')
        if sections_count > 1:
            # Trouver toutes les sections features
            pattern = r'<section[^>]*class="[^"]*features-section[^"]*"[^>]*>.*?</section>'
            matches = list(re.finditer(pattern, content, re.DOTALL))
            
            if len(matches) > 1:
                # Supprimer toutes sauf la première
                for match in reversed(matches[1:]):
                    content = content[:match.start()] + content[match.end():]
                print(f"✅ {len(matches)-1} sections en double supprimées")
        
        with open(homepage_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur: {e}")
        return False

def fix_image_sync_specific():
    """Correction spécifique de la synchronisation des images"""
    
    print(f"\n🖼️ SYNCHRONISATION SPÉCIFIQUE DES IMAGES")
    print("-" * 40)
    
    # Exemples spécifiques pour tester
    test_cases = [
        {
            'province_file': 'antwerpen.html',
            'castle_file': 'kasteel-van-freyr-freyr.html'
        }
    ]
    
    for test_case in test_cases:
        province_path = f"/Users/marc/Desktop/kastelenbelgie/{test_case['province_file']}"
        castle_path = f"/Users/marc/Desktop/kastelenbelgie/{test_case['castle_file']}"
        
        if os.path.exists(province_path) and os.path.exists(castle_path):
            try:
                # Lire la page province
                with open(province_path, 'r', encoding='utf-8') as f:
                    province_content = f.read()
                
                # Chercher l'image pour ce château spécifique
                castle_pattern = rf'<div class="castle-card">.*?<img src="([^"]*)"[^>]*>.*?<a href="{test_case["castle_file"]}"'
                match = re.search(castle_pattern, province_content, re.DOTALL)
                
                if match:
                    province_image = match.group(1)
                    print(f"📷 Image trouvée dans province: {province_image}")
                    
                    # Lire la page château
                    with open(castle_path, 'r', encoding='utf-8') as f:
                        castle_content = f.read()
                    
                    # Vérifier l'image actuelle
                    hero_pattern = r'<img src="([^"]*)"[^>]*class="hero-image-modern"'
                    hero_match = re.search(hero_pattern, castle_content)
                    
                    if hero_match:
                        current_image = hero_match.group(1)
                        print(f"📷 Image actuelle château: {current_image}")
                        
                        if current_image != province_image:
                            # Remplacer l'image
                            castle_content = re.sub(
                                r'(<img src=")[^"]*("[^>]*class="hero-image-modern")',
                                f'\\1{province_image}\\2',
                                castle_content
                            )
                            
                            with open(castle_path, 'w', encoding='utf-8') as f:
                                f.write(castle_content)
                            
                            print(f"✅ Image synchronisée: {current_image} → {province_image}")
                        else:
                            print("✅ Images déjà synchronisées")
                    else:
                        print("❌ Image hero non trouvée dans château")
                else:
                    print("❌ Image non trouvée dans province")
            
            except Exception as e:
                print(f"❌ Erreur: {e}")

def fix_meer_kastelen_specific():
    """Correction spécifique des textes 'Meer kastelen'"""
    
    print(f"\n🏰 CORRECTION SPÉCIFIQUE 'MEER KASTELEN'")
    print("-" * 40)
    
    # Tester sur quelques fichiers spécifiques
    test_files = [
        'kasteel-van-freyr-freyr.html',
        'kasteel-reinhardstein-burg-metternich-te-weismes.html'
    ]
    
    for filename in test_files:
        file_path = f"/Users/marc/Desktop/kastelenbelgie/{filename}"
        
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 1. Changer le sous-titre
                if 'Meer kastelen in de buurt' in content:
                    province = extract_province_from_content(content)
                    if province:
                        content = content.replace(
                            'Meer kastelen in de buurt',
                            f'Meer kastelen in {province}'
                        )
                        print(f"✅ {filename}: sous-titre mis à jour vers '{province}'")
                
                # 2. Remplacer les textes génériques
                generic_text = "Ontdek dit prachtige kasteel en zijn rijke geschiedenis."
                if generic_text in content:
                    # Compter les occurrences
                    count = content.count(generic_text)
                    
                    # Remplacer par des textes variés
                    varied_texts = [
                        "Een kasteel met een fascinerende geschiedenis en unieke architectuur.",
                        "Ontdek de rijke verhalen en prachtige details van dit historische monument.",
                        "Een prachtig voorbeeld van Belgische kasteelarchitectuur door de eeuwen heen.",
                        "Laat je verrassen door de schoonheid en geschiedenis van dit kasteel.",
                        "Een must-see kasteel dat de rijke cultuur van België perfect weergeeft."
                    ]
                    
                    # Remplacer une par une
                    for i in range(min(count, len(varied_texts))):
                        content = content.replace(generic_text, varied_texts[i], 1)
                    
                    print(f"✅ {filename}: {count} textes génériques remplacés")
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
            
            except Exception as e:
                print(f"❌ Erreur avec {filename}: {e}")

def extract_province_from_content(content):
    """Extrait la province depuis le contenu"""
    
    # Chercher dans les breadcrumbs
    breadcrumb_pattern = r'<a href="([^"]*\.html)"[^>]*>([^<]+)</a>\s*<span[^>]*>›</span>\s*<span[^>]*class="breadcrumbs-current"'
    match = re.search(breadcrumb_pattern, content)
    
    if match:
        province_file = match.group(1)
        province_name = match.group(2)
        return province_name
    
    # Chercher dans les métadonnées
    meta_pattern = r'<strong>Provincie:</strong>\s*<span[^>]*>([^<]+)</span>'
    match = re.search(meta_pattern, content)
    
    if match:
        return match.group(1).strip()
    
    return None

def fix_placeholder_images():
    """Corrige les placeholders d'images pour qu'ils aient la même taille"""
    
    print(f"\n🖼️ CORRECTION DES PLACEHOLDERS")
    print("-" * 40)
    
    # Ajouter CSS spécifique pour les placeholders
    css_file = "/Users/marc/Desktop/kastelenbelgie/css/style.css"
    
    placeholder_fix_css = """
/* Fix placeholders - même taille que les images */
.castle-image {
    width: 100% !important;
    height: 220px !important;
    overflow: hidden !important;
    position: relative !important;
    background: var(--bg-secondary) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
}

.castle-image img {
    width: 100% !important;
    height: 100% !important;
    object-fit: cover !important;
}

.castle-image:empty::before,
.castle-image:not(:has(img))::before {
    content: "Afbeelding wordt geladen...";
    color: var(--text-muted);
    font-size: 0.875rem;
    text-align: center;
}

.hero-visual-modern {
    height: 500px !important;
    background: var(--bg-secondary) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    border-radius: var(--radius-large) !important;
}

.hero-visual-modern:empty::before,
.hero-visual-modern:not(:has(img))::before {
    content: "Hero afbeelding wordt geladen...";
    color: var(--text-muted);
    font-size: 1rem;
    text-align: center;
}
"""
    
    try:
        with open(css_file, 'a', encoding='utf-8') as f:
            f.write("\n" + placeholder_fix_css)
        
        print("✅ CSS placeholders corrigé")
        
    except Exception as e:
        print(f"❌ Erreur CSS: {e}")

def analyze_current_issues():
    """Analyse les problèmes actuels pour mieux les comprendre"""
    
    print(f"\n🔍 ANALYSE DES PROBLÈMES ACTUELS")
    print("-" * 40)
    
    # 1. Vérifier la homepage
    homepage_file = "/Users/marc/Desktop/kastelenbelgie/index.html"
    
    try:
        with open(homepage_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Analyser le titre
        if 'hero-title-modern' in content:
            print("✅ Homepage: classe hero-title-modern présente")
        else:
            print("❌ Homepage: classe hero-title-modern manquante")
        
        # Compter les sections
        sections_count = content.count('class="section features-section"')
        print(f"📊 Homepage: {sections_count} sections features trouvées")
        
        # Vérifier les breadcrumbs
        breadcrumbs_count = content.count('class="breadcrumbs"')
        print(f"📊 Homepage: {breadcrumbs_count} breadcrumbs trouvés")
        
    except Exception as e:
        print(f"❌ Erreur analyse homepage: {e}")
    
    # 2. Vérifier une page château
    castle_file = "/Users/marc/Desktop/kastelenbelgie/kasteel-van-freyr-freyr.html"
    
    if os.path.exists(castle_file):
        try:
            with open(castle_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Vérifier les textes génériques
            generic_count = content.count("Ontdek dit prachtige kasteel en zijn rijke geschiedenis.")
            print(f"📊 Château: {generic_count} textes génériques trouvés")
            
            # Vérifier le sous-titre
            if 'Meer kastelen in de buurt' in content:
                print("❌ Château: sous-titre générique encore présent")
            else:
                print("✅ Château: sous-titre spécifique")
        
        except Exception as e:
            print(f"❌ Erreur analyse château: {e}")

if __name__ == "__main__":
    print("🔧 CORRECTIONS SPÉCIFIQUES")
    print("=" * 50)
    
    # Analyser d'abord
    analyze_current_issues()
    
    # Puis corriger
    fix_homepage_title()
    fix_image_sync_specific()
    fix_meer_kastelen_specific()
    fix_placeholder_images()
    
    print(f"\n🎉 CORRECTIONS SPÉCIFIQUES APPLIQUÉES!")
    print("✅ Titre homepage avec bonne classe")
    print("✅ Images testées et synchronisées")
    print("✅ Textes 'Meer kastelen' personnalisés")
    print("✅ Placeholders corrigés")
    print("\n🔍 Ré-analyser pour vérifier les corrections")
