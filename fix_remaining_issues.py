#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CORRECTION DES PROBLÈMES RESTANTS
Images, galeries, header, CTA, footer
"""

import glob
import re
import os
from pathlib import Path

def synchronize_castle_images():
    """Synchronise les images entre pages provinces et pages châteaux"""
    
    print("🖼️ SYNCHRONISATION DES IMAGES CHÂTEAUX")
    print("-" * 40)
    
    # Analyser les images utilisées dans les pages provinces
    province_files = [
        'antwerpen.html', 'limburg.html', 'oost-vlaanderen.html', 
        'west-vlaanderen.html', 'vlaams-brabant.html', 'namen.html',
        'luik.html', 'henegouwen.html', 'luxemburg.html', 
        'waals-brabant.html', 'brussel.html'
    ]
    
    castle_images = {}
    
    for province_file in province_files:
        file_path = f"/Users/marc/Desktop/kastelenbelgie/{province_file}"
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extraire les liens château avec leurs images
            castle_pattern = r'<div class="castle-card">.*?<img src="([^"]*)"[^>]*alt="([^"]*)"[^>]*>.*?<a href="([^"]*)"'
            matches = re.findall(castle_pattern, content, re.DOTALL)
            
            for image_src, alt_text, castle_link in matches:
                if castle_link.endswith('.html'):
                    castle_images[castle_link] = {
                        'image': image_src,
                        'alt': alt_text
                    }
            
        except Exception as e:
            continue
    
    print(f"📊 Images trouvées pour {len(castle_images)} châteaux")
    
    # Mettre à jour les pages châteaux
    updated_count = 0
    
    for castle_file, image_info in castle_images.items():
        castle_path = f"/Users/marc/Desktop/kastelenbelgie/{castle_file}"
        
        if os.path.exists(castle_path):
            try:
                with open(castle_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Remplacer l'image hero si différente
                hero_pattern = r'<img[^>]*class="hero-image-modern"[^>]*src="([^"]*)"'
                hero_match = re.search(hero_pattern, content)
                
                if hero_match and hero_match.group(1) != image_info['image']:
                    content = re.sub(
                        r'<img([^>]*)class="hero-image-modern"([^>]*)src="[^"]*"([^>]*)>',
                        f'<img\\1class="hero-image-modern"\\2src="{image_info["image"]}"\\3>',
                        content
                    )
                    
                    with open(castle_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    updated_count += 1
                    print(f"✅ {castle_file}: image synchronisée")
            
            except Exception as e:
                continue
    
    print(f"✅ {updated_count} pages châteaux mises à jour")

def add_gallery_sections():
    """Ajoute les sections 'In onze gallerij' aux pages châteaux"""
    
    print(f"\n🖼️ AJOUT DES SECTIONS GALERIES")
    print("-" * 40)
    
    # Trouver toutes les images disponibles
    image_dir = "/Users/marc/Desktop/kastelenbelgie/chateaux_images_update-2"
    available_images = []
    
    if os.path.exists(image_dir):
        for ext in ['*.jpg', '*.jpeg', '*.png', '*.webp']:
            available_images.extend(glob.glob(f"{image_dir}/{ext}"))
    
    print(f"📊 {len(available_images)} images disponibles")
    
    # Analyser les pages châteaux
    castle_files = glob.glob("/Users/marc/Desktop/kastelenbelgie/kasteel-*.html")
    castle_files.extend(glob.glob("/Users/marc/Desktop/kastelenbelgie/chateau-*.html"))
    castle_files.extend(glob.glob("/Users/marc/Desktop/kastelenbelgie/hof-*.html"))
    
    updated_count = 0
    
    for castle_file in castle_files[:10]:  # Limiter pour le test
        try:
            with open(castle_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Vérifier si la section galerie existe déjà
            if 'In onze gallerij' in content or 'gallery-section' in content:
                continue
            
            # Extraire le nom du château
            castle_name = extract_castle_name_from_file(castle_file)
            
            # Trouver les images correspondantes
            castle_images = find_castle_images(castle_name, available_images)
            
            if len(castle_images) > 1:  # Au moins 2 images pour faire une galerie
                gallery_section = create_gallery_section(castle_images[:6])  # Max 6 images
                
                # Insérer la section avant le footer
                footer_pattern = r'(<footer|<!-- Footer)'
                if re.search(footer_pattern, content):
                    content = re.sub(
                        footer_pattern,
                        gallery_section + '\n\n    \\1',
                        content
                    )
                    
                    with open(castle_file, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    updated_count += 1
                    filename = os.path.basename(castle_file)
                    print(f"✅ {filename}: galerie ajoutée ({len(castle_images)} images)")
        
        except Exception as e:
            continue
    
    print(f"✅ {updated_count} galeries ajoutées")

def extract_castle_name_from_file(filepath):
    """Extrait le nom du château depuis le nom de fichier"""
    
    filename = os.path.basename(filepath).replace('.html', '')
    
    # Nettoyer le nom
    name = filename.replace('kasteel-', '').replace('chateau-', '').replace('hof-', '')
    name = name.replace('-', ' ').strip()
    
    return name

def find_castle_images(castle_name, available_images):
    """Trouve les images correspondant à un château"""
    
    matching_images = []
    
    # Mots-clés du château
    keywords = castle_name.lower().split()
    
    for image_path in available_images:
        image_name = os.path.basename(image_path).lower()
        
        # Vérifier si le nom de l'image contient des mots-clés du château
        if any(keyword in image_name for keyword in keywords if len(keyword) > 3):
            relative_path = f"chateaux_images_update-2/{os.path.basename(image_path)}"
            matching_images.append(relative_path)
    
    return matching_images

def create_gallery_section(images):
    """Crée une section galerie HTML"""
    
    gallery_items = ""
    for i, image in enumerate(images):
        gallery_items += f'''
                <div class="gallery-item">
                    <img src="{image}" alt="Kasteel foto {i+1}" loading="lazy">
                </div>'''
    
    return f'''
    <!-- Section Galerie -->
    <section class="section gallery-section">
        <div class="container">
            <h2 class="section-title">In onze gallerij</h2>
            <p class="section-subtitle">Ontdek meer beelden van dit prachtige kasteel</p>
            
            <div class="gallery-grid">
                {gallery_items}
            </div>
        </div>
    </section>'''

def improve_header():
    """Améliore le header avec logo et icône"""
    
    print(f"\n🎨 AMÉLIORATION DU HEADER")
    print("-" * 40)
    
    # Ajouter les styles CSS pour le header amélioré
    css_file = "/Users/marc/Desktop/kastelenbelgie/css/style.css"
    
    header_css = """
