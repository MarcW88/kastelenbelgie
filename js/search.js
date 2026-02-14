// Fonctionnalité de recherche pour kastelenbelgie.be

// Liste complète des châteaux (générée automatiquement)
const castles = [
    {name: "Algemene Voorwaarden", url: "algemene-voorwaarden.html"},
    {name: "Bisschoppenhof", url: "bisschoppenhof-deurne.html"},
    {name: "Braemkasteel", url: "braemkasteel-gentbrugge.html"},
    {name: "Burcht reuland", url: "burcht-reuland-reuland-burg-reuland.html"},
    {name: "Burchtruine van Montquintin", url: "burchtruine-van-montquintin-montquintin-dampicourt.html"},
    {name: "Chateau de Prelle", url: "chateau-de-prelle-manage.html"},
    {name: "Chateau de bellaire", url: "chateau-de-bellaire-haltinne.html"},
    {name: "Chateau de la tournette", url: "chateau-de-la-tournette-nijvel.html"},
    {name: "Chateau le duc", url: "chateau-le-duc-ucimont.html"},
    {name: "Citadel van hoei", url: "citadel-van-hoei-hoei.html"},
    {name: "Commanderij van sint pieters voeren", url: "commanderij-van-sint-pieters-voeren-te-sint-pieters-voeren-te-voeren.html"},
    {name: "De berlaarhof", url: "de-berlaarhof-berlaar.html"},
    {name: "De beukenhof", url: "de-beukenhof-kapellen.html"},
    {name: "De cijnshof van boutersem", url: "de-cijnshof-van-boutersem-zandhoven.html"},
    {name: "De hof ter beke", url: "de-hof-ter-beke-wilrijk.html"},
    {name: "De hof van riemen", url: "de-hof-van-riemen-heist-op-den-berg.html"},
    {name: "De hof van veltwijck", url: "de-hof-van-veltwijck-ekeren.html"},
    {name: "De solhof", url: "de-solhof-aartselaar.html"},
    {name: "Domein de ghellinck", url: "domein-de-ghellinck-elsegem.html"},
    {name: "Gaverkasteel", url: "gaverkasteel-deerlijk.html"},
    {name: "Het grafelijk slot van male", url: "het-grafelijk-slot-van-male-sint-kruis.html"},
    {name: "Het rood kasteel", url: "het-rood-kasteel-te-linden.html"},
    {name: "Het wit kasteel", url: "het-wit-kasteel-te-linden.html"},
    {name: "Hof te melis", url: "hof-te-melis-lippelo.html"},
    {name: "Hof ter borght", url: "hof-ter-borght-westmeerbeek.html"},
    {name: "Hof van liere", url: "hof-van-liere-zandhoven.html"},
    {name: "Hof van ringen", url: "hof-van-ringen-lier.html"},
    {name: "Hof van roosendael", url: "hof-van-roosendael-merksem.html"},
    {name: "Kasteel Beauregard", url: "kasteel-beauregard-froyennes.html"},
    {name: "Kasteel Laresteen", url: "kasteel-laresteen-lovendegem.html"},
    {name: "Kasteel Mohimont", url: "kasteel-mohimont-villers-devant-orval.html"},
    {name: "Kasteel Petite-Somme", url: "kasteel-petite-somme-petite-somme.html"},
    {name: "Kasteel altembrouck", url: "kasteel-altembrouck-s-gravenvoeren-te-voeren.html"},
    {name: "Kasteel arendsnest", url: "kasteel-arendsnest-edegem.html"},
    {name: "Kasteel baelen", url: "kasteel-baelen-hendrik-kapelle.html"},
    {name: "Kasteel bayard", url: "kasteel-bayard-dhuy.html"},
    {name: "Kasteel befferhof", url: "kasteel-befferhof-bonheiden.html"},
    {name: "Kasteel belvedere", url: "kasteel-belvedere-te-laken-brussel.html"},
    {name: "Kasteel blauw huys", url: "kasteel-blauw-huys-drongen-gent.html"},
    {name: "Kasteel blauwhuis", url: "kasteel-blauwhuis-izegem.html"},
    {name: "Kasteel boeckenberg", url: "kasteel-boeckenberg-deurne.html"},
    {name: "Kasteel borghoven", url: "kasteel-borghoven-piringen-bij-tongeren.html"},
    {name: "Kasteel borgwal", url: "kasteel-borgwal-gavere.html"},
    {name: "Kasteel borluut", url: "kasteel-borluut-sint-denijs-westrem.html"},
    {name: "Kasteel borrekens", url: "kasteel-borrekens-vorselaar.html"},
    {name: "Kasteel bouckenborgh", url: "kasteel-bouckenborgh-merksem.html"},
    {name: "Kasteel brunsode", url: "kasteel-brunsode-tilff.html"},
    {name: "Kasteel cantecroy", url: "kasteel-cantecroy-mortsel.html"},
    {name: "Kasteel carolinaberg", url: "kasteel-carolinaberg-stokkem.html"},
    {name: "Kasteel casier", url: "kasteel-casier-waregem.html"},
    {name: "Kasteel claeys bouuaert", url: "kasteel-claeys-bouuaert-mariakerke.html"},
    {name: "Kasteel cortewalle", url: "kasteel-cortewalle-beveren-waas.html"},
    {name: "Kasteel daalbroek", url: "kasteel-daalbroek-rekem.html"},
    {name: "Kasteel daspremont lynden", url: "kasteel-daspremont-lynden-oud-rekem-gemeente-lanaken.html"},
    {name: "Kasteel de bist", url: "kasteel-de-bist-ekeren.html"},
    {name: "Kasteel de blauwe toren", url: "kasteel-de-blauwe-toren-varsenare.html"},
    {name: "Kasteel de campagne", url: "kasteel-de-campagne-drongen-gent.html"},
    {name: "Kasteel de commanderij", url: "kasteel-de-commanderij-sint-pieters-voeren.html"},
    {name: "Kasteel de faille", url: "kasteel-de-faille-brugge.html"},
    {name: "Kasteel de hoof teuven", url: "kasteel-de-hoof-teuven-te-voeren.html"},
    {name: "Kasteel de marnix", url: "kasteel-de-marnix-te-overijse.html"},
    {name: "Kasteel de merode", url: "kasteel-de-merode-westerlo.html"},
    {name: "Kasteel de merode", url: "kasteel-de-merode-te-dilbeek.html"},
    {name: "Kasteel de motte groot gelmen", url: "kasteel-de-motte-groot-gelmen-bij-sint-truiden.html"},
    {name: "Kasteel de pelichy", url: "kasteel-de-pelichy-gent.html"},
    {name: "Kasteel de renesse", url: "kasteel-de-renesse-oostmalle.html"},
    {name: "Kasteel de rivieren", url: "kasteel-de-rivieren-te-ganshoren.html"},
    {name: "Kasteel des cailloux", url: "kasteel-des-cailloux-geldenaken.html"},
    {name: "Kasteel diepenbroeck", url: "kasteel-diepenbroeck-lovendegem.html"},
    {name: "Kasteel diependael", url: "kasteel-diependael-elewijt.html"},
    {name: "Kasteel doverschie", url: "kasteel-doverschie-te-grimbergen.html"},
    {name: "Kasteel drie koningen", url: "kasteel-drie-koningen-beernem.html"},
    {name: "Kasteel du lac genval", url: "kasteel-du-lac-genval.html"},
    {name: "Kasteel duras", url: "kasteel-duras-te-duras.html"},
    {name: "Kasteel edelhof", url: "kasteel-edelhof-munsterbilzen.html"},
    {name: "Kasteel en park", url: "kasteel-en-park-ter-rijst-te-heikruis.html"},
    {name: "Kasteel engelhof", url: "kasteel-engelhof-houthalen.html"},
    {name: "Kasteel eyneburg", url: "kasteel-eyneburg-hergenrath.html"},
    {name: "Kasteel fallon de keyser", url: "kasteel-fallon-de-keyser-destelbergen.html"},
    {name: "Kasteel gavergracht", url: "kasteel-gavergracht-vinderhoute.html"},
    {name: "Kasteel grevenbroek", url: "kasteel-grevenbroek-achel.html"},
    {name: "Kasteel groenendaal", url: "kasteel-groenendaal-merksem.html"},
    {name: "Kasteel groenendaal", url: "kasteel-groenendaal-te-waltwilder-gemeente-bilzen.html"},
    {name: "Kasteel groenveld", url: "kasteel-groenveld-te-grimbergen.html"},
    {name: "Kasteel hof ter saksen", url: "kasteel-hof-ter-saksen-beveren-waas.html"},
    {name: "Kasteel hoogveld", url: "kasteel-hoogveld-vliermaal.html"},
    {name: "Kasteel hoogveld", url: "kasteel-hoogveld-veldegem.html"},
    {name: "Kasteel hovorst", url: "kasteel-hovorst-viersel.html"},
    {name: "Kasteel hulsberg", url: "kasteel-hulsberg-borgloon.html"},
    {name: "Kasteel ingelmunster", url: "kasteel-ingelmunster-ingelmunster.html"},
    {name: "Kasteel isschot", url: "kasteel-isschot-itegem.html"},
    {name: "Kasteel karreveld", url: "kasteel-karreveld-te-sint-jans-molenbeek.html"},
    {name: "Kasteel kijckuit", url: "kasteel-kijckuit-wijnegem.html"},
    {name: "Kasteel la motte", url: "kasteel-la-motte-te-sint-ulriks-kapelle.html"},
    {name: "Kasteel laide", url: "kasteel-laide-fagne-steinbach.html"},
    {name: "Kasteel le fy", url: "kasteel-le-fy-esneux.html"},
    {name: "Kasteel leva", url: "kasteel-leva-alken.html"},
    {name: "Kasteel lhirondelle", url: "kasteel-lhirondelle-oteppe.html"},
    {name: "Kasteel lozer", url: "kasteel-lozer-lozer-kruishoutem.html"},
    {name: "Kasteel mariahove", url: "kasteel-mariahove-bellem.html"},
    {name: "Kasteel marnix de sainte aldegonde", url: "kasteel-marnix-de-sainte-aldegonde-bornem.html"},
    {name: "Kasteel maxburg", url: "kasteel-maxburg-meer.html"},
    {name: "Kasteel meerlenhof", url: "kasteel-meerlenhof-hoboken.html"},
    {name: "Kasteel miranda", url: "kasteel-miranda-celles.html"},
    {name: "Kasteel mussenborg", url: "kasteel-mussenborg-edegem.html"},
    {name: "Kasteel nieuwland", url: "kasteel-nieuwland-te-aarschot.html"},
    {name: "Kasteel ommerstein", url: "kasteel-ommerstein-te-rotem-bij-dilsen.html"},
    {name: "Kasteel oude kluis", url: "kasteel-oude-kluis-gent.html"},
    {name: "Kasteel pulhof", url: "kasteel-pulhof-wijnegem.html"},
    {name: "Kasteel puyenbrug", url: "kasteel-puyenbrug-domein-puyenbroeck-wachtebeke.html"},
    {name: "Kasteel ravenhof", url: "kasteel-ravenhof-torhout-torhout.html"},
    {name: "Kasteel reinhardstein", url: "kasteel-reinhardstein-burg-metternich-te-weismes.html"},
    {name: "Kasteel roos", url: "kasteel-roos-waasmunster.html"},
    {name: "Kasteel rose", url: "kasteel-rose-orp-le-petit.html"},
    {name: "Kasteel rouge bas", url: "kasteel-rouge-bas-oha-wanze.html"},
    {name: "Kasteel saint pierre", url: "kasteel-saint-pierre-beauraing.html"},
    {name: "Kasteel scheldevelde", url: "kasteel-scheldevelde-de-pinte.html"},
    {name: "Kasteel selsaete", url: "kasteel-selsaete-wommelgem.html"},
    {name: "Kasteel slotendries", url: "kasteel-slotendries-oostakker.html"},
    {name: "Kasteel solvay", url: "kasteel-solvay-kasteel-van-ter-hulpen-terhulpen.html"},
    {name: "Kasteel stas de richelle", url: "kasteel-stas-de-richelle-heusden.html"},
    {name: "Kasteel t hooghe", url: "kasteel-t-hooghe-kortrijk.html"},
    {name: "Kasteel ten bieze", url: "kasteel-ten-bieze-beerlegem.html"},
    {name: "Kasteel ter beken", url: "kasteel-ter-beken-mariakerke-gent.html"},
    {name: "Kasteel ter borcht", url: "kasteel-ter-borcht-meulebeke.html"},
    {name: "Kasteel ter elst", url: "kasteel-ter-elst-duffel.html"},
    {name: "Kasteel ter leyen", url: "kasteel-ter-leyen-boekhoute.html"},
    {name: "Kasteel ter lucht", url: "kasteel-ter-lucht-sint-andries.html"},
    {name: "Kasteel ter meeren", url: "kasteel-ter-meeren-sterrebeek-zaventem.html"},
    {name: "Kasteel ter motten", url: "kasteel-ter-motten-te-dilsen.html"},
    {name: "Kasteel terlaemen", url: "kasteel-terlaemen-te-viversel-zolder-gemeente-heusden-zolder.html"},
    {name: "Kasteel terlinden", url: "kasteel-terlinden-aalst.html"},
    {name: "Kasteel tudor", url: "kasteel-tudor-sint-andries.html"},
    {name: "Kasteel van Attre", url: "kasteel-van-attre-attre.html"},
    {name: "Kasteel van Boussu", url: "kasteel-van-boussu-boussu.html"},
    {name: "Kasteel van Deulin", url: "kasteel-van-deulin-deulin-fronville.html"},
    {name: "Kasteel van Durbuy", url: "kasteel-van-durbuy-durbuy.html"},
    {name: "Kasteel van Fosteau", url: "kasteel-van-fosteau-leers-et-fosteau.html"},
    {name: "Kasteel van Habay-la-Neuve", url: "kasteel-van-habay-la-neuve-habay-la-neuve.html"},
    {name: "Kasteel van La Berlière", url: "kasteel-van-la-berliere-houtaing.html"},
    {name: "Kasteel van La Roche-en-Ardenne", url: "kasteel-van-la-roche-en-ardenne-la-roche-en-ardenne.html"},
    {name: "Kasteel van Mirwart", url: "kasteel-van-mirwart-mirwart-saint-hubert.html"},
    {name: "Kasteel van Orval", url: "kasteel-van-orval-villers-devant-orval.html"},
    {name: "Kasteel van Porcheresse", url: "kasteel-van-porcheresse-daverdisse.html"},
    {name: "Kasteel van Roumont", url: "kasteel-van-roumont-roumont.html"},
    {name: "Kasteel van Sohier", url: "kasteel-van-sohier-sohier.html"},
    {name: "Kasteel van Spiere", url: "kasteel-van-spiere-spiere.html"},
    {name: "Kasteel van Tavigny", url: "kasteel-van-tavigny-tavigny-houffalize.html"},
    {name: "Kasteel van Templeuve", url: "kasteel-van-templeuve-templeuve.html"},
    {name: "Kasteel van Voneche", url: "kasteel-van-voneche-voneche.html"},
    {name: "Kasteel van Vêves", url: "kasteel-van-veves-te-celles.html"},
    {name: "Kasteel van Wippelgem", url: "kasteel-van-wippelgem-wippelgem.html"},
    {name: "Kasteel van altena", url: "kasteel-van-altena-kruibeke.html"},
    {name: "Kasteel van altena", url: "kasteel-van-altena-kontich.html"},
    {name: "Kasteel van awans", url: "kasteel-van-awans-awans.html"},
    {name: "Kasteel van baronville", url: "kasteel-van-baronville-baronville-belgie.html"},
    {name: "Kasteel van beauraing", url: "kasteel-van-beauraing-beauraing.html"},
    {name: "Kasteel van beervelde", url: "kasteel-van-beervelde-beervelde.html"},
    {name: "Kasteel van berlare", url: "kasteel-van-berlare-berlare.html"},
    {name: "Kasteel van beusdael", url: "kasteel-van-beusdael-bij-sippenaeken.html"},
    {name: "Kasteel van bever", url: "kasteel-van-bever-te-strombeek-bever.html"},
    {name: "Kasteel van biez", url: "kasteel-van-biez-peruwelz.html"},
    {name: "Kasteel van blekkom", url: "kasteel-van-blekkom-loksbergen.html"},
    {name: "Kasteel van bokrijk", url: "kasteel-van-bokrijk-genk.html"},
    {name: "Kasteel van bouchout", url: "kasteel-van-bouchout-te-meise.html"},
    {name: "Kasteel van braine le chateau", url: "kasteel-van-braine-le-chateau-kasteelbrakel.html"},
    {name: "Kasteel van brasschaat", url: "kasteel-van-brasschaat-brasschaat.html"},
    {name: "Kasteel van coloma", url: "kasteel-van-coloma-te-sint-pieters-leeuw.html"},
    {name: "Kasteel van corroy le chateau", url: "kasteel-van-corroy-le-chateau-corroy-le-chateau.html"},
    {name: "Kasteel van dieupart", url: "kasteel-van-dieupart-aywaille.html"},
    {name: "Kasteel van elverdinge", url: "kasteel-van-elverdinge-ieper.html"},
    {name: "Kasteel van fougeraie", url: "kasteel-van-fougeraie-te-ukkel.html"},
    {name: "Kasteel van freyr", url: "kasteel-van-freyr-freyr.html"},
    {name: "Kasteel van froidcourt", url: "kasteel-van-froidcourt-stoumont.html"},
    {name: "Kasteel van genval", url: "kasteel-van-genval-rixensart.html"},
    {name: "Kasteel van gravenhof", url: "kasteel-van-gravenhof-te-dworp.html"},
    {name: "Kasteel van haltinne", url: "kasteel-van-haltinne-haltinne.html"},
    {name: "Kasteel van haversin", url: "kasteel-van-haversin-serinchamps.html"},
    {name: "Kasteel van heetvelde", url: "kasteel-van-heetvelde-te-oetingen.html"},
    {name: "Kasteel van hermalle sous huy", url: "kasteel-van-hermalle-sous-huy-hermalle-sous-huy-engis.html"},
    {name: "Kasteel van jeanne", url: "kasteel-van-jeanne-de-merode-nieuw-kasteel-westerlo.html"},
    {name: "Kasteel van julius caesar", url: "kasteel-van-julius-caesar-doornik.html"},
    {name: "Kasteel van kruishoutem", url: "kasteel-van-kruishoutem-kruishoutem.html"},
    {name: "Kasteel van leeuwergem", url: "kasteel-van-leeuwergem-leeuwergem-zottegem.html"},
    {name: "Kasteel van limont", url: "kasteel-van-limont-donceel.html"},
    {name: "Kasteel van longchamps", url: "kasteel-van-longchamps-longchamps-bertogne.html"},
    {name: "Kasteel van melveren", url: "kasteel-van-melveren-sint-truiden.html"},
    {name: "Kasteel van moere", url: "kasteel-van-moere-le-bon-sejour-moere.html"},
    {name: "Kasteel van moerkerke", url: "kasteel-van-moerkerke-moerkerke.html"},
    {name: "Kasteel van mombeek", url: "kasteel-van-mombeek-hasselt.html"},
    {name: "Kasteel van montaigle", url: "kasteel-van-montaigle-falaen.html"},
    {name: "Kasteel van montjardin", url: "kasteel-van-montjardin-sougne-remouchamps.html"},
    {name: "Kasteel van moriensart", url: "kasteel-van-moriensart-ceroux-mousty.html"},
    {name: "Kasteel van mouffrin", url: "kasteel-van-mouffrin-natoye.html"},
    {name: "Kasteel van neigem", url: "kasteel-van-neigem-meerbeke.html"},
    {name: "Kasteel van nieuwenhoven", url: "kasteel-van-nieuwenhoven-te-sint-truiden.html"},
    {name: "Kasteel van nokere", url: "kasteel-van-nokere-nokere-kruishoutem.html"},
    {name: "Kasteel van obsinnich remersdaal te voeren", url: "kasteel-van-obsinnich-remersdaal-te-voeren.html"},
    {name: "Kasteel van olsene", url: "kasteel-van-olsene-olsene-zulte.html"},
    {name: "Kasteel van regelsbrugge", url: "kasteel-van-regelsbrugge-aalst.html"},
    {name: "Kasteel van rethy", url: "kasteel-van-rethy-retie.html"},
    {name: "Kasteel van rivieren", url: "kasteel-van-rivieren-te-aarschot.html"},
    {name: "Kasteel van rixensart", url: "kasteel-van-rixensart-rixensart.html"},
    {name: "Kasteel van roborst", url: "kasteel-van-roborst-roborst.html"},
    {name: "Kasteel van rond", url: "kasteel-van-rond-chene-esneux.html"},
    {name: "Kasteel van rullingen", url: "kasteel-van-rullingen-te-kuttekoven-gemeente-borgloon.html"},
    {name: "Kasteel van s gravenwezel", url: "kasteel-van-s-gravenwezel-s-gravenwezel.html"},
    {name: "Kasteel van saffelberg", url: "kasteel-van-saffelberg-gooik.html"},
    {name: "Kasteel van schoonhoven", url: "kasteel-van-schoonhoven-te-aarschot.html"},
    {name: "Kasteel van schoten", url: "kasteel-van-schoten-schoten.html"},
    {name: "Kasteel van seneffe", url: "kasteel-van-seneffe-seneffe.html"},
    {name: "Kasteel van seraing", url: "kasteel-van-seraing-le-chateau-seraing-le-chateau.html"},
    {name: "Kasteel van skeuvre", url: "kasteel-van-skeuvre-natoye.html"},
    {name: "Kasteel van sombreffe", url: "kasteel-van-sombreffe-sombreffe.html"},
    {name: "Kasteel van spontin", url: "kasteel-van-spontin-spontin.html"},
    {name: "Kasteel van strijtem", url: "kasteel-van-strijtem-strijtem.html"},
    {name: "Kasteel van tieghem", url: "kasteel-van-tieghem-de-ten-berghe-mariakerke.html"},
    {name: "Kasteel van tillegem", url: "kasteel-van-tillegem-sint-michiels.html"},
    {name: "Kasteel van veerle", url: "kasteel-van-veerle-laakdal.html"},
    {name: "Kasteel van veulen", url: "kasteel-van-veulen-veulen.html"},
    {name: "Kasteel van vianden", url: "kasteel-van-vianden-vianden.html"},
    {name: "Kasteel van villers schoten", url: "kasteel-van-villers-schoten.html"},
    {name: "Kasteel van voorde", url: "kasteel-van-voorde-voorde.html"},
    {name: "Kasteel van vorst", url: "kasteel-van-vorst-meerlaer-laakdal.html"},
    {name: "Kasteel van wakken", url: "kasteel-van-wakken-wakken.html"},
    {name: "Kasteel van waleffe", url: "kasteel-van-waleffe-les-waleffes.html"},
    {name: "Kasteel van waroux", url: "kasteel-van-waroux-alleur.html"},
    {name: "Kasteel van wedergrate", url: "kasteel-van-wedergrate-ninove.html"},
    {name: "Kasteel van wegimont", url: "kasteel-van-wegimont-ayeneux-soumagne.html"},
    {name: "Kasteel van weillen", url: "kasteel-van-weillen-weilen.html"},
    {name: "Kasteel van wemmel", url: "kasteel-van-wemmel-te-wemmel.html"},
    {name: "Kasteel van westmalle", url: "kasteel-van-westmalle-westmalle.html"},
    {name: "Kasteel van wideux", url: "kasteel-van-wideux-hasselt.html"},
    {name: "Kasteel van wijer", url: "kasteel-van-wijer-te-wijer-gemeente-nieuwerkerken.html"},
    {name: "Kasteel van wimmertingen", url: "kasteel-van-wimmertingen-wimmertingen.html"},
    {name: "Kasteel van wodemont", url: "kasteel-van-wodemont-neufchateau-luik.html"},
    {name: "Kasteel van zellaer", url: "kasteel-van-zellaer-bonheiden.html"},
    {name: "Kasteel vieux chateau", url: "kasteel-vieux-chateau-saive-blegny.html"},
    {name: "Kasteel viteux", url: "kasteel-viteux-de-pinte.html"},
    {name: "Kasteel vogelsanck", url: "kasteel-vogelsanck-te-zolder-gemeente-heusden-zolder.html"},
    {name: "Kasteel waalborre", url: "kasteel-waalborre-te-asse.html"},
    {name: "Kasteel walburg", url: "kasteel-walburg-sint-niklaas.html"},
    {name: "Kasteel wittouck", url: "kasteel-wittouck-sint-pieters-leeuw.html"},
    {name: "Kastelen brussel", url: "kastelen-brussel.html"},
    {name: "Kastelen in Brussels Hoofdstedelijk Gewest", url: "brussel.html"},
    {name: "Kastelen waals brabant", url: "kastelen-waals-brabant.html"},
    {name: "Koninklijk kasteel van ciergnon", url: "koninklijk-kasteel-van-ciergnon-houyet.html"},
    {name: "Oud kasteel van vichte", url: "oud-kasteel-van-vichte-vichte.html"},
    {name: "Paleis op de koudenberg", url: "paleis-op-de-koudenberg-te-brussel.html"},
    {name: "Privacybeleid", url: "privacybeleid.html"},
    {name: "Rentmeesterij van alden biesen", url: "rentmeesterij-van-alden-biesen-te-diepenbeek.html"},
    {name: "Rood kasteel", url: "rood-kasteel-guigoven.html"},
    {name: "Sint-Antoniuskasteel", url: "sint-antoniuskasteel-celles.html"},
    {name: "Test Design Moderne - Kastelen België", url: "test-modern-design.html"},
    {name: "Vrieselhof", url: "vrieselhof-oelegem.html"},
    {name: "Waterburcht millen", url: "waterburcht-millen-millen-te-riemst.html"},
    {name: "Waterkasteel van moorsel", url: "waterkasteel-van-moorsel-moorsel.html"},
    {name: "Waterkasteel van schoonbeek", url: "waterkasteel-van-schoonbeek-te-beverst-gemeente-bilzen.html"},
    {name: "Waterslot cleydael", url: "waterslot-cleydael-aartselaar.html"},
];

