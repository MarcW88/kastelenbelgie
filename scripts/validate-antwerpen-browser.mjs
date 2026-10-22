import { chromium } from 'playwright';
import { spawn } from 'node:child_process';
import fs from 'node:fs';
import assert from 'node:assert/strict';

const server = spawn('python3', ['-m','http.server','8765','--bind','127.0.0.1'], {stdio:'ignore'});
const sleep = ms => new Promise(r=>setTimeout(r,ms));
let browser;
try {
  await sleep(2000);
  browser = await chromium.launch({headless:true});
  fs.mkdirSync('.artifacts/antwerpen-review',{recursive:true});
  for (const [device,width,height] of [['desktop',1440,900],['mobile',390,844]]) {
    const page=await browser.newPage({viewport:{width,height},deviceScaleFactor:1});
    const errors=[];
    page.on('pageerror',e=>errors.push(e.message));
    const response=await page.goto('http://127.0.0.1:8765/kastelen/antwerpen/',{waitUntil:'networkidle'});
    assert.equal(response.status(),200,'HTTP response '+device);
    assert.equal(await page.locator('h1').count(),1,'one H1 '+device);
    assert.equal(await page.locator('.visit-card').count(),6,'six visit cards '+device);
    assert.equal(await page.locator('.planning-section').count(),2,'two planning sections '+device);
    assert.equal(await page.locator('.visit-card a.visit-source').count(),6,'six source links '+device);
    assert.equal(await page.locator('meta[name="robots"]').getAttribute('content'),'noindex,follow');
    const text=await page.locator('main').innerText();
    assert(text.includes('Kasteel de Renesse'));
    assert(!text.includes('Gabarit klaar'));
    assert(!text.includes('Inhoud nog te schrijven'));
    assert.equal(errors.length,0,'browser exceptions '+device+': '+errors.join('; '));
    const dims=await page.evaluate(()=>({scroll:document.documentElement.scrollWidth,client:document.documentElement.clientWidth}));
    assert(dims.scroll<=dims.client+2,'horizontal overflow '+device+': '+JSON.stringify(dims));
    await page.screenshot({path:'.artifacts/antwerpen-review/'+device+'.png',fullPage:true});
    console.log(device,'PASS',JSON.stringify(dims),'screenshot saved');
    await page.close();
  }
} finally {
  if(browser)await browser.close();
  server.kill();
}
