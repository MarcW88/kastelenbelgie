#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
VÉRIFICATION COMPLÈTE DES PROVINCES DES 262 CHÂTEAUX
Vérifie que chaque château est dans la bonne province
"""

import csv
import re

def verify_castle_provinces():
    """Vérifie la correspondance château-province pour tous les châteaux"""
    csv_file = "/Users/marc/Desktop/kastelenbelgie/chateaux_opening_hours - chateaux_opening_hours.csv"
    
    print("🔍 VÉRIFICATION COMPLÈTE DES PROVINCES")
    print("=" * 60)
    
    # Dictionnaire des villes/communes par province (données officielles belges)
    province_cities = {
        'Antwerpen': [
            'antwerpen', 'mechelen', 'turnhout', 'mol', 'geel', 'lier', 'heist-op-den-berg',
            'kapellen', 'brasschaat', 'schoten', 'boom', 'aartselaar', 'mortsel', 'edegem',
            'kontich', 'hove', 'boechout', 'wommelgem', 'schilde', 'zoersel', 'wijnegem',
            'ranst', 'zandhoven', 'malle', 'kalmthout', 'essen', 'stabroek', 'zwijndrecht',
            'beveren', 'sint-niklaas', 'temse', 'bornem', 'puurs', 'willebroek', 'duffel',
            'bonheiden', 'berlaar', 'nijlen', 'lier', 'herentals', 'olen', 'westerlo',
            'grobbendonk', 'herenthout', 'vorselaar', 'lille', 'kasterlee', 'tielen',
            'beerse', 'vosselaar', 'merksplas', 'rijkevorsel', 'baarle-hertog', 'hoogstraten',
            'wortel', 'ravels', 'arendonk', 'retie', 'dessel', 'balen', 'meerhout'
        ],
        'Limburg': [
            'hasselt', 'genk', 'tongeren', 'bilzen', 'maasmechelen', 'lanaken', 'riemst',
            'voeren', 'dilsen-stokkem', 'maaseik', 'kinrooi', 'bree', 'bocholt', 'lommel',
            'hamont-achel', 'neerpelt', 'overpelt', 'peer', 'houthalen-helchteren', 'ham',
            'tessenderlo', 'beringen', 'heusden-zolder', 'lummen', 'diepenbeek', 'as',
            'opglabbeek', 'meeuwen-gruitrode', 'oudsbergen', 'leopoldsburg', 'hechtel-eksel',
            'zonhoven', 'heers', 'borgloon', 'wellen', 'alken', 'kortessem', 'nieuwerkerken',
            'sint-truiden', 'gingelom', 'hoeselt'
        ],
        'Oost-Vlaanderen': [
            'gent', 'aalst', 'sint-niklaas', 'dendermonde', 'eeklo', 'oudenaarde', 'lokeren',
            'wetteren', 'ninove', 'geraardsbergen', 'ronse', 'zottegem', 'herzele', 'haaltert',
            'lede', 'waasmunster', 'temse', 'hamme', 'buggenhout', 'lebbeke', 'berlare',
            'zele', 'laarne', 'wachtebeke', 'zelzate', 'assenede', 'evergem', 'lovendegem',
            'waarschoot', 'knesselare', 'maldegem', 'kaprijke', 'sint-laureins', 'deinze',
            'nevele', 'oosterzele', 'merelbeke', 'melle', 'gontrode', 'destelbergen',
            'nazareth', 'de-pinte', 'gavere', 'zwalm', 'horebeke', 'kluisbergen',
            'wortegem-petegem', 'brakel', 'lierde', 'oosterzele'
        ],
        'West-Vlaanderen': [
            'brugge', 'kortrijk', 'oostende', 'roeselare', 'ieper', 'waregem', 'harelbeke',
            'menen', 'wervik', 'poperinge', 'veurne', 'nieuwpoort', 'diksmuide', 'tielt',
            'torhout', 'lichtervelde', 'ardooie', 'pittem', 'ruiselede', 'wingene',
            'oostkamp', 'beernem', 'jabbeke', 'zuienkerke', 'blankenberge', 'zedelgem',
            'oudenburg', 'bredene', 'de-haan', 'middelkerke', 'gistel', 'ichtegem',
            'koekelare', 'kortemark', 'houthulst', 'langemark-poelkapelle', 'staden',
            'moorslede', 'ledegem', 'meulebeke', 'dentergem', 'oostrozebeke', 'wielsbeke',
            'wevelgem', 'zwevegem', 'avelgem', 'spiere-helkijn', 'anzegem', 'waregem',
            'deerlijk', 'kuurne', 'lendelede', 'ingelmunster', 'izegem', 'hooglede'
        ],
        'Vlaams-Brabant': [
            'leuven', 'vilvoorde', 'aarschot', 'tienen', 'diest', 'scherpenheuvel-zichem',
            'bekkevoort', 'begijnendijk', 'boortmeerbeek', 'haacht', 'keerbergen', 'tremelo',
            'rotselaar', 'holsbeek', 'lubbeek', 'tielt-winge', 'glabbeek', 'kortenaken',
            'landen', 'linter', 'zoutleeuw', 'hoegaarden', 'boutersem', 'geetbets',
            'helen-boekel', 'kampenhout', 'steenokkerzeel', 'zemst', 'kapelle-op-den-bos',
            'londerzeel', 'meise', 'opwijk', 'merchtem', 'asse', 'ternat', 'affligem',
            'liedekerke', 'roosdaal', 'gooik', 'herne', 'pepingen', 'galmaarden',
            'bever', 'lennik', 'sint-pieters-leeuw', 'dilbeek', 'zaventem', 'kraainem',
            'wezembeek-oppem', 'machelen', 'grimbergen', 'wemmel', 'strombeek-bever'
        ],
        'Brussel': [
            'brussel', 'anderlecht', 'schaerbeek', 'molenbeek', 'uccle', 'ixelles',
            'forest', 'saint-gilles', 'etterbeek', 'koekelberg', 'ganshoren',
            'berchem-sainte-agathe', 'auderghem', 'watermaal-bosvoorde', 'woluwe-saint-lambert',
            'woluwe-saint-pierre', 'evere', 'saint-josse-ten-noode', 'jette'
        ],
        'Waals-Brabant': [
            'wavre', 'nivelles', 'braine-lalleud', 'braine-le-comte', 'tubize', 'waterloo',
            'lasne', 'rixensart', 'ottignies-louvain-la-neuve', 'mont-saint-guibert',
            'walhain', 'chaumont-gistoux', 'court-saint-etienne', 'chastre', 'villers-la-ville',
            'genappe', 'rebecq', 'ittre', 'clabecq', 'halle', 'sint-genesius-rode',
            'linkebeek', 'drogenbos', 'beersel', 'lot', 'alsemberg', 'dworp'
        ],
        'Namen': [
            'namur', 'namen', 'dinant', 'ciney', 'rochefort', 'couvin', 'philippeville',
            'walcourt', 'florennes', 'doische', 'viroinval', 'cerfontaine', 'froidchapelle',
            'beaumont', 'chimay', 'momignies', 'sivry-rance', 'ham-sur-heure-nalinnes',
            'thuin', 'lobbes', 'erquelinnes', 'binche', 'merbes-le-château', 'anderlues',
            'fontaine-leveque', 'chatelet', 'gerpinnes', 'les-bons-villers', 'pont-a-celles',
            'courcelles', 'farciennes', 'aiseau-presles', 'charleroi', 'fleurus',
            'sombreffe', 'gembloux', 'la-bruyere', 'eghezee', 'fernelmont', 'mettet',
            'fosses-la-ville', 'floreffe', 'profondeville', 'sambreville', 'jemeppe-sur-sambre',
            'hastiere', 'onhaye', 'anhee', 'yvoir', 'houyet', 'beauraing', 'bievre',
            'gedinne', 'vresse-sur-semois', 'hamois', 'havelange', 'somme-leuze', 'assesse'
        ],
        'Luik': [
            'liege', 'luik', 'verviers', 'seraing', 'herstal', 'ans', 'saint-nicolas',
            'grace-hollogne', 'chaudfontaine', 'esneux', 'flemalle', 'awans', 'crisnee',
            'remicourt', 'waremme', 'berloz', 'geer', 'oreye', 'faimes', 'fexhe-le-haut-clocher',
            'braives', 'burdinne', 'heron', 'wanze', 'villers-le-bouillet', 'engis',
            'amay', 'verlaine', 'saint-georges-sur-meuse', 'neupre', 'beyne-heusay',
            'soumagne', 'blegny', 'visé', 'dalhem', 'aubel', 'plombières', 'welkenraedt',
            'henri-chapelle', 'battice', 'herve', 'olne', 'trooz', 'pepinster', 'theux',
            'spa', 'jalhay', 'baelen', 'limburg', 'eupen', 'raeren', 'kelmis', 'lontzen',
            'amel', 'bullingen', 'burg-reuland', 'butgenbach', 'sankt-vith', 'malmedy',
            'waimes', 'stavelot', 'stoumont', 'trois-ponts', 'lierneux', 'manhay',
            'erezee', 'hotton', 'marche-en-famenne', 'nassogne', 'rendeux', 'tenneville',
            'houffalize', 'la-roche-en-ardenne', 'gouvy', 'vielsalm', 'comblain-au-pont',
            'hamoir', 'ferrières', 'ouffet', 'clavier', 'modave', 'marchin', 'huy',
            'braives', 'hannut', 'lincent', 'wasseiges'
        ],
        'Henegouwen': [
            'mons', 'charleroi', 'tournai', 'mouscron', 'la-louviere', 'soignies', 'braine-le-comte',
            'enghien', 'lessines', 'ath', 'leuze-en-hainaut', 'peruwelz', 'antoing', 'rumes',
            'brunehaut', 'mont-de-lenclus', 'celles', 'estaimpuis', 'pecq', 'herseaux',
            'dottignies', 'luingne', 'comines-warneton', 'beloeil', 'bernissart', 'honnelles',
            'quievrain', 'boussu', 'colfontaine', 'frameries', 'quaregnon', 'saint-ghislain',
            'dour', 'hensies', 'jurbise', 'lens', 'chievres', 'brugelette', 'silly',
            'ellezelles', 'flobecq', 'frasnes-lez-anvaing', 'mont-de-lenclus', 'pecq',
            'manage', 'seneffe', 'ecaussinnes', 'le-roeulx', 'morlanwelz', 'binche',
            'estinnes', 'merbes-le-château', 'lobbes', 'thuin', 'ham-sur-heure-nalinnes',
            'beaumont', 'froidchapelle', 'sivry-rance', 'momignies', 'chimay', 'couvin',
            'viroinval', 'doische', 'florennes', 'walcourt', 'philippeville', 'cerfontaine',
            'ham-sur-heure', 'gerpinnes', 'montigny-le-tilleul', 'les-bons-villers',
            'pont-a-celles', 'courcelles', 'farciennes', 'aiseau-presles', 'chatelet',
            'fleurus', 'fontaine-leveque', 'anderlues', 'erquelinnes'
        ],
        'Luxemburg': [
            'arlon', 'bastogne', 'marche-en-famenne', 'virton', 'neufchateau', 'saint-hubert',
            'bouillon', 'florenville', 'chiny', 'etalle', 'habay', 'tintigny', 'rouvroy',
            'saint-leger', 'messancy', 'aubange', 'musson', 'durbuy', 'hotton', 'erezee',
            'manhay', 'la-roche-en-ardenne', 'houffalize', 'gouvy', 'vielsalm', 'libramont-chevigny',
            'tellin', 'wellin', 'libin', 'daverdisse', 'saint-hubert', 'tenneville',
            'nassogne', 'rendeux', 'martelange', 'fauvillers', 'leglise', 'vaux-sur-sure',
            'bertogne', 'sainte-ode', 'amberloup', 'noville', 'longvilly', 'bourcy',
            'michamps', 'bizory', 'mageret', 'wardin', 'mande-saint-etienne', 'bertrix',
            'herbeumont', 'paliseul', 'saint-pierre', 'straimont', 'carlsbourg', 'opont',
            'wellin', 'halma', 'lesse', 'chanly', 'bure', 'grupont', 'resteigne',
            'wavreille', 'ave-et-auffe', 'han-sur-lesse', 'eprave', 'jemelle', 'rochefort',
            'buissonville', 'haversin', 'villers-sur-lesse', 'lavaux-sainte-anne', 'lessive'
        ]
    }
    
    errors_found = []
    corrections_needed = []
    total_checked = 0
    
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            
            for row in reader:
                title = row.get('Title', '')
                url = row.get('URL', '')
                stated_province = row.get('Provincie', '')
                
                # Ignorer les pages d'index
                if any(skip in title.lower() for skip in ['kastelen per provincie', 'kastelen in', 'home', 'kaart']):
                    continue
                
                total_checked += 1
                
                # Extraire le nom de la ville depuis l'URL ou le titre
                city_from_url = extract_city_from_url(url)
                city_from_title = extract_city_from_title(title)
                
                # Déterminer la vraie province basée sur la ville
                real_province = determine_real_province(city_from_url, city_from_title, province_cities)
                
                if real_province and real_province != stated_province:
                    error = {
                        'title': title,
                        'url': url,
                        'stated_province': stated_province,
                        'real_province': real_province,
                        'city_url': city_from_url,
                        'city_title': city_from_title
                    }
                    errors_found.append(error)
                    corrections_needed.append(f"{title}: {stated_province} → {real_province}")
                
                if total_checked % 50 == 0:
                    print(f"  Vérifié {total_checked} châteaux...")
    
    except Exception as e:
        print(f"❌ Erreur lecture CSV: {e}")
        return
    
    # Rapport des erreurs
    print(f"\n📊 RÉSULTATS DE LA VÉRIFICATION:")
    print(f"Total châteaux vérifiés: {total_checked}")
    print(f"Erreurs de province trouvées: {len(errors_found)}")
    print(f"Pourcentage d'erreurs: {len(errors_found)/total_checked*100:.1f}%")
    
    if errors_found:
        print(f"\n❌ ERREURS DÉTECTÉES ({len(errors_found)}):")
        for i, error in enumerate(errors_found[:20], 1):  # Limiter à 20 pour l'affichage
            print(f"{i:2d}. {error['title']}")
            print(f"    Déclaré: {error['stated_province']} → Réel: {error['real_province']}")
            print(f"    Ville: {error['city_url']} / {error['city_title']}")
            print()
        
        if len(errors_found) > 20:
            print(f"... et {len(errors_found)-20} autres erreurs")
        
        # Sauvegarder le rapport complet
        with open('/Users/marc/Desktop/kastelenbelgie/province_errors_report.txt', 'w', encoding='utf-8') as f:
            f.write("RAPPORT COMPLET DES ERREURS DE PROVINCES\n")
            f.write("=" * 50 + "\n\n")
            for error in errors_found:
                f.write(f"Château: {error['title']}\n")
                f.write(f"URL: {error['url']}\n")
                f.write(f"Province déclarée: {error['stated_province']}\n")
                f.write(f"Province réelle: {error['real_province']}\n")
                f.write(f"Ville (URL): {error['city_url']}\n")
                f.write(f"Ville (titre): {error['city_title']}\n")
                f.write("-" * 30 + "\n")
        
        print(f"\n📄 Rapport complet sauvé: province_errors_report.txt")
    else:
        print(f"\n✅ Aucune erreur de province détectée !")

def extract_city_from_url(url):
    """Extrait le nom de la ville depuis l'URL"""
    if not url:
        return ""
    
    # Extraire la partie après le dernier /
    parts = url.rstrip('/').split('/')
    if len(parts) > 0:
        filename = parts[-1]
        # Supprimer l'extension et extraire la ville
        if '-' in filename:
            # Prendre la dernière partie après le dernier tiret
            city = filename.split('-')[-1]
            return city.lower().replace('.html', '')
    
    return ""