// Fonction de recherche
function searchCastles(query) {
    if (!query || query.length < 2) {
        return [];
    }
    
    const searchTerm = query.toLowerCase();
    return castles.filter(castle => 
        castle.name.toLowerCase().includes(searchTerm)
    ).slice(0, 8); // Limiter à 8 résultats
}

// Affichage des résultats
function displaySearchResults(results) {
    const resultsContainer = document.getElementById('search-results');
    
    if (!resultsContainer) {
        return;
    }
    
    if (results.length === 0) {
        resultsContainer.style.display = 'none';
        return;
    }
    
    resultsContainer.innerHTML = results.map(castle => `
        <div class="search-result-item">
            <a href="${castle.url}">
                <span class="castle-icon">🏰</span>
                <span class="castle-name">${castle.name}</span>
            </a>
        </div>
    `).join('');
    
    resultsContainer.style.display = 'block';
}

// Initialisation de la recherche
function initializeSearch() {
    const searchInput = document.getElementById('search-input');
    const searchResults = document.getElementById('search-results');
    
    if (!searchInput) {
        return;
    }
    
    // Créer le conteneur de résultats s'il n'existe pas
    if (!searchResults) {
        const resultsDiv = document.createElement('div');
        resultsDiv.id = 'search-results';
        resultsDiv.className = 'search-results';
        searchInput.parentNode.appendChild(resultsDiv);
    }
    
    // Event listener pour la saisie
    searchInput.addEventListener('input', function(e) {
        const query = e.target.value;
        const results = searchCastles(query);
        displaySearchResults(results);
    });
    
    // Masquer les résultats quand on clique ailleurs
    document.addEventListener('click', function(e) {
        if (!e.target.closest('.search-box')) {
            const resultsContainer = document.getElementById('search-results');
            if (resultsContainer) {
                resultsContainer.style.display = 'none';
            }
        }
    });
    
    // Empêcher la fermeture quand on clique dans la search box
    const searchBox = document.querySelector('.search-box');
    if (searchBox) {
        searchBox.addEventListener('click', function(e) {
            e.stopPropagation();
        });
    }
}

