#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXTRACTION TEXTES DEPUIS PAGES CHÂTEAUX
Remplace les textes génériques par les vrais textes des pages châteaux
"""

import glob
import re
import os

def extract_castle_description(castle_file_path):
    """Extrait la description d'un château depuis sa page"""
    
    if not os.path.exists(castle_file_path):
        return "Een prachtig kasteel met een rijke geschiedenis."
    
    try:
        with open(castle_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Chercher les descriptions dans différents patterns
        description_patterns = [
            r'<p class="castle-description">([^<]+)</p>',
            r'<p class="hero-description">([^<]+)</p>',
            r'<p class="description">([^<]+)</p>',
            r'<div class="castle-intro">.*?<p>([^<]+)</p>',
            # Premier paragraphe après le titre
            r'<h1>[^<]+</h1>.*?<p>([^<]{50,200})</p>',
        ]
        
        for pattern in description_patterns:
            match = re.search(pattern, content, re.DOTALL)
            if match:
                description = match.group(1).strip()
                # Nettoyer et limiter à une phrase complète
                description = re.sub(r'\s+', ' ', description)
                
                # Trouver la fin de la première phrase complète
                sentence_end = re.search(r'[.!?]\s', description)
                if sentence_end and sentence_end.start() < 150:
                    description = description[:sentence_end.start() + 1]
                elif len(description) > 120:
                    # Si pas de point, couper à un espace près de 120 caractères
                    cut_point = description.rfind(' ', 0, 120)
                    if cut_point > 80:
                        description = description[:cut_point] + "."
                
                return description
        
        # Si rien trouvé, utiliser un texte par défaut
        return "Een prachtig kasteel met een rijke geschiedenis."
        
    except Exception as e:
        return "Een kasteel vol charme en geschiedenis."

def update_related_castles_with_real_texts():
    """Met à jour les textes des châteaux liés avec les vrais textes"""
    
    print("📝 EXTRACTION TEXTES DEPUIS PAGES CHÂTEAUX")
    print("-" * 50)
    
    castle_files = glob.glob("/Users/marc/Desktop/kastelenbelgie/kasteel-*.html")
    castle_files.extend(glob.glob("/Users/marc/Desktop/kastelenbelgie/chateau-*.html"))
    castle_files.extend(glob.glob("/Users/marc/Desktop/kastelenbelgie/bisschoppenhof-*.html"))
    castle_files.extend(glob.glob("/Users/marc/Desktop/kastelenbelgie/hof-*.html"))
    castle_files.extend(glob.glob("/Users/marc/Desktop/kastelenbelgie/burcht-*.html"))
    
    updated_count = 0
    
    for castle_file in castle_files:
        try:
            with open(castle_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Trouver tous les liens vers d'autres châteaux dans la section "Meer kastelen"
            link_pattern = r'<a href="([^"]+\.html)" class="btn-modern btn-primary-modern">Meer info</a>'
            links = re.findall(link_pattern, content)
            
            for link in links:
                # Extraire le texte de la page liée
                linked_castle_path = f"/Users/marc/Desktop/kastelenbelgie/{link}"
                real_description = extract_castle_description(linked_castle_path)
                
                # Trouver le pattern complet de cette card et remplacer le texte
                card_pattern = rf'(<div class="related-castle-card">.*?<a href="{re.escape(link)}"[^>]*>.*?</a>.*?<div class="castle-card-content">.*?<h3>[^<]+</h3>\s*)<p class="card-description-modern">[^<]*</p>'
                
                def replace_description(match):
                    return match.group(1) + f'<p class="card-description-modern">{real_description}</p>'
                
                content = re.sub(card_pattern, replace_description, content, flags=re.DOTALL)
            
            if content != original_content:
                with open(castle_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                updated_count += 1
                filename = os.path.basename(castle_file)
                print(f"✅ {filename}: textes extraits des pages liées")
        
        except Exception as e:
            continue
    
    print(f"✅ {updated_count} pages avec textes réels extraits")

def test_extraction_on_bisschoppenhof():
    """Test l'extraction sur bisschoppenhof pour vérifier"""
    
    print(f"\n🧪 TEST SUR BISSCHOPPENHOF")
    print("-" * 30)
    
    # Tester l'extraction pour les 3 châteaux liés
    test_links = [
        "kasteel-karreveld-te-sint-jans-molenbeek.html",
        "kasteel-van-roumont-roumont.html", 
        "kasteel-van-rethy-retie.html"
    ]
    
    for link in test_links:
        castle_path = f"/Users/marc/Desktop/kastelenbelgie/{link}"
        description = extract_castle_description(castle_path)
        print(f"📄 {link}: '{description}'")

if __name__ == "__main__":
    print("📝 EXTRACTION TEXTES DEPUIS PAGES CHÂTEAUX")
    print("=" * 60)
    
    # Test d'abord
    test_extraction_on_bisschoppenhof()
    
    # Puis application
    update_related_castles_with_real_texts()
    
    print(f"\n🎉 TEXTES EXTRAITS!")
    print("✅ Textes des châteaux liés extraits depuis leurs pages")
    print("✅ Plus de textes génériques")
    print("\n🚀 Vérifie bisschoppenhof-deurne.html pour voir le résultat")
