import {chromium} from '@playwright/test';
import {spawn} from 'node:child_process';
import fs from 'node:fs';
const routes=['/bezoeken/bezoekbare-kastelen/','/bezoeken/kastelen-met-kinderen/','/bezoeken/kastelen-overnachten/','/bezoeken/kastelen-met-rondleiding/','/bezoeken/gratis-kastelen/','/bezoeken/kastelen-met-park/','/','/kastelen/oost-vlaanderen/','/kasteel/gravensteen/','/routes/','/gidsen/','/soorten/'];
const server=spawn('python3',['-m','http.server','4189','--bind','127.0.0.1'],{stdio:'ignore'});
const output='.artifacts/integration-review';fs.mkdirSync(output,{recursive:true});
let failures=[],results=[];
try{
 await new Promise(r=>setTimeout(r,1000));let browser=await chromium.launch();
 for(const width of [1440,768,390]){const page=await browser.newPage({viewport:{width,height:900}});
  for(const route of routes){let errors=[];page.on('pageerror',e=>errors.push(String(e)));const res=await page.goto('http://127.0.0.1:4189'+route,{waitUntil:'domcontentloaded'});await page.screenshot({path:`${output}/${width}-${route.replaceAll('/','-')||'home'}.png`,fullPage:true});
   const info=await page.evaluate(()=>({title:document.title,h1:document.querySelectorAll('h1').length,robots:document.querySelector('meta[name="robots"]')?.content,overflow:document.documentElement.scrollWidth>document.documentElement.clientWidth,affiliate:[...document.querySelectorAll('[data-affiliate-key]')].map(a=>({key:a.dataset.affiliateKey,href:a.href,rel:a.rel}))}));
   if(res.status()!==200||info.h1!==1||info.robots!=='index,follow'||info.overflow||errors.length)failures.push({route,width,status:res.status(),errors,...info});
   if(width===390){let b=page.locator('[data-menu]');await b.click();if(await b.getAttribute('aria-expanded')!=='true')failures.push({route,width,error:'mobile menu did not open'});await b.click()}
   results.push({route,width,status:res.status(),...info});page.removeAllListeners('pageerror');
  }await page.close();
 }
 await browser.close();fs.writeFileSync(`${output}/report.json`,JSON.stringify({results,failures},null,2));console.log(JSON.stringify({pages:results.length,failures},null,2));if(failures.length)process.exitCode=1;
}finally{server.kill()}
