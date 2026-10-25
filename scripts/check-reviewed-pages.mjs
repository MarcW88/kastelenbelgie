import fs from 'node:fs';
import path from 'node:path';
const root = path.resolve(import.meta.dirname, '..');
const manifest = path.join(root, 'content/reviewed-pages.json');
if (!fs.existsSync(manifest)) process.exit(0);
const host = fs.readFileSync(path.join(root, 'CNAME'), 'utf8').trim();
let checked = 0;
for (const entry of JSON.parse(fs.readFileSync(manifest, 'utf8'))) {
  const filename = path.join(root, entry.route.slice(1), 'index.html');
  const html = fs.readFileSync(filename, 'utf8');
  const body = fs.readFileSync(path.join(root, entry.source), 'utf8');
  const fail = issue => { throw new Error(`${entry.route}: ${issue}`); };
  if (!html.includes(body)) fail('Reviewed source content was not preserved in the rendered page.');
  if ((html.match(/<h1\b/g) || []).length !== 1) fail('Expected exactly one H1.');
  if (!html.includes('<meta name="robots" content="index,follow">')) fail('Indexation policy changed.');
  if (!html.includes(`<link rel="canonical" href="https://${host}${entry.route}">`)) fail('Canonical mismatch.');
  if (/Inhoud nog te schrijven|Gabarit klaar|Nog te classificeren/.test(body)) fail('Editorial placeholder remains.');
  for (const match of html.matchAll(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/g)) JSON.parse(match[1]);
  for (const match of html.matchAll(/href="([^"]+)"/g)) {
    const url = new URL(match[1], `https://${host}/`);
    if (url.hostname !== host) continue;
    const target = path.join(root, decodeURIComponent(url.pathname).slice(1), url.pathname.endsWith('/') ? 'index.html' : '');
    if (!fs.existsSync(target)) fail(`Internal target missing: ${url.pathname}`);
    if (url.hash && url.pathname === entry.route && !html.includes(`id="${url.hash.slice(1)}"`)) fail(`Anchor missing: ${url.hash}`);
  }
  // Province-card and structured-data contracts: keep the regional index in sync with its fiches.
  if (/^\/kastelen\/(?:west-vlaanderen|oost-vlaanderen|vlaams-brabant|antwerpen|limburg|waals-brabant|henegouwen|namen|luik|luxemburg|brussel)\/$/.test(entry.route)) {
    const cards = [...body.matchAll(/<article class="visit-card" id="([^"]+)"([\s\S]*?)<\/article>/g)];
    if (!cards.length) fail('No castle selection cards found.');
    const ids = new Set();
    for (const [, id, card] of cards) {
      if (ids.has(id)) fail(`Duplicate castle card: ${id}`);
      ids.add(id);
      if (!/<figure class="visit-card-photo">[\s\S]*?<img[^>]+src="[^"]+"[^>]+alt="[^"]+"/.test(card)) fail(`Photo or alt missing: ${id}`);
      if (!/href="\/kasteel\/[^"]+\/"/.test(card) || !card.includes('Bekijk onze kasteelfiche')) fail(`Fiche link missing: ${id}`);
      if (!/class="visit-source" href="https?:\/\//.test(card)) fail(`Official link missing: ${id}`);
      if (/<h3[^>]*>\s*<a\b/.test(card)) fail(`Castle heading linked: ${id}`);
    }
    const graph = entry.schema?.['@graph'];
    const list = graph?.find(item => item['@type'] === 'ItemList');
    if (!list || list.numberOfItems !== cards.length || list.itemListElement?.length !== cards.length) fail('Castle ItemList JSON-LD count mismatch.');
    for (const [index, item] of list.itemListElement.entries()) {
      if (item.position !== index + 1 || !ids.has(item.url?.split('#')[1])) fail('Castle ItemList JSON-LD target mismatch.');
    }
    if (!html.includes(`"numberOfItems":${cards.length}`)) fail('Rendered castle ItemList JSON-LD outdated.');
  }
  checked++;
}
console.log(`${checked} reviewed page(s): source preservation, metadata, robots, JSON-LD and internal links PASS.`);
