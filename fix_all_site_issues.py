#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CORRECTION COMPLÈTE DU SITE
Corrige tous les problèmes identifiés
"""

import glob
import re
import os
from pathlib import Path

def fix_homepage_title():
    """Ajoute un titre complet à la homepage"""
    
    print("📝 CORRECTION DU TITRE DE LA HOMEPAGE")
    print("-" * 40)
    
    homepage_file = "/Users/marc/Desktop/kastelenbelgie/index.html"
    
    try:
        with open(homepage_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remplacer le titre actuel par un titre plus complet
        if '<h1>Laat de <span class="highlight">reis beginnen</span></h1>' in content:
            new_title = '<h1>Ontdek de mooiste <span class="highlight">kastelen van België</span></h1>'
            content = content.replace(
                '<h1>Laat de <span class="highlight">reis beginnen</span></h1>',
                new_title
            )
            
            with open(homepage_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print("✅ Titre de la homepage mis à jour")
            return True
    
    except Exception as e:
        print(f"❌ Erreur correction titre: {e}")
        return False

def fix_province_assignment():
    """Corrige l'assignation des châteaux aux provinces"""
    
    print(f"\n🏛️ CORRECTION DES ASSIGNATIONS DE PROVINCES")
    print("-" * 40)
    
    # Corrections connues
    corrections = {
        'kasteel-van-braine-le-chateau-kasteelbrakel.html': {
            'old_province': 'Limburg',
            'new_province': 'Waals-Brabant',
            'new_province_file': 'waals-brabant.html'
        }
    }
    
    for filename, correction in corrections.items():
        file_path = f"/Users/marc/Desktop/kastelenbelgie/{filename}"
        
        if os.path.exists(file_path):
            try:
                # Corriger la page château
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Mettre à jour la province dans la page
                content = re.sub(
                    r'<strong>Provincie:</strong>\s*<span[^>]*>[^<]*</span>',
                    f'<strong>Provincie:</strong> <span class="province-name">{correction["new_province"]}</span>',
                    content
                )
                
                # Mettre à jour les breadcrumbs
                content = re.sub(
                    r'href="[^"]*\.html"[^>]*>[^<]*</a>(\s*<span[^>]*>›</span>)',
                    f'href="{correction["new_province_file"]}">{correction["new_province"]}</a>\\1',
                    content
                )
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                # Déplacer le château vers la bonne page province
                move_castle_to_correct_province(filename, correction)
                
                print(f"✅ {filename}: {correction['old_province']} → {correction['new_province']}")
                
            except Exception as e:
                print(f"❌ Erreur avec {filename}: {e}")

def move_castle_to_correct_province(castle_filename, correction):
    """Déplace un château vers la bonne page province"""
    
    old_province_file = get_province_filename(correction['old_province'])
    new_province_file = correction['new_province_file']
    
    # Retirer de l'ancienne province
    if old_province_file:
        remove_castle_from_province(castle_filename, old_province_file)
    
    # Ajouter à la nouvelle province
    add_castle_to_province(castle_filename, new_province_file)

def get_province_filename(province_name):
    """Convertit un nom de province en nom de fichier"""
    
    mappings = {
        'Limburg': 'limburg.html',
        'Waals-Brabant': 'waals-brabant.html',
        'Antwerpen': 'antwerpen.html',
        'Oost-Vlaanderen': 'oost-vlaanderen.html',
        'West-Vlaanderen': 'west-vlaanderen.html',
        'Vlaams-Brabant': 'vlaams-brabant.html',
        'Namen': 'namen.html',
        'Luik': 'luik.html',
        'Henegouwen': 'henegouwen.html',
        'Luxemburg': 'luxemburg.html',
        'Brussel': 'brussel.html'
    }
    
    return mappings.get(province_name)

