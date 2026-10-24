import { chromium } from '@playwright/test';
import { spawn } from 'node:child_process';
import { mkdir, writeFile } from 'node:fs/promises';
const route = '/kasteel/kasteel-van-beloeil/';
const port = 4187;
const local = 'http://127.0.0.1:' + port + route;
const production = 'https://kastelenbelgie.be' + route;
const server = spawn('python3', ['-m', 'http.server', String(port), '--bind', '127.0.0.1'], { stdio: 'ignore' });
const out = '.artifacts/beloeil-visual';
await mkdir(out, {recursive:true});
const results = [];
let browser;
try {
  for (let k=0;k<60;k++) { try { if((await fetch(local)).ok) break; } catch {} await new Promise(r=>setTimeout(r,250)); if(k===59)throw Error('Local server failed'); }
  browser = await chromium.launch({headless:true});
  for(const target of [{name:'local',url:local},{name:'production',url:production}]) {
    for(const viewport of [{name:'desktop',width:1440,height:900},{name:'mobile',width:390,height:844}]) {
      const page=await browser.newPage({viewport:{width:viewport.width,height:viewport.height},deviceScaleFactor:1});
      let status=null,error=null;
      try {
        const response=await page.goto(target.url,{waitUntil:'domcontentloaded',timeout:25000});
        status=response?.status()??null;
        await page.waitForTimeout(1500);
        const data=await page.evaluate(()=>{
          const img=document.querySelector('.beloeil-lead-photo img');
          const links=[...document.querySelectorAll('.castle-editorial-toc a[href^="#"]')];
          return {title:document.title,h1:document.querySelectorAll('h1').length,hero:!!document.querySelector('.castle-editorial-intro'),visitPanel:!!document.querySelector('#praktisch-bezoek.castle-visit-panel'),tocLinks:links.length,brokenAnchors:links.map(a=>a.hash.slice(1)).filter(id=>!document.getElementById(id)),image:img?{src:img.currentSrc,loaded:img.complete&&img.naturalWidth>0,naturalWidth:img.naturalWidth}:null,horizontalOverflow:document.documentElement.scrollWidth>document.documentElement.clientWidth,scrollWidth:document.documentElement.scrollWidth,clientWidth:document.documentElement.clientWidth,robots:document.querySelector('meta[name="robots"]')?.content};
        const screenshot=out+'/'+target.name+'-'+viewport.name+'.png';
        await page.screenshot({path:screenshot,fullPage:true});
        results.push({target:target.name,viewport:viewport.name,status,...data,screenshot});
      } catch(e){error=String(e);results.push({target:target.name,viewport:viewport.name,status,error});}
      await page.close();
    }
  }
} finally {await browser?.close();server.kill();}
await writeFile(out+'/report.json',JSON.stringify({commit:process.env.GITHUB_SHA??null,results},null,2)+'\n');
console.log(JSON.stringify(results,null,2));
const localResults=results.filter(x=>x.target==='local');
if(localResults.some(x=>x.error||x.status!==200||x.h1!==1||!x.hero||!x.visitPanel||x.tocLinks<4||x.brokenAnchors.length||x.horizontalOverflow||!x.image?.loaded))process.exitCode=1;
