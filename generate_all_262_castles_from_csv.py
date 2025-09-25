#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
GÉNÉRATION DE TOUTES LES 262 PAGES CHÂTEAUX DEPUIS CSV
Lit le fichier chateaux_opening_hours.csv et génère toutes les pages
"""

import os
import re
import csv
import time
import requests
from urllib.parse import quote, urlparse

# Configuration Wikipedia
WIKIPEDIA_SEARCH_API = "https://fr.wikipedia.org/w/api.php"
WIKIPEDIA_NL_API = "https://nl.wikipedia.org/w/api.php"

def search_wikipedia_multi_language(castle_name, location=""):
    """Recherche un château sur Wikipedia FR et NL"""
    try:
        search_terms = [
            castle_name,
            castle_name.replace("Kasteel", "Château"),
            castle_name.replace("van", "de"),
            f"{castle_name} {location}",
            f"Château {castle_name.replace('Kasteel', '').strip()}"
        ]
        
        # Essayer d'abord en français
        for term in search_terms:
            params = {
                'action': 'query',
                'format': 'json',
                'list': 'search',
                'srsearch': term,
                'srlimit': 3
            }
            
            response = requests.get(WIKIPEDIA_SEARCH_API, params=params, timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data.get('query', {}).get('search'):
                    return data['query']['search'][0]['title'], 'fr'
            
            time.sleep(0.5)
        
        # Essayer en néerlandais
        for term in search_terms:
            params = {
                'action': 'query',
                'format': 'json',
                'list': 'search',
                'srsearch': term,
                'srlimit': 3
            }
            
            response = requests.get(WIKIPEDIA_NL_API, params=params, timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data.get('query', {}).get('search'):
                    return data['query']['search'][0]['title'], 'nl'
            
            time.sleep(0.5)
        
        return None, None
    except Exception as e:
        print(f"Erreur recherche Wikipedia pour {castle_name}: {e}")
        return None, None

def get_wikipedia_content(page_title, language='fr'):
    """Récupère le contenu Wikipedia d'une page"""
    try:
        api_url = WIKIPEDIA_SEARCH_API if language == 'fr' else WIKIPEDIA_NL_API
        
        params = {
            'action': 'query',
            'format': 'json',
            'titles': page_title,
            'prop': 'extracts',
            'exintro': True,
            'explaintext': True,
            'exsectionformat': 'plain'
        }
        
        response = requests.get(api_url, params=params, timeout=10)
        if response.status_code == 200:
            data = response.json()
            pages = data.get('query', {}).get('pages', {})
            for page_id, page_info in pages.items():
                if 'extract' in page_info:
                    return page_info['extract']
        
        return None
    except Exception as e:
        print(f"Erreur récupération contenu Wikipedia: {e}")
        return None

