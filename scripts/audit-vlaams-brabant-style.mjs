import fs from 'node:fs';
const slugs=['kasteel-van-gaasbeek','kasteel-van-beersel','kasteel-groenenberg','kasteel-coloma','kasteel-van-bouchout','arenbergkasteel','kasteel-van-horst'];
const stop=new Set(['kasteel','bezoek','bezoeken','worden','kunnen','volgens','tussen','alleen','omdat','museums','allemaal','daarvoor']);
function tokens(s){return new Set(s.toLowerCase().replace(/<[^>]*>/g,' ').replace(/[^\p{L}\s]/gu,' ').split(/\s+/).filter(x=>x.length>5&&!stop.has(x)));}
function sim(a,b){const x=tokens(a),y=tokens(b);return [...x].filter(z=>y.has(z)).length/Math.max(1,Math.min(x.size,y.size));}
const reports=[];
for(const slug of slugs){
 const html=fs.readFileSync('content/kasteel/'+slug+'/body.html','utf8');
 const parts=[...html.matchAll(/<section\b[^>]*>([\s\S]*?)<\/section>/g)].map(m=>m[1]);
 const sections=parts.map(p=>({heading:(p.match(/<h2[^>]*>([^<]+)<\/h2>/)||[])[1]||'',body:[...p.matchAll(/<p[^>]*>([\s\S]*?)<\/p>/g)].map(x=>x[1]).join(' ')})).filter(x=>x.heading&&!/Officiële toegang/.test(x.heading));
 const findings=[];
 const phrases=['een andere ervaring','niet zomaar','de reden om','dat betekent niet','het is belangrijk','voor je vertrekt'];
 for(const phrase of phrases){const n=sections.filter(s=>s.body.toLowerCase().includes(phrase)).length;if(n>1)findings.push({pass:'humanizer',severity:'medium',issue:'repeated mechanical phrasing',evidence:phrase,sections:n,fix:'Vary or consolidate overlapping prose while preserving specific facts.'});}
 for(let i=0;i<sections.length;i++)for(let j=i+1;j<sections.length;j++){const score=sim(sections[i].body,sections[j].body);if(score>0.6)findings.push({pass:'anti-ai-slop',severity:'high',issue:'substantial repeated section content',headings:[sections[i].heading,sections[j].heading],similarity:score,fix:'Merge duplicated information or provide truly distinctive research.'});}
 const words=html.replace(/<[^>]*>/g,' ').trim().split(/\s+/).length;
 if(words<300)findings.push({pass:'editorial-depth',severity:'review',issue:'short page; investigate depth against SERP and evidence',words,fix:'Research missing user needs before adding prose.'});
 reports.push({slug,words,findings});
}
const output={generatedAt:new Date().toISOString(),scope:'Vlaams-Brabant',method:'Heuristic machine lint aligned with humanizer/anti-ai-slop, not full subjective specialist execution.',pages:reports};
fs.mkdirSync('.artifacts/qa',{recursive:true});fs.writeFileSync('.artifacts/qa/vlaams-brabant-style-review.json',JSON.stringify(output,null,2)+'\n');
for(const p of reports)console.log(p.slug,p.words,'words;',p.findings.length,'findings');
if(reports.some(p=>p.findings.some(f=>f.severity==='high')))process.exitCode=1;
console.log('PASS means no high-severity matching-pattern heuristics; it is NOT editorial approval.');
