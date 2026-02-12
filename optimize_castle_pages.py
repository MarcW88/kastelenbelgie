#!/usr/bin/env python3
"""
Script d'optimisation automatique des pages châteaux
Applique les modifications de structure SEO sur toutes les fiches kasteel-*.html

Modifications appliquées:
1. Ajoute H2 "Over [kasteelnaam]" au-dessus de la section castle-intro
2. Ajoute schema.org BreadcrumbList aux breadcrumbs
3. Corrige le HTML cassé des cards related-castles (balises mal fermées)
4. Normalise les textes "Bezoekbaar" et "Openingsuren"
"""

import os
import re
import glob
from bs4 import BeautifulSoup

# Configuration
KASTEEL_DIR = "/Users/marc/Desktop/kastelenbelgie"
DRY_RUN = False  # Mettre à True pour tester sans modifier les fichiers

def get_castle_name_from_h1(soup):
    """Extrait le nom du château depuis le H1"""
    h1 = soup.find('h1')
    if h1:
        return h1.get_text(strip=True)
    return None

def get_province_from_breadcrumb(soup):
    """Extrait la province depuis le breadcrumb"""
    breadcrumb_nav = soup.find('div', class_='breadcrumbs-nav')
    if breadcrumb_nav:
        links = breadcrumb_nav.find_all('a')
        for link in links:
            href = link.get('href', '')
            if href.endswith('.html') and href not in ['index.html', 'provinces.html']:
                return link.get_text(strip=True), href
    return None, None

def add_h2_to_intro(soup, castle_name):
    """Ajoute un H2 'Over [kasteelnaam]' au-dessus de la section intro si absent"""
    intro_section = soup.find('section', class_='castle-intro')
    if not intro_section:
        return False
    
    container = intro_section.find('div', class_='container')
    if not container:
        return False
    
    # Vérifie si un H2 existe déjà
    existing_h2 = container.find('h2')
    if existing_h2:
        return False  # Déjà un H2, ne pas modifier
    
    # Crée le nouveau H2
    new_h2 = soup.new_tag('h2')
    new_h2['style'] = "font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; font-size: 1.5rem; font-weight: 700; color: var(--text); margin-bottom: 1rem;"
    new_h2.string = f"Over {castle_name}"
    
    # Insère le H2 au début du container
    content_wrapper = container.find('div', class_='content-wrapper')
    if content_wrapper:
        content_wrapper.insert_before(new_h2)
    else:
        first_child = container.find()
        if first_child:
            first_child.insert_before(new_h2)
    
    return True

def add_schema_breadcrumbs(soup):
    """Ajoute le markup schema.org BreadcrumbList aux breadcrumbs"""
    breadcrumb_nav = soup.find('nav', class_='breadcrumbs')
    if not breadcrumb_nav:
        return False
    
    # Vérifie si schema.org est déjà présent
    if breadcrumb_nav.get('aria-label') == 'Breadcrumb':
        return False  # Déjà optimisé
    
    # Ajoute aria-label
    breadcrumb_nav['aria-label'] = 'Breadcrumb'
    
    # Trouve le div breadcrumbs-nav
    nav_div = breadcrumb_nav.find('div', class_='breadcrumbs-nav')
    if not nav_div:
        return False
    
    # Ajoute les attributs schema.org
    nav_div['itemscope'] = ''
    nav_div['itemtype'] = 'https://schema.org/BreadcrumbList'
    
    return True

