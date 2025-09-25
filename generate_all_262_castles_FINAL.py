#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
GÉNÉRATION FINALE DE TOUTES LES 262 PAGES CHÂTEAUX
Version complète avec Wikipedia, images, GPS et related castles
"""

import os
import csv
import time
from complete_castle_generator_fixed import CompleteCastleGenerator

def main():
    """Fonction principale pour générer toutes les pages châteaux"""
    csv_file = "/Users/marc/Desktop/kastelenbelgie/chateaux_opening_hours - chateaux_opening_hours.csv"
    
    print("🏰 GÉNÉRATION FINALE DE TOUTES LES PAGES CHÂTEAUX")
    print("=" * 70)
    print("✅ Wikipedia scraping avancé (300+ mots minimum)")
    print("✅ Images depuis chateaux_images_update-2 (seuil 50%)")
    print("✅ Coordonnées GPS depuis chateaux_coord.csv")
    print("✅ Related castles avec images et descriptions")
    print("✅ Liens avec ancres spécifiques (provincie X)")
    print("=" * 70)
    print(f"📄 Lecture du fichier: {csv_file}")
    
    if not os.path.exists(csv_file):
        print(f"❌ Fichier CSV non trouvé: {csv_file}")
        return
    
    # Initialiser le générateur
    generator = CompleteCastleGenerator()
    
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
                title = row.get('Title', 'Sans titre')
                print(f"\n[{i}/{total_rows}] Traitement de: {title}")
                
                try:
                    if generator.should_skip_entry(row):
                        print(f"  ⏭️ Ignoré (page d'index ou non-château)")
                        skipped_pages.append(title)
                        continue
                    
                    # Créer la page complète
                    filename = generator.create_complete_castle_page(row)
                    
                    if filename:
                        created_pages.append(filename)
                        print(f"  🎉 Succès: {filename}.html")
                        
                        # Pause entre les châteaux pour respecter les APIs
                        if i % 10 == 0:  # Pause plus longue tous les 10 châteaux
                            print(f"  ⏸️ Pause de 10 secondes (traité {i} châteaux)")
                            time.sleep(10)
                        else:
                            time.sleep(3)
                    
                except Exception as e:
                    error_msg = f"Erreur avec {title}: {e}"
                    print(f"  ❌ {error_msg}")
                    errors.append(error_msg)
                    generator.stats['errors'].append(error_msg)
                    continue
    
    except Exception as e:
        print(f"❌ Erreur lecture CSV: {e}")
        return
    
    # Rapport final détaillé
    print(f"\n{'='*70}")
    print("📊 RAPPORT FINAL COMPLET")
    print(f"{'='*70}")
    print(f"✅ Pages créées: {len(created_pages)}")
    print(f"⏭️ Pages ignorées: {len(skipped_pages)}")
    print(f"❌ Erreurs: {len(errors)}")
    print(f"📈 TOTAL PAGES CHÂTEAUX: {len(created_pages)} pages")
    
    print(f"\n📊 STATISTIQUES DÉTAILLÉES:")
    print(f"🔍 Wikipedia trouvé: {generator.stats['wikipedia_found']}/{generator.stats['total_processed']} ({generator.stats['wikipedia_found']/max(generator.stats['total_processed'],1)*100:.1f}%)")
    print(f"🖼️ Images trouvées: {generator.stats['images_found']}/{generator.stats['total_processed']} ({generator.stats['images_found']/max(generator.stats['total_processed'],1)*100:.1f}%)")
    print(f"📍 Coordonnées GPS: {generator.stats['coordinates_found']}/{generator.stats['total_processed']} ({generator.stats['coordinates_found']/max(generator.stats['total_processed'],1)*100:.1f}%)")
    
    if errors:
        print(f"\n⚠️ ERREURS RENCONTRÉES:")
        for error in errors[:10]:  # Limiter à 10 erreurs
            print(f"  • {error}")
        if len(errors) > 10:
            print(f"  ... et {len(errors)-10} autres erreurs")
    
    print(f"\n🎯 AMÉLIORATIONS APPORTÉES:")
    print("1. ✅ Scraping Wikipedia avancé avec 300+ mots minimum")
    print("2. ✅ Images automatiques depuis chateaux_images_update-2")
    print("3. ✅ Coordonnées GPS précises pour les cartes")
    print("4. ✅ Related castles avec images et descriptions Wikipedia")
    print("5. ✅ Liens avec ancres spécifiques 'provincie X'")
    print("6. ✅ Formulaires de réservation conditionnels")
    
    print(f"\n🚀 PROCHAINES ÉTAPES:")
    print("1. Configurer la clé API Google Maps (remplacer YOUR_API_KEY)")
    print("2. Vérifier les liens internes entre pages")
    print("3. Tester les formulaires de réservation")
    print("4. Optimiser les images pour le web")
    
    print(f"\n🎊 FÉLICITATIONS ! {len(created_pages)} pages châteaux générées avec succès !")

if __name__ == "__main__":
    main()
