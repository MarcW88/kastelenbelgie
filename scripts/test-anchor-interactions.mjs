import { chromium } from '@playwright/test';
import { spawn } from 'node:child_process';
import assert from 'node:assert/strict';
const server=spawn('python3',['-m','http.server','8123','--bind','127.0.0.1'],{stdio:'ignore'});
const routes=['/kasteel/gravensteen/','/kasteel/kasteel-van-loppem/','/kastelen/oost-vlaanderen/','/gidsen/middeleeuws-kasteel/','/soorten/waterkastelen/','/bezoeken/kastelen-met-kinderen/','/inspiratie/mooiste-kastelen-belgie/','/routes/kastelenroute-ardennen/'];
try {
 await new Promise(resolve=>setTimeout(resolve,1000));
 const browser=await chromium.launch({headless:true}); let tested=0;
 for(const viewport of [{width:1440,height:900},{width:390,height:844}]){
  const page=await browser.newPage({viewport});
  for(const route of routes){
   const response=await page.goto('http://127.0.0.1:8123'+route); assert.equal(response.status(),200,route);
   const links=page.locator('aside nav[aria-label="Spring naar onderdelen"] a'); const n=await links.count();
   for(let i=0;i<n;i++){
    const link=links.nth(i); const href=await link.getAttribute('href'); const expected=new URL(href,'http://127.0.0.1:8123'+route);
    await link.click(); assert.equal(new URL(page.url()).pathname,expected.pathname,`${route} ${href}`); assert.equal(new URL(page.url()).hash,expected.hash,`${route} ${href}`);
    const target=page.locator(`[id="${decodeURIComponent(expected.hash.slice(1))}"]`); assert.equal(await target.count(),1,`${route} ${href}`);
    assert(await target.evaluate(el=>{const r=el.getBoundingClientRect();return r.bottom>0&&r.top<innerHeight}),`${route} ${href} target not visible`); tested++;
   }
  }
  await page.close();
 }
 assert(tested>0,'No sidebar links tested');console.log(`${tested} sidebar clicks passed across desktop and mobile`);await browser.close();
} finally {server.kill();}
