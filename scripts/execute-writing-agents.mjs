import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
const root=process.cwd();
const slugs=['kasteel-marnix-de-sainte-aldegonde','kasteel-dursel','kasteel-de-renesse','paleis-op-de-meir','kasteel-rivierenhof','sterckshof'];
const stages=['humanizer','general-writing','anti-ai-slop'];
const model=process.env.OPENAI_MODEL||'gpt-4.1';
const dry=process.argv.includes('--dry-run');
const requested=process.argv.find(x=>x.startsWith('--slug='))?.slice(7);
if(requested&&!slugs.includes(requested))throw Error('Unknown or unauthorized slug');
const selected=requested?[requested]:slugs;
const instructions=Object.fromEntries(stages.map(s=>[s,fs.readFileSync('.agents/skills/'+s+'/SKILL.md','utf8')]));
const sha=t=>crypto.createHash('sha256').update(t).digest('hex');
const audit={model,dryRun:dry,runs:[]};
const report='.artifacts/ai-editor/antwerpen-run.json';
fs.mkdirSync(path.dirname(report),{recursive:true});
async function revise(input,stage,slug){
 const response=await fetch('https://api.openai.com/v1/responses',{method:'POST',headers:{'Content-Type':'application/json',Authorization:'Bearer '+process.env.OPENAI_API_KEY},body:JSON.stringify({
 model,store:false,
 instructions:'You are performing the canonical '+stage+' editorial skill for a Dutch-Belgian castle web article. Follow the full skill below. Return only the complete revised HTML, no markdown fences, no commentary. Do not add unsourced historical claims, ticket numbers or current access facts. Do not change IDs, links, tags, navigation, non-prose markup or the noindex policy. Preserve all specific facts unless demonstrably inconsistent.\n\n'+instructions[stage],
 input:'Edit this FULL source body for '+slug+'. Keep it parseable and preserve all page sections except remove genuinely redundant editorial sections. Return FULL HTML only.\n\n'+input,
 max_output_tokens:12000
 })});
 const payload=await response.json();
 if(!response.ok||payload.error)throw Error('Provider '+response.status+': '+JSON.stringify(payload.error||payload).slice(0,400));
 const out=(payload.output||[]).flatMap(x=>x.content||[]).filter(x=>x.type==='output_text').map(x=>x.text).join('').trim();
 if(payload.status!=='completed'||!out)throw Error('Incomplete model response: '+payload.status);
 return out.replace(/^\x60\x60\x60(?:html)?\s*/i,'').replace(/\s*\x60\x60\x60$/,'');
}
function validate(before,after,slug){
 if(!after.includes('<section')||!after.includes('</section>')||!after.includes('<h1'))throw Error('Malformed output');
 if((after.match(/<h1\b/g)||[]).length!==1)throw Error('H1 count changed');
 const links=x=>[...x.matchAll(/href="([^"]+)"/g)].map(m=>m[1]).sort();
 const ids=x=>[...x.matchAll(/\bid="([^"]+)"/g)].map(m=>m[1]).sort();
 if(JSON.stringify(links(before))!==JSON.stringify(links(after)))throw Error('Link targets changed');
 const oldIds=ids(before),newIds=ids(after);
 if(!oldIds.every(id=>newIds.includes(id)))throw Error('Structural anchors removed');
 if(after.length<before.length*.55||after.length>before.length*1.55)throw Error('Excessive change requires review');
 if(!after.includes('/kastelen/antwerpen/'))throw Error('Province link removed');
}
for(const slug of selected){
 const file=path.join(root,'content/kasteel',slug,'body.html');const before=fs.readFileSync(file,'utf8');
 let current=before;const record={slug,initialSha256:sha(before),passes:[]};audit.runs.push(record);
 try{
  for(const stage of stages){
   if(dry){record.passes.push({stage,skillSha256:sha(instructions[stage]),status:'CONFIG_OK'});continue;}
   const next=await revise(current,stage,slug);validate(current,next,slug);
   record.passes.push({stage,skillSha256:sha(instructions[stage]),beforeSha256:sha(current),afterSha256:sha(next),changed:current!==next,status:'PASS'});
   current=next;
  }
  if(!dry){fs.writeFileSync(file,current);record.finalSha256=sha(current);record.status='PASS';}
  else record.status='CONFIG_OK';
 }catch(e){record.status='FAIL';record.error=String(e.message);fs.writeFileSync(report,JSON.stringify(audit,null,2)+'\n');throw e;}
 fs.writeFileSync(report,JSON.stringify(audit,null,2)+'\n');
 console.log(slug,record.status,record.passes.map(x=>x.stage+':'+x.status).join(', '));
}
