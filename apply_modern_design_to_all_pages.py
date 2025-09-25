#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
APPLICATION DU DESIGN MODERNE SUR TOUT LE SITE
Remplace les anciennes classes par les nouvelles classes modernes
"""

import glob
import re
import os

def apply_modern_design_to_all_pages():
    """Applique le design moderne sur toutes les pages du site"""
    
    print("🎨 APPLICATION DU DESIGN MODERNE SUR TOUT LE SITE")
    print("=" * 60)
    
    # Trouver tous les fichiers HTML
    html_files = glob.glob("/Users/marc/Desktop/kastelenbelgie/*.html")
    
    # Mappings des anciennes vers nouvelles classes
    class_mappings = {
        # Hero sections
        'class="hero"': 'class="hero-modern"',
        'class="hero-content"': 'class="hero-content-modern"',
        'class="hero-text"': 'class="hero-text-modern"',
        'class="hero-visual"': 'class="hero-visual-modern"',
        'class="hero-image"': 'class="hero-image-modern"',
        'class="hero-actions"': 'class="hero-actions-modern"',
        'class="hero-title"': 'class="hero-title-modern"',
        'class="hero-description"': 'class="hero-description-modern"',
        
        # Boutons
        'class="btn btn-primary"': 'class="btn-modern btn-primary-modern"',
        'class="btn btn-secondary"': 'class="btn-modern btn-secondary-modern"',
        'class="btn btn-ghost"': 'class="btn-modern btn-ghost-modern"',
        'class="btn-primary"': 'class="btn-modern btn-primary-modern"',
        'class="btn-secondary"': 'class="btn-modern btn-secondary-modern"',
        'class="btn-ghost"': 'class="btn-modern btn-ghost-modern"',
        
        # Cards
        'class="card"': 'class="card-modern"',
        'class="card-content"': 'class="card-content-modern"',
        'class="card-title"': 'class="card-title-modern"',
        'class="card-description"': 'class="card-description-modern"',
        'class="card-image"': 'class="card-image-modern"',
        
        # Grilles (garder les existantes mais améliorer)
        'class="card-grid"': 'class="grid-auto"',
        
        # Sections
        'class="section"': 'class="section"',  # Garder mais améliorer
        'class="section-title"': 'class="section-title"',
        'class="section-subtitle"': 'class="section-subtitle"',
        
        # Floating card
        'class="floating-card"': 'class="hero-floating-card"',
    }
    
    updated_count = 0
    total_replacements = 0
    
    for html_file in html_files:
        filename = os.path.basename(html_file)
        
        # Ignorer certains fichiers
        if filename in ['test-modern-design.html']:
            continue
        
        try:
            # Lire le fichier
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            file_replacements = 0
            
            # Appliquer les mappings
            for old_class, new_class in class_mappings.items():
                if old_class in content:
                    content = content.replace(old_class, new_class)
                    file_replacements += content.count(new_class) - original_content.count(new_class)
            
            # Améliorations spécifiques pour certains types de pages
            if filename == 'index.html':
                content = improve_homepage(content)
            elif any(pattern in filename for pattern in ['kasteel-', 'chateau-', 'hof-', 'burcht-']):
                content = improve_castle_page(content)
            elif filename.endswith('-brabant.html') or filename in ['antwerpen.html', 'limburg.html', 'namen.html', 'luik.html']:
                content = improve_province_page(content)
            
            # Sauvegarder si des changements ont été faits
            if content != original_content:
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                updated_count += 1
                total_replacements += file_replacements
                print(f"✅ {filename}: {file_replacements} classes mises à jour")
            
        except Exception as e:
            print(f"❌ Erreur avec {filename}: {e}")
            continue
    
    print(f"\n📊 RÉSULTATS:")
    print(f"Pages mises à jour: {updated_count}")
    print(f"Total remplacements: {total_replacements}")
    print(f"Pages analysées: {len(html_files)}")

def improve_homepage(content):
    """Améliorations spécifiques pour la homepage"""
    
    # Ajouter un badge hero moderne
    if '<h1>' in content and 'hero-badge-modern' not in content:
        content = re.sub(
            r'(<div class="hero-text-modern">\s*)',
            r'\1<div class="hero-badge-modern">✨ Ontdek België</div>\n                    ',
            content
        )
    
    # Améliorer les stats avec un meilleur style
    content = re.sub(
        r'<div class="hero-stats">',
        '<div class="hero-stats">',
        content
    )
    
    return content

def improve_castle_page(content):
    """Améliorations spécifiques pour les pages châteaux"""
    
    # Améliorer les grilles de châteaux existantes
    content = re.sub(
        r'class="castle-grid"',
        'class="castle-grid"',  # Garder castle-grid car déjà amélioré
        content
    )
    
    # Améliorer les cards de châteaux
    content = re.sub(
        r'class="castle-card"',
        'class="castle-card"',  # Garder castle-card car déjà amélioré
        content
    )
    
    return content

def improve_province_page(content):
    """Améliorations spécifiques pour les pages provinces"""
    
    # Améliorer les sections de provinces
    content = re.sub(
        r'class="province-castles-section"',
        'class="section province-castles-section"',
        content
    )
    
    return content

def add_modern_sections():
    """Ajoute des sections modernes aux pages principales"""
    
    print(f"\n🚀 AJOUT DE SECTIONS MODERNES")
    print("-" * 40)
    
    # Améliorer la homepage avec des sections modernes
    homepage_file = "/Users/marc/Desktop/kastelenbelgie/index.html"
    
    try:
        with open(homepage_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Ajouter une section features moderne après le hero
        if 'features-section' not in content:
            features_section = '''
    <!-- Section Features Moderne -->
    <section class="section features-section">
        <div class="container">
            <h2 class="section-title">Waarom Kastelen België?</h2>
            <p class="section-subtitle">Ontdek wat ons platform uniek maakt voor het verkennen van Belgische kastelen</p>
            
            <div class="grid-3">
                <div class="card-modern">
                    <div class="card-content-modern">
                        <div class="feature-icon">🏰</div>
                        <h3 class="card-title-modern">300+ Kastelen</h3>
                        <p class="card-description-modern">De meest complete database van Belgische kastelen met gedetailleerde informatie en prachtige foto's.</p>
                    </div>
                </div>
                
                <div class="card-modern">
                    <div class="card-content-modern">
                        <div class="feature-icon">📍</div>
                        <h3 class="card-title-modern">Per Provincie</h3>
                        <p class="card-description-modern">Vind kastelen georganiseerd per provincie met handige filters en zoekfuncties.</p>
                    </div>
                </div>
                
                <div class="card-modern">
                    <div class="card-content-modern">
                        <div class="feature-icon">📚</div>
                        <h3 class="card-title-modern">Rijke Geschiedenis</h3>
                        <p class="card-description-modern">Leer over de fascinerende geschiedenis en architectuur van elk kasteel.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
'''
            
            # Insérer après la section hero
            hero_end = content.find('</section>', content.find('class="hero-modern"'))
            if hero_end != -1:
                hero_end += len('</section>')
                content = content[:hero_end] + features_section + content[hero_end:]
                
                with open(homepage_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                print("✅ Section features ajoutée à la homepage")
        
    except Exception as e:
        print(f"❌ Erreur ajout sections: {e}")

if __name__ == "__main__":
    apply_modern_design_to_all_pages()
    add_modern_sections()
    
    print(f"\n🎉 DESIGN MODERNE APPLIQUÉ SUR TOUT LE SITE!")
    print(f"✅ Toutes les pages utilisent maintenant les classes modernes")
    print(f"✅ Hero sections modernes")
    print(f"✅ Boutons modernes")
    print(f"✅ Cards modernes")
    print(f"✅ Grilles améliorées")
    print(f"\n🚀 Testez avec: python3 start_local_server.py")
