#!/usr/bin/env python3
"""
Script pour ajouter des données structurées Schema.org aux pages provinces
- Place (AdministrativeArea)
- TouristDestination
- ItemList (liste des châteaux)
"""

import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent
BASE_URL = "https://kastelenbelgie.be"

PROVINCES = {
    "luxemburg.html": {
        "name": "Luxemburg",
        "name_full": "Provincie Luxemburg",
        "description": "Ontdek de mooiste kastelen in de provincie Luxemburg. Diepe Ardense valleien, dichte bossen en charmante stadjes langs de Semois en de Ourthe.",
        "region": "Wallonië",
        "geo": {"lat": "49.8167", "lon": "5.4167"},
        "castles": [
            {"name": "Kasteel van Durbuy", "url": "kasteel-van-durbuy-durbuy.html"},
            {"name": "Kasteel van Orval", "url": "kasteel-van-orval-villers-devant-orval.html"},
            {"name": "Kasteel van Porcheresse", "url": "kasteel-van-porcheresse-daverdisse.html"},
            {"name": "Kasteel van Longchamps", "url": "kasteel-van-longchamps-longchamps-bertogne.html"},
            {"name": "Kasteel van Mirwart", "url": "kasteel-van-mirwart-mirwart-saint-hubert.html"},
            {"name": "Kasteel van Deulin", "url": "kasteel-van-deulin-deulin-fronville.html"},
        ]
    },
    "antwerpen.html": {
        "name": "Antwerpen",
        "name_full": "Provincie Antwerpen",
        "description": "Ontdek de mooiste kastelen in de provincie Antwerpen. Van historische burchten tot elegante landgoederen in de Kempen en rond de Scheldestad.",
        "region": "Vlaanderen",
        "geo": {"lat": "51.2194", "lon": "4.4025"},
        "castles": []
    },
    "limburg.html": {
        "name": "Limburg",
        "name_full": "Provincie Limburg",
        "description": "Ontdek de mooiste kastelen in de provincie Limburg. Historische kastelen en landgoederen in het groene Haspengouw en de Kempen.",
        "region": "Vlaanderen",
        "geo": {"lat": "50.9311", "lon": "5.3378"},
        "castles": []
    },
    "oost-vlaanderen.html": {
        "name": "Oost-Vlaanderen",
        "name_full": "Provincie Oost-Vlaanderen",
        "description": "Ontdek de mooiste kastelen in Oost-Vlaanderen. Van de Gravensteen in Gent tot romantische kasteeldomeinen langs de Schelde.",
        "region": "Vlaanderen",
        "geo": {"lat": "51.0500", "lon": "3.7333"},
        "castles": []
    },
    "west-vlaanderen.html": {
        "name": "West-Vlaanderen",
        "name_full": "Provincie West-Vlaanderen",
        "description": "Ontdek de mooiste kastelen in West-Vlaanderen. Historische burchten en landgoederen van Brugge tot de kust.",
        "region": "Vlaanderen",
        "geo": {"lat": "51.0536", "lon": "3.1458"},
        "castles": []
    },
    "vlaams-brabant.html": {
        "name": "Vlaams-Brabant",
        "name_full": "Provincie Vlaams-Brabant",
        "description": "Ontdek de mooiste kastelen in Vlaams-Brabant. Kastelen en landgoederen rond Leuven en het Hageland.",
        "region": "Vlaanderen",
        "geo": {"lat": "50.8798", "lon": "4.7005"},
        "castles": []
    },
    "waals-brabant.html": {
        "name": "Waals-Brabant",
        "name_full": "Provincie Waals-Brabant",
        "description": "Ontdek de mooiste kastelen in Waals-Brabant. Elegante kasteeldomeinen en historische landgoederen ten zuiden van Brussel.",
        "region": "Wallonië",
        "geo": {"lat": "50.6333", "lon": "4.5667"},
        "castles": []
    },
    "henegouwen.html": {
        "name": "Henegouwen",
        "name_full": "Provincie Henegouwen",
        "description": "Ontdek de mooiste kastelen in Henegouwen. Van middeleeuwse burchten tot industrieel erfgoed in het zuiden van België.",
        "region": "Wallonië",
        "geo": {"lat": "50.4542", "lon": "3.9567"},
        "castles": []
    },
    "luik.html": {
        "name": "Luik",
        "name_full": "Provincie Luik",
        "description": "Ontdek de mooiste kastelen in de provincie Luik. Historische burchten en kasteeldomeinen in de Ardennen en langs de Maas.",
        "region": "Wallonië",
        "geo": {"lat": "50.6326", "lon": "5.5797"},
        "castles": []
    },
    "namen.html": {
        "name": "Namen",
        "name_full": "Provincie Namen",
        "description": "Ontdek de mooiste kastelen in de provincie Namen. Van de Citadel van Namen tot romantische kasteeldomeinen in de Condroz.",
        "region": "Wallonië",
        "geo": {"lat": "50.4669", "lon": "4.8675"},
        "castles": []
    },
    "brussel.html": {
        "name": "Brussel",
        "name_full": "Brussels Hoofdstedelijk Gewest",
        "description": "Ontdek de mooiste kastelen in Brussel. Koninklijke paleizen en historische kasteeldomeinen in de hoofdstad.",
        "region": "Brussel",
        "geo": {"lat": "50.8503", "lon": "4.3517"},
        "castles": []
    }
}