// Styles CSS pour les résultats de recherche
const searchStyles = `
.search-box {
    position: relative;
}

.search-results {
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
    z-index: 1000;
    max-height: 300px;
    overflow-y: auto;
    display: none;
}

.search-result-item {
    border-bottom: 1px solid #f1f5f9;
}

.search-result-item:last-child {
    border-bottom: none;
}

.search-result-item a {
    display: flex;
    align-items: center;
    padding: 0.75rem 1rem;
    text-decoration: none;
    color: #374151;
    transition: background-color 0.2s ease;
}

.search-result-item a:hover {
    background-color: #f8fafc;
}

.castle-icon {
    margin-right: 0.75rem;
    font-size: 1.2rem;
}

.castle-name {
    font-weight: 500;
}

.search-input {
    width: 100%;
    padding: 0.5rem 1rem;
    border: 1px solid #d1d5db;
    border-radius: 6px;
    font-size: 0.9rem;
    transition: border-color 0.2s ease, box-shadow 0.2s ease;
}

.search-input:focus {
    outline: none;
    border-color: #667eea;
    box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

@media (max-width: 768px) {
    .search-results {
        left: -100px;
        right: -100px;
    }
}
`;

// Ajouter les styles CSS
function addSearchStyles() {
    const styleSheet = document.createElement('style');
    styleSheet.textContent = searchStyles;
    document.head.appendChild(styleSheet);
}

