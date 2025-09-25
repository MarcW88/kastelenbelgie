#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CORRECTION AUTOMATIQUE DES PROVINCES DES CHÂTEAUX
Corrige les 121 erreurs de provinces détectées
"""

import csv
import shutil
from verify_castle_provinces import extract_city_from_url, extract_city_from_title, determine_real_province

def fix_castle_provinces():
    """Corrige automatiquement les provinces incorrectes"""
    csv_file = "/Users/marc/Desktop/kastelenbelgie/chateaux_opening_hours - chateaux_opening_hours.csv"
    backup_file = "/Users/marc/Desktop/kastelenbelgie/chateaux_opening_hours_BACKUP.csv"
    
    print("🔧 CORRECTION DES PROVINCES DES CHÂTEAUX")
    print("=" * 50)
    
    # Créer une sauvegarde
    shutil.copy2(csv_file, backup_file)
    print(f"✅ Sauvegarde créée: {backup_file}")
    
    # Dictionnaire des provinces et villes (même que dans verify)
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
            'sint-truiden', 'gingelom', 'hoeselt', 'houthalen', 'zolder'
        ],
        'Oost-Vlaanderen': [
            'gent', 'aalst', 'sint-niklaas', 'dendermonde', 'eeklo', 'oudenaarde', 'lokeren',
            'wetteren', 'ninove', 'geraardsbergen', 'ronse', 'zottegem', 'herzele', 'haaltert',
            'lede', 'waasmunster', 'temse', 'hamme', 'buggenhout', 'lebbeke', 'berlare',
            'zele', 'laarne', 'wachtebeke', 'zelzate', 'assenede', 'evergem', 'lovendegem',
            'waarschoot', 'knesselare', 'maldegem', 'kaprijke', 'sint-laureins', 'deinze',
            'nevele', 'oosterzele', 'merelbeke', 'melle', 'gontrode', 'destelbergen',
            'nazareth', 'de-pinte', 'gavere', 'zwalm', 'horebeke', 'kluisbergen',
            'wortegem-petegem', 'brakel', 'lierde', 'oosterzele', 'dilsen'
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
            'deerlijk', 'kuurne', 'lendelede', 'ingelmunster', 'izegem', 'hooglede', 'elverdinge'
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
            'wezembeek-oppem', 'machelen', 'grimbergen', 'wemmel', 'strombeek-bever', 'bouchout'
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
            'gedinne', 'vresse-sur-semois', 'hamois', 'havelange', 'somme-leuze', 'assesse', 'celles'
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
            'braives', 'hannut', 'lincent', 'wasseiges', 'froidcourt'
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
            'fleurus', 'fontaine-leveque', 'anderlues', 'erquelinnes', 'biez'
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
            'buissonville', 'haversin', 'villers-sur-lesse', 'lavaux-sainte-anne', 'lessive', 'porcheresse'
        ]
    }
    
    corrections_made = 0
    rows_to_write = []
    
    try:
        # Lire le CSV et corriger les provinces
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            fieldnames = reader.fieldnames
            
            for row in reader:
                title = row.get('Title', '')
                url = row.get('URL', '')
                stated_province = row.get('Provincie', '')
                
                # Ignorer les pages d'index
                if any(skip in title.lower() for skip in ['kastelen per provincie', 'kastelen in', 'home', 'kaart']):
                    rows_to_write.append(row)
                    continue
                
                # Extraire les villes et déterminer la vraie province
                city_from_url = extract_city_from_url(url)
                city_from_title = extract_city_from_title(title)
                real_province = determine_real_province(city_from_url, city_from_title, province_cities)
                
                # Corriger si nécessaire
                if real_province and real_province != stated_province:
                    print(f"✅ Correction: {title}")
                    print(f"   {stated_province} → {real_province}")
                    row['Provincie'] = real_province
                    corrections_made += 1
                
                rows_to_write.append(row)
        
        # Écrire le CSV corrigé
        with open(csv_file, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows_to_write)
        
        print(f"\n📊 CORRECTIONS APPLIQUÉES:")
        print(f"Total corrections: {corrections_made}")
        print(f"Fichier mis à jour: {csv_file}")
        print(f"Sauvegarde disponible: {backup_file}")
        
    except Exception as e:
        print(f"❌ Erreur: {e}")

if __name__ == "__main__":
    fix_castle_provinces()
