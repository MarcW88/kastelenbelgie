#!/usr/bin/env python3
"""
Script pour ajouter des données structurées Schema.org aux pages villes/châteaux Luxembourg
- Place (City)
- TouristDestination
- LandmarksOrHistoricalBuildings (château)
- BreadcrumbList
"""

import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent
BASE_URL = "https://kastelenbelgie.be"

CITY_PAGES = {
    "kasteel-van-durbuy-durbuy.html": {
        "city": "Durbuy",
        "city_description": "Durbuy, de kleinste stad van België, ligt in de provincie Luxemburg aan de oevers van de Ourthe.",
        "castle_name": "Kasteel van Durbuy",
        "castle_description": "Neogotisch privékasteel van de familie d'Ursel, dat uittorent boven de Ourthe en de oude stad Durbuy.",
        "geo": {"lat": "50.3528", "lon": "5.4567"},
        "province": "Luxemburg"
    },
    "kasteel-van-deulin-deulin-fronville.html": {
        "city": "Deulin",
        "city_description": "Deulin is een dorpje in de gemeente Hotton, gelegen in de vallei van de Ourthe in de provincie Luxemburg.",
        "castle_name": "Kasteel van Deulin",
        "castle_description": "18de-eeuws familiekasteel in Deulin bij Hotton, bekend om zijn kunst- en antiekbeurzen en brocantes.",
        "geo": {"lat": "50.2833", "lon": "5.4500"},
        "province": "Luxemburg"
    },
    "kasteel-van-mirwart-mirwart-saint-hubert.html": {
        "city": "Mirwart",
        "city_description": "Mirwart is een dorp in de gemeente Saint-Hubert, midden in het provinciaal Domein van Mirwart in de Ardennen.",
        "castle_name": "Kasteel van Mirwart",
        "castle_description": "Historisch kasteel op een rots boven het dorp Mirwart, nu een kasteelhotel in het hart van de Ardennen.",
        "geo": {"lat": "50.0167", "lon": "5.2833"},
        "province": "Luxemburg"
    },
    "kasteel-van-longchamps-longchamps-bertogne.html": {
        "city": "Longchamps",
        "city_description": "Longchamps is een gehucht in de gemeente Bertogne, tussen Bastogne en La Roche-en-Ardenne in de Ardennen.",
        "castle_name": "Kasteel van Longchamps",
        "castle_description": "Kasteeldomein met park en vijvers in Longchamps, verhuurd als vakantieverblijf in de Ardennen.",
        "geo": {"lat": "50.0833", "lon": "5.6667"},
        "province": "Luxemburg"
    },
    "kasteel-van-porcheresse-daverdisse.html": {
        "city": "Porcheresse",
        "city_description": "Porcheresse is een dorp in de gemeente Daverdisse, in een rustige en groene omgeving van de Ardennen.",
        "castle_name": "Kasteel van Porcheresse",
        "castle_description": "Kasteeldomein in Porcheresse dat functioneert als B&B en vakantieverblijf in de Ardense bossen.",
        "geo": {"lat": "50.0500", "lon": "5.1167"},
        "province": "Luxemburg"
    },
    "kasteel-van-orval-villers-devant-orval.html": {
        "city": "Villers-devant-Orval",
        "city_description": "Villers-devant-Orval is een dorp in de Gaume, bekend om de nabijgelegen Abdij van Orval.",
        "castle_name": "Kasteel van Orval",
        "castle_description": "Privékasteeldomein nabij de beroemde Abdij van Orval in de Gaume, niet toegankelijk voor bezoekers.",
        "geo": {"lat": "49.6333", "lon": "5.3500"},
        "province": "Luxemburg"
    }
}