// Fonction pour filtrer la liste des châteaux sur alle-kastelen.html
function initializePageFilter() {
    // Vérifier si on est sur alle-kastelen.html
    if (!window.location.pathname.includes('alle-kastelen')) {
        return;
    }
    
    // Récupérer les paramètres URL
    const urlParams = new URLSearchParams(window.location.search);
    const query = urlParams.get('q');
    const type = urlParams.get('type');
    const regio = urlParams.get('regio');
    
    if (!query && !type && !regio) {
        return;
    }
    
    // Filtrer les éléments de la liste
    const castleItems = document.querySelectorAll('.castle-list-item');
    const letterSections = document.querySelectorAll('.letter-section');
    let visibleCount = 0;
    
    castleItems.forEach(item => {
        const link = item.querySelector('.castle-link');
        const meta = item.querySelector('.castle-meta');
        
        if (!link) return;
        
        const name = link.textContent.toLowerCase();
        const location = meta ? meta.textContent.toLowerCase() : '';
        const searchText = name + ' ' + location;
        
        let visible = true;
        
        // Filtre par recherche texte
        if (query) {
            const searchTerms = query.toLowerCase().split(' ');
            visible = searchTerms.every(term => searchText.includes(term));
        }
        
        // Filtre par région
        if (visible && regio) {
            const vlaamseProvincies = ['antwerpen', 'limburg', 'oost-vlaanderen', 'west-vlaanderen', 'vlaams-brabant'];
            const waalseProvincies = ['luik', 'namen', 'henegouwen', 'luxemburg', 'waals-brabant'];
            
            if (regio === 'vlaanderen') {
                visible = vlaamseProvincies.some(p => location.includes(p));
            } else if (regio === 'wallonie') {
                visible = waalseProvincies.some(p => location.includes(p));
            } else if (regio === 'brussel') {
                visible = location.includes('brussel');
            }
        }
        
        item.style.display = visible ? '' : 'none';
        if (visible) visibleCount++;
    });
    
    // Masquer les sections de lettres vides
    letterSections.forEach(section => {
        const visibleItems = section.querySelectorAll('.castle-list-item[style=""], .castle-list-item:not([style])');
        const hasVisible = Array.from(section.querySelectorAll('.castle-list-item')).some(
            item => item.style.display !== 'none'
        );
        section.style.display = hasVisible ? '' : 'none';
    });
    
    // Afficher un message avec les résultats
    const introSection = document.querySelector('.annuaire-intro');
    if (introSection && (query || regio || type)) {
        const resultMsg = document.createElement('div');
        resultMsg.style.cssText = 'background: var(--bg-secondary); padding: 1.25rem; border-radius: 12px; margin-top: 1.5rem; text-align: center; border: 1px solid var(--border);';
        
        let filterText = '';
        if (query) filterText += `"<strong>${query}</strong>"`;
        if (regio) {
            const regioNames = {vlaanderen: 'Vlaanderen', wallonie: 'Wallonië', brussel: 'Brussel'};
            filterText += (filterText ? ' in ' : '') + `<strong>${regioNames[regio] || regio}</strong>`;
        }
        if (type) {
            const typeNames = {bezoek: 'Bezoek/museum', overnachten: 'Overnachting', evenement: 'Evenement', wandeling: 'Wandeling'};
            filterText += (filterText ? ', ' : '') + `type: <strong>${typeNames[type] || type}</strong>`;
        }
        
        resultMsg.innerHTML = `
            <p style="margin: 0 0 0.75rem; font-size: 1.1rem;">
                🏰 <strong>${visibleCount}</strong> kastelen gevonden ${filterText ? 'voor ' + filterText : ''}
            </p>
            <a href="alle-kastelen.html" style="color: var(--primary); font-weight: 500;">← Toon alle kastelen</a>
        `;
        introSection.appendChild(resultMsg);
        
        // Mettre à jour le titre de la page
        document.title = `Zoekresultaten: ${visibleCount} kastelen | kastelenbelgie.be`;
    }
}

