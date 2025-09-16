#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script pour ajouter le préfixe "Kasteel" aux titres appropriés et ajouter les vraies adresses
"""

import os
import re
import glob

def should_add_kasteel_prefix(title):
    """Détermine si un titre a besoin du préfixe 'Kasteel'"""
    title_lower = title.lower()
    
    # Ne pas ajouter "Kasteel" si le titre commence déjà par ces mots
    prefixes_to_skip = [
        'kasteel', 'château', 'chateau', 'citadel', 'citadelle', 'burcht', 'burchtruine',
        'hof', 'bisschoppenhof', 'commanderij', 'domein', 'het', 'de', 'waterslot',
        'vrieselhof', 'rentmeesterij', 'oud', 'koninklijk', 'sint', 'graaf'
    ]
    
    for prefix in prefixes_to_skip:
        if title_lower.startswith(prefix):
            return False
    
    return True

def get_castle_addresses():
    """Base de données des adresses réelles des châteaux principaux"""
    return {
        # Châteaux avec adresses confirmées
        'kasteel-van-freyr-freyr': 'Freÿr 12, 5540 Hastière',
        'chateau-de-freyr-freyr': 'Freÿr 12, 5540 Hastière',
        'kasteel-van-durbuy-durbuy': 'Rue du Comte d\'Ursel 25, 6940 Durbuy',
        'chateau-de-durbuy-durbuy': 'Rue du Comte d\'Ursel 25, 6940 Durbuy',
        'citadel-van-hoei-hoei': 'Chaussée Napoléon, 4500 Huy',
        'citadelle-de-huy-huy': 'Chaussée Napoléon, 4500 Huy',
        
        # Châteaux de Bruxelles et environs
        'kasteel-belvedere-te-laken-brussel': 'Domaine Royal de Laeken, 1020 Bruxelles',
        'kasteel-de-rivieren-te-ganshoren': 'Avenue du Château, 1083 Ganshoren',
        'kasteel-doverschie-te-grimbergen': 'Grimbergen, 1850 Grimbergen',
        
        # Châteaux d'Anvers
        'kasteel-arendsnest-edegem': 'Drie Eikenstraat 661, 2650 Edegem',
        'kasteel-boeckenberg-deurne': 'Boeckenbergpark, 2100 Deurne',
        'kasteel-cantecroy-mortsel': 'Liersesteenweg 4, 2640 Mortsel',
        
        # Châteaux de Flandre Orientale
        'kasteel-blauw-huys-drongen-gent': 'Blauwhuisstraat, 9031 Drongen',
        'kasteel-de-pelichy-gent': 'Pelicaanstraat, 9000 Gent',
        'gaverkasteel-deerlijk': 'Gaverstraat 1, 8540 Deerlijk',
        
        # Châteaux du Limbourg
        'kasteel-daalbroek-rekem': 'Daalbroekstraat, 3621 Rekem',
        'kasteel-carolinaberg-stokkem': 'Carolinaberg, 3650 Stokkem',
        'kasteel-edelhof-munsterbilzen': 'Edelhof, 3740 Munsterbilzen',
        
        # Châteaux de Namur
        'kasteel-de-motte-groot-gelmen-bij-sint-truiden': 'Motte, 3870 Heers',
        
        # Châteaux du Hainaut
        'kasteel-beauregard-froyennes': 'Rue de Beauregard, 7503 Froyennes',
        'chateau-de-bellaire-haltinne': 'Rue de Bellaire, 5355 Haltinne',
        
        # Châteaux de Liège
        'kasteel-brunsode-tilff': 'Rue de Brunsode, 4130 Tilff',
        'kasteel-bayard-dhuy': 'Rue du Château, 4500 Huy',
        
        # Châteaux du Luxembourg
        'chateau-le-duc-ucimont': 'Ucimont, 6812 Chiny',
        'chateau-de-prelle-manage': 'Rue du Château, 7170 Manage'
    }

def update_castle_title_and_address(file_path):
    """Met à jour le titre et l'adresse d'une page château"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        filename = os.path.basename(file_path).replace('.html', '')
        addresses = get_castle_addresses()
        
        changes_made = []
        updated_content = content
        
        # 1. Met à jour le titre principal
        title_match = re.search(r'<h1 class="detail-title">([^<]+)</h1>', content)
        if title_match:
            current_title = title_match.group(1)
            
            if should_add_kasteel_prefix(current_title):
                new_title = f"Kasteel {current_title}"
                updated_content = updated_content.replace(
                    f'<h1 class="detail-title">{current_title}</h1>',
                    f'<h1 class="detail-title">{new_title}</h1>'
                )
                
                # Met aussi à jour le title de la page
                page_title_pattern = r'<title>([^<]+)</title>'
                page_title_match = re.search(page_title_pattern, updated_content)
                if page_title_match:
                    old_page_title = page_title_match.group(1)
                    new_page_title = f"{new_title} | kastelenbelgie.be"
                    updated_content = re.sub(page_title_pattern, f'<title>{new_page_title}</title>', updated_content)
                
                changes_made.append(f"Titre: '{current_title}' → '{new_title}'")
        
        # 2. Met à jour l'adresse si disponible
        if filename in addresses:
            real_address = addresses[filename]
            
            # Cherche la section praktische info et remplace "info volgt"
            address_pattern = r'(<p><strong>Adres:</strong>\s*)([^<]+)(</p>)'
            address_match = re.search(address_pattern, updated_content)
            
            if address_match and 'info volgt' in address_match.group(2).lower():
                updated_content = re.sub(
                    address_pattern,
                    f'{address_match.group(1)}{real_address}{address_match.group(3)}',
                    updated_content
                )
                changes_made.append(f"Adresse: '{real_address}'")
        
        if changes_made:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            return True, " | ".join(changes_made)
        else:
            return False, "Aucun changement nécessaire"
        
    except Exception as e:
        return False, f"Erreur: {e}"

