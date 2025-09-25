#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ANALYSE DES ERREURS DE PROVINCES
Détecte les châteaux mal assignés aux provinces
"""

import glob
import re
import csv
from collections import defaultdict

def analyze_province_errors():
    """Analyse les erreurs de provinces dans les pages châteaux"""
    
    print("🔍 ANALYSE DES ERREURS DE PROVINCES")
    print("=" * 50)
    
    # Charger les données correctes des châteaux
    correct_provinces = load_correct_castle_data()
    
    # Analyser les pages châteaux
    castle_files = glob.glob("/Users/marc/Desktop/kastelenbelgie/kasteel-*.html")
    castle_files.extend(glob.glob("/Users/marc/Desktop/kastelenbelgie/chateau-*.html"))
    castle_files.extend(glob.glob("/Users/marc/Desktop/kastelenbelgie/hof-*.html"))
    castle_files.extend(glob.glob("/Users/marc/Desktop/kastelenbelgie/burcht-*.html"))
    
    errors = []
    
    for castle_file in castle_files:
        try:
            with open(castle_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extraire le nom du château et la province de la page
            castle_name = extract_castle_name(content, castle_file)
            page_province = extract_province_from_page(content)
            
            if castle_name and page_province:
                # Vérifier si c'est correct
                correct_province = find_correct_province(castle_name, correct_provinces)
                
                if correct_province and correct_province.lower() != page_province.lower():
                    errors.append({
                        'file': castle_file.split('/')[-1],
                        'castle_name': castle_name,
                        'current_province': page_province,
                        'correct_province': correct_province
                    })
                    print(f"❌ {castle_name}: {page_province} → {correct_province}")
        
        except Exception as e:
            continue
    
    print(f"\n📊 RÉSULTATS:")
    print(f"Pages châteaux analysées: {len(castle_files)}")
    print(f"Erreurs détectées: {len(errors)}")
    
    return errors

def load_correct_castle_data():
    """Charge les données correctes des châteaux depuis le CSV"""
    
    correct_data = {}
    csv_file = "/Users/marc/Desktop/kastelenbelgie/kastelen_belgie_corrected.csv"
    
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                castle_name = row.get('Kasteel', '').strip()
                province = row.get('Provincie', '').strip()
                if castle_name and province:
                    correct_data[castle_name.lower()] = province
    except Exception as e:
        print(f"⚠️ Erreur lecture CSV: {e}")
    
    return correct_data

def extract_castle_name(content, filename):
    """Extrait le nom du château depuis le contenu ou le nom de fichier"""
    
    # Essayer d'extraire depuis le title
    title_match = re.search(r'<title>([^|]+)', content)
    if title_match:
        return title_match.group(1).strip()
    
    # Essayer depuis le h1
    h1_match = re.search(r'<h1[^>]*>([^<]+)</h1>', content)
    if h1_match:
        return h1_match.group(1).strip()
    
    # Fallback: depuis le nom de fichier
    filename_base = filename.split('/')[-1].replace('.html', '')
    return filename_base.replace('-', ' ').title()

def extract_province_from_page(content):
    """Extrait la province depuis la page château"""
    
    # Chercher dans les métadonnées
    province_match = re.search(r'<strong>Provincie:</strong>\s*<span[^>]*>([^<]+)</span>', content)
    if province_match:
        return province_match.group(1).strip()
    
    # Chercher dans les breadcrumbs
    breadcrumb_match = re.search(r'href="([^"]*\.html)"[^>]*>([^<]*)</a>[^<]*<span[^>]*>›</span>', content)
    if breadcrumb_match:
        return breadcrumb_match.group(2).strip()
    
    return None

def find_correct_province(castle_name, correct_data):
    """Trouve la province correcte pour un château"""
    
    # Recherche exacte
    if castle_name.lower() in correct_data:
        return correct_data[castle_name.lower()]
    
    # Recherche approximative
    for correct_name, province in correct_data.items():
        if castle_name.lower() in correct_name or correct_name in castle_name.lower():
            return province
    
    # Cas spéciaux connus
    special_cases = {
        'braine le chateau': 'Waals-Brabant',
        'kasteel van braine-le-chateau': 'Waals-Brabant',
        'château de braine-le-château': 'Waals-Brabant',
    }
    
    for pattern, province in special_cases.items():
        if pattern in castle_name.lower():
            return province
    
    return None

def analyze_province_pages():
    """Analyse les pages provinces pour voir quels châteaux y sont listés"""
    
    print(f"\n🏛️ ANALYSE DES PAGES PROVINCES")
    print("-" * 40)
    
    province_files = [
        'antwerpen.html', 'limburg.html', 'oost-vlaanderen.html', 
        'west-vlaanderen.html', 'vlaams-brabant.html', 'namen.html',
        'luik.html', 'henegouwen.html', 'luxemburg.html', 
        'waals-brabant.html', 'brussel.html'
    ]
    
    province_castles = {}
    
    for province_file in province_files:
        file_path = f"/Users/marc/Desktop/kastelenbelgie/{province_file}"
        province_name = province_file.replace('.html', '').replace('-', ' ').title()
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extraire les liens vers les châteaux
            castle_links = re.findall(r'href="([^"]*kasteel[^"]*\.html)"', content)
            castle_links.extend(re.findall(r'href="([^"]*chateau[^"]*\.html)"', content))
            castle_links.extend(re.findall(r'href="([^"]*hof[^"]*\.html)"', content))
            
            province_castles[province_name] = castle_links
            print(f"📄 {province_name}: {len(castle_links)} châteaux")
            
        except Exception as e:
            print(f"❌ Erreur avec {province_file}: {e}")
    
    return province_castles

if __name__ == "__main__":
    errors = analyze_province_errors()
    province_castles = analyze_province_pages()
    
    if errors:
        print(f"\n🔧 CORRECTIONS NÉCESSAIRES:")
        for error in errors[:10]:  # Montrer les 10 premiers
            print(f"• {error['castle_name']}: {error['current_province']} → {error['correct_province']}")
        
        if len(errors) > 10:
            print(f"... et {len(errors)-10} autres erreurs")
    else:
        print(f"\n✅ Aucune erreur de province détectée!")
    
    print(f"\n🚀 Prochaine étape: Créer un script de correction automatique")
