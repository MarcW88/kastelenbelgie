import fs from'node:fs';import path from'node:path';const root=path.resolve(import.meta.dirname,'..');let n=0,e=[];function w(d){for(const x of fs.readdirSync(d,{withFileTypes:true})){if(['.git','.agents','.artifacts','node_modules','content'].includes(x.name))continue;const p=path.join(d,x.name);if(x.isDirectory())w(p);else if(x.name.endsWith('.html')){n++;const s=fs.readFileSync(p,'utf8');if(!s.includes('assets/styles.css'))e.push(`${p}: CSS ontbreekt`);if(!s.includes('noindex,follow'))e.push(`${p}: robots ontbreekt`)}}}w(root);
const homepage=fs.readFileSync(path.join(root,'index.html'),'utf8');
const leafletCss=path.join(root,'assets','leaflet.css');
if(!homepage.includes('href="/assets/leaflet.css"'))e.push('Homepage: local Leaflet CSS link missing');
if(!fs.existsSync(leafletCss))e.push('Homepage: Leaflet stylesheet not found');
else if(!fs.readFileSync(leafletCss,'utf8').includes('.leaflet-tile'))e.push('Homepage: Leaflet tile layout CSS incomplete');
if(homepage.includes('sha256-p4NxAoJBhIIN+hmNHrzxD1SMzUe5y6H/qR6yr4A44='))e.push('Homepage: invalid Leaflet CSS integrity digest is still present');
if(e.length){console.error(e.join('\n'));process.exit(1)}console.log(`${n} pagina's gecontroleerd.`);
