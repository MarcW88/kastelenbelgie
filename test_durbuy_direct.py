#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
TEST DIRECT POUR DURBUY
"""

from advanced_wikipedia_scraper import AdvancedWikipediaScraper

def test_durbuy_direct():
    scraper = AdvancedWikipediaScraper()
    
    # Test direct avec "Durbuy" (ville)
    print("🔍 Test direct avec 'Durbuy'...")
    result = scraper.scrape_castle_info("Durbuy", "Luxemburg")
    
    if result:
        print(f"✅ Trouvé: {result['source_title']} ({result['source_language']})")
        print(f"Mots: {result['word_count']}")
        print(f"Paragraphes: {len(result['paragraphs'])}")
        for i, p in enumerate(result['paragraphs'], 1):
            print(f"  {i}. ({len(p.split())} mots) {p[:100]}...")
    else:
        print("❌ Pas trouvé")

if __name__ == "__main__":
    test_durbuy_direct()
