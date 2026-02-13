#!/usr/bin/env python3
"""
Script pour générer la page annuaire alle-kastelen.html
Liste alphabétique de tous les châteaux sur kastelenbelgie.be
"""

import os
import re
from pathlib import Path
from collections import defaultdict

def extract_castle_info(html_file):
    """Extrait le nom du château et la province depuis un fichier HTML"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extraire le titre h1
    h1_match = re.search(r'<h1[^>]*>([^<]+)</h1>', content)
    if h1_match:
        name = h1_match.group(1).strip()
    else:
        # Fallback: utiliser le nom du fichier
        name = html_file.stem.replace('-', ' ').title()
    
    # Extraire la province
    province_match = re.search(r'<strong>Provincie:</strong>\s*<span[^>]*>([^<]+)</span>', content)
    if province_match:
        province = province_match.group(1).strip()
    else:
        province = "Onbekend"
    
    # Extraire la localité depuis le breadcrumb ou l'adresse
    location_match = re.search(r'<strong>Adres:</strong>\s*<span[^>]*>([^<]+)</span>', content)
    if location_match:
        address = location_match.group(1).strip()
        # Extraire la ville (généralement après le code postal)
        city_match = re.search(r'\d{4}\s+([^,]+)', address)
        if city_match:
            location = city_match.group(1).strip()
        else:
            location = address.split(',')[-1].strip() if ',' in address else ""
    else:
        location = ""
    
    return {
        'name': name,
        'province': province,
        'location': location,
        'file': html_file.name
    }

def generate_annuaire():
    """Génère la page annuaire"""
    base_path = Path('/Users/marc/Desktop/kastelenbelgie')
    
    # Trouver tous les fichiers de châteaux
    castle_files = []
    patterns = ['kasteel-*.html', 'hof-*.html', 'citadel-*.html', 'burcht-*.html', 'slot-*.html']
    
    for pattern in patterns:
        castle_files.extend(base_path.glob(pattern))
    
    # Exclure les fichiers backup/old
    castle_files = [f for f in castle_files if '-old' not in f.name and '-backup' not in f.name and '-new' not in f.name]
    
    # Extraire les infos de chaque château
    castles = []
    for f in castle_files:
        try:
            info = extract_castle_info(f)
            castles.append(info)
        except Exception as e:
            print(f"Erreur avec {f}: {e}")
    
    # Trier par nom
    castles.sort(key=lambda x: x['name'].lower())
    
    # Grouper par première lettre
    by_letter = defaultdict(list)
    for castle in castles:
        first_letter = castle['name'][0].upper()
        if first_letter.isalpha():
            by_letter[first_letter].append(castle)
        else:
            by_letter['#'].append(castle)
    
    # Générer le HTML
    html = generate_html(castles, by_letter)
    
    # Écrire le fichier
    output_file = base_path / 'alle-kastelen.html'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"Annuaire généré: {output_file}")
    print(f"Total: {len(castles)} châteaux")

def generate_html(castles, by_letter):
    """Génère le HTML de la page annuaire"""
    
    # Lettres disponibles
    available_letters = sorted(by_letter.keys())
    
    # Générer les liens d'ancrage
    anchor_links = ' '.join([
        f'<a href="#{letter}" class="alphabet-link">{letter}</a>'
        for letter in available_letters
    ])
    
    # Générer les sections par lettre
    sections = []
    for letter in available_letters:
        castle_list = '\n'.join([
            f'''<div class="castle-list-item">
<a href="{c['file']}" class="castle-link">{c['name']}</a>
<span class="castle-meta">{c['province']}{' – ' + c['location'] if c['location'] else ''}</span>
</div>'''
            for c in by_letter[letter]
        ])
        
        sections.append(f'''
<section class="letter-section" id="{letter}">
<h2 class="letter-heading">{letter}</h2>
<div class="castle-list">
{castle_list}
</div>
</section>
''')
    
    all_sections = '\n'.join(sections)
    
    html = f'''<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Alle kastelen in België (A–Z) | kastelenbelgie.be</title>
<meta content="Alfabetische lijst van alle kastelen in België. Ontdek meer dan {len(castles)} kastelen per provincie met praktische informatie en geschiedenis." name="description"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&amp;display=swap" rel="stylesheet"/>
<link href="css/style.css" rel="stylesheet"/>
<link href="favicon.svg" rel="icon" type="image/svg+xml"/>
<style>
.alphabet-nav {{
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    justify-content: center;
    padding: 1.5rem;
    background: var(--cream);
    border-radius: 12px;
    margin-bottom: 2rem;
    position: sticky;
    top: 80px;
    z-index: 100;
}}
.alphabet-link {{
    display: flex;
    align-items: center;
    justify-content: center;
    width: 40px;
    height: 40px;
    background: white;
    border-radius: 8px;
    font-weight: 600;
    color: var(--text);
    text-decoration: none;
    transition: all 0.2s;
    border: 1px solid var(--border);
}}
.alphabet-link:hover {{
    background: var(--primary);
    color: white;
    border-color: var(--primary);
}}
.letter-section {{
    margin-bottom: 3rem;
    scroll-margin-top: 150px;
}}
.letter-heading {{
    font-size: 2rem;
    font-weight: 800;
    color: var(--primary);
    border-bottom: 3px solid var(--primary);
    padding-bottom: 0.5rem;
    margin-bottom: 1.5rem;
}}
.castle-list {{
    display: grid;
    gap: 0.75rem;
}}
.castle-list-item {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 1.5rem;
    background: white;
    border-radius: 8px;
    border: 1px solid var(--border);
    transition: all 0.2s;
}}
.castle-list-item:hover {{
    border-color: var(--primary);
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}}
.castle-link {{
    font-weight: 600;
    color: var(--text);
    text-decoration: none;
}}
.castle-link:hover {{
    color: var(--primary);
}}
.castle-meta {{
    font-size: 0.9rem;
    color: var(--text-light);
}}
.annuaire-intro {{
    text-align: center;
    max-width: 800px;
    margin: 0 auto 2rem;
}}
.annuaire-stats {{
    display: flex;
    justify-content: center;
    gap: 2rem;
    margin: 2rem 0;
}}
.stat-item {{
    text-align: center;
}}
.stat-number {{
    font-size: 2.5rem;
    font-weight: 800;
    color: var(--primary);
    display: block;
}}
.stat-label {{
    font-size: 0.9rem;
    color: var(--text-light);
}}
@media (max-width: 768px) {{
    .alphabet-link {{
        width: 32px;
        height: 32px;
        font-size: 0.9rem;
    }}
    .castle-list-item {{
        flex-direction: column;
        align-items: flex-start;
        gap: 0.25rem;
    }}
}}
</style>
</head>
<body>
<!-- Navigation -->
<nav class="navbar">
<div class="container">
<div class="nav-container">
<a class="logo" href="index.html">
<div class="logo-icon">🏰</div>
                    kastelenbelgie
                </a>
<div class="nav-menu">
<a class="nav-link" href="provinces.html">Kastelen</a>
<a class="nav-link active" href="alle-kastelen.html">A–Z</a>
<a class="nav-link" href="blog.html">Blog</a>
<a class="nav-link" href="contact.html">Contact</a>
<div class="search-box">
<input class="search-input" id="search-input" placeholder="Zoek kasteel..." type="text"/>
</div>
</div>
</div>
</div>
</nav>

<!-- Breadcrumbs -->
<nav aria-label="Breadcrumb" class="breadcrumbs">
<div class="breadcrumbs-container">
<div class="breadcrumbs-nav">
<a href="index.html">Home</a>
<span class="breadcrumbs-separator">›</span>
<span class="breadcrumbs-current">Alle kastelen (A–Z)</span>
</div>
</div>
</nav>

<!-- Hero Section -->
<section class="page-hero" style="background: linear-gradient(135deg, var(--cream) 0%, white 100%); padding: 3rem 0;">
<div class="container">
<h1 style="text-align: center; font-size: 2.5rem; margin-bottom: 1rem;">Alle kastelen in België (A–Z)</h1>
<div class="annuaire-intro">
<p>Ontdek de volledige alfabetische lijst van alle kastelen op kastelenbelgie.be. Van middeleeuwse burchten tot elegante landhuizen, van Vlaanderen tot Wallonië.</p>
</div>
<div class="annuaire-stats">
<div class="stat-item">
<span class="stat-number">{len(castles)}</span>
<span class="stat-label">Kastelen</span>
</div>
<div class="stat-item">
<span class="stat-number">11</span>
<span class="stat-label">Provincies</span>
</div>
<div class="stat-item">
<span class="stat-number">{len(available_letters)}</span>
<span class="stat-label">Letters</span>
</div>
</div>
<p style="text-align: center; margin-top: 1rem;">
<a href="provinces.html" class="btn-modern btn-secondary-modern">📍 Bekijk kastelen per provincie</a>
</p>
</div>
</section>

<!-- Alphabet Navigation -->
<section style="padding: 0 0 2rem;">
<div class="container">
<div class="alphabet-nav">
{anchor_links}
</div>
</div>
</section>

<!-- Castle List -->
<section style="padding: 0 0 4rem;">
<div class="container">
{all_sections}
</div>
</section>

<!-- Back to top -->
<div style="text-align: center; padding: 2rem;">
<a href="#" class="btn-modern btn-primary-modern">↑ Terug naar boven</a>
</div>

<!-- Footer -->
<footer class="footer" style="background: #1E2523; color: #F5F3EF; padding: 0;">
<div class="container" style="max-width: 1200px; margin: 0 auto; padding: 0 1.5rem;">
<div class="footer-top" style="display: grid; grid-template-columns: 1.5fr 1fr; gap: 3rem; padding: 3rem 0; border-bottom: 1px solid rgba(255,255,255,0.1);">
<div>
<h3 style="font-size: 1.4rem; font-weight: 700; margin-bottom: 1rem; color: #F5F3EF;">
                        🏰 Kastelen België
                    </h3>
<p style="color: #D4C7B4; line-height: 1.7; margin-bottom: 1.5rem; font-size: 0.95rem;">
<strong>Dé gids voor kastelen in België.</strong> Ontdek meer dan 300 kastelen per provincie, 
                        plan je bezoek met praktische info en laat je inspireren door eeuwenoude verhalen 
                        en prachtige foto's uit meer dan duizend jaar Belgische geschiedenis.
                    </p>
<div style="display: flex; gap: 2rem; flex-wrap: wrap;">
<div style="font-size: 0.85rem; color: #D4C7B4;">
<strong style="display: block; color: #C89A3B; font-size: 1.1rem;">300+</strong>
                            Kastelen
                        </div>
<div style="font-size: 0.85rem; color: #D4C7B4;">
<strong style="display: block; color: #C89A3B; font-size: 1.1rem;">11</strong>
                            Provincies
                        </div>
<div style="font-size: 0.85rem; color: #D4C7B4;">
<strong style="display: block; color: #C89A3B; font-size: 1.1rem;">1000+</strong>
                            Jaar geschiedenis
                        </div>
</div>
</div>
<div style="background: rgba(255,255,255,0.05); padding: 1.5rem; border-radius: 12px; border: 1px solid rgba(255,255,255,0.1);">
<h4 style="color: #F5F3EF; margin-bottom: 1rem; font-size: 1rem;">📬 Contact &amp; Volg Ons</h4>
<p style="color: #D4C7B4; font-size: 0.9rem; margin-bottom: 1rem;">
                        Vragen over een kasteel? Suggesties? We horen graag van je!
                    </p>
<div style="display: flex; gap: 0.75rem; margin-bottom: 1rem;">
<a aria-label="E-mail" href="mailto:info@kastelenbelgie.be" style="width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; background: rgba(255,255,255,0.1); border-radius: 50%; color: #F5F3EF; text-decoration: none;">📧</a>
<a aria-label="Instagram" href="https://www.instagram.com/kastelenbelgie" style="width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; background: rgba(255,255,255,0.1); border-radius: 50%; color: #F5F3EF; text-decoration: none;">📷</a>
<a aria-label="Facebook" href="https://www.facebook.com/kastelenbelgie" style="width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; background: rgba(255,255,255,0.1); border-radius: 50%; color: #F5F3EF; text-decoration: none;">f</a>
</div>
<a href="contact.html" style="color: #C89A3B; font-size: 0.9rem; text-decoration: none;">→ Contactformulier</a>
</div>
</div>
<div class="footer-grid" style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 2rem; padding: 2.5rem 0; border-bottom: 1px solid rgba(255,255,255,0.1);">
<div>
<h4 style="color: #F5F3EF; margin-bottom: 1.2rem; font-size: 0.9rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;">Kastelen Vlaanderen</h4>
<ul style="list-style: none; padding: 0; margin: 0;">
<li style="margin-bottom: 0.6rem;"><a href="antwerpen.html" style="color: #D4C7B4; text-decoration: none; font-size: 0.9rem;">Kastelen in Antwerpen</a></li>
<li style="margin-bottom: 0.6rem;"><a href="vlaams-brabant.html" style="color: #D4C7B4; text-decoration: none; font-size: 0.9rem;">Kastelen in Vlaams-Brabant</a></li>
<li style="margin-bottom: 0.6rem;"><a href="oost-vlaanderen.html" style="color: #D4C7B4; text-decoration: none; font-size: 0.9rem;">Kastelen in Oost-Vlaanderen</a></li>
<li style="margin-bottom: 0.6rem;"><a href="west-vlaanderen.html" style="color: #D4C7B4; text-decoration: none; font-size: 0.9rem;">Kastelen in West-Vlaanderen</a></li>
<li style="margin-bottom: 0.6rem;"><a href="limburg.html" style="color: #D4C7B4; text-decoration: none; font-size: 0.9rem;">Kastelen in Limburg</a></li>
<li style="margin-bottom: 0.6rem;"><a href="provinces.html" style="color: #C89A3B; font-weight: 600; text-decoration: none; font-size: 0.9rem;">→ Alle provincies</a></li>
</ul>
</div>
<div>
<h4 style="color: #F5F3EF; margin-bottom: 1.2rem; font-size: 0.9rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;">Kastelen Wallonië</h4>
<ul style="list-style: none; padding: 0; margin: 0;">
<li style="margin-bottom: 0.6rem;"><a href="namen.html" style="color: #D4C7B4; text-decoration: none; font-size: 0.9rem;">Kastelen in Namen</a></li>
<li style="margin-bottom: 0.6rem;"><a href="luik.html" style="color: #D4C7B4; text-decoration: none; font-size: 0.9rem;">Kastelen in Luik</a></li>
<li style="margin-bottom: 0.6rem;"><a href="henegouwen.html" style="color: #D4C7B4; text-decoration: none; font-size: 0.9rem;">Kastelen in Henegouwen</a></li>
<li style="margin-bottom: 0.6rem;"><a href="luxemburg.html" style="color: #D4C7B4; text-decoration: none; font-size: 0.9rem;">Kastelen in Luxemburg</a></li>
<li style="margin-bottom: 0.6rem;"><a href="waals-brabant.html" style="color: #D4C7B4; text-decoration: none; font-size: 0.9rem;">Kastelen in Waals-Brabant</a></li>
<li style="margin-bottom: 0.6rem;"><a href="brussel.html" style="color: #D4C7B4; text-decoration: none; font-size: 0.9rem;">Kastelen in Brussel</a></li>
</ul>
</div>
<div>
<h4 style="color: #F5F3EF; margin-bottom: 1.2rem; font-size: 0.9rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;">Populaire Kastelen</h4>
<ul style="list-style: none; padding: 0; margin: 0;">
<li style="margin-bottom: 0.6rem;"><a href="kasteel-van-freyr-freyr.html" style="color: #D4C7B4; text-decoration: none; font-size: 0.9rem;">Kasteel van Freÿr</a></li>
<li style="margin-bottom: 0.6rem;"><a href="citadel-van-hoei-hoei.html" style="color: #D4C7B4; text-decoration: none; font-size: 0.9rem;">Citadel van Hoei</a></li>
<li style="margin-bottom: 0.6rem;"><a href="kasteel-de-merode-westerlo.html" style="color: #D4C7B4; text-decoration: none; font-size: 0.9rem;">Kasteel de Merode</a></li>
<li style="margin-bottom: 0.6rem;"><a href="kasteel-van-durbuy-durbuy.html" style="color: #D4C7B4; text-decoration: none; font-size: 0.9rem;">Kasteel van Durbuy</a></li>
<li style="margin-bottom: 0.6rem;"><a href="kasteel-van-bouchout-te-meise.html" style="color: #D4C7B4; text-decoration: none; font-size: 0.9rem;">Kasteel van Bouchout</a></li>
<li style="margin-bottom: 0.6rem;"><a href="kasteel-reinhardstein-burg-metternich-te-weismes.html" style="color: #D4C7B4; text-decoration: none; font-size: 0.9rem;">Kasteel Reinhardstein</a></li>
</ul>
</div>
<div>
<h4 style="color: #F5F3EF; margin-bottom: 1.2rem; font-size: 0.9rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;">Blog &amp; Informatie</h4>
<ul style="list-style: none; padding: 0; margin: 0;">
<li style="margin-bottom: 0.6rem;"><a href="blog.html" style="color: #D4C7B4; text-decoration: none; font-size: 0.9rem;">📖 Blog</a></li>
<li style="margin-bottom: 0.6rem;"><a href="alle-kastelen.html" style="color: #D4C7B4; text-decoration: none; font-size: 0.9rem;">🔤 Alle kastelen A–Z</a></li>
<li style="margin-bottom: 0.6rem;"><a href="blog-mooiste-kastelen-belgie.html" style="color: #D4C7B4; text-decoration: none; font-size: 0.9rem;">Mooiste kastelen van België</a></li>
<li style="margin-bottom: 0.6rem;"><a href="contact.html" style="color: #D4C7B4; text-decoration: none; font-size: 0.9rem;">💬 Contact</a></li>
<li style="margin-bottom: 0.6rem;"><a href="privacybeleid.html" style="color: #D4C7B4; text-decoration: none; font-size: 0.9rem;">Privacybeleid</a></li>
<li style="margin-bottom: 0.6rem;"><a href="algemene-voorwaarden.html" style="color: #D4C7B4; text-decoration: none; font-size: 0.9rem;">Algemene voorwaarden</a></li>
</ul>
</div>
</div>
<div class="footer-bottom" style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; padding: 2rem 0;">
<div>
<p style="color: #D4C7B4; font-size: 0.85rem; line-height: 1.6; margin: 0;">
<strong style="color: #F5F3EF;">© 2024 Kastelen België.</strong> Alle rechten voorbehouden.
                        <br/><br/>
<span style="color: #8A857D;">Op Kastelenbelgie.be vind je meer dan 300 kastelen in België, 
                        netjes gebundeld per provincie met praktische informatie en tips.</span>
</p>
</div>
<div style="text-align: right;">
<p style="color: #8A857D; font-size: 0.85rem; margin: 0 0 0.5rem 0;">
                        Gemaakt met ❤️ voor het Belgische erfgoed
                    </p>
<a href="#" style="color: #C89A3B; text-decoration: none; font-size: 0.85rem;">Terug naar boven ↑</a>
</div>
</div>
</div>
</footer>
<script src="js/search.js"></script>
</body>
</html>
'''
    return html

if __name__ == '__main__':
    generate_annuaire()
