import fs from 'node:fs';
const slugs=['kasteel-van-loppem','kasteel-beauvoorde','kasteel-van-rumbeke','kasteel-wijnendale','kasteel-tillegem','kasteel-tudor','kasteel-beisbroek','kasteel-de-blankaart'];
const gates=['AUDIT','RESEARCH','SERP','BRIEF','FACT_CHECK','GEO','HUMANIZER','GENERAL_WRITING','ANTI_AI_SLOP','SEO','EDITORIAL_QA','PLAYWRIGHT','PUBLISH_REVIEW'];
let failures=0;
for (const slug of slugs) {
  const p='content/reviews/kasteel/'+slug+'/workflow-evidence.json';
  if (!fs.existsSync(p)) {
    console.log('BLOCKED',slug,'missing',p);failures++;continue;
  }
  let evidence;
  try { evidence=JSON.parse(fs.readFileSync(p,'utf8')); }
  catch(e){console.log('BLOCKED',slug,'invalid JSON',e.message);failures++;continue;}
  let blocked=[];
  for(const name of gates){
    const g=evidence.gates?.[name];
    if(!g || g.status!=='PASS' || !Array.isArray(g.evidence) || !g.evidence.length) blocked.push(name);
  }
  const review=fs.readFileSync('content/reviews/kasteel/'+slug+'/post-write-gap-check.md','utf8');
  if(/FAIL\s*[—-]\s*KEEP_NOINDEX|Decision:\s*FAIL|Research and specialist gates incomplete/i.test(review)) blocked.push('REVIEW_DOCUMENT_CONFLICT');
  if(blocked.length){console.log('BLOCKED',slug,blocked.join(', '));failures++;}
  else console.log('READY_FOR_HUMAN_VALIDATION',slug);
}
console.log(failures?'Editorial gates blocked for '+failures+' pages. No publishing approval can be inferred.':'All evidence checks passed. Human validation is still mandatory for indexation.');
if(failures)process.exitCode=1;