def extract_castles_from_html(filepath: Path) -> list:
    """Extrait les châteaux listés dans une page province"""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    castles = []
    # Pattern pour trouver les cartes château
    pattern = r'<h3>([^<]+)</h3>.*?<a href="([^"]+)"[^>]*>Meer info</a>'
    matches = re.findall(pattern, content, re.DOTALL)
    
    for name, url in matches:
        if url.endswith('.html') and 'kasteel' in url.lower():
            castles.append({"name": name.strip(), "url": url})
    
    return castles


def build_structured_data(province_key: str, province_data: dict) -> str:
    """Construit le JSON-LD pour une page province"""
    
    # Extraire les châteaux de la page si pas déjà définis
    if not province_data["castles"]:
        filepath = BASE_DIR / province_key
        if filepath.exists():
            province_data["castles"] = extract_castles_from_html(filepath)
    
    structured_data = {
        "@context": "https://schema.org",
        "@graph": [
            # 1. AdministrativeArea (Province)
            {
                "@type": "AdministrativeArea",
                "@id": f"{BASE_URL}/{province_key}#province",
                "name": province_data["name_full"],
                "description": province_data["description"],
                "containedInPlace": {
                    "@type": "Country",
                    "name": "België"
                },
                "geo": {
                    "@type": "GeoCoordinates",
                    "latitude": province_data["geo"]["lat"],
                    "longitude": province_data["geo"]["lon"]
                }
            },
            # 2. TouristDestination
            {
                "@type": "TouristDestination",
                "@id": f"{BASE_URL}/{province_key}#destination",
                "name": f"Kastelen in {province_data['name']}",
                "description": province_data["description"],
                "touristType": [
                    "Cultuurliefhebbers",
                    "Geschiedenisliefhebbers",
                    "Families"
                ],
                "containedInPlace": {
                    "@id": f"{BASE_URL}/{province_key}#province"
                }
            },
            # 3. WebPage
            {
                "@type": "WebPage",
                "@id": f"{BASE_URL}/{province_key}",
                "name": f"Kastelen in {province_data['name']} | kastelenbelgie.be",
                "description": province_data["description"],
                "url": f"{BASE_URL}/{province_key}",
                "isPartOf": {
                    "@type": "WebSite",
                    "name": "Kastelen België",
                    "url": BASE_URL
                },
                "about": {
                    "@id": f"{BASE_URL}/{province_key}#destination"
                }
            }
        ]
    }
    
    # 4. ItemList (si châteaux présents)
    if province_data["castles"]:
        item_list = {
            "@type": "ItemList",
            "@id": f"{BASE_URL}/{province_key}#castles-list",
            "name": f"Kastelen in {province_data['name']}",
            "description": f"Overzicht van kastelen in de provincie {province_data['name']}",
            "numberOfItems": len(province_data["castles"]),
            "itemListElement": []
        }
        
        for i, castle in enumerate(province_data["castles"], 1):
            item_list["itemListElement"].append({
                "@type": "ListItem",
                "position": i,
                "name": castle["name"],
                "url": f"{BASE_URL}/{castle['url']}"
            })
        
        structured_data["@graph"].append(item_list)
    
    return json.dumps(structured_data, indent=2, ensure_ascii=False)


def add_structured_data_to_page(filepath: Path, structured_data: str) -> bool:
    """Ajoute ou remplace les données structurées dans une page HTML"""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Vérifier si des données structurées existent déjà
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


def process_all_provinces():
    """Traite toutes les pages provinces"""
    print("🏰 Ajout des données structurées aux pages provinces...\n")
    
    for province_key, province_data in PROVINCES.items():
        filepath = BASE_DIR / province_key
        
        if not filepath.exists():
            print(f"⚠️  Page non trouvée: {province_key}")
            continue
        
        structured_data = build_structured_data(province_key, province_data)
        add_structured_data_to_page(filepath, structured_data)
    
    print("\n✅ Terminé!")


if __name__ == "__main__":
    process_all_provinces()
