#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
TEST SPÉCIFIQUE POUR KASTEEL VAN DURBUY ET BEAUREGARD
"""

import csv
from complete_castle_generator_fixed import CompleteCastleGenerator

def test_specific_castles():
    """Test sur châteaux spécifiques pour vérifier le scraping"""
    csv_file = "/Users/marc/Desktop/kastelenbelgie/chateaux_opening_hours - chateaux_opening_hours.csv"
    
    print("🧪 TEST SPÉCIFIQUE CHÂTEAUX")
    print("=" * 50)
    
    generator = CompleteCastleGenerator()
    
    # Châteaux de test spécifiques
    test_targets = [
        "Kasteel van Durbuy",
        "Kasteel Beauregard"
    ]
    
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            title = row.get('Title', '')
            
            if any(target in title for target in test_targets):
                print(f"\n🏰 TEST DÉTAILLÉ: {title}")
                print("-" * 50)
                
                # Test direct du scraper Wikipedia
                print("🔍 Test scraper Wikipedia direct:")
                wiki_result = generator.wikipedia_scraper.scrape_castle_info(
                    title, 
                    row.get('Provincie', ''),
                    ""
                )
                
                if wiki_result:
                    print(f"✅ WIKIPEDIA TROUVÉ:")
                    print(f"  Source: {wiki_result['source_title']} ({wiki_result['source_language']})")
                    print(f"  Mots: {wiki_result['word_count']}")
                    print(f"  Similarité: {wiki_result['similarity_score']:.2f}")
                    print(f"  Paragraphes:")
                    for i, p in enumerate(wiki_result['paragraphs'], 1):
                        print(f"    {i}. {p[:100]}...")
                else:
                    print("❌ WIKIPEDIA: Rien trouvé")
                
                print()
                
                # Test complet de génération
                try:
                    filename = generator.create_complete_castle_page(row)
                    if filename:
                        print(f"✅ PAGE GÉNÉRÉE: {filename}.html")
                    else:
                        print(f"❌ ÉCHEC: Pas de fichier créé")
                        
                except Exception as e:
                    print(f"❌ ERREUR: {e}")
                
                print("=" * 50)
    
    print("\n📊 STATISTIQUES FINALES:")
    print(f"Wikipedia trouvé: {generator.stats['wikipedia_found']}")
    print(f"Images trouvées: {generator.stats['images_found']}")
    print(f"Coordonnées GPS: {generator.stats['coordinates_found']}")

if __name__ == "__main__":
    test_specific_castles()
