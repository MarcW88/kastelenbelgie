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
    // Every local section jump must target a real ID on the same page.
    const route = '/' + path.relative(root,path.dirname(p)).split(path.sep).join('/').replace(/^\.$/,'').replace(/\/$/,'');
    const pageRoute = route === '/' ? '/' : route + '/';
    for (const link of html.matchAll(/href="([^"]+)"/g)) {
      const raw = link[1];
      if (!raw || /^(?:https?:|mailto:|tel:|javascript:)/i.test(raw)) continue;
      const base = html.match(/<base\s+href=["']([^"']+)["']/i)?.[1];
      const target = new URL(raw, new URL(base || pageRoute, 'https://kastelenbelgie.be' + pageRoute));
      if (target.hostname !== 'kastelenbelgie.be') continue;
      if (target.pathname.startsWith('/kasteel/') && target.pathname.endsWith('/')) {
        const targetFile = path.join(root,target.pathname.slice(1),'index.html');
        if (!fs.existsSync(targetFile)) failures.push(rel+': castle link leads to missing page '+target.pathname);
      }
      if (target.hash && target.pathname === pageRoute && !html.includes('id="'+decodeURIComponent(target.hash.slice(1))+'"'))
        failures.push(rel+': section link has no destination '+raw);
      if (raw.startsWith('#') && html.includes('<base href="/">'))
        failures.push(rel+': fragment link would navigate to homepage '+raw);
    }
    checked++;
  }
}
scan(root);
if(failures.length){console.error(failures.slice(0,40).join('\n'));console.error(failures.length+' errors');process.exit(1);}
console.log(checked+' HTML routes checked: index,follow + current navigation PASS');
