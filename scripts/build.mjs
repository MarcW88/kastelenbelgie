import { applyReviewedPages } from './apply-reviewed-pages.mjs';
import fs from'node:fs';import path from'node:path';import {createHash} from 'node:crypto';const root=path.resolve(import.meta.dirname,'..');
const pages={kastelen:['vlaanderen','wallonie','brussel','west-vlaanderen','oost-vlaanderen','antwerpen','vlaams-brabant','limburg','waals-brabant','henegouwen','namen','luik','luxemburg'],bezoeken:['bezoekbare-kastelen','kastelen-met-kinderen','gratis-kastelen','kastelen-met-tuin','kastelen-met-park','kastelen-met-rondleiding','kastelen-overnachten'],soorten:['middeleeuwse-kastelen','burchten','waterkastelen','kasteelruines','kasteeldomeinen','paleizen'],inspiratie:['mooiste-kastelen-belgie','mooiste-kastelen-vlaanderen','mooiste-kastelen-wallonie','kastelen-ardennen','kastelen-weekend'],routes:['kastelenroute-ardennen','kastelenroute-oost-vlaanderen','kastelenroute-rond-gent'],gidsen:['geschiedenis-kastelen-belgie','kasteel-burcht-paleis-verschil','middeleeuws-kasteel','architectuur-kastelen','kastelen-in-belgie-kaart'],kasteel:['gravensteen','kasteel-van-veves','kasteel-van-freyr','kasteel-van-lavaux-sainte-anne','burcht-reinhardstein','kasteel-van-beloeil','kasteel-van-seneffe','kasteel-van-chimay','kasteel-van-modave','kasteel-van-jehay','kasteel-van-bouillon','feodaal-kasteel-la-roche-en-ardenne','coudenbergpaleis','koninklijk-paleis-van-brussel','karreveldkasteel','kasteel-malou','kasteel-de-rivieren','kasteel-van-laken-en-koninklijke-serres','kasteel-van-laarne','kasteel-ooidonk','kasteel-van-poeke','kasteel-wissekerke','kasteel-cortewalle','domein-breivelde','park-van-beervelde','kasteel-van-loppem','kasteel-beauvoorde','kasteel-van-rumbeke','kasteel-wijnendale','kasteel-tillegem','kasteel-tudor','kasteel-beisbroek','kasteel-de-blankaart','kasteel-van-gaasbeek','kasteel-van-beersel','kasteel-groenenberg','kasteel-coloma','kasteel-van-bouchout','arenbergkasteel','kasteel-van-horst','kasteel-ter-rijst','kasteel-van-groot-bijgaarden','kasteel-marnix-de-sainte-aldegonde','kasteel-dursel','kasteel-de-renesse','paleis-op-de-meir','kasteel-rivierenhof','sterckshof','landcommanderij-alden-biesen','kasteel-van-heers','kasteel-van-hex','kasteel-van-ordingen','kasteelbrouwerij-ter-dolen','domein-bokrijk','kasteel-van-rixensart','kasteel-van-terhulpen','kasteel-van-bois-seigneur-isaac','kasteel-van-corroy-le-chateau','kasteel-van-montaigle','kasteel-van-spontin','kasteel-van-fallais','kasteel-van-mirwart','kasteel-van-attre','kasteel-van-havre','kasteel-van-fagnolle','kasteel-daspremont-lynden','kasteel-van-leut','wijnkasteel-genoels-elderen','kasteel-van-walzin','kasteel-van-annevoie','kasteel-van-sombreffe','kasteel-van-boussu','kasteel-van-waroux']};
const labels={kastelen:'Kastelen per regio',bezoeken:'Bezoeken',soorten:'Thema’s',inspiratie:'Inspiratie',routes:'Routes',gidsen:'Verhalen & gidsen',kasteel:'Kasteelfiches'};
const special={wallonie:'Wallonië',brussel:'Brussel','oost-vlaanderen':'Oost-Vlaanderen','west-vlaanderen':'West-Vlaanderen','vlaams-brabant':'Vlaams-Brabant','waals-brabant':'Waals-Brabant',luik:'Luik',luxemburg:'Luxemburg','kasteel-van-veves':'Kasteel van Vêves','burcht-reinhardstein':'Burcht Reinhardstein','kasteel-van-beloeil':'Kasteel van Beloeil','kasteel-van-modave':'Kasteel van Modave',gravensteen:'Gravensteen'};
const title=s=>special[s]||s.split('-').map((x,i)=>i?x:x[0].toUpperCase()+x.slice(1)).join(' ').replace('belgie','België').replace('kasteelruines','kasteelruïnes');
const header=(light=false)=>`<header class="header ${light?'light':''}"><div class="container header-row"><a class="brand" href="/"><img src="assets/logo.svg" alt=""><span>Kastelen België</span></a><nav class="nav" data-nav id="primary-navigation" aria-label="Hoofdnavigatie"><a href="kastelen/">Ontdekken</a><a href="/#castle-map">Kaart</a><a href="soorten/">Thema’s</a><a href="routes/">Routes</a><a href="gidsen/">Verhalen</a></nav><div class="header-actions"><button class="nav-btn" data-surprise>Verras me</button><button class="nav-btn menu" data-menu aria-controls="primary-navigation" aria-label="Menu" aria-expanded="false">☰</button></div></div></header>`;
const footer=`<footer class="footer" aria-label="Voettekst"><div class="container">
<div class="footer-intro"><div class="footer-identity"><a class="brand footer-brand" href="/"><img src="/assets/logo.svg" alt="" width="42" height="42"><span>Kastelen België</span></a><p>Een onafhankelijke gids om het Belgische kastelenerfgoed te begrijpen, te ontdekken en een bezoek voor te bereiden.</p></div><div class="footer-feature"><span class="eyebrow">Begin bij het verhaal</span><p>Wat maakt een burcht anders dan een paleis?</p><a href="/gidsen/kasteel-burcht-paleis-verschil/">Lees het verschil <span aria-hidden="true">→</span></a></div></div>
<div class="footer-grid">
<div class="footer-group"><h2>Een bezoek voorbereiden</h2><p>Van toegankelijkheid tot een wandeling rond het domein.</p><a href="/bezoeken/bezoekbare-kastelen/">Kastelen die je kunt bezoeken</a><a href="/bezoeken/kastelen-met-kinderen/">Op stap met kinderen</a><a href="/bezoeken/kastelen-met-tuin/">Kastelen met park en tuin</a><a href="/bezoeken/kastelen-overnachten/">Overnachten bij een kasteel</a></div>
<div class="footer-group"><h2>Meer begrijpen</h2><p>Verdiep je in bouwstijlen, geschiedenis en erfgoed.</p><a href="/gidsen/geschiedenis-kastelen-belgie/">Geschiedenis van kastelen</a><a href="/gidsen/architectuur-kastelen/">Kasteelarchitectuur herkennen</a><a href="/gidsen/middeleeuws-kasteel/">Het middeleeuwse kasteel</a><a href="/soorten/kasteelruines/">Wat vertellen kasteelruïnes?</a></div>
<div class="footer-group"><h2>Bijzondere ontdekkingen</h2><p>Een paar mooie invalshoeken voor je volgende uitstap.</p><a href="/soorten/waterkastelen/">Waterkastelen en slotgrachten</a><a href="/soorten/kasteeldomeinen/">Historische kasteeldomeinen</a><a href="/soorten/paleizen/">Paleizen en residenties</a><a href="/inspiratie/mooiste-kastelen-belgie/">De mooiste kastelen van België</a></div>
</div>
<div class="footer-bottom"><span>© 2026 Kastelen België · Onafhankelijke erfgoedgids</span><span>Bezoekuren en toegang kunnen veranderen. Controleer altijd de officiële bron.</span></div></div></footer>`;
const shell=(t,b,home=false)=>`<!doctype html><html lang="nl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><base href="/"><meta name="robots" content="index,follow"><title>${t} | Kastelen België</title><meta name="description" content="Ontdek kastelen in België per provincie, type en ervaring."><link rel="icon" href="assets/logo.svg"><link rel="stylesheet" href="assets/styles.css"></head><body>${header(!home)}<main>${b}</main>${footer}<script src="assets/app.js"></script></body></html>`;
const castleRows=[['Gravensteen','Gent · Oost-Vlaanderen','visit kids'],['Kasteel van Vêves','Celles · Namen','visit kids'],['Burcht Reinhardstein','Ovifat · Luik','visit medieval'],['Kasteel van Beloeil','Beloeil · Henegouwen','garden'],['Kasteel van Modave','Modave · Luik','visit garden']];
const home=`<section class="hero"><figure class="editorial-media" data-generated-image="homepage-heritage-hero" style="width:100%;max-width:none;margin:28px 0 32px;">
  <img src="/assets/generated/homepage-heritage-hero.webp" alt="Sfeervolle redactionele illustratie van een denkbeeldige stenen burcht in een groen landschap" width="1536" height="1024" loading="lazy" decoding="async" style="width:100%;height:auto;aspect-ratio:1536/1024;object-fit:cover;border-radius:var(--radius-md);display:block;">
</figure>\n<div class="container hero-content"><span class="eyebrow">Een atlas van Belgisch erfgoed</span><h1>Ontdek de kastelen van <em>België.</em></h1><p>Van middeleeuwse burchten tot kasteeldomeinen, verborgen ruïnes en historische tuinen.</p><form class="searchbox" action="/zoeken/" method="get"><input type="search" name="q" aria-label="Zoek een kasteel of plaats" placeholder="Zoek een kasteel, plaats of provincie…"><select name="type" aria-label="Wat zoek je?"><option value="">Alle onderwerpen</option><option value="kasteel">Kastelen</option><option value="kastelen">Provincies en regio’s</option><option value="soorten">Thema’s</option><option value="bezoeken">Bezoeken</option><option value="gidsen">Verhalen en gidsen</option></select><button type="submit">Vind kastelen</button></form><div class="hero-links"><a href="/#castle-map">Bekijk de kaart →</a><a href="kastelen/">Ontdek per provincie →</a></div></div><span class="coord">50.5039° N · 4.4699° E</span></section>
<section class="section"><div class="container"><div class="section-head"><div><span class="eyebrow">Verkennen</span><h2>Kastelen op de kaart</h2></div><p>Een eerste visuele verkenning. Openingstijden en toegankelijkheid worden pas getoond wanneer ze actueel geverifieerd zijn.</p></div><div class="map-shell"><div class="results"><div class="result-count">5 kastelen op de interactieve kaart</div><div class="filters"><button class="filter active" data-filter="all">Alle</button><button class="filter" data-filter="visit">Bezoekbaar</button><button class="filter" data-filter="kids">Met kinderen</button><button class="filter" data-filter="medieval">Middeleeuws</button><button class="filter" data-filter="garden">Park & tuin</button></div>${castleRows.map(([n,l,f])=>`<a class="castle-row" data-castle="${f}" href="kasteel/${Object.keys(special).find(k=>special[k]===n)||n.toLowerCase().replaceAll(' ','-')}/"><div><strong>${n}</strong><span>${l}</span></div><b>↗</b></a>`).join('')}</div><div class="map live-map" id="castle-map" role="region" aria-label="Interactieve kaart van kastelen in België"><div class="map-interactive" id="belgium-castle-map" aria-label="Kaart met aanklikbare kastelen"></div><div class="map-help">Klik op een markering om een kasteelfiche te openen · <a href="kastelen/">Alle provincies →</a></div></div></div></div></section>
<section class="section"><div class="container"><div class="section-head"><div><span class="eyebrow">Elf bestemmingen</span><h2>Ontdek per provincie</h2></div><a class="text-link" href="kastelen/">Alle regio’s →</a></div><div class="province-grid">${['west-vlaanderen','oost-vlaanderen','antwerpen','vlaams-brabant','limburg','waals-brabant','henegouwen','namen','luik','luxemburg','brussel'].map((x,i)=>`<a class="province" href="kastelen/${x}/"><span class="num">${String(i+1).padStart(2,'0')}</span><h3>${title(x)}</h3><span>Kastelen en domeinen ontdekken →</span></a>`).join('')}</div></div></section>
<section class="section"><div class="container feature"><div class="feature-art" aria-label="Illustratieve erfgoedfoto"><figure class="editorial-media" data-generated-image="home-feature-heritage" style="width:100%;max-width:none;margin:28px 0 32px;">
  <img src="/assets/generated/home-feature-heritage.webp" alt="Redactionele sfeerillustratie van Belgisch kastelenerfgoed, geen foto van een bestaande locatie" width="1024" height="768" loading="lazy" decoding="async" style="width:100%;height:auto;aspect-ratio:1024/768;object-fit:cover;border-radius:var(--radius-md);display:block;">
</figure></div><div class="feature-copy"><span class="eyebrow">Bijzondere plek</span><h2>Kasteel van Vêves</h2><p>Een fiche-opzet waarin architectuur, geschiedenis en praktische bezoekinformatie elk hun eigen ritme krijgen.</p><a class="text-link" href="kasteel/kasteel-van-veves/">Ontdek de plek →</a></div></div></section>
<section class="section"><div class="container"><div class="section-head"><div><span class="eyebrow">Selecties</span><h2>Kies je manier van ontdekken</h2></div><p>Niet één eindeloze lijst, maar verschillende redactionele blikken op hetzelfde erfgoed.</p></div><div class="theme-grid"><a class="theme" href="soorten/middeleeuwse-kastelen/"><figure class="editorial-media" data-generated-image="home-theme-medieval" style="width:100%;max-width:none;margin:28px 0 32px;">
  <img src="/assets/generated/home-theme-medieval.webp" alt="Redactionele sfeerillustratie van Belgisch kastelenerfgoed, geen foto van een bestaande locatie" width="1024" height="768" loading="lazy" decoding="async" style="width:100%;height:auto;aspect-ratio:1024/768;object-fit:cover;border-radius:var(--radius-md);display:block;">
</figure><span>Door de eeuwen</span><h3>Middeleeuws België</h3></a><a class="theme" href="bezoeken/kastelen-met-kinderen/"><figure class="editorial-media" data-generated-image="home-theme-family" style="width:100%;max-width:none;margin:28px 0 32px;">
  <img src="/assets/generated/home-theme-family.webp" alt="Redactionele sfeerillustratie van Belgisch kastelenerfgoed, geen foto van een bestaande locatie" width="1024" height="768" loading="lazy" decoding="async" style="width:100%;height:auto;aspect-ratio:1024/768;object-fit:cover;border-radius:var(--radius-md);display:block;">
</figure><span>Een dag samen</span><h3>Met kinderen</h3></a><a class="theme" href="bezoeken/kastelen-met-tuin/"><figure class="editorial-media" data-generated-image="home-theme-garden" style="width:100%;max-width:none;margin:28px 0 32px;">
  <img src="/assets/generated/home-theme-garden.webp" alt="Redactionele sfeerillustratie van Belgisch kastelenerfgoed, geen foto van een bestaande locatie" width="1024" height="768" loading="lazy" decoding="async" style="width:100%;height:auto;aspect-ratio:1024/768;object-fit:cover;border-radius:var(--radius-md);display:block;">
</figure><span>Buiten</span><h3>Park & tuin</h3></a><a class="theme" href="inspiratie/mooiste-kastelen-belgie/"><figure class="editorial-media" data-generated-image="home-theme-highlights" style="width:100%;max-width:none;margin:28px 0 32px;">
  <img src="/assets/generated/home-theme-highlights.webp" alt="Redactionele sfeerillustratie van Belgisch kastelenerfgoed, geen foto van een bestaande locatie" width="1024" height="768" loading="lazy" decoding="async" style="width:100%;height:auto;aspect-ratio:1024/768;object-fit:cover;border-radius:var(--radius-md);display:block;">
</figure><span>Redactionele selectie</span><h3>Bijzondere plekken</h3></a></div></div></section>
<section class="section"><div class="container route"><div class="route-copy"><span class="eyebrow">Routes & uitstappen</span><h2>Een dag langs kastelen</h2><p class="muted">De routegidsen combineren straks drie tot zes locaties met afstand, volgorde en relevante haltes.</p><div class="route-meta"><span>4 locaties</span><span>1 dag</span><span>Data te verifiëren</span></div><a class="text-link" href="routes/kastelenroute-ardennen/">Bekijk de route →</a></div><div class="route-map"><figure class="editorial-media" data-generated-image="home-route-atmosphere" style="width:100%;max-width:none;margin:28px 0 32px;">
  <img src="/assets/generated/home-route-atmosphere.webp" alt="Redactionele sfeerillustratie van Belgisch kastelenerfgoed, geen foto van een bestaande locatie" width="1024" height="768" loading="lazy" decoding="async" style="width:100%;height:auto;aspect-ratio:1024/768;object-fit:cover;border-radius:var(--radius-md);display:block;">
</figure><svg viewBox="0 0 600 430" aria-hidden="true"><path d="M70 340C150 320 130 210 245 220S360 95 520 85" fill="none" stroke="#33483D" stroke-width="3" stroke-dasharray="7 9"/><g fill="#8C493E">${[[70,340],[245,220],[365,135],[520,85]].map(([x,y])=>`<circle cx="${x}" cy="${y}" r="9"/>`).join('')}</g></svg></div></div></section><section class="section"><div class="container trust"><div><strong>Entiteiten, geen losse lijstjes</strong><p>Elke plek wordt verbonden met regio, type, periode en ervaring.</p></div><div><strong>Praktische data met bron</strong><p>Actuele claims krijgen een bron en controledatum.</p></div><div><strong>Verkennen én plannen</strong><p>Kaart, verhaal en bezoekinformatie vullen elkaar aan.</p></div></div></section>`;
const homeHtml = shell('Ontdek kastelen in België',home,true)
  .replace('</head>', '<link rel="stylesheet" href="/assets/leaflet.css"></head>')
  .replace('<script src="assets/app.js"></script>', '<script defer src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin=""></script><script defer src="assets/app.js"></script>');
