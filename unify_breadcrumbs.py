#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
UNIFICATION DES BREADCRUMBS SUR TOUT LE SITE
Applique le même style de breadcrumbs partout
"""

import glob
import re

def unify_breadcrumbs():
    """Unifie les breadcrumbs sur toutes les pages du site"""
    
    print("🧭 UNIFICATION DES BREADCRUMBS SUR TOUT LE SITE")
    print("=" * 60)
    
    # Trouver tous les fichiers HTML
    html_files = glob.glob("/Users/marc/Desktop/kastelenbelgie/*.html")
    
    updated_count = 0
    
    for html_file in html_files:
        try:
            # Ignorer certains fichiers
            filename = html_file.split('/')[-1]
            if filename in ['index.html', 'login.html', 'register.html', 'dashboard.html', 'admin.html']:
                continue
            
            # Lire le fichier
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Déterminer le type de page et générer les breadcrumbs appropriés
            breadcrumb_html = generate_breadcrumbs_for_page(filename, content)
            
            if not breadcrumb_html:
                continue
            
            # Chercher et remplacer les breadcrumbs existants
            breadcrumb_patterns = [
                r'<nav class="breadcrumb-nav">.*?</nav>',
                r'<!-- Breadcrumbs -->.*?</nav>',
                r'<div class="breadcrumb">.*?</div>',
                r'<nav class="breadcrumb">.*?</nav>'
            ]
            
            content_modified = False
            for pattern in breadcrumb_patterns:
                if re.search(pattern, content, re.DOTALL):
                    content = re.sub(pattern, breadcrumb_html, content, flags=re.DOTALL)
                    content_modified = True
                    break
            
            # Si pas de breadcrumbs existants, les ajouter après la navigation
            if not content_modified:
                nav_end = content.find('</nav>')
                if nav_end != -1:
                    nav_end += len('</nav>')
                    content = content[:nav_end] + '\n\n' + breadcrumb_html + content[nav_end:]
                    content_modified = True
            
            if content_modified:
                # Sauvegarder
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                updated_count += 1
                print(f"✅ {filename}: breadcrumbs unifiés")
            
        except Exception as e:
            print(f"❌ Erreur avec {html_file}: {e}")
            continue
    
    print(f"\n📊 RÉSULTATS:")
    print(f"Pages mises à jour: {updated_count}")

def generate_breadcrumbs_for_page(filename, content):
    """Génère les breadcrumbs appropriés selon le type de page"""
    
    # Style unifié des breadcrumbs
    breadcrumb_nav_start = '''    <nav class="breadcrumb-nav">
        <div class="container">
            <nav class="breadcrumb">'''
    
    breadcrumb_nav_end = '''            </nav>
        </div>
    </nav>'''
    
    # Pages provinces
    if filename in ['antwerpen.html', 'limburg.html', 'oost-vlaanderen.html', 'west-vlaanderen.html', 
                    'vlaams-brabant.html', 'namen.html', 'luik.html', 'henegouwen.html', 
                    'luxemburg.html', 'waals-brabant.html', 'brussel.html']:
        
        province_name = get_province_display_name(filename)
        breadcrumb_content = f'''
                <a href="index.html">Home</a>
                <span class="breadcrumb-separator">›</span>
                <a href="provinces.html">Provincies</a>
                <span class="breadcrumb-separator">›</span>
                <span class="breadcrumb-current">{province_name}</span>'''
    
    # Pages châteaux
    elif any(pattern in filename for pattern in ['kasteel-', 'hof-', 'het-', 'de-', 'sint-', 'chateau-', 
                                                 'burcht-', 'paleis-', 'commanderij-', 'waterkasteel-', 
                                                 'waterburcht-', 'koninklijk-', 'gaverkasteel-', 'citadel-',
                                                 'domein-', 'bisschoppenhof-', 'waterslot-', 'braemkasteel-',
                                                 'vrieselhof-', 'rood-', 'rentmeesterij-', 'oud-']):
        
        # Extraire le nom du château et la province
        castle_name = extract_castle_name_from_content(content)
        province = extract_province_from_content(content)
        
        if castle_name and province:
            province_file = get_province_filename(province)
            breadcrumb_content = f'''
                <a href="index.html">Home</a>
                <span class="breadcrumb-separator">›</span>
                <a href="provinces.html">Provincies</a>
                <span class="breadcrumb-separator">›</span>
                <a href="{province_file}">{province}</a>
                <span class="breadcrumb-separator">›</span>
                <span class="breadcrumb-current">{castle_name}</span>'''
        else:
            return None
    
    # Pages blog
    elif filename.startswith('blog-'):
        breadcrumb_content = '''
                <a href="index.html">Home</a>
                <span class="breadcrumb-separator">›</span>
                <a href="blog.html">Blog</a>
                <span class="breadcrumb-separator">›</span>
                <span class="breadcrumb-current">Article</span>'''
    
    # Page blog principale
    elif filename == 'blog.html':
        breadcrumb_content = '''
                <a href="index.html">Home</a>
                <span class="breadcrumb-separator">›</span>
                <span class="breadcrumb-current">Blog</span>'''
    
    # Page provinces
    elif filename == 'provinces.html':
        breadcrumb_content = '''
                <a href="index.html">Home</a>
                <span class="breadcrumb-separator">›</span>
                <span class="breadcrumb-current">Provincies</span>'''
    
    # Page contact
    elif filename == 'contact.html':
        breadcrumb_content = '''
                <a href="index.html">Home</a>
                <span class="breadcrumb-separator">›</span>
                <span class="breadcrumb-current">Contact</span>'''
    
    # Page kastelen
    elif filename == 'kastelen.html':
        breadcrumb_content = '''
                <a href="index.html">Home</a>
                <span class="breadcrumb-separator">›</span>
                <span class="breadcrumb-current">Alle Kastelen</span>'''
    
    # Page kaart
    elif filename == 'kaart.html':
        breadcrumb_content = '''
                <a href="index.html">Home</a>
                <span class="breadcrumb-separator">›</span>
                <span class="breadcrumb-current">Kastelenkaart</span>'''
    
    else:
        return None
    
    return breadcrumb_nav_start + breadcrumb_content + breadcrumb_nav_end

def get_province_display_name(filename):
    """Obtient le nom d'affichage de la province"""
    mapping = {
        'antwerpen.html': 'Antwerpen',
        'limburg.html': 'Limburg',
        'oost-vlaanderen.html': 'Oost-Vlaanderen',
        'west-vlaanderen.html': 'West-Vlaanderen',
        'vlaams-brabant.html': 'Vlaams-Brabant',
        'namen.html': 'Namen',
        'luik.html': 'Luik',
        'henegouwen.html': 'Henegouwen',
        'luxemburg.html': 'Luxemburg',
        'waals-brabant.html': 'Waals-Brabant',
        'brussel.html': 'Brussel'
    }
    return mapping.get(filename, 'Province')

