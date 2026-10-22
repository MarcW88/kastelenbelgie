import fs from 'node:fs';
import assert from 'node:assert/strict';
const slugs=['kasteel-van-loppem','kasteel-beauvoorde','kasteel-van-rumbeke','kasteel-wijnendale','kasteel-tillegem','kasteel-tudor','kasteel-beisbroek','kasteel-de-blankaart'];
const entries=JSON.parse(fs.readFileSync('content/reviewed-pages.json','utf8'));
const province=fs.readFileSync('content/kastelen/west-vlaanderen/body.html','utf8');
const normalize=s=>s.replace(/\s+/g,' ').trim();
let failed=false;
for(const slug of slugs){
  const route='/kasteel/'+slug+'/';
  const e=entries.find(x=>x.route===route);
  const src='content/kasteel/'+slug+'/body.html';
  const out='kasteel/'+slug+'/index.html';
  try{
    assert.ok(e && e.source===src,'route/manifest missing');
    assert.ok(fs.existsSync(src)&&fs.existsSync(out),'missing source/render');
    const body=fs.readFileSync(src,'utf8'),html=fs.readFileSync(out,'utf8');
    assert.ok(html.includes(body),'source not reproduced in generated page');
    assert.ok(province.includes('href="'+route+'"'),'province link missing');
    assert.equal((body.match(/<h1\b/g)||[]).length,1,'H1 count');
    assert.ok((body.match(/<h2\b/g)||[]).length>=3,'insufficient editorial sections');
    assert.ok(/href="https:\/\//.test(body),'no official source');
    assert.ok(html.includes('noindex,follow'),'indexation unexpectedly changed');
    assert.ok(html.includes('rel="canonical"'),'canonical missing');
    assert.ok(html.includes('castle-detail.css'),'detail stylesheet missing');
    for(const path of ['content/research/kasteel/'+slug+'/serp-coverage.md','content/briefs/kasteel/'+slug+'.md','content/reviews/kasteel/'+slug+'/post-write-gap-check.md']) assert.ok(fs.existsSync(path),'missing workflow artifact: '+path);
    console.log('TECH PASS',slug,'words',normalize(body.replace(/<[^>]*>/g,' ')).split(' ').length);
  }catch(e){failed=true; console.error('TECH FAIL',slug,e.message)}
}
if(failed)process.exit(1);
console.log('Structural checks passed; these do NOT certify factuality, SERP coverage, human QA or PUBLISH_REVIEW.');
