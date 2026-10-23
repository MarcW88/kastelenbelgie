import fs from 'node:fs';
import assert from 'node:assert/strict';
const slugs=['kasteel-marnix-de-sainte-aldegonde','kasteel-dursel','kasteel-de-renesse','paleis-op-de-meir','kasteel-rivierenhof','sterckshof'];
const ids=['bornem','ursel','renesse','meir','rivierenhof','sterckshof'];
const entries=JSON.parse(fs.readFileSync('content/reviewed-pages.json','utf8'));
const province=fs.readFileSync('content/kastelen/antwerpen/body.html','utf8');
let fails=0;
for(let i=0;i<slugs.length;i++){const slug=slugs[i],route='/kasteel/'+slug+'/',src='content/kasteel/'+slug+'/body.html',dst='kasteel/'+slug+'/index.html';
try{
const e=entries.find(x=>x.route===route); assert.ok(e && e.source===src,'reviewed manifest route');
const body=fs.readFileSync(src,'utf8'),html=fs.readFileSync(dst,'utf8');
assert.ok(html.includes(body),'canonical source copied into render');
assert.ok(province.includes('href="'+route+'"'),'province detail link');
assert.ok(province.includes('id="'+ids[i]+'"'),'province card');
assert.equal((body.match(/<h1\b/g)||[]).length,1,'one h1');
assert.ok((body.match(/<h2\b/g)||[]).length>=4,'h2 count');
assert.ok(/href="https:\/\//.test(body),'official source link');
assert.ok(html.includes('noindex,follow'),'indexation guard');
assert.ok(html.includes('rel="canonical"'),'canonical');
assert.ok(html.includes('castle-detail.css'),'stylesheet');
for(const p of ['content/research/kasteel/'+slug+'/serp-coverage.md','content/briefs/kasteel/'+slug+'.md','content/reviews/kasteel/'+slug+'/post-write-gap-check.md'])assert.ok(fs.existsSync(p),'missing artifact '+p);
console.log('TECH PASS',slug,body.replace(/<[^>]*>/g,' ').trim().split(/\s+/).length,'words');
}catch(e){console.error('TECH FAIL',slug,e.message);fails++;}
}
console.log('Technical gates do not substitute research, fact verification, humanizer, anti-ai-slop or editorial PUBLISH_REVIEW.');
if(fails)process.exitCode=1;
