import fs from 'node:fs';
const slugs=['kasteel-van-loppem','kasteel-beauvoorde','kasteel-van-rumbeke','kasteel-wijnendale','kasteel-tillegem','kasteel-tudor','kasteel-beisbroek','kasteel-de-blankaart'];
const norm=s=>s.toLowerCase().normalize('NFKD').replace(/<[^>]*>/g,' ').replace(/&[a-z]+;/g,' ').replace(/[^a-z0-9à-ÿ\s]/g,' ').replace(/\s+/g,' ').trim();
const tokens=s=>new Set(norm(s).split(' ').filter(x=>x.length>=5&&!['kasteel','bezoek','bezoeken','worden','kunnen','volgens','waarbij','daarom','domein','kasteelheer'].includes(x)));
const similarity=(a,b)=>{const x=tokens(a),y=tokens(b);const n=[...x].filter(w=>y.has(w)).length;return n/Math.max(1,Math.min(x.size,y.size));};
const pages=[];
for(const slug of slugs){
 const html=fs.readFileSync('content/kasteel/'+slug+'/body.html','utf8');
 const sections=[...html.matchAll(/<section\b[^>]*>([\s\S]*?)<\/section>/g)].map(m=>({heading:(m[1].match(/<h2[^>]*>([\s\S]*?)<\/h2>/)||[])[1]?.replace(/<[^>]+>/g,'').trim()||'',prose:[...m[1].matchAll(/<p[^>]*>([\s\S]*?)<\/p>/g)].map(z=>z[1].replace(/<[^>]*>/g,'').trim()).filter(Boolean)})).filter(x=>x.heading&&!/controleer (de actuele|je bezoek)/i.test(x.heading));
 const findings=[];
 // Humanizer: repetitive transitions, CTA and editorial filler; preserve factual details.
 const paragraphs=sections.flatMap(x=>x.prose);
 const patterns=[[/\bdat maakt (het|de|dit)\b/gi,'vague explanatory bridge'],[/\bhet is (belangrijk|essentieel) om\b/gi,'generic importance claim'],[/\bgeen (klassiek|gewone|typisch)\b/gi,'repetitive contrast wording'],[/\bwie vooral\b/gi,'reused audience transition']];
 for(const [regex,label] of patterns){const examples=paragraphs.flatMap(t=>[...t.matchAll(regex)].map(m=>t.slice(Math.max(0,m.index-35),Math.min(t.length,m.index+70))));if(examples.length>=2)findings.push({pass:'humanizer',severity:'medium',issue:label,count:examples.length,evidence:examples.slice(0,3),fix:'Vary the sentence logic or replace generalized transition with a specific visitor decision.'});}
 // Anti-AI slop: duplicated promises, same informational sections and templated structure.
 for(let i=0;i<sections.length;i++)for(let j=i+1;j<sections.length;j++){
  const a=sections[i],b=sections[j],score=similarity(a.prose.join(' '),b.prose.join(' '));
  if(score>=0.53 && a.prose.join(' ').length>140 && b.prose.join(' ').length>140) findings.push({pass:'anti-ai-slop',severity:score>=0.70?'high':'medium',issue:'Overlapping section substance',sections:[a.heading,b.heading],similarity:Number(score.toFixed(2)),fix:'Merge or replace repeating claims; retain unique sourced information.'});
 }
 if(sections.length>=6) findings.push({pass:'anti-ai-slop',severity:'review',issue:'Many short sections may fragment the topic',count:sections.length,fix:'Review narrative sequence; do not equate section count with quality.'});
 pages.push({slug,sections:sections.length,findings});
}
const report={generatedAt:new Date().toISOString(),method:'Heuristic editorial review: source HTML paragraphs; canonical humanizer and anti-ai-slop SKILL.md retained unchanged. Results require a human editorial pass.',pages,summary:{pages:pages.length,high:pages.flatMap(x=>x.findings).filter(f=>f.severity==='high').length,medium:pages.flatMap(x=>x.findings).filter(f=>f.severity==='medium').length}};
fs.mkdirSync('.artifacts/qa',{recursive:true});
fs.writeFileSync('.artifacts/qa/west-flanders-style-audit.json',JSON.stringify(report,null,2)+'\n');
for(const p of pages)console.log(p.slug+': '+p.findings.map(f=>f.pass+':'+f.severity+':'+f.issue).join(' | '));
console.log('Heuristic audit generated; NOT a humanizer rewrite, AI-authorship detector, or full editorial PASS.');
if(report.summary.high>0)process.exitCode=1;