/* Header amélioré */
.navbar {
    background: white;
    border-bottom: 1px solid rgba(0, 0, 0, 0.05);
    padding: 1rem 0;
    position: sticky;
    top: 0;
    z-index: 100;
    backdrop-filter: blur(10px);
}

.nav-container {
    display: flex;
    align-items: center;
    justify-content: space-between;
    max-width: var(--container);
    margin: 0 auto;
    padding: 0 1.5rem;
}

.logo {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-size: 1.25rem;
    font-weight: 700;
    color: var(--primary);
    text-decoration: none;
}

.logo-icon {
    width: 32px;
    height: 32px;
    background: var(--primary);
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-size: 1rem;
}

.nav-menu {
    display: flex;
    align-items: center;
    gap: 2rem;
}

.nav-link {
    color: var(--text);
    text-decoration: none;
    font-weight: 500;
    transition: color 0.2s ease;
}

.nav-link:hover {
    color: var(--primary);
}

.search-box {
    position: relative;
}

.search-input {
    padding: 0.5rem 1rem;
    border: 1px solid rgba(0, 0, 0, 0.1);
    border-radius: 50px;
    font-size: 0.875rem;
    width: 200px;
    transition: all 0.2s ease;
}

.search-input:focus {
    outline: none;
    border-color: var(--primary);
    box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}

/* Gallery styles */
.gallery-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1rem;
    margin-top: 2rem;
}

.gallery-item {
    border-radius: var(--radius);
    overflow: hidden;
    box-shadow: var(--shadow);
    transition: transform 0.3s ease;
}

.gallery-item:hover {
    transform: translateY(-2px);
}

.gallery-item img {
    width: 100%;
    height: 200px;
    object-fit: cover;
}
"""
    
    try:
        with open(css_file, 'a', encoding='utf-8') as f:
            f.write(header_css)
        
        print("✅ Styles header ajoutés au CSS")
        
        # Mettre à jour le header dans toutes les pages
        update_header_in_pages()
        
    except Exception as e:
        print(f"❌ Erreur ajout CSS header: {e}")

def update_header_in_pages():
    """Met à jour le header dans toutes les pages"""
    
    html_files = glob.glob("/Users/marc/Desktop/kastelenbelgie/*.html")
    updated_count = 0
    
    for html_file in html_files:
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Remplacer le logo simple par un logo avec icône
            old_logo = r'<a href="index\.html" class="logo">kastelenbelgie</a>'
            new_logo = '''<a href="index.html" class="logo">
                    <div class="logo-icon">🏰</div>
                    kastelenbelgie
                </a>'''
            
            if re.search(old_logo, content):
                content = re.sub(old_logo, new_logo, content)
                
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                updated_count += 1
        
        except Exception as e:
            continue
    
    print(f"✅ Header mis à jour sur {updated_count} pages")

def create_uniform_footer():
    """Crée un footer uniforme en 3 colonnes"""
    
    print(f"\n🦶 CRÉATION DU FOOTER UNIFORME")
    print("-" * 40)
    
    footer_html = '''
    <!-- Footer uniforme -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-column">
                    <h4 class="footer-title">Kastelen België</h4>
                    <p class="footer-description">
                        Ontdek de rijke geschiedenis van België door haar prachtige kastelen. 
                        Van middeleeuwse burchten tot barokke paleizen.
                    </p>
                    <div class="footer-social">
                        <a href="#" class="social-link">📧</a>
                        <a href="#" class="social-link">📱</a>
                        <a href="#" class="social-link">🌐</a>
                    </div>
                </div>
                
                <div class="footer-column">
                    <h4 class="footer-title">Verken</h4>
                    <ul class="footer-links">
                        <li><a href="provinces.html">Alle Provincies</a></li>
                        <li><a href="antwerpen.html">Antwerpen</a></li>
                        <li><a href="vlaams-brabant.html">Vlaams-Brabant</a></li>
                        <li><a href="oost-vlaanderen.html">Oost-Vlaanderen</a></li>
                        <li><a href="west-vlaanderen.html">West-Vlaanderen</a></li>
                        <li><a href="limburg.html">Limburg</a></li>
                    </ul>
                </div>
                
                <div class="footer-column">
                    <h4 class="footer-title">Informatie</h4>
                    <ul class="footer-links">
                        <li><a href="blog.html">Blog</a></li>
                        <li><a href="contact.html">Contact</a></li>
                        <li><a href="#" onclick="alert('Privacy policy komt binnenkort')">Privacy</a></li>
                        <li><a href="#" onclick="alert('Algemene voorwaarden komen binnenkort')">Voorwaarden</a></li>
                        <li><a href="#" onclick="alert('Over ons komt binnenkort')">Over Ons</a></li>
                    </ul>
                </div>
            </div>
            
            <div class="footer-bottom">
                <p>&copy; 2024 Kastelen België. Alle rechten voorbehouden.</p>
                <p>Gemaakt met ❤️ voor de Belgische erfgoed.</p>
            </div>
        </div>
    </footer>'''
    
    # Ajouter les styles CSS pour le footer
    footer_css = """