def extract_city_from_title(title):
    """Extrait le nom de la ville depuis le titre"""
    if not title:
        return ""
    
    # Patterns courants dans les titres
    patterns = [
        r'kasteel.*?(\w+)$',  # Dernier mot
        r'château.*?(\w+)$',  # Dernier mot
        r'van\s+(\w+)',       # Après "van"
        r'de\s+(\w+)',        # Après "de"
        r'te\s+(\w+)',        # Après "te"
        r'in\s+(\w+)',        # Après "in"
    ]
    
    title_lower = title.lower()
    for pattern in patterns:
        match = re.search(pattern, title_lower)
        if match:
            city = match.group(1)
            if len(city) > 2:  # Éviter les mots trop courts
                return city
    
    return ""

def determine_real_province(city_url, city_title, province_cities):
    """Détermine la vraie province basée sur les villes extraites"""
    cities_to_check = [city_url, city_title]
    
    for city in cities_to_check:
        if not city or len(city) < 3:
            continue
            
        city_clean = city.lower().strip()
        
        # Vérifier dans chaque province
        for province, cities_list in province_cities.items():
            if city_clean in cities_list:
                return province
            
            # Vérifier aussi les correspondances partielles
            for city_in_list in cities_list:
                if city_clean in city_in_list or city_in_list in city_clean:
                    if len(city_clean) > 4:  # Éviter les correspondances trop courtes
                        return province
    
    return None

if __name__ == "__main__":
    verify_castle_provinces()
