#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script pour uniformiser les titres des châteaux et améliorer les pages provinces
"""

import os
import re
import glob

def clean_castle_title(title):
    """Nettoie et uniformise le titre d'un château"""
    # Enlève les minuscules au début
    title = title.strip()
    
    # Patterns à nettoyer
    patterns_to_remove = [
        r'\s*-\s*[^-]*$',  # Enlève tout après le dernier tiret (localisation)
        r'\s+te\s+\w+$',   # Enlève "te [ville]"
        r'\s+in\s+\w+$',   # Enlève "in [ville]"
        r'\s+van\s+\w+$',  # Enlève "van [ville]" à la fin
        r'\s+\w+\s*$',     # Enlève le dernier mot s'il semble être une ville
    ]
    
    # Applique les patterns de nettoyage
    cleaned = title
    for pattern in patterns_to_remove:
        # Teste si le pattern correspond et si le résultat n'est pas trop court
        test_result = re.sub(pattern, '', cleaned, flags=re.IGNORECASE).strip()
        if len(test_result) > 5:  # Garde au moins 5 caractères
            cleaned = test_result
    
    # Capitalise correctement
    words = cleaned.split()
    capitalized_words = []
    
    for i, word in enumerate(words):
        word_lower = word.lower()
        
        # Mots qui restent en minuscules (sauf en début de titre)
        if i > 0 and word_lower in ['van', 'de', 'het', 'der', 'des', 'du', 'la', 'le', 'te', 'op', 'aan', 'in']:
            capitalized_words.append(word_lower)
        else:
            # Capitalise la première lettre
            capitalized_words.append(word_lower.capitalize())
    
    return ' '.join(capitalized_words)

def update_castle_titles(file_path):
    """Met à jour le titre d'une page château"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Trouve le titre actuel
        title_match = re.search(r'<h1 class="detail-title">([^<]+)</h1>', content)
        if not title_match:
            return False, "Titre non trouvé"
        
        current_title = title_match.group(1)
        new_title = clean_castle_title(current_title)
        
        if current_title.lower() == new_title.lower():
            return False, "Titre déjà correct"
        
        # Remplace le titre
        new_content = content.replace(
            f'<h1 class="detail-title">{current_title}</h1>',
            f'<h1 class="detail-title">{new_title}</h1>'
        )
        
        # Met aussi à jour le title de la page si nécessaire
        page_title_pattern = r'<title>([^<]+)</title>'
        page_title_match = re.search(page_title_pattern, content)
        if page_title_match:
            old_page_title = page_title_match.group(1)
            new_page_title = f"{new_title} | kastelenbelgie.be"
            new_content = re.sub(page_title_pattern, f'<title>{new_page_title}</title>', new_content)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True, f"'{current_title}' → '{new_title}'"
        
    except Exception as e:
        return False, f"Erreur: {e}"

def update_province_content_and_alignment():
    """Met à jour le contenu et l'alignement des pages provinces"""
    
    province_files = [
        '/Users/marc/Desktop/kastelenbelgie/antwerpen.html',
        '/Users/marc/Desktop/kastelenbelgie/oost-vlaanderen.html',
        '/Users/marc/Desktop/kastelenbelgie/west-vlaanderen.html',
        '/Users/marc/Desktop/kastelenbelgie/limburg.html',
        '/Users/marc/Desktop/kastelenbelgie/vlaams-brabant.html',
        '/Users/marc/Desktop/kastelenbelgie/namen.html',
        '/Users/marc/Desktop/kastelenbelgie/luik.html',
        '/Users/marc/Desktop/kastelenbelgie/luxemburg.html',
        '/Users/marc/Desktop/kastelenbelgie/henegouwen.html',
        '/Users/marc/Desktop/kastelenbelgie/waals-brabant.html'
    ]
    
    updated_count = 0
    
    for file_path in province_files:
        if not os.path.exists(file_path):
            continue
            
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Ajoute des liens dans le contenu s'ils n'existent pas déjà
            if 'href="provinces.html"' in content and 'href="index.html"' in content:
                # Les liens existent déjà, passe au suivant
                continue
            
            # Trouve le contenu de la province
            province_content_pattern = r'(<p class="lead">[^<]+</p>\s*<p>)([^<]+)(</p>)'
            match = re.search(province_content_pattern, content)
            
            if match:
                lead_part = match.group(1)
                description_part = match.group(2)
                end_part = match.group(3)
                
                # Ajoute des liens dans la description
                enhanced_description = description_part
                
                # Ajoute un lien vers toutes les provinces si pas déjà présent
                if 'provinces.html' not in enhanced_description:
                    enhanced_description += ' Ontdek ook <a href="provinces.html">alle provincies van België</a> en hun unieke kasteelcollecties.'
                
                # Ajoute un lien vers la homepage si pas déjà présent
                if 'index.html' not in enhanced_description:
                    enhanced_description += ' Bezoek onze <a href="index.html">homepage</a> voor meer informatie over kastelen in België.'
                
                # Remplace le contenu
                new_province_content = lead_part + enhanced_description + end_part
                content = re.sub(province_content_pattern, new_province_content, content)
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                updated_count += 1
        
        except Exception as e:
            print(f"Erreur avec {os.path.basename(file_path)}: {e}")
    
    return updated_count

