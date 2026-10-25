// Global navigation: provinces always means the full regional directory, not Flanders only.
document.querySelectorAll('[data-nav] a').forEach(a=>{if(a.textContent.trim()==='Provincies')a.setAttribute('href','/kastelen/');});
const menu=document.querySelector('[data-menu]'),nav=document.querySelector('[data-nav]');menu?.addEventListener('click',()=>{const o=nav.classList.toggle('open');menu.setAttribute('aria-expanded',o)});
const surprise=['kasteel/gravensteen/','kasteel/kasteel-van-veves/','kasteel/burcht-reinhardstein/','kasteel/kasteel-van-beloeil/','kasteel/kasteel-van-modave/'];document.querySelectorAll('[data-surprise]').forEach(b=>b.addEventListener('click',()=>location.href=surprise[Math.floor(Math.random()*surprise.length)]));
const castleLocations=[
 {name:'Gravensteen',location:'Gent · Oost-Vlaanderen',lat:51.0572,lng:3.7209,href:'/kasteel/gravensteen/',tags:['visit','kids']},
 {name:'Kasteel van Vêves',location:'Celles · Namen',lat:50.2214,lng:4.9822,href:'/kasteel/kasteel-van-veves/',tags:['visit','kids','medieval']},
 {name:'Burcht Reinhardstein',location:'Ovifat · Luik',lat:50.4558,lng:6.1118,href:'/kasteel/burcht-reinhardstein/',tags:['visit','medieval']},
 {name:'Kasteel van Beloeil',location:'Beloeil · Henegouwen',lat:50.5484,lng:3.7305,href:'/kasteel/kasteel-van-beloeil/',tags:['garden']},
 {name:'Kasteel van Modave',location:'Modave · Luik',lat:50.4419,lng:5.2955,href:'/kasteel/kasteel-van-modave/',tags:['visit','garden']}
];
const chips=[...document.querySelectorAll('[data-filter]')],cards=[...document.querySelectorAll('[data-castle]')];
const mapElement=document.getElementById('belgium-castle-map');let castleMap=null;const mapMarkers=[];
if(mapElement&&window.L){
 castleMap=L.map(mapElement,{scrollWheelZoom:false,zoomControl:true}).setView([50.6,4.7],8);
 // Use another public tile host if the primary layer returns missing tiles.
 // Prevent half-rendered maps with isolated patches of background.
 const primaryTiles=L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{maxZoom:18,attribution:'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'});
 const backupTiles=L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png',{maxZoom:18,attribution:'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>'});
 let tileFallbackActive=false;
 primaryTiles.on('tileerror',()=>{
   if(tileFallbackActive)return;
   tileFallbackActive=true;
   castleMap.removeLayer(primaryTiles);
   backupTiles.addTo(castleMap);
   castleMap.invalidateSize();
 });
 primaryTiles.addTo(castleMap);
 for(const castle of castleLocations){const marker=L.marker([castle.lat,castle.lng]).bindPopup('<strong>'+castle.name+'</strong><br>'+castle.location+'<br><a href="'+castle.href+'">Bekijk kasteelfiche →</a>');marker.addTo(castleMap);mapMarkers.push({marker,tags:castle.tags});}
 const bounds=L.latLngBounds(castleLocations.map(p=>[p.lat,p.lng]));castleMap.fitBounds(bounds.pad(.20),{maxZoom:9});requestAnimationFrame(()=>castleMap.invalidateSize());setTimeout(()=>castleMap.invalidateSize(),250);
}else if(mapElement){mapElement.innerHTML='<p class="map-unavailable">De kaart kon niet geladen worden. Gebruik de links naar de kastelen hiernaast.</p>';}
chips.forEach(chip=>chip.addEventListener('click',()=>{
 chips.forEach(x=>x.classList.remove('active'));chip.classList.add('active');
 const f=chip.dataset.filter;
 cards.forEach(c=>c.hidden=f!=='all'&&!c.dataset.castle.split(' ').includes(f));
 if(castleMap){const filtered=[];for(const entry of mapMarkers){const show=f==='all'||entry.tags.includes(f);if(show){entry.marker.addTo(castleMap);filtered.push(entry.marker.getLatLng());}else castleMap.removeLayer(entry.marker);}if(filtered.length)castleMap.fitBounds(L.latLngBounds(filtered).pad(.28),{maxZoom:9});}
}));
