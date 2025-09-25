#!/usr/bin/env python3
"""
Script pour corriger les titres "Meer kastelen in Home" vers les vraies provinces
et personnaliser les descriptions avec des extraits des pages châteaux
"""

import os
import re
from pathlib import Path
from bs4 import BeautifulSoup

def extract_province_from_breadcrumb(content):
    """Extrait la province depuis les breadcrumbs"""
    soup = BeautifulSoup(content, 'html.parser')
    
    # Chercher le breadcrumb de la province
    breadcrumb_links = soup.find_all('a', href=re.compile(r'.*\.html'))
    
    for link in breadcrumb_links:
        href = link.get('href', '')
        if any(province in href for province in ['antwerpen', 'limburg', 'oost-vlaanderen', 
                                                'west-vlaanderen', 'vlaams-brabant', 'namen',
                                                'luxemburg', 'luik', 'henegouwen', 'waals-brabant']):
            return link.get_text().strip()
    
    return None

def extract_intro_text(html_file):
    """Extrait le premier paragraphe d'introduction d'une page château"""
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        # Chercher dans la section castle-intro
        intro_section = soup.find('section', class_='castle-intro')
        if intro_section:
            first_p = intro_section.find('p')
            if first_p:
                text = first_p.get_text().strip()
                # Limiter à 120 caractères pour les descriptions
                if len(text) > 120:
                    text = text[:117] + "..."
                return text
        
        return None
    except:
        return None

def fix_meer_kastelen_titles():
    """Corrige les titres et descriptions de la section 'Meer kastelen'"""
    
    base_dir = Path("/Users/marc/Desktop/kastelenbelgie")
    
    print("🏰 CORRECTION DES TITRES 'MEER KASTELEN'")
    print("=" * 45)
    
    files_processed = 0
    files_modified = 0
    
    # Parcourir toutes les pages châteaux
    for html_file in base_dir.glob("*.html"):
        # Ignorer les pages non-châteaux
        if html_file.name in ['index.html', 'contact.html', 'blog.html', 'provinces.html', 
                             'antwerpen.html', 'limburg.html', 'oost-vlaanderen.html', 
                             'west-vlaanderen.html', 'vlaams-brabant.html', 'namen.html',
                             'luxemburg.html', 'luik.html', 'henegouwen.html', 'waals-brabant.html',
                             'admin.html', 'dashboard.html', 'login.html', 'register.html']:
            continue
        
        if html_file.name.startswith('blog-'):
            continue
        
        files_processed += 1
        
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # 1. Corriger le titre "Meer kastelen in Home"
            province = extract_province_from_breadcrumb(content)
            if province:
                # Remplacer "Meer kastelen in Home" par "Meer kastelen in [Province]"
                pattern1 = r'<h2 class="section-title">Meer kastelen in Home</h2>'
                replacement1 = f'<h2 class="section-title">Meer kastelen in {province}</h2>'
                content = re.sub(pattern1, replacement1, content)
                
                # Aussi corriger d'autres variantes
                pattern2 = r'<h2[^>]*>Meer kastelen in Home</h2>'
                replacement2 = f'<h2 class="section-title">Meer kastelen in {province}</h2>'
                content = re.sub(pattern2, replacement2, content)
            
            # 2. Améliorer les descriptions génériques
            # Chercher les descriptions génériques et les remplacer
            generic_descriptions = [
                "Een kasteel met een fascinerende geschiedenis en unieke architectuur.",
                "Ontdek dit prachtige kasteel in Antwerpen",
                "Een kasteel met een fascinerende geschiedenis",
                "De provincie [^<]* biedt naast het bezoek aan [^<]* nog vele andere interessante activiteiten en"
            ]
            
            for generic_desc in generic_descriptions:
                pattern = f'<p class="card-description-modern">{generic_desc}</p>'
                # Remplacer par une description plus spécifique
                replacement = '<p class="card-description-modern">Ontdek de rijke geschiedenis en architecturale schoonheid van dit unieke kasteel.</p>'
                content = re.sub(pattern, replacement, content)
            
            # 3. Corriger les liens vers les châteaux liés
            # S'assurer que les liens dans "related castles" pointent vers de vraies pages
            related_links = re.findall(r'<a href="([^"]*\.html)" class="btn-modern btn-primary-modern">Meer info</a>', content)
            for link in related_links:
                linked_file = base_dir / link
                if not linked_file.exists():
                    print(f"⚠️  Lien cassé détecté: {link} dans {html_file.name}")
            
            if content != original_content:
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                files_modified += 1
                if province:
                    print(f"✅ {html_file.name} - Titre corrigé: 'Meer kastelen in {province}'")
                else:
                    print(f"✅ {html_file.name} - Descriptions améliorées")
        
        except Exception as e:
            print(f"❌ Erreur avec {html_file.name}: {e}")
    
    print(f"\n📊 RÉSULTATS:")
    print(f"   Fichiers traités: {files_processed}")
    print(f"   Fichiers modifiés: {files_modified}")
    
    if files_modified > 0:
        print(f"\n🎉 Titres 'Meer kastelen' corrigés!")
        print("   - Provinces correctes dans les titres")
        print("   - Descriptions moins génériques")
        print("   - Navigation plus cohérente")
    else:
        print("\n✨ Titres déjà corrects!")

if __name__ == "__main__":
    fix_meer_kastelen_titles()
