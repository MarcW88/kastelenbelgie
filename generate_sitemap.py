#!/usr/bin/env python3
"""
Script pour générer le sitemap.xml du site kastelenbelgie.be
"""

import os
from pathlib import Path
from datetime import datetime

BASE_URL = "https://kastelenbelgie.be"
DIRECTORY = "/Users/marc/Desktop/kastelenbelgie"
OUTPUT_FILE = os.path.join(DIRECTORY, "sitemap.xml")

# Fichiers à exclure du sitemap
EXCLUDE_FILES = [
    "test-modern-design.html",
    "kasteel-van-dieupart-aywaille-old.html",
    "kasteel-van-freyr-freyr-backup.html",
]

def get_priority(filename):
    """Détermine la priorité d'une page."""
    if filename == "index.html":
        return "1.0"
    elif filename == "provinces.html":
        return "0.9"
    elif filename == "alle-kastelen.html":
        return "0.9"
    elif filename in ["antwerpen.html", "oost-vlaanderen.html", "west-vlaanderen.html", 
                      "vlaams-brabant.html", "limburg.html", "luik.html", "namen.html",
                      "luxemburg.html", "henegouwen.html", "waals-brabant.html", "brussel.html"]:
        return "0.8"
    elif filename == "blog.html":
        return "0.7"
    elif filename == "contact.html":
        return "0.5"
    elif filename == "privacybeleid.html":
        return "0.3"
    else:
        return "0.6"  # Pages de châteaux

def get_changefreq(filename):
    """Détermine la fréquence de mise à jour."""
    if filename == "index.html":
        return "weekly"
    elif filename in ["provinces.html", "alle-kastelen.html"]:
        return "weekly"
    elif filename == "blog.html":
        return "weekly"
    else:
        return "monthly"

def generate_sitemap():
    """Génère le fichier sitemap.xml."""
    
    html_files = list(Path(DIRECTORY).glob("*.html"))
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Filtrer les fichiers exclus
    html_files = [f for f in html_files if f.name not in EXCLUDE_FILES]
    
    # Trier: index en premier, puis provinces, puis alphabétique
    def sort_key(f):
        name = f.name
        if name == "index.html":
            return (0, name)
        elif name == "provinces.html":
            return (1, name)
        elif name == "alle-kastelen.html":
            return (2, name)
        else:
            return (3, name)
    
    html_files = sorted(html_files, key=sort_key)
    
    # Générer le XML
    xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    for filepath in html_files:
        filename = filepath.name
        url = f"{BASE_URL}/{filename}"
        priority = get_priority(filename)
        changefreq = get_changefreq(filename)
        
        xml_content += f"""  <url>
    <loc>{url}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>{changefreq}</changefreq>
    <priority>{priority}</priority>
  </url>
"""
    
    xml_content += '</urlset>\n'
    
    # Écrire le fichier
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(xml_content)
    
    print(f"✅ Sitemap généré: {OUTPUT_FILE}")
    print(f"📄 {len(html_files)} URLs incluses")

if __name__ == "__main__":
    generate_sitemap()