fs.writeFileSync(path.join(root,'index.html'), homeHtml);
for(const[cat,slugs]of Object.entries(pages)){const d=path.join(root,cat);fs.mkdirSync(d,{recursive:true});fs.writeFileSync(path.join(d,'index.html'),shell(labels[cat],cat==='kastelen'?fs.readFileSync(path.join(root,'content/kastelen/overview.html'),'utf8'):cat==='routes'?fs.readFileSync(path.join(root,'content/routes/overview.html'),'utf8'):cat==='gidsen'||cat==='soorten'?fs.readFileSync(path.join(root,'content',cat,'overview.html'),'utf8'):`<section class="page-header"><div class="container"><div class="crumbs"><a href="/">Home</a> · ${labels[cat]}</div><span class="eyebrow">Atlas</span><h1>${labels[cat]}</h1><p>Deze atlasweergave staat klaar voor geverifieerde locaties, kaartgegevens en redactionele context.</p></div></section><section class="section"><div class="container directory">${slugs.map(s=>`<a href="${cat}/${s}/">${title(s)} →</a>`).join('')}</div></section>`));for(const s of slugs){const p=path.join(d,s);fs.mkdirSync(p,{recursive:true});const t=title(s);fs.writeFileSync(path.join(p,'index.html'),shell(t,`<section class="page-header"><div class="container"><div class="crumbs"><a href="/">Home</a> · <a href="${cat}/">${labels[cat]}</a> · ${t}</div><span class="eyebrow">${labels[cat]}</span><h1>${t}</h1><p>Gabarit klaar voor een eigen redactionele compositie en geverifieerde erfgoeddata.</p></div></section><div class="container template"><article><section class="placeholder"><span class="eyebrow">Ontdekken</span><h2>Waarom deze plek of selectie bijzonder is</h2><p class="muted">Inhoud nog te schrijven.</p></section><section class="placeholder"><span class="eyebrow">Erfgoed</span><h2>Geschiedenis en architectuur</h2><p class="muted">Bronnen en tijdlijn nog te documenteren.</p></section><section class="placeholder"><span class="eyebrow">Plannen</span><h2>Praktische informatie</h2><p class="muted">Geen openingstijden of prijzen vóór actuele verificatie.</p></section></article><aside><div class="side"><h3>In één oogopslag</h3><div class="fact"><span>Locatie</span>Nog te verifiëren</div><div class="fact"><span>Type</span>Nog te classificeren</div><div class="fact"><span>Bezoekbaar</span>Onbekend</div><div class="fact"><span>Laatste controle</span>Nog niet gecontroleerd</div></div></aside></div>`));}}
for(const[slug,t]of[['over-ons','Over deze atlas'],['bronnen','Bronnen & methode'],['contact','Contact']]){const p=path.join(root,slug);fs.mkdirSync(p,{recursive:true});fs.writeFileSync(path.join(p,'index.html'),shell(t,`<section class="page-header"><div class="container"><div class="crumbs"><a href="/">Home</a> · ${t}</div><span class="eyebrow">Over het project</span><h1>${t}</h1><p>Deze pagina wacht op bevestigde projectinformatie.</p></div></section>`));}
console.log(`${1+Object.keys(pages).length+Object.values(pages).flat().length+3} pagina's gegenereerd.`);

