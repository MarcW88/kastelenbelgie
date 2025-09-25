#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MISE À JOUR DES PAGES PROVINCES AVEC LISTES DE CHÂTEAUX
Ajoute les listes complètes de châteaux avec images sur chaque page province
"""

from castle_organizer import CastleOrganizer
import re

def update_province_castle_lists():
    """Met à jour toutes les pages provinces avec leurs listes de châteaux"""
    
    print("🏛️ MISE À JOUR DES PAGES PROVINCES AVEC LISTES DE CHÂTEAUX")
    print("=" * 70)
    
    # Charger les données des châteaux
    organizer = CastleOrganizer()
    organizer.load_castles_data()
    
    # Mapping des provinces vers leurs fichiers
    province_files = {
        'Antwerpen': 'antwerpen.html',
        'Limburg': 'limburg.html',
        'Oost-Vlaanderen': 'oost-vlaanderen.html',
        'West-Vlaanderen': 'west-vlaanderen.html',
        'Vlaams-Brabant': 'vlaams-brabant.html',
        'Namen': 'namen.html',
        'Luik': 'luik.html',
        'Henegouwen': 'henegouwen.html',
        'Luxemburg': 'luxemburg.html',
        'Waals-Brabant': 'waals-brabant.html',
        'Brussel': 'brussel.html'
    }
    
    updated_count = 0
    
    for province, filename in province_files.items():
        file_path = f"/Users/marc/Desktop/kastelenbelgie/{filename}"
        
        try:
            # Lire le fichier de la province
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Générer la liste HTML des châteaux pour cette province
            castle_list_html = organizer.generate_province_castle_list_html(province)
            
            if not castle_list_html:
                print(f"⚠️ Aucun château trouvé pour {province}")
                continue
            
            # Créer la section complète
            castle_section = f'''
    <!-- Section Châteaux de la Province -->
    <section class="province-castles-section">
        <div class="container">
            <h2 class="section-title">Kastelen in {province}</h2>
            <p class="section-description">Ontdek alle prachtige kastelen in de provincie {province}</p>
            {castle_list_html}
        </div>
    </section>
'''
            
            # Chercher la section avec les cards génériques à remplacer
            cards_pattern = r'<!-- Kastelen Grid -->.*?<section class="section">.*?</section>'
            cards_match = re.search(cards_pattern, content, re.DOTALL)
            
            if cards_match:
                # Remplacer la section cards par la vraie liste de châteaux
                new_content = content[:cards_match.start()] + castle_section + content[cards_match.end():]
                
                # Sauvegarder
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                castle_count = len(organizer.castles_by_province.get(province, []))
                print(f"✅ {province}: {castle_count} châteaux ajoutés")
                updated_count += 1
            else:
                print(f"⚠️ Section intro non trouvée dans {filename}")
                
        except FileNotFoundError:
            print(f"⚠️ Fichier non trouvé: {filename}")
        except Exception as e:
            print(f"❌ Erreur avec {filename}: {e}")
    
    print(f"\n📊 RÉSULTATS:")
    print(f"Pages provinces mises à jour: {updated_count}")
    print(f"Total châteaux organisés: {sum(len(castles) for castles in organizer.castles_by_province.values())}")

if __name__ == "__main__":
    update_province_castle_lists()
