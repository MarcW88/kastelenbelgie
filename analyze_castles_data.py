#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ANALYSE DES DONNÉES DES CHÂTEAUX
Organise les données pour la création du site
"""

import re
import json
from collections import defaultdict

# Données des châteaux extraites de la liste
CASTLES_DATA = """
Kasteel engelhof|https://kastelenbelgie.be/nl/kasteel-engelhof-houthalen/|Luik|Kasteel Engelhof|Hengelhoefdreef 2, 3530 Houthalen-Helchteren
Kasteel Beauregard|https://kastelenbelgie.be/nl/kasteel-beauregard-froyennes/|Luik|Château Beauregard|Beauregard, 6530 Thuin
Kasteel karreveld|https://kastelenbelgie.be/nl/kasteel-karreveld-te-sint-jans-molenbeek/|Luik|Kasteelhoeve Karreveld|Jean de la Hoeselaan 32, 1080 Sint-Jans-Molenbeek|08:30–17:00|08:30–17:00|08:30–18:00|08:30–18:00|08:30–18:00|08:30–18:00|08:30–18:00
Kasteel van wegimont|https://kastelenbelgie.be/nl/kasteel-van-wegimont-ayeneux-soumagne/|Luik|Château de Wégimont|4630 Liège|09:00–17:00|09:00–17:00|09:00–17:00|09:00–17:00|09:00–17:00|09:00–17:00|09:00–17:00
Kasteel ter lucht|https://kastelenbelgie.be/nl/kasteel-ter-lucht-sint-andries/|Luik|Kasteel van Waroux|Rue de Waroux 301, 4432 Ans|Gesloten|14:00–18:00|14:00–18:00|14:00–18:00|14:00–18:00|14:00–18:00|14:00–18:00
Hof ter borght|https://kastelenbelgie.be/nl/hof-ter-borght-westmeerbeek/|Luik|Hof ter Borght|Heide 41, 2235 Hulshout
Kasteel van Durbuy|https://kastelenbelgie.be/nl/kasteel-van-durbuy-durbuy/|Luik|Kasteel van Durbuy|6940 Durbuy
Kasteel van fougeraie|https://kastelenbelgie.be/nl/kasteel-van-fougeraie-te-ukkel/|Luik|Kasteel van Jehay|Rue du Parc 1, 4540 Amay|11:00–18:00|11:00–18:00|11:00–18:00|11:00–18:00|11:00–18:00|11:00–18:00|11:00–18:00
Kasteel Mohimont|https://kastelenbelgie.be/nl/kasteel-mohimont-villers-devant-orval/|Luik|Château de Wégimont|4630 Liège|09:00–17:00|09:00–17:00|09:00–17:00|09:00–17:00|09:00–17:00|09:00–17:00|09:00–17:00
Kasteel van Orval|https://kastelenbelgie.be/nl/kasteel-van-orval-villers-devant-orval/|Luxemburg|Kasteel van Orval|Orval 5, 6823 Florenville
Kasteel van Templeuve|https://kastelenbelgie.be/nl/kasteel-van-templeuve-templeuve/|Henegouwen|Templeuve Castle|7520 Tournai
Kasteel van biez|https://kastelenbelgie.be/nl/kasteel-van-biez-peruwelz/|Namen|Château De Beez|Av. du Chateau de Beez, 5000 Namur|24 uur geopend|24 uur geopend|24 uur geopend|24 uur geopend|24 uur geopend|24 uur geopend|24 uur geopend
Kasteel van Roumont|https://kastelenbelgie.be/nl/kasteel-van-roumont-roumont/|Antwerpen|Château Mondron (XIXe siècle)|Chau. du Château Mondron 159, 6040 Charleroi|08:30–16:30|08:30–16:30|08:30–16:30|08:30–16:30|08:30–16:30|Gesloten|Gesloten
Kasteel van rethy|https://kastelenbelgie.be/nl/kasteel-van-rethy-retie/|Limburg|Kasteel van Rijkel|Dionysius van Leeuwenstraat 23, 3840 Tongeren-Borgloon
Kasteel van wijer|https://kastelenbelgie.be/nl/kasteel-van-wijer-te-wijer-gemeente-nieuwerkerken/|Antwerpen|Castle of Wijer|Grotestraat 205, 3850 Nieuwerkerken
Kasteel van bouchout|https://kastelenbelgie.be/nl/kasteel-van-bouchout-te-meise/|Antwerpen|Kasteel van Bouchout|1860 Meise|10:00–17:00|10:00–17:00|10:00–17:00|10:00–17:00|10:00–17:00|10:00–17:00|10:00–17:00
Kasteel ter borcht|https://kastelenbelgie.be/nl/kasteel-ter-borcht-meulebeke/|Antwerpen|Kasteel Ter Borcht|Baronielaan 27-29, 8760 Tielt
Kasteel van heetvelde|https://kastelenbelgie.be/nl/kasteel-van-heetvelde-te-oetingen/|Vlaams-Brabant|Kasteel van Heetvelde|Oude Heerbaan 83, 1755 Pajottegem
Kasteel hulsberg|https://kastelenbelgie.be/nl/kasteel-hulsberg-borgloon/|Luxemburg|Kasteel Hulsberg|St.-Truidersteenweg 101, 3840 Tongeren-Borgloon
Kasteel van Voneche|https://kastelenbelgie.be/nl/kasteel-van-voneche-voneche/|Luxemburg|Château de Vonêche|Rue Le Parc, 5570 Beauraing
Sint-Antoniuskasteel|https://kastelenbelgie.be/nl/sint-antoniuskasteel-celles/|Henegouwen|Kasteel van Antoing|Pl. Bara, 7640 Antoing|Gesloten|Gesloten|Gesloten|15:00–17:00|Gesloten|Gesloten|15:00–17:00
Citadel van hoei|https://kastelenbelgie.be/nl/citadel-van-hoei-hoei/|Luik|Fort van Hoei|Chau. de Napoléon, 4500 Huy|13:30–18:00|10:30–18:00|10:30–18:00|10:30–18:00|10:30–18:00|10:30–18:00|10:30–18:00
Kasteel van freyr|https://kastelenbelgie.be/nl/kasteel-van-freyr-freyr/|Antwerpen|Kasteel van Freÿr|Freyr 12, 5540 Hastière|Gesloten|11:00–17:00|11:00–17:00|11:00–17:00|11:00–17:00|11:00–17:00|11:00–17:00
"""

def parse_castle_data():
    """Parse les données des châteaux"""
    castles = []
    provinces = defaultdict(list)
    
    lines = [line.strip() for line in CASTLES_DATA.strip().split('\n') if line.strip()]
    
    for line in lines:
        parts = line.split('|')
        if len(parts) >= 5:
            title = parts[0]
            url = parts[1]
            province = parts[2]
            name_found = parts[3]
            address = parts[4]
            
            # Extraire le slug de l'URL
            slug = url.split('/')[-2] if url.endswith('/') else url.split('/')[-1]
            
            # Heures d'ouverture (si disponibles)
            opening_hours = {}
            if len(parts) > 5:
                days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
                for i, day in enumerate(days):
                    if len(parts) > 5 + i:
                        opening_hours[day] = parts[5 + i]
            
            castle = {
                'title': title,
                'slug': slug,
                'url': url,
                'province': province,
                'name_found': name_found,
                'address': address,
                'opening_hours': opening_hours,
                'has_opening_hours': len(opening_hours) > 0
            }
            
            castles.append(castle)
            provinces[province].append(castle)
    
    return castles, dict(provinces)

def find_castle_images(slug):
    """Trouve les images correspondant à un château"""
    import os
    images_dir = "/Users/marc/Desktop/kastelenbelgie/chateaux_images_update-2"
    
    # Normaliser le slug pour la recherche d'images
    # Remplacer les tirets par des underscores et capitaliser
    image_base = slug.replace('kasteel-', '').replace('chateau-', '').replace('citadel-', '').replace('burcht-', '')
    image_base = image_base.replace('-', '_')
    
    # Patterns possibles pour les noms d'images
    possible_patterns = [
        f"Kasteel_{image_base}_",
        f"Chateau_{image_base}_",
        f"Citadel_{image_base}_",
        f"Burcht_{image_base}_",
        image_base.replace('_', '_van_'),
        image_base.title().replace('_', '_')
    ]
    
    found_images = []
    
    try:
        all_files = os.listdir(images_dir)
        for pattern in possible_patterns:
            matching_files = [f for f in all_files if f.lower().startswith(pattern.lower()) and f.endswith('.jpg')]
            if matching_files:
                found_images.extend(matching_files)
                break
    except:
        pass
    
    return found_images[:6]  # Maximum 6 images

def generate_provinces_list():
    """Génère la liste des provinces belges"""
    return [
        {'name': 'Antwerpen', 'slug': 'antwerpen'},
        {'name': 'Limburg', 'slug': 'limburg'},
        {'name': 'Oost-Vlaanderen', 'slug': 'oost-vlaanderen'},
        {'name': 'West-Vlaanderen', 'slug': 'west-vlaanderen'},
        {'name': 'Vlaams-Brabant', 'slug': 'vlaams-brabant'},
        {'name': 'Brussel', 'slug': 'brussel'},
        {'name': 'Waals-Brabant', 'slug': 'waals-brabant'},
        {'name': 'Henegouwen', 'slug': 'henegouwen'},
        {'name': 'Namen', 'slug': 'namen'},
        {'name': 'Luik', 'slug': 'luik'},
        {'name': 'Luxemburg', 'slug': 'luxemburg'}
    ]

def main():
    """Fonction principale"""
    print("🏰 ANALYSE DES DONNÉES DES CHÂTEAUX")
    print("=" * 50)
    
    # Parser les données
    castles, provinces = parse_castle_data()
    
    print(f"📊 {len(castles)} châteaux analysés")
    print(f"📍 {len(provinces)} provinces trouvées")
    
    # Statistiques par province
    print("\n📈 RÉPARTITION PAR PROVINCE:")
    for province, castle_list in provinces.items():
        print(f"  • {province}: {len(castle_list)} châteaux")
    
    # Châteaux avec heures d'ouverture
    with_hours = [c for c in castles if c['has_opening_hours']]
    print(f"\n⏰ {len(with_hours)} châteaux avec heures d'ouverture")
    
    # Vérifier les images disponibles
    print("\n🖼️  VÉRIFICATION DES IMAGES:")
    images_found = 0
    for castle in castles[:10]:  # Test sur les 10 premiers
        images = find_castle_images(castle['slug'])
        if images:
            images_found += 1
            print(f"  ✅ {castle['title']}: {len(images)} images")
        else:
            print(f"  ❌ {castle['title']}: aucune image")
    
    # Sauvegarder les données analysées
    output_data = {
        'castles': castles,
        'provinces': provinces,
        'provinces_list': generate_provinces_list(),
        'stats': {
            'total_castles': len(castles),
            'total_provinces': len(provinces),
            'castles_with_hours': len(with_hours)
        }
    }
    
    with open('/Users/marc/Desktop/kastelenbelgie/castles_data.json', 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n💾 Données sauvegardées dans castles_data.json")
    print("✅ Analyse terminée !")

if __name__ == "__main__":
    main()