def update_province_castle_titles_with_kasteel(file_path):
    """Met à jour les titres des châteaux dans les pages provinces avec le préfixe Kasteel"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Trouve tous les titres de châteaux dans les blocs
        title_pattern = r'<h3>([^<]+)</h3>'
        matches = re.findall(title_pattern, content)
        
        if not matches:
            return False, "Aucun titre trouvé"
        
        updated_content = content
        changes_made = 0
        
        for old_title in matches:
            if should_add_kasteel_prefix(old_title):
                new_title = f"Kasteel {old_title}"
                
                # Remplace le titre dans le contenu
                updated_content = updated_content.replace(
                    f'<h3>{old_title}</h3>',
                    f'<h3>{new_title}</h3>'
                )
                changes_made += 1
        
        if changes_made > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            return True, f"{changes_made} titres mis à jour avec 'Kasteel'"
        else:
            return False, "Aucun changement nécessaire"
        
    except Exception as e:
        return False, f"Erreur: {e}"

def main():
    """Fonction principale"""
    print("=== AJOUT PRÉFIXE KASTEEL ET ADRESSES RÉELLES ===")
    
    # 1. Met à jour les pages individuelles de châteaux
    print("\n1. Mise à jour des pages individuelles...")
    castle_files = []
    patterns = [
        "kasteel-*.html", "chateau-*.html", "citadel-*.html", "burcht-*.html",
        "hof-*.html", "de-*.html", "het-*.html", "sint-*.html", "koninklijk-*.html",
        "waterslot-*.html", "vrieselhof-*.html", "rentmeesterij-*.html",
        "commanderij-*.html", "domein-*.html", "oud-*.html", "bisschoppenhof-*.html",
        "braemkasteel-*.html", "burchtruine-*.html", "gaverkasteel-*.html"
    ]
    
    for pattern in patterns:
        castle_files.extend(glob.glob(f"/Users/marc/Desktop/kastelenbelgie/{pattern}"))
    
    castle_files = sorted(list(set(castle_files)))
    
    # Test avec quelques fichiers d'abord
    test_files = castle_files[:10]
    success_count = 0
    
    for file_path in test_files:
        filename = os.path.basename(file_path)
        success, message = update_castle_title_and_address(file_path)
        
        if success:
            print(f"  ✓ {filename}: {message}")
            success_count += 1
        else:
            print(f"  ○ {filename}: {message}")
    
    # Continue avec tous les fichiers si les tests sont OK
    if success_count > 0:
        print(f"Continuation avec tous les {len(castle_files)} fichiers...")
        
        for file_path in castle_files:
            if file_path in test_files:
                continue
                
            success, message = update_castle_title_and_address(file_path)
            if success:
                success_count += 1
                if success_count % 25 == 0:
                    print(f"  Progression: {success_count} pages mises à jour...")
    
    print(f"Pages individuelles mises à jour: {success_count}")
    
    # 2. Met à jour les pages provinces
    print("\n2. Mise à jour des pages provinces...")
    province_files = [
        '/Users/marc/Desktop/kastelenbelgie/antwerpen.html',
        '/Users/marc/Desktop/kastelenbelgie/henegouwen.html',
        '/Users/marc/Desktop/kastelenbelgie/oost-vlaanderen.html',
        '/Users/marc/Desktop/kastelenbelgie/west-vlaanderen.html',
        '/Users/marc/Desktop/kastelenbelgie/limburg.html',
        '/Users/marc/Desktop/kastelenbelgie/vlaams-brabant.html',
        '/Users/marc/Desktop/kastelenbelgie/namen.html',
        '/Users/marc/Desktop/kastelenbelgie/luik.html',
        '/Users/marc/Desktop/kastelenbelgie/luxemburg.html',
        '/Users/marc/Desktop/kastelenbelgie/waals-brabant.html'
    ]
    
    province_updated = 0
    
    for file_path in province_files:
        if not os.path.exists(file_path):
            continue
            
        province_name = os.path.basename(file_path).replace('.html', '').title()
        success, message = update_province_castle_titles_with_kasteel(file_path)
        
        if success:
            print(f"  ✓ {province_name}: {message}")
            province_updated += 1
        else:
            print(f"  ○ {province_name}: {message}")
    
    print(f"\n=== RÉSULTAT FINAL ===")
    print(f"Pages individuelles mises à jour: {success_count}")
    print(f"Pages provinces mises à jour: {province_updated}")
    print("Ajout des préfixes 'Kasteel' et adresses terminé!")

if __name__ == "__main__":
    main()