def remove_castle_from_province(castle_filename, province_file):
    """Retire un château d'une page province"""
    
    file_path = f"/Users/marc/Desktop/kastelenbelgie/{province_file}"
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Chercher et supprimer la card du château
        castle_name_base = castle_filename.replace('.html', '')
        
        # Pattern pour trouver la card complète
        pattern = rf'<div class="castle-card">.*?href="{castle_filename}".*?</div>\s*</div>'
        content = re.sub(pattern, '', content, flags=re.DOTALL)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"  ➖ Retiré de {province_file}")
        
    except Exception as e:
        print(f"  ❌ Erreur retrait de {province_file}: {e}")

def add_castle_to_province(castle_filename, province_file):
    """Ajoute un château à une page province"""
    
    file_path = f"/Users/marc/Desktop/kastelenbelgie/{province_file}"
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Créer la card du château
        castle_card = create_castle_card_for_province(castle_filename)
        
        # Trouver où insérer la card (dans la grille)
        grid_pattern = r'(<div class="castle-grid">)'
        if re.search(grid_pattern, content):
            content = re.sub(
                grid_pattern,
                f'\\1\n{castle_card}',
                content
            )
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"  ➕ Ajouté à {province_file}")
        
    except Exception as e:
        print(f"  ❌ Erreur ajout à {province_file}: {e}")

def create_castle_card_for_province(castle_filename):
    """Crée une card de château pour une page province"""
    
    # Extraire les infos du château depuis sa page
    file_path = f"/Users/marc/Desktop/kastelenbelgie/{castle_filename}"
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extraire le nom
        title_match = re.search(r'<title>([^|]+)', content)
        castle_name = title_match.group(1).strip() if title_match else "Kasteel"
        
        # Extraire l'image
        img_match = re.search(r'<img[^>]*src="([^"]*)"[^>]*alt="[^"]*"[^>]*class="hero-image-modern"', content)
        image_src = img_match.group(1) if img_match else "assets/placeholder-castle.jpg"
        
        return f'''
                <div class="castle-card">
                    <div class="castle-image">
                        <img src="{image_src}" alt="{castle_name}" loading="lazy">
                    </div>
                    <div class="castle-card-content">
                        <h3>{castle_name}</h3>
                        <p class="card-description">Ontdek dit prachtige kasteel en zijn rijke geschiedenis.</p>
                        <a href="{castle_filename}" class="btn-modern btn-primary-modern">Meer info</a>
                    </div>
                </div>
        '''
        
    except Exception as e:
        return f'''
                <div class="castle-card">
                    <div class="castle-image">
                        <img src="assets/placeholder-castle.jpg" alt="Kasteel" loading="lazy">
                    </div>
                    <div class="castle-card-content">
                        <h3>Kasteel</h3>
                        <p class="card-description">Ontdek dit prachtige kasteel en zijn rijke geschiedenis.</p>
                        <a href="{castle_filename}" class="btn-modern btn-primary-modern">Meer info</a>
                    </div>
                </div>
        '''

def fix_breadcrumbs_visibility():
    """Rend les breadcrumbs visibles sur toutes les pages"""
    
    print(f"\n🧭 CORRECTION DE LA VISIBILITÉ DES BREADCRUMBS")
    print("-" * 40)
    
    # Ajouter les styles CSS pour les breadcrumbs
    css_file = "/Users/marc/Desktop/kastelenbelgie/css/style.css"
    
    breadcrumb_css = """
/* Breadcrumbs visibles */
.breadcrumbs {
    background: var(--bg-secondary);
    padding: 1rem 0;
    border-bottom: 1px solid rgba(0, 0, 0, 0.05);
}

.breadcrumbs-container {
    max-width: var(--container);
    margin: 0 auto;
    padding: 0 1.5rem;
}

.breadcrumbs-nav {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-size: 0.875rem;
    color: var(--text-light);
}

.breadcrumbs-nav a {
    color: var(--primary);
    text-decoration: none;
    transition: color 0.2s ease;
}

.breadcrumbs-nav a:hover {
    color: var(--primary-dark);
}

.breadcrumbs-separator {
    color: var(--text-muted);
    margin: 0 0.25rem;
}

.breadcrumbs-current {
    color: var(--text);
    font-weight: 500;
}
"""
    
    try:
        with open(css_file, 'a', encoding='utf-8') as f:
            f.write(breadcrumb_css)
        
        print("✅ Styles breadcrumbs ajoutés au CSS")
        
        # Mettre à jour les breadcrumbs dans les pages
        update_breadcrumbs_in_pages()
        
    except Exception as e:
        print(f"❌ Erreur ajout CSS breadcrumbs: {e}")