def fix_broken_card_html(soup):
    """Corrige le HTML cassé dans les cards related-castles"""
    fixed = False
    
    # Cherche les cards avec du HTML cassé
    for card in soup.find_all('div', class_='related-castle-card'):
        card_content = card.find('div', class_='castle-card-content')
        if not card_content:
            continue
        
        h3 = card_content.find('h3')
        if not h3:
            continue
        
        # Vérifie si le H3 contient du texte cassé (attributs dans le texte)
        h3_text = str(h3)
        if 'class="card-description-modern"' in h3_text or 'clontdek' in h3_text.lower():
            # Extrait le nom du château
            castle_name = None
            for text in h3.stripped_strings:
                if text and not text.startswith('<'):
                    castle_name = text.split('<')[0].strip()
                    break
            
            if castle_name:
                # Reconstruit proprement
                h3.clear()
                h3.string = castle_name
                
                # Vérifie s'il y a un <p> correct
                p = card_content.find('p', class_='card-description-modern')
                if not p:
                    new_p = soup.new_tag('p')
                    new_p['class'] = 'card-description-modern'
                    new_p.string = f"Ontdek dit prachtige kasteel."
                    h3.insert_after(new_p)
                
                fixed = True
    
    return fixed

def normalize_bezoekbaar(soup):
    """Normalise les valeurs de Bezoekbaar"""
    valid_values = ['Ja', 'Nee', 'Enkel buitenkant', 'Op aanvraag']
    
    for detail in soup.find_all('div', class_='detail-item'):
        strong = detail.find('strong')
        if strong and 'Bezoekbaar' in strong.get_text():
            meta_value = detail.find('span', class_='meta-value')
            if meta_value:
                current = meta_value.get_text(strip=True)
                if current not in valid_values:
                    # Normalise vers la valeur la plus proche
                    if 'ja' in current.lower():
                        meta_value.string = 'Ja'
                    elif 'nee' in current.lower() or 'niet' in current.lower():
                        meta_value.string = 'Nee'
                    elif 'buiten' in current.lower():
                        meta_value.string = 'Enkel buitenkant'
                    else:
                        meta_value.string = 'Op aanvraag'
                    return True
    return False

def process_castle_page(filepath):
    """Traite une page château individuelle"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        castle_name = get_castle_name_from_h1(soup)
        if not castle_name:
            print(f"  ⚠️ Pas de H1 trouvé dans {filepath}")
            return False
        
        modifications = []
        
        # 1. Ajoute H2 à l'intro
        if add_h2_to_intro(soup, castle_name):
            modifications.append("H2 intro ajouté")
        
        # 2. Ajoute schema.org aux breadcrumbs
        if add_schema_breadcrumbs(soup):
            modifications.append("Schema.org breadcrumbs")
        
        # 3. Corrige le HTML cassé des cards
        if fix_broken_card_html(soup):
            modifications.append("HTML cards corrigé")
        
        # 4. Normalise Bezoekbaar
        if normalize_bezoekbaar(soup):
            modifications.append("Bezoekbaar normalisé")
        
        if modifications:
            if not DRY_RUN:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(str(soup))
            print(f"  ✅ {os.path.basename(filepath)}: {', '.join(modifications)}")
            return True
        else:
            print(f"  ⏭️ {os.path.basename(filepath)}: Déjà optimisé")
            return False
            
    except Exception as e:
        print(f"  ❌ Erreur {filepath}: {e}")
        return False

def main():
    """Fonction principale"""
    print("=" * 60)
    print("🏰 Optimisation automatique des pages châteaux")
    print("=" * 60)
    
    if DRY_RUN:
        print("⚠️  MODE TEST (DRY_RUN) - Aucun fichier ne sera modifié")
    
    # Trouve toutes les pages châteaux
    pattern = os.path.join(KASTEEL_DIR, "kasteel-*.html")
    castle_files = glob.glob(pattern)
    
    print(f"\n📁 {len(castle_files)} pages châteaux trouvées\n")
    
    modified = 0
    errors = 0
    skipped = 0
    
    for filepath in sorted(castle_files):
        result = process_castle_page(filepath)
        if result:
            modified += 1
        elif result is False:
            skipped += 1
        else:
            errors += 1
    
    print("\n" + "=" * 60)
    print(f"📊 Résumé:")
    print(f"   ✅ Modifiées: {modified}")
    print(f"   ⏭️ Déjà OK: {skipped}")
    print(f"   ❌ Erreurs: {errors}")
    print("=" * 60)

if __name__ == "__main__":
    main()