def add_province_alignment_css():
    """Ajoute le CSS pour aligner le texte à gauche dans les pages provinces"""
    css_code = '''
/* Province content alignment */
.province-content {
  text-align: left;
}

.province-content .lead {
  text-align: left;
}

.province-navigation {
  text-align: center;
  margin-top: 2rem;
}'''
    
    css_file = '/Users/marc/Desktop/kastelenbelgie/css/style.css'
    
    try:
        with open(css_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remplace l'ancien CSS centré par le nouveau aligné à gauche
        if 'text-align: center' in content and '.province-content' in content:
            # Remplace le CSS existant
            content = re.sub(
                r'\.province-content \{[^}]*text-align:\s*center[^}]*\}',
                '.province-content {\n  max-width: 800px;\n  margin: 0 auto;\n  text-align: left;\n}',
                content
            )
            
            with open(css_file, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        elif '/* Province content alignment */' not in content:
            with open(css_file, 'a', encoding='utf-8') as f:
                f.write(css_code)
            return True
        
        return False
        
    except Exception as e:
        print(f"Erreur CSS: {e}")
        return False

def main():
    """Fonction principale"""
    print("=== AMÉLIORATION TITRES ET PAGES PROVINCES ===")
    
    # 1. Uniformise les titres des châteaux
    print("\n1. Uniformisation des titres de châteaux...")
    castle_files = []
    patterns = [
        "kasteel-*.html", "chateau-*.html", "citadel-*.html", "burcht-*.html",
        "hof-*.html", "de-*.html", "het-*.html", "sint-*.html", "koninklijk-*.html",
        "waterslot-*.html", "vrieselhof-*.html", "rentmeesterij-*.html",
        "commanderij-*.html", "domein-*.html", "oud-*.html", "bisschoppenhof-*.html",
        "braemkasteel-*.html", "burchtruine-*.html", "gaverkasteel-*.html"
    ]
    
    for pattern in patterns:
        castle_files.extend(glob.glob(f"/Users/marc/Desktop/kastelenbelgie/{pattern}"))
    
    castle_files = sorted(list(set(castle_files)))
    print(f"Trouvé {len(castle_files)} pages de châteaux")
    
    # Test avec quelques fichiers
    test_files = castle_files[:5]
    success_count = 0
    
    for file_path in test_files:
        filename = os.path.basename(file_path)
        success, message = update_castle_titles(file_path)
        
        if success:
            print(f"  ✓ {filename}: {message}")
            success_count += 1
        else:
            print(f"  ○ {filename}: {message}")
    
    # Continue avec tous les fichiers
    if success_count > 0:
        print(f"Continuation avec tous les {len(castle_files)} fichiers...")
        
        for file_path in castle_files:
            if file_path in test_files:
                continue
                
            success, message = update_castle_titles(file_path)
            if success:
                success_count += 1
                if success_count % 25 == 0:
                    print(f"  Progression: {success_count} titres mis à jour...")
    
    print(f"Titres de châteaux mis à jour: {success_count}")
    
    # 2. Met à jour les pages provinces
    print("\n2. Amélioration des pages provinces...")
    
    # Ajoute le CSS d'alignement
    if add_province_alignment_css():
        print("  ✓ CSS d'alignement ajouté")
    else:
        print("  ○ CSS d'alignement déjà présent")
    
    # Met à jour le contenu avec liens
    province_updated = update_province_content_and_alignment()
    print(f"  ✓ {province_updated} pages provinces mises à jour avec liens")
    
    print(f"\n=== RÉSULTAT FINAL ===")
    print(f"Titres de châteaux uniformisés: {success_count}")
    print(f"Pages provinces améliorées: {province_updated}")
    print("Améliorations terminées!")

if __name__ == "__main__":
    main()