def build_structured_data(page_key: str, page_data: dict) -> str:
    """Construit le JSON-LD pour une page ville/château"""
    
    structured_data = {
        "@context": "https://schema.org",
        "@graph": [
            # 1. Place (City)
            {
                "@type": "Place",
                "@id": f"{BASE_URL}/{page_key}#city",
                "name": page_data["city"],
                "description": page_data["city_description"],
                "address": {
                    "@type": "PostalAddress",
                    "addressLocality": page_data["city"],
                    "addressRegion": page_data["province"],
                    "addressCountry": "BE"
                },
                "geo": {
                    "@type": "GeoCoordinates",
                    "latitude": page_data["geo"]["lat"],
                    "longitude": page_data["geo"]["lon"]
                }
            },
            # 2. LandmarksOrHistoricalBuildings (château)
            {
                "@type": "LandmarksOrHistoricalBuildings",
                "@id": f"{BASE_URL}/{page_key}#castle",
                "name": page_data["castle_name"],
                "description": page_data["castle_description"],
                "url": f"{BASE_URL}/{page_key}",
                "containedInPlace": {
                    "@id": f"{BASE_URL}/{page_key}#city"
                },
                "geo": {
                    "@type": "GeoCoordinates",
                    "latitude": page_data["geo"]["lat"],
                    "longitude": page_data["geo"]["lon"]
                }
            },
            # 3. TouristDestination
            {
                "@type": "TouristDestination",
                "@id": f"{BASE_URL}/{page_key}#destination",
                "name": f"{page_data['castle_name']} - {page_data['city']}",
                "description": page_data["castle_description"],
                "touristType": [
                    "Cultuurliefhebbers",
                    "Geschiedenisliefhebbers",
                    "Families"
                ],
                "includesAttraction": {
                    "@id": f"{BASE_URL}/{page_key}#castle"
                }
            },
            # 4. WebPage
            {
                "@type": "WebPage",
                "@id": f"{BASE_URL}/{page_key}",
                "name": f"{page_data['castle_name']} | kastelenbelgie.be",
                "description": page_data["castle_description"],
                "url": f"{BASE_URL}/{page_key}",
                "isPartOf": {
                    "@type": "WebSite",
                    "name": "Kastelen België",
                    "url": BASE_URL
                },
                "about": {
                    "@id": f"{BASE_URL}/{page_key}#castle"
                }
            },
            # 5. BreadcrumbList
            {
                "@type": "BreadcrumbList",
                "@id": f"{BASE_URL}/{page_key}#breadcrumb",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": 1,
                        "name": "Home",
                        "item": BASE_URL
                    },
                    {
                        "@type": "ListItem",
                        "position": 2,
                        "name": page_data["province"],
                        "item": f"{BASE_URL}/{page_data['province'].lower()}.html"
                    },
                    {
                        "@type": "ListItem",
                        "position": 3,
                        "name": page_data["castle_name"]
                    }
                ]
            }
        ]
    }
    
    return json.dumps(structured_data, indent=2, ensure_ascii=False)


def add_structured_data_to_page(filepath: Path, structured_data: str) -> bool:
    """Ajoute ou remplace les données structurées dans une page HTML"""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Vérifier si des données structurées @graph existent déjà
    existing_pattern = r'<script type="application/ld\+json">\s*\{[^}]*"@graph"[^<]*</script>'
    
    script_tag = f'<script type="application/ld+json">\n{structured_data}\n</script>'
    
    if re.search(existing_pattern, content, re.DOTALL):
        # Remplacer les données existantes
        content = re.sub(existing_pattern, script_tag, content, flags=re.DOTALL)
        print(f"🔄 Mis à jour: {filepath.name}")
    else:
        # Ajouter avant </head>
        content = content.replace('</head>', f'{script_tag}\n</head>')
        print(f"✅ Ajouté: {filepath.name}")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    
    return True


def process_all_city_pages():
    """Traite toutes les pages villes/châteaux"""
    print("🏰 Ajout des données structurées aux pages villes Luxembourg...\n")
    
    for page_key, page_data in CITY_PAGES.items():
        filepath = BASE_DIR / page_key
        
        if not filepath.exists():
            print(f"⚠️  Page non trouvée: {page_key}")
            continue
        
        structured_data = build_structured_data(page_key, page_data)
        add_structured_data_to_page(filepath, structured_data)
    
    print("\n✅ Terminé!")


if __name__ == "__main__":
    process_all_city_pages()
