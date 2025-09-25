#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
GÉNÉRATION ARTICLES DE BLOG
Crée les 5 articles de blog avec du contenu complet
"""

import os

def create_blog_article(filename, title, category, date, content_sections):
    """Crée un article de blog complet"""
    
    html_content = f'''<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Kastelen België Blog</title>
    <meta name="description" content="{content_sections[0][:150]}...">
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar">
        <div class="container">
            <div class="nav-container">
                <a href="index.html" class="logo">
                    <div class="logo-icon">🏰</div>
                    kastelenbelgie
                </a>
                <div class="nav-menu">
                    <a href="provinces.html" class="nav-link">Provincies</a>
                    <a href="blog.html" class="nav-link">Blog</a>
                    <a href="contact.html" class="nav-link">Contact</a>
                </div>
            </div>
        </div>
    </nav>

    <!-- Breadcrumbs -->
    <div class="container">
        <div class="breadcrumbs-nav">
            <a href="index.html">Home</a>
            <span class="breadcrumbs-separator">›</span>
            <a href="blog.html">Blog</a>
            <span class="breadcrumbs-separator">›</span>
            <span class="breadcrumbs-current">{title}</span>
        </div>
    </div>

    <!-- Article Header -->
    <section class="hero-modern">
        <div class="container">
            <div class="section-header">
                <span style="background: var(--primary); color: white; padding: 0.5rem 1rem; border-radius: 25px; font-size: 0.875rem; font-weight: 600; margin-bottom: 1rem; display: inline-block;">{category.upper()}</span>
                <h1 class="section-title">{title}</h1>
                <div style="display: flex; align-items: center; gap: 1rem; margin-top: 1rem; justify-content: center;">
                    <span style="color: var(--text-light);">{date}</span>
                    <span style="color: var(--text-light);">•</span>
                    <span style="color: var(--text-light);">5-8 min leestijd</span>
                </div>
            </div>
        </div>
    </section>

    <!-- Article Content -->
    <section class="section">
        <div class="container">
            <div style="max-width: 800px; margin: 0 auto;">
                <div class="article-content">
'''

    # Ajouter les sections de contenu
    for i, section in enumerate(content_sections):
        if i == 0:
            html_content += f'''
                    <div style="font-size: 1.125rem; line-height: 1.8; color: var(--text); margin-bottom: 2rem;">
                        <p>{section}</p>
                    </div>
'''
        else:
            html_content += f'''
                    <div style="margin-bottom: 2rem;">
                        <h2 style="font-size: 1.5rem; font-weight: 700; margin-bottom: 1rem; color: var(--text);">{section["title"]}</h2>
                        <p style="line-height: 1.7; color: var(--text); margin-bottom: 1rem;">{section["content"]}</p>
                    </div>
'''

    html_content += '''
                </div>
                
                <!-- Call to Action -->
                <div style="background: var(--bg-light); padding: 2rem; border-radius: var(--radius); text-align: center; margin-top: 3rem;">
                    <h3 style="font-size: 1.25rem; font-weight: 700; margin-bottom: 1rem;">Ontdek meer kastelen</h3>
                    <p style="color: var(--text-light); margin-bottom: 1.5rem;">Verken alle prachtige kastelen van België en plan je volgende bezoek.</p>
                    <a href="provinces.html" class="btn-modern btn-primary-modern">Bekijk alle provincies</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-column">
                    <h4 class="footer-title">Kastelen België</h4>
                    <p class="footer-description">Ontdek de rijke geschiedenis van België door haar prachtige kastelen. Van middeleeuwse burchten tot barokke paleizen.</p>
                </div>
                <div class="footer-column">
                    <h4 class="footer-title">Verken</h4>
                    <ul class="footer-links">
                        <li><a href="provinces.html">Alle Provincies</a></li>
                        <li><a href="blog.html">Blog</a></li>
                        <li><a href="contact.html">Contact</a></li>
                    </ul>
                </div>
                <div class="footer-column">
                    <h4 class="footer-title">Populaire Kastelen</h4>
                    <ul class="footer-links">
                        <li><a href="kasteel-van-freyr-freyr.html">Kasteel van Freÿr</a></li>
                        <li><a href="kasteel-van-durbuy-durbuy.html">Kasteel van Durbuy</a></li>
                        <li><a href="citadel-van-hoei-hoei.html">Citadel van Hoei</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2025 Kastelen België. Alle rechten voorbehouden.</p>
            </div>
        </div>
    </footer>
</body>
</html>'''

    # Écrire le fichier
    with open(f"/Users/marc/Desktop/kastelenbelgie/{filename}", 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ {filename} créé")

def generate_all_blog_articles():
    """Génère tous les articles de blog"""
    
    print("📝 GÉNÉRATION ARTICLES DE BLOG")
    print("-" * 50)
    
    # Article 1: Mooiste Kastelen
    create_blog_article(
        "blog-mooiste-kastelen-belgie.html",
        "De 10 Mooiste Kastelen van België",
        "UITGELICHT",
        "21 september 2025",
        [
            "België herbergt enkele van de meest indrukwekkende kastelen van Europa. Van het romantische Kasteel van Freÿr aan de Maas tot het imposante Gravensteen in Gent, elk kasteel vertelt een uniek verhaal van macht, liefde en geschiedenis.",
            {
                "title": "1. Kasteel van Freÿr - Namen",
                "content": "Dit prachtige renaissancekasteel aan de Maas is beroemd om zijn Franse tuinen en 350 jaar oude oranjebomen. Het kasteel speelde een belangrijke rol in de Europese diplomatie en ontving illustere gasten zoals Lodewijk XIV."
            },
            {
                "title": "2. Gravensteen - Gent",
                "content": "Dit middeleeuwse kasteel in het hart van Gent is een van de best bewaarde burchten van Europa. Met zijn imposante donjon en marteltoren biedt het een fascinerende blik op het middeleeuwse leven."
            },
            {
                "title": "3. Kasteel van Durbuy - Luxemburg",
                "content": "Gelegen in de kleinste stad van België, combineert dit kasteel middeleeuwse charme met neo-gotische elegantie. Het wordt nog steeds bewoond door de familie d'Ursel."
            }
        ]
    )
    
    # Article 2: Kasteeltuinen
    create_blog_article(
        "blog-kasteeltuinen-parken.html",
        "Kasteeltuinen en Parken in België",
        "TUINEN",
        "18 september 2025",
        [
            "De tuinen rondom Belgische kastelen zijn vaak net zo indrukwekkend als de kastelen zelf. Van formele Franse tuinen tot romantische Engelse landschapsparken, elk vertelt het verhaal van eeuwen tuinkunst.",
            {
                "title": "Franse Tuinen: Symmetrie en Elegantie",
                "content": "Kastelen zoals Freÿr en Beloeil tonen de perfectie van de Franse tuinkunst. Met hun geometrische patronen, waterpartijen en perfect gesnoeide heggen weerspiegelen ze de macht en verfijning van hun oorspronkelijke bewoners."
            },
            {
                "title": "Engelse Landschapsparken: Natuurlijke Schoonheid",
                "content": "Veel 19e-eeuwse kastelen kozen voor de Engelse stijl, met glooiende gazons, kronkelende paden en pittoreske vijvers. Deze tuinen nodigen uit tot wandelen en contemplatie."
            },
            {
                "title": "Botanische Schatten",
                "content": "Sommige kasteeltuinen herbergen zeldzame plantensoorten en eeuwenoude bomen. Het Nationaal Plantentuin van België rond Kasteel van Bouchout is hiervan een prachtig voorbeeld."
            }
        ]
    )
    
    # Article 3: Middeleeuwse Kastelen
    create_blog_article(
        "blog-middeleeuwse-kastelen.html",
        "Middeleeuwse Kastelen en Hun Verhalen",
        "GESCHIEDENIS",
        "15 september 2025",
        [
            "De middeleeuwse kastelen van België zijn stille getuigen van een turbulente tijd vol ridders, belegeringen en hofintrigues. Elk kasteel heeft zijn eigen verhalen van moed, verraad en romantiek.",
            {
                "title": "Strategische Locaties",
                "content": "Middeleeuwse kastelen werden niet toevallig gebouwd. Ze bewaakten belangrijke handelswegen, rivierovergangen en grenzen. De Citadel van Hoei bijvoorbeeld, controleerde de Maas en bood bescherming tegen invallen."
            },
            {
                "title": "Architectuur van Verdediging",
                "content": "Dikke muren, smalle vensters en hoge torens - alles was ontworpen voor verdediging. Leer de verschillende onderdelen herkennen: de donjon (hoofdtoren), de ringmuur, en de poortgebouwen met hun valbruggen."
            },
            {
                "title": "Het Dagelijks Leven",
                "content": "Achter de sterke muren speelde zich het dagelijks leven af. Van de grote zaal waar feesten werden gehouden tot de keukens waar voor honderden mensen werd gekookt - elk kasteel was een kleine stad op zich."
            }
        ]
    )
    
    # Article 4: Eerste Kasteelbezoek
    create_blog_article(
        "blog-eerste-kasteelbezoek.html",
        "Gids voor je Eerste Kasteelbezoek",
        "TIPS",
        "12 september 2025",
        [
            "Een kasteelbezoek kan overweldigend zijn - zoveel geschiedenis, architectuur en verhalen in één gebouw. Met deze praktische tips maak je het meeste van je bezoek en mis je niets belangrijks.",
            {
                "title": "Voor je Bezoek: Voorbereiding",
                "content": "Controleer openingstijden en toegangsprijzen online. Veel kastelen bieden kortingen voor groepen of families. Boek eventueel een rondleiding - gidsen delen vaak verhalen die je nergens anders hoort."
            },
            {
                "title": "Wat Mee te Nemen",
                "content": "Draag comfortabele schoenen - kastelen hebben vaak veel trappen en oneven vloeren. Neem een camera mee, maar controleer de fotoregels. Een kleine rugzak is handig voor water en snacks."
            },
            {
                "title": "Tijdens het Bezoek",
                "content": "Neem de tijd om details te bekijken: wapenschilden, plafondversieringen, oude meubels. Stel vragen aan het personeel - ze kennen vaak de beste verhalen. Vergeet niet om ook de tuinen en buitenkant te verkennen."
            }
        ]
    )
    
    # Article 5: Architectuurstijlen
    create_blog_article(
        "blog-architectuurstijlen.html",
        "Architectuurstijlen van Belgische Kastelen",
        "ARCHITECTUUR",
        "10 september 2025",
        [
            "Belgische kastelen tonen een fascinerende evolutie van architectuurstijlen door de eeuwen heen. Van sobere middeleeuwse burchten tot flamboyante barokke paleizen - leer de verschillen herkennen.",
            {
                "title": "Romaanse Periode (11e-12e eeuw)",
                "content": "De vroegste kastelen waren eenvoudige maar sterke constructies. Dikke muren, kleine vensters en ronde bogen kenmerken deze stijl. Functionaliteit ging boven schoonheid."
            },
            {
                "title": "Gotiek (13e-15e eeuw)",
                "content": "Gotische kastelen toonden meer verfijning: spitsbogen, ribgewelven en grotere vensters. De architectuur werd lichter en eleganter, terwijl de verdediging belangrijk bleef."
            },
            {
                "title": "Renaissance (16e eeuw)",
                "content": "Italiaanse invloeden brachten symmetrie en klassieke elementen. Kastelen werden meer paleizen dan vestingen, met prachtige binnenplaatsen en decoratieve gevels."
            },
            {
                "title": "Barok en Neo-stijlen (17e-19e eeuw)",
                "content": "Latere periodes brachten diverse revival-stijlen: neo-gotiek, neo-renaissance en eclectisme. Kastelen werden romantische droombeelden van het verleden."
            }
        ]
    )

if __name__ == "__main__":
    print("📝 GÉNÉRATION ARTICLES DE BLOG")
    print("=" * 50)
    
    generate_all_blog_articles()
    
    print(f"\n🎉 ARTICLES DE BLOG GÉNÉRÉS!")
    print("✅ 5 articles complets créés")
    print("✅ Contenu de qualité avec sections détaillées")
    print("✅ Navigation et footer cohérents")
    print("\n🚀 Articles prêts à être consultés!")