def generate_rich_content(castle_name, province, wiki_content=None):
    """Génère un contenu riche pour le château"""
    if wiki_content and len(wiki_content) > 200:
        # Nettoyer et utiliser le contenu Wikipedia
        content = re.sub(r'\[.*?\]', '', wiki_content)
        content = re.sub(r'\s+', ' ', content).strip()
        
        # Diviser en 3 paragraphes
        sentences = re.split(r'[.!?]+', content)
        sentences = [s.strip() for s in sentences if len(s.strip()) > 20]
        
        paragraphs = []
        sentences_per_paragraph = max(1, len(sentences) // 3)
        
        for i in range(0, len(sentences), sentences_per_paragraph):
            paragraph_sentences = sentences[i:i + sentences_per_paragraph]
            paragraph = '. '.join(paragraph_sentences)
            if paragraph and not paragraph.endswith('.'):
                paragraph += '.'
            paragraphs.append(paragraph)
        
        # S'assurer d'avoir exactement 3 paragraphes
        while len(paragraphs) < 3:
            paragraphs.append(f"Dit kasteel vertegenwoordigt een belangrijk onderdeel van het Belgische culturele erfgoed in {province}.")
        
        return paragraphs[:3]
    
    # Contenu par défaut enrichi
    return [
        f"{castle_name} is een historisch kasteel dat een belangrijke rol heeft gespeeld in de geschiedenis van {province}. Dit prachtige monument getuigt van eeuwen van architecturale evolutie en cultureel erfgoed dat kenmerkend is voor de Belgische kastelen.",
        f"Het kasteel heeft door de jaren heen verschillende eigenaren gekend en heeft meerdere renovaties ondergaan die de architecturale stijlen van verschillende periodes weerspiegelen. De structuur combineert elementen uit verschillende bouwperiodes.",
        f"Vandaag de dag staat {castle_name} als een symbool van het rijke historische erfgoed van {province} en trekt het bezoekers van over de hele wereld aan."
    ]

def get_filename_from_url(url):
    """Extraire le nom du fichier de l'URL"""
    url_path = urlparse(url).path
    filename = url_path.split('/')[-2] if url_path.endswith('/') else url_path.split('/')[-1]
    return filename if filename else "kasteel"

def should_skip_entry(row):
    """Détermine si une entrée doit être ignorée"""
    skip_keywords = [
        "kastelen per provincie", "kastelen in", "kastelen-", 
        "kaart", "home", "belgië"
    ]
    
    title = row.get('Title', '').lower()
    return any(keyword in title for keyword in skip_keywords)

from create_castle_page_function import create_castle_page_from_csv_row

def main():
    """Fonction principale"""
    csv_file = "/Users/marc/Desktop/kastelenbelgie/chateaux_opening_hours - chateaux_opening_hours.csv"
    
    print("🏰 GÉNÉRATION DE TOUTES LES PAGES CHÂTEAUX DEPUIS CSV")
    print("=" * 70)
    print(f"📄 Lecture du fichier: {csv_file}")
    
    if not os.path.exists(csv_file):
        print(f"❌ Fichier CSV non trouvé: {csv_file}")
        return
    
    created_pages = []
    skipped_pages = []
    errors = []
    
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            total_rows = sum(1 for row in reader)
            f.seek(0)  # Retour au début
            reader = csv.DictReader(f)
            
            print(f"📊 Total d'entrées trouvées: {total_rows}")
            print()
            
            for i, row in enumerate(reader, 1):
                print(f"\n[{i}/{total_rows}] Traitement de: {row.get('Title', 'Sans titre')}")
                
                try:
                    if should_skip_entry(row):
                        print(f"  ⏭️ Ignoré (page d'index ou non-château)")
                        skipped_pages.append(row.get('Title', 'Sans titre'))
                        continue
                    
                    filename = create_castle_page_from_csv_row(
                        row, 
                        search_wikipedia_multi_language,
                        get_wikipedia_content,
                        generate_rich_content,
                        get_filename_from_url
                    )
                    
                    if filename:
                        created_pages.append(filename)
                        time.sleep(3)  # Pause entre les requêtes
                    
                except Exception as e:
                    error_msg = f"Erreur avec {row.get('Title', 'Sans titre')}: {e}"
                    print(f"  ❌ {error_msg}")
                    errors.append(error_msg)
                    continue
    
    except Exception as e:
        print(f"❌ Erreur lecture CSV: {e}")
        return
    
    # Rapport final
    print(f"\n{'='*70}")
    print("📊 RAPPORT FINAL")
    print(f"{'='*70}")
    print(f"✅ Pages créées: {len(created_pages)}")
    print(f"⏭️ Pages ignorées: {len(skipped_pages)}")
    print(f"❌ Erreurs: {len(errors)}")
    print(f"📈 TOTAL PAGES CHÂTEAUX: {len(created_pages)} pages")
    
    if errors:
        print(f"\n⚠️ ERREURS RENCONTRÉES:")
        for error in errors[:10]:  # Limiter à 10 erreurs
            print(f"  • {error}")
    
    print(f"\n🎯 PROCHAINES ÉTAPES:")
    print("1. Configurer la clé API Google Maps")
    print("2. Ajouter de vraies images de châteaux")
    print("3. Tester les formulaires de réservation")
    print("4. Vérifier les liens internes")
    
if __name__ == "__main__":
    main()
