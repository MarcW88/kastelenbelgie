import fs from 'node:fs';
import path from 'node:path';
const root = path.resolve(import.meta.dirname, '..');
const excluded = new Set(['.git','.github','.agents','.content','.artifacts','node_modules','content','docs']);
let checked = 0;
const failures = [];
function scan(dir) {
  for (const entry of fs.readdirSync(dir, {withFileTypes:true})) {
    if (entry.isDirectory()) { if (!excluded.has(entry.name)) scan(path.join(dir,entry.name)); continue; }
    if (entry.name !== 'index.html') continue;
    const p=path.join(dir,entry.name), html=fs.readFileSync(p,'utf8');
    const rel=path.relative(root,p);
    const robots=[...html.matchAll(/<meta\s+name="robots"\s+content="([^"]+)"/gi)];
    if (robots.length!==1 || robots[0][1]!== 'index,follow') failures.push(rel+': robots is not exactly index,follow');
    if (!html.includes('id="primary-navigation"') || !html.includes('href="/#castle-map">Kaart') || html.includes('>Provincies</a>')) failures.push(rel+': old/incorrect navigation');
    checked++;
  }
}
scan(root);
if(failures.length){console.error(failures.slice(0,40).join('\n'));console.error(failures.length+' errors');process.exit(1);}
console.log(checked+' HTML routes checked: index,follow + current navigation PASS');