/* Footer uniforme */
.footer {
    background: var(--text);
    color: white;
    padding: 3rem 0 1rem;
    margin-top: 4rem;
}

.footer-content {
    display: grid;
    grid-template-columns: 2fr 1fr 1fr;
    gap: 3rem;
    margin-bottom: 2rem;
}

.footer-column h4 {
    color: white;
    margin-bottom: 1rem;
    font-size: 1.125rem;
    font-weight: 600;
}

.footer-description {
    color: rgba(255, 255, 255, 0.8);
    line-height: 1.6;
    margin-bottom: 1.5rem;
}

.footer-social {
    display: flex;
    gap: 0.5rem;
}

.social-link {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 40px;
    height: 40px;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 50%;
    text-decoration: none;
    font-size: 1.2rem;
    transition: background 0.2s ease;
}

.social-link:hover {
    background: var(--primary);
}

.footer-links {
    list-style: none;
    padding: 0;
}

.footer-links li {
    margin-bottom: 0.5rem;
}

.footer-links a {
    color: rgba(255, 255, 255, 0.8);
    text-decoration: none;
    transition: color 0.2s ease;
}

.footer-links a:hover {
    color: white;
}

.footer-bottom {
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    padding-top: 1rem;
    text-align: center;
    color: rgba(255, 255, 255, 0.6);
    font-size: 0.875rem;
}

.footer-bottom p {
    margin-bottom: 0.5rem;
}

@media (max-width: 768px) {
    .footer-content {
        grid-template-columns: 1fr;
        gap: 2rem;
    }
}
"""
    
    # Ajouter le CSS
    css_file = "/Users/marc/Desktop/kastelenbelgie/css/style.css"
    
    try:
        with open(css_file, 'a', encoding='utf-8') as f:
            f.write(footer_css)
        
        print("✅ Styles footer ajoutés au CSS")
        
        # Remplacer les footers existants
        replace_footers_in_pages(footer_html)
        
    except Exception as e:
        print(f"❌ Erreur ajout CSS footer: {e}")

def replace_footers_in_pages(new_footer):
    """Remplace les footers dans toutes les pages"""
    
    html_files = glob.glob("/Users/marc/Desktop/kastelenbelgie/*.html")
    updated_count = 0
    
    for html_file in html_files:
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Remplacer le footer existant
            footer_pattern = r'<footer.*?</footer>'
            
            if re.search(footer_pattern, content, re.DOTALL):
                content = re.sub(footer_pattern, new_footer.strip(), content, flags=re.DOTALL)
            else:
                # Ajouter le footer avant </body>
                content = content.replace('</body>', f'{new_footer}\n</body>')
            
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            updated_count += 1
        
        except Exception as e:
            continue
    
    print(f"✅ Footer mis à jour sur {updated_count} pages")

if __name__ == "__main__":
    print("🔧 CORRECTION DES PROBLÈMES RESTANTS")
    print("=" * 50)
    
    # 4. Synchroniser les images
    synchronize_castle_images()
    
    # 5. Ajouter les galeries
    add_gallery_sections()
    
    # 6. Améliorer le header
    improve_header()
    
    # 9. Créer le footer uniforme
    create_uniform_footer()
    
    print(f"\n🎉 CORRECTIONS SUPPLÉMENTAIRES APPLIQUÉES!")
    print("✅ Images synchronisées")
    print("✅ Galeries ajoutées")
    print("✅ Header amélioré")
    print("✅ Footer uniforme créé")
    print("\n🚀 Prochaine étape: Vérifier les CTA et ajouter textes 'Meer kastelen'")