def update_breadcrumbs_in_pages():
    """Met à jour les breadcrumbs dans toutes les pages"""
    
    html_files = glob.glob("/Users/marc/Desktop/kastelenbelgie/*.html")
    updated_count = 0
    
    for html_file in html_files:
        if 'test-' in html_file or 'index.html' in html_file:
            continue
        
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Chercher les breadcrumbs existants et les améliorer
            if 'breadcrumb' in content.lower():
                # Remplacer par une structure moderne
                breadcrumb_pattern = r'<nav[^>]*breadcrumb[^>]*>.*?</nav>'
                
                filename = os.path.basename(html_file)
                new_breadcrumbs = create_modern_breadcrumbs(filename, content)
                
                content = re.sub(breadcrumb_pattern, new_breadcrumbs, content, flags=re.DOTALL)
                
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                updated_count += 1
        
        except Exception as e:
            continue
    
    print(f"✅ Breadcrumbs mis à jour sur {updated_count} pages")

def create_modern_breadcrumbs(filename, content):
    """Crée des breadcrumbs modernes pour une page"""
    
    # Déterminer le type de page
    if any(pattern in filename for pattern in ['kasteel-', 'chateau-', 'hof-', 'burcht-']):
        # Page château
        province = extract_province_from_content(content)
        castle_name = extract_castle_name_from_content(content)
        
        return f'''
    <nav class="breadcrumbs">
        <div class="breadcrumbs-container">
            <div class="breadcrumbs-nav">
                <a href="index.html">Home</a>
                <span class="breadcrumbs-separator">›</span>
                <a href="provinces.html">Provincies</a>
                <span class="breadcrumbs-separator">›</span>
                <a href="{get_province_filename(province) or '#'}">{province or 'Provincie'}</a>
                <span class="breadcrumbs-separator">›</span>
                <span class="breadcrumbs-current">{castle_name or 'Kasteel'}</span>
            </div>
        </div>
    </nav>
        '''
    else:
        # Page province
        province_name = filename.replace('.html', '').replace('-', ' ').title()
        
        return f'''
    <nav class="breadcrumbs">
        <div class="breadcrumbs-container">
            <div class="breadcrumbs-nav">
                <a href="index.html">Home</a>
                <span class="breadcrumbs-separator">›</span>
                <a href="provinces.html">Provincies</a>
                <span class="breadcrumbs-separator">›</span>
                <span class="breadcrumbs-current">{province_name}</span>
            </div>
        </div>
    </nav>
        '''

def extract_province_from_content(content):
    """Extrait la province depuis le contenu"""
    
    match = re.search(r'<strong>Provincie:</strong>\s*<span[^>]*>([^<]+)</span>', content)
    return match.group(1).strip() if match else None

def extract_castle_name_from_content(content):
    """Extrait le nom du château depuis le contenu"""
    
    match = re.search(r'<title>([^|]+)', content)
    return match.group(1).strip() if match else None

if __name__ == "__main__":
    print("🔧 CORRECTION COMPLÈTE DU SITE")
    print("=" * 50)
    
    # 1. Corriger le titre de la homepage
    fix_homepage_title()
    
    # 2. Corriger les assignations de provinces
    fix_province_assignment()
    
    # 3. Rendre les breadcrumbs visibles
    fix_breadcrumbs_visibility()
    
    print(f"\n🎉 CORRECTIONS APPLIQUÉES!")
    print("✅ Titre homepage mis à jour")
    print("✅ Provinces corrigées")
    print("✅ Breadcrumbs rendus visibles")
    print("\n🚀 Prochaines étapes: Images, galeries, header, CTA, footer")
