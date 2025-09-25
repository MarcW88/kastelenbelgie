#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CRÉATION DES PAGES PROVINCES
Génère toutes les pages provinces avec leurs châteaux
"""

import os

# Template pour la page provinces principale
PROVINCES_PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kastelen per Provincie | kastelenbelgie.be</title>
    <meta name="description" content="Ontdek kastelen per provincie in België. Van Antwerpen tot Luxemburg, elk provincie heeft zijn eigen unieke kastelen en geschiedenis.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/modern-style.css">
    <link rel="icon" type="image/svg+xml" href="favicon.svg">
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar">
        <div class="container">
            <div class="nav-container">
                <a href="index.html" class="logo">kastelenbelgie</a>
                <div class="nav-menu">
                    <a href="provinces.html" class="nav-link">Kastelen</a>
                    <a href="blog.html" class="nav-link">Blog</a>
                    <a href="contact.html" class="nav-link">Contact</a>
                    <div class="search-box">
                        <input type="text" placeholder="Zoek kasteel..." class="search-input">
                    </div>
                </div>
            </div>
        </div>
    </nav>

    <!-- Hero -->
    <section class="hero">
        <div class="container">
            <div class="section-header">
                <h1 class="section-title">Kastelen per Provincie</h1>
                <p class="section-subtitle">Ontdek de rijke geschiedenis van België door haar prachtige kastelen, georganiseerd per provincie</p>
            </div>
        </div>
    </section>

    <!-- Provincies Grid -->
    <section class="section">
        <div class="container">
            <div class="cards-grid">
                <a href="antwerpen.html" class="province-card">
                    <div class="province-header">
                        <h3 class="province-title">Antwerpen</h3>
                        <span class="province-count">45+ kastelen</span>
                    </div>
                    <p class="province-description">Van het Steen in Antwerpen tot de kastelen in de Kempen. Ontdek de rijke geschiedenis van de diamantprovincie.</p>
                    <span class="province-link">Bekijk kastelen →</span>
                </a>

                <a href="limburg.html" class="province-card">
                    <div class="province-header">
                        <h3 class="province-title">Limburg</h3>
                        <span class="province-count">25+ kastelen</span>
                    </div>
                    <p class="province-description">Waterkastelen en historische sites in de groene provincie. Van Alden Biesen tot kleinere pareltjes.</p>
                    <span class="province-link">Bekijk kastelen →</span>
                </a>

                <a href="oost-vlaanderen.html" class="province-card">
                    <div class="province-header">
                        <h3 class="province-title">Oost-Vlaanderen</h3>
                        <span class="province-count">35+ kastelen</span>
                    </div>
                    <p class="province-description">Van het Gravensteen in Gent tot verborgen kastelen in het Vlaamse landschap.</p>
                    <span class="province-link">Bekijk kastelen →</span>
                </a>

                <a href="west-vlaanderen.html" class="province-card">
                    <div class="province-header">
                        <h3 class="province-title">West-Vlaanderen</h3>
                        <span class="province-count">30+ kastelen</span>
                    </div>
                    <p class="province-description">Kastelen aan de kust en in het binnenland, van Brugge tot de Westhoek.</p>
                    <span class="province-link">Bekijk kastelen →</span>
                </a>

                <a href="vlaams-brabant.html" class="province-card">
                    <div class="province-header">
                        <h3 class="province-title">Vlaams-Brabant</h3>
                        <span class="province-count">20+ kastelen</span>
                    </div>
                    <p class="province-description">Kastelen rond Leuven en in het Pajottenland, rijk aan geschiedenis en cultuur.</p>
                    <span class="province-link">Bekijk kastelen →</span>
                </a>

                <a href="brussel.html" class="province-card">
                    <div class="province-header">
                        <h3 class="province-title">Brussels Hoofdstedelijk Gewest</h3>
                        <span class="province-count">10+ kastelen</span>
                    </div>
                    <p class="province-description">Historische sites en kastelen in en rond de hoofdstad van Europa.</p>
                    <span class="province-link">Bekijk kastelen →</span>
                </a>

                <a href="waals-brabant.html" class="province-card">
                    <div class="province-header">
                        <h3 class="province-title">Waals-Brabant</h3>
                        <span class="province-count">15+ kastelen</span>
                    </div>
                    <p class="province-description">Kastelen in het Waalse Brabant, van Waterloo tot Nivelles.</p>
                    <span class="province-link">Bekijk kastelen →</span>
                </a>

                <a href="henegouwen.html" class="province-card">
                    <div class="province-header">
                        <h3 class="province-title">Henegouwen</h3>
                        <span class="province-count">40+ kastelen</span>
                    </div>
                    <p class="province-description">Van Doornik tot Bergen, ontdek de kastelen van deze historische provincie.</p>
                    <span class="province-link">Bekijk kastelen →</span>
                </a>

                <a href="namen.html" class="province-card">
                    <div class="province-header">
                        <h3 class="province-title">Namen</h3>
                        <span class="province-count">50+ kastelen</span>
                    </div>
                    <p class="province-description">Majestueuze kastelen langs de Maas en in de Ardennen, vol geschiedenis en natuurschoon.</p>
                    <span class="province-link">Bekijk kastelen →</span>
                </a>

                <a href="luik.html" class="province-card">
                    <div class="province-header">
                        <h3 class="province-title">Luik</h3>
                        <span class="province-count">60+ kastelen</span>
                    </div>
                    <p class="province-description">Van de Citadel van Luik tot kastelen in de Ardennen, een rijke geschiedenis in steen.</p>
                    <span class="province-link">Bekijk kastelen →</span>
                </a>

                <a href="luxemburg.html" class="province-card">
                    <div class="province-header">
                        <h3 class="province-title">Luxemburg</h3>
                        <span class="province-count">35+ kastelen</span>
                    </div>
                    <p class="province-description">Kastelen in de Belgische Ardennen, omgeven door prachtige natuur en geschiedenis.</p>
                    <span class="province-link">Bekijk kastelen →</span>
                </a>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h4>Kastelen</h4>
                    <ul>
                        <li><a href="provinces.html">Alle kastelen</a></li>
                        <li><a href="antwerpen.html">Antwerpen</a></li>
                        <li><a href="limburg.html">Limburg</a></li>
                        <li><a href="oost-vlaanderen.html">Oost-Vlaanderen</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4>Informatie</h4>
                    <ul>
                        <li><a href="blog.html">Blog</a></li>
                        <li><a href="contact.html">Contact</a></li>
                        <li><a href="algemene-voorwaarden.html">Algemene voorwaarden</a></li>
                        <li><a href="privacybeleid.html">Privacybeleid</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4>kastelenbelgie.be</h4>
                    <p>Ontdek de mooiste kastelen van België en beleef eeuwenoude geschiedenis.</p>
                </div>
            </div>
            <div class="footer-bottom">
                <p>© 2025 kastelenbelgie.be. Alle rechten voorbehouden.</p>
            </div>
        </div>
    </footer>
</body>
</html>"""