def get_province_filename(province):
    """Obtient le nom de fichier de la province"""
    mapping = {
        'Antwerpen': 'antwerpen.html',
        'Limburg': 'limburg.html',
        'Oost-Vlaanderen': 'oost-vlaanderen.html',
        'West-Vlaanderen': 'west-vlaanderen.html',
        'Vlaams-Brabant': 'vlaams-brabant.html',
        'Namen': 'namen.html',
        'Luik': 'luik.html',
        'Henegouwen': 'henegouwen.html',
        'Luxemburg': 'luxemburg.html',
        'Waals-Brabant': 'waals-brabant.html',
        'Brussel': 'brussel.html'
    }
    return mapping.get(province, 'provinces.html')

def extract_castle_name_from_content(content):
    """Extrait le nom du château depuis le contenu HTML"""
    # Chercher dans le title
    title_match = re.search(r'<title>([^|]+)', content)
    if title_match:
        return title_match.group(1).strip()
    
    # Chercher dans le h1
    h1_match = re.search(r'<h1[^>]*>([^<]+)</h1>', content)
    if h1_match:
        return h1_match.group(1).strip()
    
    return None

def extract_province_from_content(content):
    """Extrait la province depuis le contenu HTML"""
    province_match = re.search(r'<strong>Provincie:</strong>\s*<span[^>]*>([^<]+)</span>', content)
    if province_match:
        return province_match.group(1).strip()
    return None

if __name__ == "__main__":
    unify_breadcrumbs()
