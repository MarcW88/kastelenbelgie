import fs from 'node:fs';
import path from 'node:path';
const ROOT=process.cwd();
const slugs=['kasteel-van-loppem','kasteel-beauvoorde','kasteel-van-rumbeke','kasteel-wijnendale','kasteel-tillegem','kasteel-tudor','kasteel-beisbroek','kasteel-de-blankaart'];
const specialists=['seo-content-audit','content-refresh','seo-keyword','search-intent','seo-competitor','fact-check','content-brief-authoring','brand-voice','content-and-copy','seo-aeo-geo','internal-linking-audit','humanizer','general-writing','anti-ai-slop','seo-onpage','seo-technical','seo-best-practices','editorial-qa'];
const exists=p=>fs.existsSync(path.join(ROOT,p));
const read=p=>fs.readFileSync(path.join(ROOT,p),'utf8');
const checks=[];
function add(slug,gate,ok,evidence){checks.push({slug,gate,status:ok?'PASS':'BLOCKED',evidence});}
for(const specialist of specialists){
  add('repo','SKILL:'+specialist,exists('.agents/skills/'+specialist+'/SKILL.md'),'.agents/skills/'+specialist+'/SKILL.md');
}
const manifest=JSON.parse(read('content/reviewed-pages.json'));
const province=read('content/kastelen/west-vlaanderen/body.html');
const h2Signatures=[];
for(const slug of slugs){
 const route='/kasteel/'+slug+'/';
 const bodyPath='content/kasteel/'+slug+'/body.html',renderPath='kasteel/'+slug+'/index.html';
 const researchPath='content/research/kasteel/'+slug+'/serp-coverage.md';
 const briefPath='content/briefs/kasteel/'+slug+'.md';
 const reviewPath='content/reviews/kasteel/'+slug+'/post-write-gap-check.md';
 const entry=manifest.find(x=>x.route===route);
 add(slug,'OWNERSHIP',Boolean(entry&&entry.source===bodyPath),route);
 add(slug,'RESEARCH_ARTIFACT',exists(researchPath),researchPath);
 add(slug,'BRIEF_ARTIFACT',exists(briefPath),briefPath);
 add(slug,'POST_WRITE_ARTIFACT',exists(reviewPath),reviewPath);
 if(!exists(bodyPath)||!exists(renderPath)){add(slug,'RENDER',false,'missing editorial source or HTML');continue;}
 const body=read(bodyPath),render=read(renderPath);
 const headings=[...body.matchAll(/<h2[^>]*>(.*?)<\/h2>/gs)].map(x=>x[1].replace(/<[^>]+>/g,'').trim().toLowerCase());
 h2Signatures.push({slug,signature:headings.join('|')});
 add(slug,'BUILD_SOURCE_MATCH',render.includes(body),renderPath);
 add(slug,'INTERNAL_LINK',province.includes('href="'+route+'"'),route);
 add(slug,'CANONICAL',render.includes('href="https://kastelenbelgie.be'+route+'"'),renderPath);
 add(slug,'INDEXATION_GUARD',render.includes('noindex,follow'),renderPath);
 add(slug,'SEO_METADATA',Boolean(entry&&render.includes('content="'+entry.description.replace(/&/g,'&amp;')+'"')&&!render.includes('Ontdek Kasteel van Laarne in Oost-Vlaanderen')),renderPath);
 add(slug,'PRIMARY_OFFICIAL_SOURCE',/href="https:\/\//.test(body),bodyPath);
 add(slug,'ONE_H1',(body.match(/<h1\b/g)||[]).length===1,bodyPath);
 add(slug,'ACTUAL_CLAIM_AUDIT',exists(reviewPath)&&/fact.check|factual|feit/i.test(read(reviewPath)),reviewPath);
 if(exists(researchPath)){
  const text=read(researchPath);
  add(slug,'RESEARCH_GAP_DISCLOSURE',/DATA_GAP|BLOCKED|PARTIAL/i.test(text),researchPath);
 }
 if(exists(reviewPath)){
  const t=read(reviewPath);
  add(slug,'PUBLISH_REVIEW_DOCUMENTED',/KEEP_NOINDEX|READY_FOR_HUMAN_VALIDATION/i.test(t),reviewPath);
 }
}
for(let i=0;i<h2Signatures.length;i++)for(let j=i+1;j<h2Signatures.length;j++){
 if(h2Signatures[i].signature===h2Signatures[j].signature) add(h2Signatures[i].slug,'CLONED_HEADINGS',false,'Matches '+h2Signatures[j].slug);
}
const failures=checks.filter(x=>x.status==='BLOCKED');
const result={generatedAt:new Date().toISOString(),scope:'West-Vlaanderen',results:checks,summary:{passed:checks.length-failures.length,blocked:failures.length}};
fs.mkdirSync('.artifacts/qa',{recursive:true});
fs.writeFileSync('.artifacts/qa/west-flanders-machine-gates.json',JSON.stringify(result,null,2)+'\n');
for(const x of checks) console.log(x.status,x.slug,x.gate,x.evidence);
console.log('Machine checks: '+result.summary.passed+' PASS, '+failures.length+' BLOCKED.');
console.log('NOTICE: Machine checks are NOT humanizer, historical fact-check, competitor audit, visual review or final editorial approval. NEVER auto-mark PUBLISH_REVIEW PASS or remove noindex.');
if(failures.length)process.exitCode=1;