// Fonction pour initialiser l'autocomplete sur le hero search
function initializeHeroSearch() {
    const heroInput = document.getElementById('q');
    if (!heroInput) return;
    
    // Créer le conteneur de suggestions
    const suggestionsDiv = document.createElement('div');
    suggestionsDiv.id = 'hero-suggestions';
    suggestionsDiv.style.cssText = `
        position: absolute;
        top: 100%;
        left: 0;
        right: 0;
        background: white;
        border: 1px solid #ddd;
        border-radius: 10px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.15);
        z-index: 1000;
        max-height: 250px;
        overflow-y: auto;
        display: none;
        margin-top: 4px;
    `;
    
    // Positionner le parent en relative
    const parentField = heroInput.closest('.search-hero-field');
    if (parentField) {
        parentField.style.position = 'relative';
        parentField.appendChild(suggestionsDiv);
    }
    
    // Event listener pour la saisie
    heroInput.addEventListener('input', function(e) {
        const query = e.target.value;
        if (query.length < 2) {
            suggestionsDiv.style.display = 'none';
            return;
        }
        
        const results = searchCastles(query);
        if (results.length === 0) {
            suggestionsDiv.style.display = 'none';
            return;
        }
        
        suggestionsDiv.innerHTML = results.map(castle => `
            <div class="hero-suggestion-item" style="padding: 0.75rem 1rem; border-bottom: 1px solid #f0f0f0; cursor: pointer;">
                <a href="${castle.url}" style="display: flex; align-items: center; text-decoration: none; color: #333;">
                    <span style="margin-right: 0.5rem;">🏰</span>
                    <span style="font-weight: 500;">${castle.name}</span>
                </a>
            </div>
        `).join('');
        
        suggestionsDiv.style.display = 'block';
        
        // Hover effect
        suggestionsDiv.querySelectorAll('.hero-suggestion-item').forEach(item => {
            item.addEventListener('mouseenter', () => item.style.background = '#f8f8f8');
            item.addEventListener('mouseleave', () => item.style.background = 'white');
        });
    });
    
    // Masquer les suggestions quand on clique ailleurs
    document.addEventListener('click', function(e) {
        if (!e.target.closest('.search-hero-field')) {
            suggestionsDiv.style.display = 'none';
        }
    });
}

// Initialiser quand le DOM est chargé
document.addEventListener('DOMContentLoaded', function() {
    addSearchStyles();
    initializeSearch();
    initializePageFilter();
    initializeHeroSearch();
});
