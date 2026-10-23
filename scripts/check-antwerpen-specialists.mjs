import fs from 'node:fs';
import path from 'node:path';
const slugs=['kasteel-marnix-de-sainte-aldegonde','kasteel-dursel','kasteel-de-renesse','paleis-op-de-meir','kasteel-rivierenhof','sterckshof'];
const needed=['seo-content-audit','seo-keyword','search-intent','seo-competitor','fact-check','content-brief-authoring','brand-voice','content-and-copy','seo-aeo-geo','internal-linking-audit','humanizer','general-writing','anti-ai-slop','seo-onpage','seo-technical','seo-best-practices','editorial-qa'];
const read=p=>fs.readFileSync(p,'utf8');
const exists=p=>fs.existsSync(p);
const results=[];
for(const slug of slugs){
 const src='content/kasteel/'+slug+'/body.html',research='content/research/kasteel/'+slug+'/serp-coverage.md',brief='content/briefs/kasteel/'+slug+'.md',review='content/reviews/kasteel/'+slug+'/post-write-gap-check.md';
 const page=read(src),r=read(research),b=read(brief),rev=read(review);
 const h2=[...page.matchAll(/<h2[^>]*>(.*?)<\/h2>/gs)].map(m=>m[1].replace(/<[^>]*>/g,'').trim());
 const evidence=[];
 const add=(stage,pass,detail)=>evidence.push({stage,status:pass?'PASS':'BLOCKED',detail});
 add('AGENT_DEPENDENCIES',needed.every(s=>exists('.agents/skills/'+s+'/SKILL.md')),'Canonical specialist SKILL.md files present for all required methods');
 add('AUDIT_INTENT',/owner: \/kasteel\//.test(r)&&/primary|primair/i.test(r),'Source research owner and primary query');
 add('RESEARCH_SOURCE',/https:\/\//.test(r),'Research official source link recorded');
 add('SERP_COMPETITOR',/top.?10|SERP/i.test(r)&&!/SERP dataset ontbreekt|top ten and SERP-feature matrix incomplete|SERP top-10 matrix.*DATA_GAP/i.test(r),'Requires actual ranked competitor evidence and missing-core-intent resolution');
 add('BRIEF',/workflow_version: museum-v1/.test(b)&&/MUST/.test(b),'Versioned brief and intent constraints');
 add('CONTENT',page.includes('<h1')&&h2.length>=4&&page.includes('https://'),'Canonical nl-BE detail body');
 add('FACT_CLAIMS',/factual|fact-check|fact.check/i.test(rev)&&!/not every historic claim independently corroborated|niet elke.*onafhankelijk/i.test(rev),'Requires per-claim linked source and date; existence of source alone is insufficient');
 add('GEO_SEO',/seo-aeo-geo/i.test(rev)&&/seo-onpage/.test(rev),'Explicit specialist checklist represented; separate human review still necessary');
 add('HUMANIZER',/humanizer.*PASS/i.test(rev),'Distinct text-aware specialist pass with before/after evidence required');
 add('GENERAL_WRITING',/general-writing.*PASS/i.test(rev),'Distinct writer review with evidence required');
 add('ANTI_AI_SLOP',/anti-ai-slop.*PASS/i.test(rev),'Distinct non-cloning review with before/after evidence required');
 add('EDITORIAL_QA',/editorial-qa.*PASS/i.test(rev),'Specialist editorial gate with source-level findings required');
 const pfile='kasteel/'+slug+'/index.html';
 add('BUILD',exists(pfile)&&read(pfile).includes(page),'Canonical built HTML matches source');
 add('PUBLISH_REVIEW',/PASS — READY_FOR_HUMAN_VALIDATION/.test(rev)&&!/FAIL — KEEP_NOINDEX/.test(rev),'Research + editorial + factual review approved; indexation remains separate');
 results.push({slug,headings:h2,stages:evidence});
}
fs.mkdirSync('.artifacts/qa',{recursive:true});
fs.writeFileSync('.artifacts/qa/antwerpen-specialist-stages.json',JSON.stringify({generatedAt:new Date().toISOString(),source:'real evidence in repo',results},null,2)+'\n');
for(const page of results){const blocked=page.stages.filter(s=>s.status==='BLOCKED');console.log(page.slug,blocked.length?'BLOCKED '+blocked.map(x=>x.stage).join(', '):'ALL VERIFIED');}
if(results.some(p=>p.stages.some(s=>s.status==='BLOCKED')))process.exitCode=1;
