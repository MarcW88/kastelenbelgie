#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script pour ajouter les images des châteaux dans la section 'related castles'
"""

import os
import re
import glob

def create_image_mapping():
    """Crée un mapping entre les noms de fichiers et les noms de châteaux"""
    
    # Mapping des images disponibles vers les noms de pages
    image_mapping = {
        # Images exactes
        'Kasteel_van_Durbuy.jpg': 'kasteel-van-durbuy-durbuy',
        'Kasteel_van_freyr.jpg': 'kasteel-van-freyr-freyr',
        'Kasteel_van_La_Roche-en-Ardenne.jpg': 'kasteel-van-la-roche-en-ardenne-la-roche-en-ardenne',
        'Kasteel_van_Mirwart.jpg': 'kasteel-van-mirwart-mirwart-saint-hubert',
        'Kasteel_arendsnest.jpg': 'kasteel-arendsnest-edegem',
        'Kasteel_borrekens.jpg': 'kasteel-borrekens-vorselaar',
        'Kasteel_bouckenborgh.jpg': 'kasteel-bouckenborgh-merksem',
        'Braemkasteel.jpg': 'braemkasteel-gentbrugge',
        'Burcht_reuland.jpg': 'burcht-reuland-reuland-burg-reuland',
        'Burchtruine_van_Montquintin.jpg': 'burchtruine-van-montquintin-montquintin-dampicourt',
        'Chateau_de_bellaire.jpg': 'chateau-de-bellaire-haltinne',
        'Chateau_de_la_tournette.jpg': 'chateau-de-la-tournette-nijvel',
        'De_cijnshof_van_boutersem.jpg': 'de-cijnshof-van-boutersem-zandhoven',
        'De_hof_van_veltwijck.jpg': 'de-hof-van-veltwijck-ekeren',
        'De_solhof.jpg': 'de-solhof-aartselaar',
        'Domein_de_ghellinck.jpg': 'domein-de-ghellinck-elsegem',
        'Het_grafelijk_slot_van_male.jpg': 'het-grafelijk-slot-van-male-sint-kruis',
        'Het_rood_kasteel.jpg': 'het-rood-kasteel-te-linden',
        'Hof_te_melis.jpg': 'hof-te-melis-lippelo',
        'Hof_ter_borght.jpg': 'hof-ter-borght-westmeerbeek',
        'Hof_van_liere.jpg': 'hof-van-liere-zandhoven',
        'Hof_van_ringen.jpg': 'hof-van-ringen-lier',
        'Hof_van_roosendael.jpg': 'hof-van-roosendael-merksem',
        'Kasteel_Beauregard.jpg': 'kasteel-beauregard-froyennes',
        'Kasteel_altembrouck.jpg': 'kasteel-altembrouck-s-gravenvoeren-te-voeren',
        'Kasteel_baelen.jpg': 'kasteel-baelen-hendrik-kapelle',
        'Kasteel_bayard.jpg': 'kasteel-bayard-dhuy',
        'Kasteel_belvedere.jpg': 'kasteel-belvedere-te-laken-brussel',
        'Kasteel_blauw_huys.jpg': 'kasteel-blauw-huys-drongen-gent',
        'Kasteel_blauwhuis.jpg': 'kasteel-blauwhuis-izegem',
        'Kasteel_borghoven.jpg': 'kasteel-borghoven-piringen-bij-tongeren',
        'Kasteel_borgwal.jpg': 'kasteel-borgwal-gavere',
        'Kasteel_borluut.jpg': 'kasteel-borluut-sint-denijs-westrem',
        'Kasteel_brunsode.jpg': 'kasteel-brunsode-tilff',
        'Kasteel_daalbroek.jpg': 'kasteel-daalbroek-rekem',
        'Kasteel_de_blankaart.jpg': 'kasteel-de-blankaart-diksmuide',
        'Kasteel_de_blauwe_toren.jpg': 'kasteel-de-blauwe-toren-varsenare',
        'Kasteel_de_campagne.jpg': 'kasteel-de-campagne-drongen-gent',
        'Kasteel_de_faille.jpg': 'kasteel-de-faille-brugge',
        'Kasteel_de_hoof_teuven.jpg': 'kasteel-de-hoof-teuven-te-voeren',
        'Kasteel_de_marnix.jpg': 'kasteel-de-marnix-te-overijse',
        'Kasteel_de_merode.jpg': 'kasteel-de-merode-westerlo',
        'Kasteel_de_motte_groot_gelmen.jpg': 'kasteel-de-motte-groot-gelmen-bij-sint-truiden',
        'Kasteel_de_rivieren.jpg': 'kasteel-de-rivieren-te-ganshoren',
        'Kasteel_des_cailloux.jpg': 'kasteel-des-cailloux-geldenaken',
        'Kasteel_diependael.jpg': 'kasteel-diependael-elewijt',
        'Kasteel_doverschie.jpg': 'kasteel-doverschie-te-grimbergen',
        'Kasteel_drie_koningen.jpg': 'kasteel-drie-koningen-beernem',
        'Kasteel_du_lac_genval.jpg': 'kasteel-du-lac-genval',
        'Kasteel_duras.jpg': 'kasteel-duras-te-duras',
        'Kasteel_edelhof.jpg': 'kasteel-edelhof-munsterbilzen',
        'Rood_kasteel.jpg': 'het-rood-kasteel-te-linden',
        'Waterslot_cleydael.jpg': 'waterslot-cleydael-schilde'
    }
    
    return image_mapping

def normalize_castle_name(name):
    """Normalise le nom d'un château pour la correspondance"""
    # Enlève les préfixes communs et normalise
    name = name.lower()
    name = re.sub(r'^(kasteel|château|chateau|hof|de|het)\s+', '', name)
    name = re.sub(r'\s+', '_', name)
    return name