# Template voor individuele provincie pagina's
PROVINCE_PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kastelen in {province_name} | kastelenbelgie.be</title>
    <meta name="description" content="Ontdek de mooiste kastelen in {province_name}. Van historische burchten tot moderne landgoederen, elk kasteel heeft zijn eigen verhaal.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/modern-style.css">
    <link rel="icon" type="image/svg+xml" href="favicon.svg">
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar">
        <div class="container">
            <div class="nav-container">
                <a href="index.html" class="logo">kastelenbelgie</a>
                <div class="nav-menu">
                    <a href="provinces.html" class="nav-link">Kastelen</a>
                    <a href="blog.html" class="nav-link">Blog</a>
                    <a href="contact.html" class="nav-link">Contact</a>
                    <div class="search-box">
                        <input type="text" placeholder="Zoek kasteel..." class="search-input">
                    </div>
                </div>
            </div>
        </div>
    </nav>

    <!-- Breadcrumbs -->
    <div style="background: var(--bg-light); padding: 1rem 0; border-bottom: 1px solid var(--border);">
        <div class="container">
            <nav style="font-size: 0.875rem; color: var(--text-light);">
                <a href="index.html" style="color: var(--text-light); text-decoration: none;">Home</a>
                <span style="margin: 0 0.5rem;">›</span>
                <a href="provinces.html" style="color: var(--text-light); text-decoration: none;">Provincies</a>
                <span style="margin: 0 0.5rem;">›</span>
                <span style="color: var(--text);">{province_name}</span>
            </nav>
        </div>
    </div>

    <!-- Hero -->
    <section class="hero">
        <div class="container">
            <div class="section-header">
                <h1 class="section-title">Kastelen in {province_name}</h1>
                <p class="section-subtitle">{province_description}</p>
            </div>
        </div>
    </section>

    <!-- Kastelen Grid -->
    <section class="section">
        <div class="container">
            <div class="cards-grid">
                {castles_content}
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h4>Kastelen</h4>
                    <ul>
                        <li><a href="provinces.html">Alle kastelen</a></li>
                        <li><a href="antwerpen.html">Antwerpen</a></li>
                        <li><a href="limburg.html">Limburg</a></li>
                        <li><a href="oost-vlaanderen.html">Oost-Vlaanderen</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4>Informatie</h4>
                    <ul>
                        <li><a href="blog.html">Blog</a></li>
                        <li><a href="contact.html">Contact</a></li>
                        <li><a href="algemene-voorwaarden.html">Algemene voorwaarden</a></li>
                        <li><a href="privacybeleid.html">Privacybeleid</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4>kastelenbelgie.be</h4>
                    <p>Ontdek de mooiste kastelen van België en beleef eeuwenoude geschiedenis.</p>
                </div>
            </div>
            <div class="footer-bottom">
                <p>© 2025 kastelenbelgie.be. Alle rechten voorbehouden.</p>
            </div>
        </div>
    </footer>
