#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
TEST RECHERCHE SIMPLE WIKIPEDIA
"""

from advanced_wikipedia_scraper import AdvancedWikipediaScraper

def test_simple_search():
    scraper = AdvancedWikipediaScraper()
    
    # Test direct avec l'API Wikipedia
    print("🔍 Test direct API Wikipedia pour 'Durbuy'...")
    
    # Test de récupération directe
    wiki_data = scraper.get_full_wikipedia_content("Durbuy", "nl")
    
    if wiki_data:
        print(f"✅ Page trouvée: {wiki_data['title']}")
        print(f"Langue: {wiki_data['language']}")
        print(f"Mots bruts: {wiki_data['word_count']}")
        print(f"Contenu (300 premiers chars): {wiki_data['content'][:300]}...")
        
        # Test du traitement
        paragraphs = scraper.process_wikipedia_content(wiki_data['content'], 300)
        print(f"\nParagraphes traités: {len(paragraphs)}")
        for i, p in enumerate(paragraphs, 1):
            print(f"  {i}. ({len(p.split())} mots) {p[:100]}...")
    else:
        print("❌ Page non trouvée")

if __name__ == "__main__":
    test_simple_search()
