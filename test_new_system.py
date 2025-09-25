#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
TEST DU NOUVEAU SYSTÈME SUR QUELQUES CHÂTEAUX
"""

import csv
from complete_castle_generator_fixed import CompleteCastleGenerator

def test_new_system():
    """Test sur 3 châteaux pour vérifier le système"""
    csv_file = "/Users/marc/Desktop/kastelenbelgie/chateaux_opening_hours - chateaux_opening_hours.csv"
    
    print("🧪 TEST DU NOUVEAU SYSTÈME")
    print("=" * 50)
    
    generator = CompleteCastleGenerator()
    
    # Châteaux de test
    test_targets = [
        "Kasteel Beauregard",
        "Kasteel van Freyr", 
        "Hof ter Borght"
    ]
    
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            title = row.get('Title', '')
            
            if any(target in title for target in test_targets):
                print(f"\n🏰 TEST: {title}")
                print("-" * 40)
                
                try:
                    filename = generator.create_complete_castle_page(row)
                    if filename:
                        print(f"✅ SUCCÈS: {filename}.html créé")
                    else:
                        print(f"❌ ÉCHEC: Pas de fichier créé")
                        
                except Exception as e:
                    print(f"❌ ERREUR: {e}")
                
                print()
    
    print("📊 STATISTIQUES DU TEST:")
    print(f"Wikipedia trouvé: {generator.stats['wikipedia_found']}")
    print(f"Images trouvées: {generator.stats['images_found']}")
    print(f"Coordonnées GPS: {generator.stats['coordinates_found']}")

if __name__ == "__main__":
    test_new_system()