// Durable editorial landing for high-intent castle visits; never overwrite it with placeholders.
const visitablePath=path.join(root,'bezoeken','bezoekbare-kastelen','index.html');
const visitableSource=fs.readFileSync(path.join(root,'content','bezoeken','bezoekbare-kastelen.html'),'utf8');
fs.writeFileSync(visitablePath,shell('Bezoekbare kastelen in België',visitableSource));

// Permanent editorial source for guided castle tours; never use the atlas placeholder.
const guidedToursPath=path.join(root,'bezoeken','kastelen-met-rondleiding','index.html');
fs.writeFileSync(guidedToursPath,shell('Kastelen met rondleiding in België',fs.readFileSync(path.join(root,'content','bezoeken','kastelen-met-rondleiding.html'),'utf8')));

const routesIndex=path.join(root,'routes/index.html');
let routesHtml=fs.readFileSync(routesIndex,'utf8');
routesHtml=routesHtml.replace('<title>Routes | Kastelen België</title>','<title>Kastelenroutes in België: Ardennen, Oost-Vlaanderen en Gent | Kastelen België</title>').replace('<meta name="description" content="Ontdek kastelen in België per provincie, type en ervaring.">','<meta name="description" content="Ontdek kastelenroutes in de Ardennen, Oost-Vlaanderen en rond Gent. Vergelijk stops, kies je regio en plan je eigen kasteeluitstap.">');
routesHtml=routesHtml.replace('</head>','<script type="application/ld+json">'+JSON.stringify({"@context":"https://schema.org","@graph":[{"@type":"CollectionPage","@id":"https://kastelenbelgie.be/routes/#webpage",url:"https://kastelenbelgie.be/routes/",name:"Kastelenroutes in België",inLanguage:"nl-BE"},{"@type":"BreadcrumbList",itemListElement:[{"@type":"ListItem",position:1,name:"Home",item:"https://kastelenbelgie.be/"},{"@type":"ListItem",position:2,name:"Routes",item:"https://kastelenbelgie.be/routes/"}]},{"@type":"ItemList",itemListElement:['kastelenroute-ardennen','kastelenroute-oost-vlaanderen','kastelenroute-rond-gent'].map((slug,i)=>({"@type":"ListItem",position:i+1,url:"https://kastelenbelgie.be/routes/"+slug+"/"}))}]})+'</script></head>');
fs.writeFileSync(routesIndex,routesHtml);

