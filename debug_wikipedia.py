#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
DEBUG WIKIPEDIA SCRAPER
"""

from advanced_wikipedia_scraper import AdvancedWikipediaScraper

def debug_wikipedia():
    scraper = AdvancedWikipediaScraper()
    
    # Test direct de récupération de contenu
    print("🔍 Test récupération contenu Durbuy...")
    
    wiki_data = scraper.get_full_wikipedia_content("Durbuy", "nl")
    
    if wiki_data:
        print(f"✅ Contenu trouvé:")
        print(f"  Titre: {wiki_data['title']}")
        print(f"  Langue: {wiki_data['language']}")
        print(f"  Mots: {wiki_data['word_count']}")
        print(f"  Contenu (premiers 500 chars): {wiki_data['content'][:500]}...")
        
        # Test du traitement
        paragraphs = scraper.process_wikipedia_content(wiki_data['content'], 300)
        print(f"\n📄 Paragraphes traités: {len(paragraphs)}")
        for i, p in enumerate(paragraphs, 1):
            print(f"  {i}. ({len(p.split())} mots) {p[:100]}...")
    else:
        print("❌ Pas de contenu trouvé")

if __name__ == "__main__":
    debug_wikipedia()