def find_image_for_castle(castle_href, image_mapping):
    """Trouve l'image correspondante pour un château donné"""
    # Extrait le nom du fichier HTML
    castle_file = castle_href.replace('.html', '')
    
    # Cherche une correspondance directe
    for image_file, mapped_castle in image_mapping.items():
        if mapped_castle == castle_file:
            return f"./chateaux_images/{image_file}"
    
    return None

def update_related_castles_with_images(file_path):
    """Met à jour la section related castles avec les images disponibles"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        image_mapping = create_image_mapping()
        
        # Trouve tous les blocs related castles
        card_pattern = r'(<a class="card" href="([^"]+)">\s*)<div class="card-media gradient-[123]"></div>'
        matches = list(re.finditer(card_pattern, content))
        
        if not matches:
            return False, "Aucune section related castles trouvée"
        
        updated_content = content
        changes_made = 0
        
        for match in matches:
            full_match = match.group(0)
            card_start = match.group(1)
            castle_href = match.group(2)
            
            # Cherche l'image correspondante
            image_path = find_image_for_castle(castle_href, image_mapping)
            
            if image_path:
                # Remplace le gradient par l'image
                new_card_media = f'<div class="card-media"><img src="{image_path}" alt="Château" class="castle-image"></div>'
                replacement = card_start + new_card_media
                
                updated_content = updated_content.replace(full_match, replacement)
                changes_made += 1
        
        if changes_made > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            return True, f"{changes_made} images ajoutées dans related castles"
        else:
            return False, "Aucune image correspondante trouvée"
        
    except Exception as e:
        return False, f"Erreur: {e}"

def main():
    """Fonction principale"""
    print("=== AJOUT D'IMAGES DANS RELATED CASTLES ===")
    
    # Trouve tous les fichiers de châteaux
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
    image_mapping = create_image_mapping()
    
    print(f"Trouvé {len(castle_files)} pages de châteaux")
    print(f"Images disponibles: {len(image_mapping)}")
    
    # Test avec quelques fichiers d'abord
    test_files = castle_files[:10]
    success_count = 0
    
    for file_path in test_files:
        filename = os.path.basename(file_path)
        success, message = update_related_castles_with_images(file_path)
        
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
                
            success, message = update_related_castles_with_images(file_path)
            if success:
                success_count += 1
                if success_count % 25 == 0:
                    print(f"  Progression: {success_count} pages mises à jour...")
    
    print(f"\n=== RÉSULTAT FINAL ===")
    print(f"Pages mises à jour avec images: {success_count}")
    print("Ajout d'images dans related castles terminé!")

if __name__ == "__main__":
    main()