const reviewed = applyReviewedPages(root, shell);
console.log(`${reviewed} gecontroleerde inhoudspagina('s) toegepast.`);


// Search is built from actual site routes and reviewed source titles at build time.
const searchRecords = [];
const reviewedEntries = JSON.parse(fs.readFileSync(path.join(root,'content/reviewed-pages.json'),'utf8'));
const reviewedByRoute = new Map(reviewedEntries.map(item=>[item.route,item]));
const addSearchRecord = (route, heading, section) => {
  const reviewed = reviewedByRoute.get(route);
  const name = reviewed ? (reviewed.title.split(' | ')[0]) : heading;
  searchRecords.push({url:route,title:name,type:section,description:reviewed?.description || '',keywords:route.replaceAll('/',' ').replaceAll('-',' ')});
};
for(const [section, slugs] of Object.entries(pages)) {
  addSearchRecord('/'+section+'/',labels[section],section);
  for(const slug of slugs) addSearchRecord('/'+section+'/'+slug+'/',title(slug),section);
}
for(const entry of reviewedEntries) {
  if (!searchRecords.some(x=>x.url===entry.route)) addSearchRecord(entry.route,entry.title,'gidsen');
}
searchRecords.sort((a,b)=>a.title.localeCompare(b.title,'nl'));
fs.writeFileSync(path.join(root,'assets/search-index.json'),JSON.stringify(searchRecords));
const searchPage = '<section class="page-header"><div class="container"><div class="crumbs"><a href="/">Home</a> · Zoeken</div><span class="eyebrow">Zoek in de kastelenatlas</span><h1>Kastelen zoeken</h1><p>Zoek op naam, provincie, regio of onderwerp. Verfijn de resultaten met een categorie.</p><form class="searchbox search-page-form" action="/zoeken/" method="get"><input type="search" name="q" aria-label="Zoekterm" placeholder="Bijvoorbeeld Gravensteen, Luik of waterkastelen…" required><select name="type" aria-label="Categorie"><option value="">Alle onderwerpen</option><option value="kasteel">Kastelen</option><option value="kastelen">Provincies en regio’s</option><option value="soorten">Thema’s</option><option value="bezoeken">Bezoeken</option><option value="gidsen">Gidsen</option></select><button type="submit">Zoeken</button></form></div></section><section class="section"><div class="container"><p id="search-status" role="status" aria-live="polite">Voer een zoekopdracht in om resultaten te zien.</p><div class="search-results" id="search-results"></div></div></section><script defer src="/assets/search.js"></script>';
fs.mkdirSync(path.join(root,'zoeken'),{recursive:true});
fs.writeFileSync(path.join(root,'zoeken/index.html'),shell('Zoeken',searchPage));

