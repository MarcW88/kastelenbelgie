#!/usr/bin/env python3
"""
Script pour personnaliser les descriptions "meer kastelen" avec de vrais extraits
des pages châteaux (phrases complètes)
"""

import os
import re
from pathlib import Path
from bs4 import BeautifulSoup

def extract_first_sentence(html_file):
    """Extrait la première phrase complète d'une page château"""
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        # Chercher dans la section castle-intro ou tour-intro
        intro_section = soup.find('section', class_=['castle-intro', 'tour-intro'])
        if not intro_section:
            # Fallback: chercher dans n'importe quelle section avec des paragraphes
            intro_section = soup.find('section')
        
        if intro_section:
            paragraphs = intro_section.find_all('p')
            for p in paragraphs:
                text = p.get_text().strip()
                if len(text) > 50:  # Ignorer les paragraphes trop courts
                    # Extraire la première phrase (jusqu'au premier point)
                    sentences = text.split('.')
                    if sentences and len(sentences[0]) > 30:
                        first_sentence = sentences[0].strip() + '.'
                        # Limiter à 150 caractères max
                        if len(first_sentence) > 150:
                            first_sentence = first_sentence[:147] + "..."
                        return first_sentence
        
        return None
    except Exception as e:
        return None

def personalize_meer_kastelen():
    """Personnalise les descriptions 'meer kastelen' avec de vrais extraits"""
    
    base_dir = Path("/Users/marc/Desktop/kastelenbelgie")
    
    print("📝 PERSONNALISATION DES DESCRIPTIONS 'MEER KASTELEN'")
    print("=" * 55)
    
    # Créer un cache des descriptions extraites
    descriptions_cache = {}
    
    print("🔍 Extraction des descriptions des pages châteaux...")
    
    # Parcourir toutes les pages châteaux pour extraire les descriptions
    for html_file in base_dir.glob("*.html"):
        # Ignorer les pages non-châteaux
        if html_file.name in ['index.html', 'contact.html', 'blog.html', 'provinces.html', 
                             'antwerpen.html', 'limburg.html', 'oost-vlaanderen.html', 
                             'west-vlaanderen.html', 'vlaams-brabant.html', 'namen.html',
                             'luxemburg.html', 'luik.html', 'henegouwen.html', 'waals-brabant.html']:
            continue
        
        if html_file.name.startswith('blog-'):
            continue
        
        description = extract_first_sentence(html_file)
        if description:
            descriptions_cache[html_file.name] = description
    
    print(f"✅ {len(descriptions_cache)} descriptions extraites")
    
    files_processed = 0
    files_modified = 0
    descriptions_updated = 0
    
    # Maintenant, mettre à jour les sections "meer kastelen"
    for html_file in base_dir.glob("*.html"):
        # Traiter seulement les pages châteaux
        if html_file.name in ['index.html', 'contact.html', 'blog.html', 'provinces.html', 
                             'antwerpen.html', 'limburg.html', 'oost-vlaanderen.html', 
                             'west-vlaanderen.html', 'vlaams-brabant.html', 'namen.html',
                             'luxemburg.html', 'luik.html', 'henegouwen.html', 'waals-brabant.html']:
            continue
        
        if html_file.name.startswith('blog-'):
            continue
        
        files_processed += 1
        
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Chercher les liens vers d'autres châteaux dans la section "meer kastelen"
            # Pattern pour trouver les liens vers les châteaux
            link_pattern = r'<a href="([^"]+\.html)" class="btn-modern btn-primary-modern">Meer info</a>'
            links = re.findall(link_pattern, content)
            
            for link in links:
                if link in descriptions_cache:
                    # Chercher la description générique correspondante
                    # Pattern pour trouver la description avant ce lien
                    desc_pattern = rf'<p class="card-description-modern">([^<]+)</p>\s*<a href="{re.escape(link)}"'
                    match = re.search(desc_pattern, content)
                    
                    if match:
                        old_description = match.group(1)
                        new_description = descriptions_cache[link]
                        
                        # Remplacer seulement si c'est une description générique
                        if any(generic in old_description for generic in [
                            "Ontdek dit prachtige kasteel",
                            "Een kasteel met een fascinerende geschiedenis",
                            "De provincie",
                            "nog vele andere interessante activiteiten"
                        ]):
                            content = content.replace(old_description, new_description)
                            descriptions_updated += 1
            
            if content != original_content:
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                files_modified += 1
                print(f"✅ {html_file.name} - Descriptions personnalisées")
        
        except Exception as e:
            print(f"❌ Erreur avec {html_file.name}: {e}")
    
    print(f"\n📊 RÉSULTATS:")
    print(f"   Fichiers traités: {files_processed}")
    print(f"   Fichiers modifiés: {files_modified}")
    print(f"   Descriptions mises à jour: {descriptions_updated}")
    
    if files_modified > 0:
        print(f"\n🎉 Descriptions personnalisées!")
        print("   - Phrases complètes extraites des pages châteaux")
        print("   - Plus de descriptions génériques")
        print("   - Contenu authentique et informatif")
        print("   - Meilleure expérience utilisateur")
    else:
        print("\n✨ Descriptions déjà personnalisées!")

if __name__ == "__main__":
    personalize_meer_kastelen()
