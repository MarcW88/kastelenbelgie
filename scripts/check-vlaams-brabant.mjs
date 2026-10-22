import fs from 'node:fs';
import assert from 'node:assert/strict';
const slugs=['kasteel-van-gaasbeek','kasteel-van-beersel','kasteel-groenenberg','kasteel-coloma','kasteel-van-bouchout','arenbergkasteel','kasteel-van-horst'];
const ids=['gaasbeek','beersel','groenenberg','coloma','bouchout','arenberg','horst'];
const entries=JSON.parse(fs.readFileSync('content/reviewed-pages.json','utf8'));
const province=fs.readFileSync('content/kastelen/vlaams-brabant/body.html','utf8');
const results=[];
for(let i=0;i<slugs.length;i++){
 const slug=slugs[i],route='/kasteel/'+slug+'/',src='content/kasteel/'+slug+'/body.html',output='kasteel/'+slug+'/index.html';
 let checks={slug,route};
 try{
 const entry=entries.find(e=>e.route===route);
 assert.ok(entry&&entry.source===src,'missing correct reviewed-page route');
 assert.ok(fs.existsSync(src)&&fs.existsSync(output),'source/render absent');
 const body=fs.readFileSync(src,'utf8'),html=fs.readFileSync(output,'utf8');
 assert.ok(html.includes(body),'render does not include canonical body');
 assert.ok(province.includes('href="'+route+'"'),'not linked from province');
 assert.ok(province.includes('id="'+ids[i]+'"'),'province anchor absent');
 assert.equal((body.match(/<h1\b/g)||[]).length,1,'exactly one h1 required');
 assert.ok((body.match(/<h2\b/g)||[]).length>=3,'insufficient sections');
 assert.ok(/href="https:\/\//.test(body),'official source absent');
 assert.ok(html.includes('noindex,follow'),'indexation guard missing');
 assert.ok(html.includes('rel="canonical"'),'canonical absent');
 assert.ok(html.includes('castle-detail.css'),'CSS absent');
 for(const p of ['content/research/kasteel/'+slug+'/serp-coverage.md','content/briefs/kasteel/'+slug+'.md','content/reviews/kasteel/'+slug+'/post-write-gap-check.md'])assert.ok(fs.existsSync(p),'missing specialist handoff: '+p);
 checks={...checks,status:'PASS',wordCount:body.replace(/<[^>]*>/g,' ').trim().split(/\s+/).length};
 console.log('PASS',slug,'render + province + source + noindex + artifacts');
 }catch(e){checks={...checks,status:'FAIL',error:e.message};console.error('FAIL',slug,e.message)}
 results.push(checks);
}
fs.mkdirSync('.artifacts/qa',{recursive:true});
fs.writeFileSync('.artifacts/qa/vlaams-brabant-machine-gates.json',JSON.stringify({generatedAt:new Date().toISOString(),results,scope:'structural machine checks only, not specialist editorial sign-off'},null,2)+'\n');
if(results.some(x=>x.status==='FAIL'))process.exitCode=1;
console.log('These checks never certify full SERP, humanizer, anti-ai-slop, factuality or publish approval.');