/* Fingerprinted URLs prevent stale CSS, scripts and editorial images after new deployments.
   GitHub Pages has a browser/CDN cache TTL; unchanged asset URLs otherwise serve old files. */
const assetFingerprint = new Map();
const getAssetFingerprint = pathname => {
  if(!assetFingerprint.has(pathname)){
    const file=path.join(root,pathname.slice(1));
    if(!fs.existsSync(file)) return null;
    assetFingerprint.set(pathname,createHash('sha256').update(fs.readFileSync(file)).digest('hex').slice(0,12));
  }
  return assetFingerprint.get(pathname);
};
function fingerprintAssets(dir){
  for(const entry of fs.readdirSync(dir,{withFileTypes:true})){
    if(entry.isDirectory()){
      if(!['.git','.github','.agents','.artifacts','.content','node_modules','content','docs'].includes(entry.name)) fingerprintAssets(path.join(dir,entry.name));
      continue;
    }
    if(entry.name!=='index.html')continue;
    const file=path.join(dir,entry.name);
    let html=fs.readFileSync(file,'utf8');
    html=html.replace(/((?:src|href)=")(\/?assets\/[^"?#]+)(?:\?v=[a-f0-9]+)?(")/g,(full,pre,asset,end)=>{
      const pathname='/'+asset.replace(/^\//,'');
      if(pathname==='/assets/leaflet.css')return full;
      const version=getAssetFingerprint(pathname);
      return version?pre+pathname+'?v='+version+end:full;
    });
    if(dir===root){
      html=html.replace(/(data-generated-image="home-feature-heritage"[\s\S]*?<img [^>]*?)loading="lazy"/,'$1loading="eager" fetchpriority="high"');
      const buildVersion=createHash('sha256').update(html).digest('hex').slice(0,12);
      fs.writeFileSync(path.join(root,'assets/site-version.json'),JSON.stringify({version:buildVersion}));
      html=html.replace('</head>','<meta name="build-version" content="'+buildVersion+'"></head>');

    }
    fs.writeFileSync(file,html);
  }
}
fingerprintAssets(root);

/* Sitewide crawlability: enforce one self-canonical for every generated HTML route. */
const siteHost = fs.readFileSync(path.join(root, 'CNAME'), 'utf8').trim();
const generatedRoutes = [];
const skipDirs = new Set(['.git', '.agents', '.artifacts', 'node_modules', 'content', '.github', 'docs']);
function indexGenerated(directory) {
  for (const entry of fs.readdirSync(directory, { withFileTypes: true })) {
    if (entry.isDirectory()) {
      if (!skipDirs.has(entry.name)) indexGenerated(path.join(directory, entry.name));
      continue;
    }
    if (entry.name !== 'index.html') continue;
    const filename = path.join(directory, entry.name);
    const pathname = path.relative(root, directory).split(path.sep).join('/');
    const route = pathname ? '/' + pathname + '/' : '/';
    const canonical = 'https://' + siteHost + route;
    let html = fs.readFileSync(filename, 'utf8');
    // Absolute base href otherwise redirects local #section links to the homepage.
    // Keep /-relative assets, but qualify local fragment navigation with this route.
    html = html.replace(/href=(["'])#([a-zA-Z0-9][a-zA-Z0-9_-]*)\1/g, (match, quote, id) => 'href=' + quote + route + '#' + id + quote);
    html = html.replace(/<meta name="robots" content="[^"]*">/i, '<meta name="robots" content="index,follow">');
    html = html.replace(/<link rel="canonical" href="[^"]*">/gi, '');
    html = html.replace('</head>', '<link rel="canonical" href="' + canonical + '"></head>');
    fs.writeFileSync(filename, html);
    generatedRoutes.push(canonical);
  }
}
indexGenerated(root);
generatedRoutes.sort();
const xmlEscape = value => value.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
fs.writeFileSync(path.join(root,'sitemap.xml'),'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+generatedRoutes.map(url=>'  <url><loc>'+xmlEscape(url)+'</loc></url>').join('\n')+'\n</urlset>\n');
fs.writeFileSync(path.join(root,'robots.txt'),'User-agent: *\nAllow: /\n\nSitemap: https://'+siteHost+'/sitemap.xml\n');
console.log(generatedRoutes.length + ' indexable URLs, self-canonicals, sitemap and robots.txt generated.');
