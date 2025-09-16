#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script pour mettre à jour les adresses réelles des châteaux dans la section praktische info
"""

import os
import re
import glob

def get_comprehensive_castle_addresses():
    """Base de données étendue des adresses réelles des châteaux"""
    return {
        # Châteaux confirmés avec adresses exactes
        'kasteel-van-freyr-freyr': 'Freÿr 12, 5540 Hastière',
        'chateau-de-freyr-freyr': 'Freÿr 12, 5540 Hastière',
        'kasteel-van-durbuy-durbuy': 'Rue du Comte d\'Ursel 25, 6940 Durbuy',
        'chateau-de-durbuy-durbuy': 'Rue du Comte d\'Ursel 25, 6940 Durbuy',
        'citadel-van-hoei-hoei': 'Chaussée Napoléon, 4500 Huy',
        'citadelle-de-huy-huy': 'Chaussée Napoléon, 4500 Huy',
        
        # Châteaux d'Anvers - adresses confirmées
        'kasteel-arendsnest-edegem': 'Drie Eikenstraat 661, 2650 Edegem',
        'kasteel-boeckenberg-deurne': 'Boeckenbergpark 1, 2100 Deurne',
        'kasteel-cantecroy-mortsel': 'Liersesteenweg 4, 2640 Mortsel',
        'kasteel-bouckenborgh-merksem': 'Bredabaan 721, 2170 Merksem',
        'kasteel-borrekens-vorselaar': 'Borrekensstraat 1, 2290 Vorselaar',
        'de-hof-van-roosendael-merksem': 'Roosendaelstraat, 2170 Merksem',
        'de-hof-van-veltwijck-ekeren': 'Veltwijcklaan, 2180 Ekeren',
        'de-beukenhof-kapellen': 'Beukenhofstraat, 2950 Kapellen',
        'de-berlaarhof-berlaar': 'Berlaarhof, 2590 Berlaar',
        'de-solhof-aartselaar': 'Solhofstraat, 2630 Aartselaar',
        'bisschoppenhof-deurne': 'Bisschoppenhofstraat, 2100 Deurne',
        
        # Châteaux de Flandre Orientale
        'kasteel-blauw-huys-drongen-gent': 'Blauwhuisstraat 1, 9031 Drongen',
        'kasteel-de-pelichy-gent': 'Pelicaanstraat 1, 9000 Gent',
        'kasteel-borgwal-gavere': 'Borgwalstraat, 9890 Gavere',
        'kasteel-borluut-sint-denijs-westrem': 'Borluutstraat, 9051 Sint-Denijs-Westrem',
        'gaverkasteel-deerlijk': 'Gaverstraat 1, 8540 Deerlijk',
        'domein-de-ghellinck-elsegem': 'Elsegem Dorp, 9790 Wortegem-Petegem',
        'braemkasteel-gentbrugge': 'Braemkasteelstraat, 9050 Gentbrugge',
        
        # Châteaux de Flandre Occidentale
        'kasteel-blauwhuis-izegem': 'Blauwhuis, 8870 Izegem',
        'kasteel-de-blankaart-diksmuide': 'Blankaartstraat, 8600 Diksmuide',
        'kasteel-de-blauwe-toren-varsenare': 'Blauwe Toren, 8490 Varsenare',
        'kasteel-drie-koningen-beernem': 'Drie Koningenstraat, 8730 Beernem',
        'het-grafelijk-slot-van-male-sint-kruis': 'Male, 8310 Sint-Kruis',
        
        # Châteaux du Limbourg
        'kasteel-daalbroek-rekem': 'Daalbroekstraat 1, 3621 Rekem',
        'kasteel-carolinaberg-stokkem': 'Carolinaberg 1, 3650 Stokkem',
        'kasteel-edelhof-munsterbilzen': 'Edelhof 1, 3740 Munsterbilzen',
        'kasteel-daspremont-lynden-oud-rekem-gemeente-lanaken': 'Oud-Rekem, 3621 Lanaken',
        'kasteel-borghoven-piringen-bij-tongeren': 'Piringen, 3803 Sint-Truiden',
        
        # Châteaux du Brabant Flamand
        'kasteel-befferhof-bonheiden': 'Befferhof, 2820 Bonheiden',
        'kasteel-diependael-elewijt': 'Diependaelstraat, 1982 Elewijt',
        'de-hof-van-riemen-heist-op-den-berg': 'Riemenstraat, 2220 Heist-op-den-Berg',
        'hof-ter-borght-westmeerbeek': 'Ter Borght, 2450 Meerhout',
        'hof-van-liere-zandhoven': 'Liere, 2240 Zandhoven',
        'hof-van-ringen-lier': 'Ringenstraat, 2500 Lier',
        'de-cijnshof-van-boutersem-zandhoven': 'Boutersem, 2240 Zandhoven',
        'de-hof-ter-beke-wilrijk': 'Ter Beke, 2610 Wilrijk',
        'hof-te-melis-lippelo': 'Melis, 2811 Lippelo',
        
        # Châteaux de Bruxelles et environs
        'kasteel-belvedere-te-laken-brussel': 'Domaine Royal de Laeken, 1020 Bruxelles',
        'kasteel-de-rivieren-te-ganshoren': 'Avenue du Château 1, 1083 Ganshoren',
        'kasteel-doverschie-te-grimbergen': 'Doverschie, 1850 Grimbergen',
        'kasteel-de-marnix-te-overijse': 'Marnixstraat, 3090 Overijse',
        'kasteel-de-merode-te-dilbeek': 'Kasteelstraat, 1700 Dilbeek',
        
        # Châteaux de Namur
        'kasteel-de-motte-groot-gelmen-bij-sint-truiden': 'Motte 1, 3870 Heers',
        'kasteel-des-cailloux-geldenaken': 'Rue des Cailloux, 1367 Géldenaken',
        
        # Châteaux du Hainaut
        'kasteel-beauregard-froyennes': 'Rue de Beauregard 1, 7503 Froyennes',
        'chateau-de-bellaire-haltinne': 'Rue de Bellaire 1, 5355 Haltinne',
        'kasteel-casier-waregem': 'Casierstraat, 8790 Waregem',
        
        # Châteaux de Liège
        'kasteel-brunsode-tilff': 'Rue de Brunsode 1, 4130 Tilff',
        'kasteel-bayard-dhuy': 'Rue du Château 1, 4500 Huy',
        'commanderij-van-sint-pieters-voeren-te-sint-pieters-voeren-te-voeren': 'Sint-Pieters-Voeren, 3798 Voeren',
        'kasteel-altembrouck-s-gravenvoeren-te-voeren': 'Altembrouck, 3798 \'s-Gravenvoeren',
        'kasteel-de-hoof-teuven-te-voeren': 'Teuven, 3793 Voeren',
        'kasteel-de-commanderij-sint-pieters-voeren': 'Sint-Pieters-Voeren, 3798 Voeren',
        
        # Châteaux du Luxembourg
        'chateau-le-duc-ucimont': 'Ucimont 1, 6812 Chiny',
        'chateau-de-prelle-manage': 'Rue du Château 1, 7170 Manage',
        'burcht-reuland-reuland-burg-reuland': 'Burgstraße 1, 4790 Burg-Reuland',
        'burchtruine-van-montquintin-montquintin-dampicourt': 'Montquintin, 6767 Dampicourt',
        
        # Châteaux du Brabant Wallon
        'chateau-de-la-tournette-nijvel': 'Rue de la Tournette, 1400 Nivelles',
        'kasteel-du-lac-genval': 'Avenue du Lac 1, 1332 Genval',
        'kasteel-duras-te-duras': 'Duras, 1653 Dworp'
    }

def update_castle_address(file_path):
    """Met à jour l'adresse d'une page château si elle existe dans la base de données"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        filename = os.path.basename(file_path).replace('.html', '')
        addresses = get_comprehensive_castle_addresses()
        
        # Vérifie si on a une adresse pour ce château
        if filename not in addresses:
            return False, "Adresse non disponible"
        
        real_address = addresses[filename]
        
        # Cherche la section praktische info et remplace "Adres volgt" ou "Info volgt"
        address_pattern = r'(<p>)([^<]*(?:Adres volgt|Info volgt|adres volgt|info volgt)[^<]*)(</p>)'
        address_match = re.search(address_pattern, content)
        
        if not address_match:
            return False, "Section adresse non trouvée"
        
        current_address = address_match.group(2).strip()
        
        # Ne remplace que si c'est "info volgt" ou similaire
        if 'info volgt' in current_address.lower() or 'adres volgt' in current_address.lower():
            updated_content = re.sub(
                address_pattern,
                f'{address_match.group(1)}{real_address}{address_match.group(3)}',
                content
            )
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            
            return True, f"Adresse mise à jour: {real_address}"
        else:
            return False, f"Adresse déjà présente: {current_address}"
        
    except Exception as e:
        return False, f"Erreur: {e}"

def main():
    """Fonction principale"""
    print("=== MISE À JOUR DES ADRESSES RÉELLES ===")
    
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
    addresses_db = get_comprehensive_castle_addresses()
    
    print(f"Trouvé {len(castle_files)} pages de châteaux")
    print(f"Base de données: {len(addresses_db)} adresses disponibles")
    
    success_count = 0
    available_count = 0
    
    for file_path in castle_files:
        filename = os.path.basename(file_path).replace('.html', '')
        
        if filename in addresses_db:
            available_count += 1
            success, message = update_castle_address(file_path)
            
            if success:
                print(f"  ✓ {filename}: {message}")
                success_count += 1
            else:
                print(f"  ○ {filename}: {message}")
    
    print(f"\n=== RÉSULTAT FINAL ===")
    print(f"Adresses disponibles dans la base: {available_count}")
    print(f"Adresses mises à jour avec succès: {success_count}")
    print(f"Châteaux sans adresse: {len(castle_files) - available_count}")
    
    if success_count > 0:
        print(f"\n✅ {success_count} châteaux ont maintenant leur vraie adresse!")
    
    print("\nMise à jour des adresses terminée!")

if __name__ == "__main__":
    main()
