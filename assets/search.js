(async function(){
  const results=document.getElementById('search-results');
  const status=document.getElementById('search-status');
  const form=document.querySelector('.search-page-form');
  if(!results||!status||!form)return;
  const params=new URLSearchParams(location.search);
  const q=(params.get('q')||'').trim().slice(0,150);
  const type=params.get('type')||'';
  form.elements.q.value=q;
  if([...form.elements.type.options].some(opt=>opt.value===type))form.elements.type.value=type;
  const normalize=text=>(text||'').normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLocaleLowerCase('nl').replace(/[^a-z0-9]+/g,' ').trim();
  const tokens=normalize(q).split(/\s+/).filter(Boolean);
  if(!tokens.length){status.textContent='Voer een zoekterm in om kastelen, regio’s en thema’s te vinden.';return;}
  status.textContent='Resultaten worden gezocht…';
  try{
    const response=await fetch('/assets/search-index.json');
    if(!response.ok)throw new Error('Search index unavailable');
    const records=await response.json();
    const matches=records.filter(item=>!type||item.type===type).map(item=>{
      const title=normalize(item.title),desc=normalize(item.description),key=normalize(item.keywords);
      if(!tokens.every(token=>title.includes(token)||desc.includes(token)||key.includes(token)))return null;
      const score=tokens.reduce((s,t)=>s+(title.includes(t)?10:0)+(key.includes(t)?4:0)+(desc.includes(t)?1:0),0)+(title===normalize(q)?20:0);
      return {item,score};
    }).filter(Boolean).sort((a,b)=>b.score-a.score||a.item.title.localeCompare(b.item.title,'nl')).slice(0,50);
    status.textContent=matches.length?matches.length+' resultaat'+(matches.length===1?'':'en')+' voor “'+q+'”'+(matches.length===50?' (eerste 50)':'')+'.':'Geen resultaten voor “'+q+'”. Probeer een andere naam, provincie of categorie.';
    results.replaceChildren();
    const sectionNames={kasteel:'Kasteel',kastelen:'Regio',soorten:'Thema',bezoeken:'Bezoeken',gidsen:'Gids',routes:'Route',inspiratie:'Inspiratie'};
    for(const {item} of matches){
      const card=document.createElement('article');card.className='search-result';
      const label=document.createElement('span');label.className='eyebrow';label.textContent=sectionNames[item.type]||'Atlas';
      const h=document.createElement('h2'),link=document.createElement('a');link.href=item.url;link.textContent=item.title;h.append(link);
      card.append(label,h);
      if(item.description){const p=document.createElement('p');p.textContent=item.description;card.append(p);}
      results.append(card);
    }
  }catch(error){status.textContent='Zoeken is tijdelijk niet beschikbaar. Ontdek kastelen via de regio’s en thema’s.';const a=document.createElement('a');a.href='/kastelen/';a.textContent='Bekijk kastelen per regio →';results.replaceChildren(a);}
})();
