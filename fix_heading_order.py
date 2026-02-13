#!/usr/bin/env python3
"""
Script pour corriger l'ordre des en-têtes H1/H2 dans les pages HTML.
Le problème: un H2 dans le placeholder d'image apparaît avant le H1.
Solution: remplacer ce H2 par un élément non-heading (p avec classe).
"""

import os
import re
from pathlib import Path

DIRECTORY = "/Users/marc/Desktop/kastelenbelgie"

# Liste des fichiers à corriger
FILES_TO_FIX = [
    "kasteel-de-merode-westerlo.html",
    "kasteel-engelhof-houthalen.html",
    "kasteel-van-fougeraie-te-ukkel.html",
    "kasteel-van-wegimont-ayeneux-soumagne.html",
    "kasteel-van-tavigny-tavigny-houffalize.html",
    "chateau-de-bellaire-haltinne.html",
    "kasteel-laide-fagne-steinbach.html",
    "kasteel-le-fy-esneux.html",
    "kasteel-van-vorst-meerlaer-laakdal.html",
    "kasteel-vieux-chateau-saive-blegny.html",
    "kasteel-van-la-roche-en-ardenne-la-roche-en-ardenne.html",
    "kasteel-van-froidcourt-stoumont.html",
    "kasteel-van-waleffe-les-waleffes.html",
    "kasteel-van-sohier-sohier.html",
    "kasteel-ter-lucht-sint-andries.html",
    "kasteel-van-wodemont-neufchateau-luik.html",
    "kasteel-van-baronville-baronville-belgie.html",
    "kasteel-mohimont-villers-devant-orval.html",
    "kasteel-maxburg-meer.html",
    "kasteel-van-moere-le-bon-sejour-moere.html",
    "kasteel-van-moriensart-ceroux-mousty.html",
    "kasteel-van-haltinne-haltinne.html",
    "kasteel-van-genval-rixensart.html",
    "chateau-le-duc-ucimont.html",
    "kasteel-van-mouffrin-natoye.html",
    "kasteel-des-cailloux-geldenaken.html",
    "kasteel-van-gravenhof-te-dworp.html",
    "kasteel-van-braine-le-chateau-kasteelbrakel.html",
    "kasteel-van-rixensart-rixensart.html",
    "kasteel-drie-koningen-beernem.html",
    "kasteel-ter-borcht-meulebeke.html",
    "kasteel-t-hooghe-kortrijk.html",
    "het-grafelijk-slot-van-male-sint-kruis.html",
    "kasteel-van-elverdinge-ieper.html",
    "kasteel-van-wakken-wakken.html",
    "kasteel-casier-waregem.html",
    "kasteel-ravenhof-torhout-torhout.html",
    "kasteel-van-spiere-spiere.html",
    "gaverkasteel-deerlijk.html",
    "kasteel-van-olsene-olsene-zulte.html",
    "kasteel-ingelmunster-ingelmunster.html",
    "kasteel-van-voorde-voorde.html",
    "kasteel-van-roumont-roumont.html",
    "kasteel-karreveld-te-sint-jans-molenbeek.html",
    "kasteel-van-nokere-nokere-kruishoutem.html",
    "kasteel-gavergracht-vinderhoute.html",
    "het-wit-kasteel-te-linden.html",
    "de-berlaarhof-berlaar.html",
    "kasteel-van-schoten-schoten.html",
    "kasteel-arendsnest-edegem.html",
    "kasteel-la-motte-te-sint-ulriks-kapelle.html",
    "de-hof-van-veltwijck-ekeren.html",
    "kasteel-cantecroy-mortsel.html",
    "kasteel-mariahove-bellem.html",
    "kasteel-solvay-kasteel-van-ter-hulpen-terhulpen.html",
    "kasteel-selsaete-wommelgem.html",
    "kasteel-van-villers-schoten.html",
    "kasteel-van-la-berliere-houtaing.html",
    "kasteel-walburg-sint-niklaas.html",
    "kasteel-van-brasschaat-brasschaat.html",
    "kasteel-kijckuit-wijnegem.html",
    "kasteel-van-dieupart-aywaille.html",
    "kasteel-mussenborg-edegem.html",
    "de-hof-van-riemen-heist-op-den-berg.html",
    "kasteel-van-tillegem-sint-michiels.html",
    "kasteel-terlaemen-te-viversel-zolder-gemeente-heusden-zolder.html",
    "kasteel-van-wijer-te-wijer-gemeente-nieuwerkerken.html",
    "kasteel-van-haversin-serinchamps.html",
    "kasteel-carolinaberg-stokkem.html",
    "kasteel-de-motte-groot-gelmen-bij-sint-truiden.html",
    "kasteel-van-obsinnich-remersdaal-te-voeren.html",
    "kasteel-van-mombeek-hasselt.html",
    "kasteel-de-commanderij-sint-pieters-voeren.html",
    "kasteel-stas-de-richelle-heusden.html",
    "commanderij-van-sint-pieters-voeren-te-sint-pieters-voeren-te-voeren.html",
    "kasteel-duras-te-duras.html",
    "waterburcht-millen-millen-te-riemst.html",
    "kasteel-daspremont-lynden-oud-rekem-gemeente-lanaken.html",
    "de-solhof-aartselaar.html",
]

def fix_heading_order(filepath):
    """Corrige l'ordre des en-têtes dans un fichier HTML."""
    
    filename = os.path.basename(filepath)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Pattern 1: H2 dans le placeholder d'image avant H1
    # <h2>📸 Kasteel naam</h2> -> <p class="placeholder-title">📸 Kasteel naam</p>
    pattern1 = r'<div class="image-placeholder">\s*<h2>(.*?)</h2>'
    replacement1 = r'<div class="image-placeholder">\n<p class="placeholder-title">\1</p>'
    content = re.sub(pattern1, replacement1, content, flags=re.DOTALL)
    
    # Pattern 2: H2 avec emoji photo dans placeholder
    pattern2 = r'<h2>📸\s*(.*?)</h2>\s*<p>Afbeelding'
    replacement2 = r'<p class="placeholder-title">📸 \1</p>\n<p>Afbeelding'
    content = re.sub(pattern2, replacement2, content)
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Corrigé: {filename}")
        return True
    else:
        print(f"⏭️  Pas de changement nécessaire: {filename}")
        return False

def main():
    """Corrige l'ordre des en-têtes dans les fichiers listés."""
    
    print(f"\n🔧 Correction de l'ordre des en-têtes H1/H2\n")
    print("=" * 60)
    
    fixed = 0
    skipped = 0
    errors = 0
    not_found = 0
    
    for filename in FILES_TO_FIX:
        filepath = os.path.join(DIRECTORY, filename)
        
        if not os.path.exists(filepath):
            print(f"⚠️  Fichier non trouvé: {filename}")
            not_found += 1
            continue
        
        try:
            result = fix_heading_order(filepath)
            if result:
                fixed += 1
            else:
                skipped += 1
        except Exception as e:
            print(f"❌ Erreur: {filename} - {e}")
            errors += 1
    
    print("=" * 60)
    print(f"\n📊 Résumé:")
    print(f"   ✅ Fichiers corrigés: {fixed}")
    print(f"   ⏭️  Pas de changement: {skipped}")
    print(f"   ⚠️  Non trouvés: {not_found}")
    print(f"   ❌ Erreurs: {errors}")
    print(f"   📁 Total fichiers traités: {len(FILES_TO_FIX)}")

if __name__ == "__main__":
    main()
