#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
TEST DU SYSTÈME CORRIGÉ DE GÉNÉRATION
"""

from complete_castle_generator_fixed import CompleteCastleGenerator

def test_corrected_system():
    generator = CompleteCastleGenerator()
    
    # Test avec Kasteel van Durbuy
    test_row = {
        'Title': 'Kasteel van Durbuy',
        'URL': 'https://kastelenbelgie.be/nl/kasteel-van-durbuy-durbuy/',
        'Provincie': 'Luxemburg',
        'FORMATTED_ADDRESS': '6940 Durbuy',
        'OPENING_HOURS_TEXT': 'Contacteer het kasteel voor actuele openingsuren',
        'CAN_VISIT': 'yes'
    }
    
    print("🧪 TEST SYSTÈME CORRIGÉ")
    print("=" * 50)
    
    result = generator.create_complete_castle_page(test_row)
    
    if result:
        print("✅ Page générée avec succès")
    else:
        print("❌ Échec génération")

if __name__ == "__main__":
    test_corrected_system()