</body>
</html>"""

def create_provinces_main_page():
    """Creëer de hoofdpagina voor provincies"""
    filename = "/Users/marc/Desktop/kastelenbelgie/provinces.html"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(PROVINCES_PAGE_TEMPLATE)
    print("✅ Hoofdpagina provinces.html aangemaakt")
    return filename

def create_province_page(province_data):
    """Creëer een individuele provincie pagina"""
    province_name = province_data['name']
    province_slug = province_data['slug']
    
    print(f"🏛️  Creëren pagina voor provincie: {province_name}")
    
    # Kastelen content (placeholder voor nu)
    castles_content = f"""
                <div class="card">
                    <div class="card-content">
                        <h3 class="card-title">Kastelen in {province_name}</h3>
                        <p class="card-description">De kastelen van {province_name} worden binnenkort toegevoegd. Kom snel terug voor een complete lijst!</p>
                    </div>
                </div>
                
                <div class="card">
                    <div class="card-content">
                        <h3 class="card-title">Historische sites</h3>
                        <p class="card-description">Naast kastelen vind je in {province_name} ook vele andere historische bezienswaardigheden.</p>
                    </div>
                </div>
                
                <div class="card">
                    <div class="card-content">
                        <h3 class="card-title">Cultuur & Erfgoed</h3>
                        <p class="card-description">Ontdek de rijke culturele geschiedenis van {province_name} door haar monumenten en musea.</p>
                    </div>
                </div>"""
    
    # Provincie beschrijvingen
    descriptions = {
        'Antwerpen': 'Ontdek de kastelen van de diamantprovincie, van het historische Steen tot de prachtige landgoederen in de Kempen.',
        'Limburg': 'Verken de waterkastelen en historische sites van de groene provincie Limburg.',
        'Oost-Vlaanderen': 'Van het Gravensteen in Gent tot verborgen pareltjes in het Vlaamse landschap.',
        'West-Vlaanderen': 'Kastelen aan de kust en in het binnenland, elk met hun eigen unieke geschiedenis.',
        'Vlaams-Brabant': 'Kastelen rond Leuven en in het Pajottenland, rijk aan geschiedenis en cultuur.',
        'Brussels Hoofdstedelijk Gewest': 'Historische sites en kastelen in en rond de hoofdstad van Europa.',
        'Waals-Brabant': 'Kastelen in het Waalse Brabant, van Waterloo tot Nivelles.',
        'Henegouwen': 'Van Doornik tot Bergen, ontdek de kastelen van deze historische provincie.',
        'Namen': 'Majestueuze kastelen langs de Maas en in de Ardennen, vol geschiedenis en natuurschoon.',
        'Luik': 'Van de Citadel van Luik tot kastelen in de Ardennen, een rijke geschiedenis in steen.',
        'Luxemburg': 'Kastelen in de Belgische Ardennen, omgeven door prachtige natuur en geschiedenis.'
    }
    
    province_description = descriptions.get(province_name, f'Ontdek de prachtige kastelen van {province_name}.')
    
    # Vul template in
    html_content = PROVINCE_PAGE_TEMPLATE.format(
        province_name=province_name,
        province_description=province_description,
        castles_content=castles_content
    )
    
    # Schrijf bestand
    filename = f"/Users/marc/Desktop/kastelenbelgie/{province_slug}.html"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"  ✅ Pagina aangemaakt: {province_slug}.html")
    return filename

def main():
    """Hoofdfunctie"""
    print("🏛️  CREËREN PROVINCIE PAGINAS")
    print("=" * 50)
    
    # Creëer hoofdpagina
    create_provinces_main_page()
    
    # Provincie data
    provinces = [
        {'name': 'Antwerpen', 'slug': 'antwerpen'},
        {'name': 'Limburg', 'slug': 'limburg'},
        {'name': 'Oost-Vlaanderen', 'slug': 'oost-vlaanderen'},
        {'name': 'West-Vlaanderen', 'slug': 'west-vlaanderen'},
        {'name': 'Vlaams-Brabant', 'slug': 'vlaams-brabant'},
        {'name': 'Brussels Hoofdstedelijk Gewest', 'slug': 'brussel'},
        {'name': 'Waals-Brabant', 'slug': 'waals-brabant'},
        {'name': 'Henegouwen', 'slug': 'henegouwen'},
        {'name': 'Namen', 'slug': 'namen'},
        {'name': 'Luik', 'slug': 'luik'},
        {'name': 'Luxemburg', 'slug': 'luxemburg'}
    ]
    
    created_pages = []
    
    # Creëer individuele provincie pagina's
    for province in provinces:
        try:
            filename = create_province_page(province)
            created_pages.append(filename)
        except Exception as e:
            print(f"❌ Fout bij {province['name']}: {e}")
    
    print(f"\n✅ {len(created_pages) + 1} provincie paginas aangemaakt!")
    print("🎯 Provincie structuur compleet")

if __name__ == "__main__":
    main()
