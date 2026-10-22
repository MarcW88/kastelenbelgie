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
  if (!html.includes('<meta name="robots" content="noindex,follow">')) fail('Indexation policy changed.');
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
  checked++;
}
console.log(`${checked} reviewed page(s): source preservation, metadata, robots, JSON-LD and internal links PASS.`);
