#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
TERMINER LES 19 CHÂTEAUX RESTANTS
"""

import csv
import os
import glob
from complete_castle_generator_fixed import CompleteCastleGenerator

def get_existing_castle_files():
    """Obtient la liste des fichiers HTML de châteaux existants"""
    patterns = [
        "kasteel-*.html", "hof-*.html", "het-*.html", "de-*.html", 
        "sint-*.html", "chateau-*.html", "burcht-*.html", "paleis-*.html",
        "commanderij-*.html", "waterkasteel-*.html", "waterburcht-*.html",
        "koninklijk-*.html", "gaverkasteel-*.html"
    ]
    
    existing_files = set()
    for pattern in patterns:
        files = glob.glob(f"/Users/marc/Desktop/kastelenbelgie/{pattern}")
        for file in files:
            basename = os.path.basename(file).replace('.html', '')
            existing_files.add(basename)
    
    return existing_files

def finish_remaining_castles():
    """Termine la génération des châteaux restants"""
    csv_file = "/Users/marc/Desktop/kastelenbelgie/chateaux_opening_hours - chateaux_opening_hours.csv"
    
    print("🏁 TERMINER LES CHÂTEAUX RESTANTS")
    print("=" * 50)
    
    # Obtenir les fichiers existants
    existing_files = get_existing_castle_files()
    print(f"📊 {len(existing_files)} châteaux déjà générés")
    
    generator = CompleteCastleGenerator()
    
    remaining_count = 0
    processed = 0
    
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            
            for row in reader:
                title = row.get('Title', '')
                url = row.get('URL', '')
                
                # Ignorer les pages d'index
                if any(skip in title.lower() for skip in ['kastelen per provincie', 'kastelen in', 'home', 'kaart']):
                    continue
                
                # Obtenir le nom du fichier
                filename = generator.get_filename_from_url(url)
                
                # Vérifier si le fichier existe déjà
                if filename in existing_files:
                    continue
                
                remaining_count += 1
                print(f"\n[{remaining_count}] 🏰 {title}")
                
                try:
                    result = generator.create_complete_castle_page(row)
                    
                    if result:
                        processed += 1
                        print(f"  ✅ Généré avec succès")
                    else:
                        print(f"  ⚠️ Ignoré")
                        
                except Exception as e:
                    print(f"  ❌ Erreur: {e}")
                    continue
    
    except Exception as e:
        print(f"❌ Erreur: {e}")
        return
    
    print(f"\n📊 RÉSULTATS:")
    print(f"Châteaux restants traités: {remaining_count}")
    print(f"Pages générées: {processed}")
    
    # Vérification finale
    final_files = get_existing_castle_files()
    print(f"Total final: {len(final_files)}/262 châteaux")
    
    if len(final_files) >= 260:
        print("🎉 GÉNÉRATION QUASI-COMPLÈTE !")
    else:
        remaining = 262 - len(final_files)
        print(f"⏳ Encore {remaining} châteaux à traiter")

if __name__ == "__main__":
    finish_remaining_castles()
