#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
GÉNÉRATION COMPLÈTE DES 262 PAGES CHÂTEAUX - VERSION CORRIGÉE
Utilise le nouveau système de contenu spécifique aux châteaux
"""

import csv
import time
from complete_castle_generator_fixed import CompleteCastleGenerator

def generate_all_castles_corrected():
    """Génère toutes les pages châteaux avec le système corrigé"""
    csv_file = "/Users/marc/Desktop/kastelenbelgie/chateaux_opening_hours - chateaux_opening_hours.csv"
    
    print("🚀 GÉNÉRATION COMPLÈTE DES PAGES CHÂTEAUX - VERSION CORRIGÉE")
    print("=" * 70)
    print("✅ Contenu spécifique aux châteaux (pas de mélange)")
    print("✅ Provinces corrigées (122 corrections)")
    print("✅ Images réelles intégrées")
    print("✅ Coordonnées GPS précises")
    print("=" * 70)
    
    generator = CompleteCastleGenerator()
    
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            total_rows = sum(1 for row in reader)
            f.seek(0)
            reader = csv.DictReader(f)
            
            print(f"📊 {total_rows} châteaux à traiter")
            print()
            
            processed = 0
            successful = 0
            skipped = 0
            
            for i, row in enumerate(reader, 1):
                title = row.get('Title', '')
                
                # Ignorer les pages d'index
                if any(skip in title.lower() for skip in ['kastelen per provincie', 'kastelen in', 'home', 'kaart']):
                    skipped += 1
                    continue
                
                print(f"[{i}/{total_rows}] Traitement de: {title}")
                
                try:
                    result = generator.create_complete_castle_page(row)
                    
                    if result:
                        successful += 1
                        print(f"  ✅ Succès")
                    else:
                        print(f"  ⚠️ Ignoré (pas assez de contenu)")
                    
                    processed += 1
                    
                    # Pause pour éviter la surcharge
                    if processed % 10 == 0:
                        print(f"\n📊 Progression: {processed} traités, {successful} réussis")
                        print("⏸️ Pause 2 secondes...")
                        time.sleep(2)
                    else:
                        time.sleep(0.5)
                        
                except Exception as e:
                    print(f"  ❌ Erreur: {e}")
                    generator.stats['errors'].append(f"{title}: {e}")
                    continue
    
    except Exception as e:
        print(f"❌ Erreur lecture CSV: {e}")
        return
    
    # Statistiques finales
    print("\n" + "=" * 70)
    print("📊 STATISTIQUES FINALES")
    print("=" * 70)
    print(f"Total traité: {processed}")
    print(f"Pages générées: {successful}")
    print(f"Pages ignorées: {skipped}")
    print(f"Contenu généré: {generator.stats['wikipedia_found']}")
    print(f"Images trouvées: {generator.stats['images_found']}")
    print(f"Coordonnées GPS: {generator.stats['coordinates_found']}")
    
    if generator.stats['errors']:
        print(f"\n❌ Erreurs ({len(generator.stats['errors'])}):")
        for error in generator.stats['errors'][:10]:  # Afficher les 10 premières
            print(f"  - {error}")
        if len(generator.stats['errors']) > 10:
            print(f"  ... et {len(generator.stats['errors'])-10} autres")
    
    success_rate = (successful / processed * 100) if processed > 0 else 0
    print(f"\n🎯 Taux de réussite: {success_rate:.1f}%")
    print("✅ Génération terminée !")

if __name__ == "__main__":
    generate_all_castles_corrected()
