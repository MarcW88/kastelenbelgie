#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ACTIVITÉS PERSONNALISÉES PAR PROVINCE
Activités spécifiques et authentiques pour chaque province belge
"""

PROVINCE_ACTIVITIES = {
    "Antwerpen": [
        {
            "title": "🏛️ Rubenshuis Antwerpen",
            "description": "Bezoek het voormalige huis en atelier van Peter Paul Rubens"
        },
        {
            "title": "⛪ Onze-Lieve-Vrouwekathedraal",
            "description": "Bewonder de gotische architectuur en Rubens' meesterwerken"
        },
        {
            "title": "🌳 Rivierenhof Park",
            "description": "Wandel door een van de mooiste parken van Antwerpen"
        },
        {
            "title": "🏰 Het Steen Museum",
            "description": "Ontdek de geschiedenis van Antwerpen in dit historische kasteel"
        }
    ],
    "Limburg": [
        {
            "title": "🌲 Nationaal Park Hoge Kempen",
            "description": "Verken de unieke heide- en boslandschappen"
        },
        {
            "title": "⛏️ Mijnmuseum Beringen",
            "description": "Ontdek de rijke mijnbouwgeschiedenis van Limburg"
        },
        {
            "title": "🍎 Fruitstreek Borgloon",
            "description": "Geniet van de bloesems en fruitboomgaarden"
        },
        {
            "title": "🏞️ Voerstreek",
            "description": "Wandel door de glooiende heuvels van Voeren"
        }
    ],
    "Oost-Vlaanderen": [
        {
            "title": "🏰 Gravensteen Gent",
            "description": "Bezoek de indrukwekkende middeleeuwse burcht"
        },
        {
            "title": "🌸 Gentse Floraliën",
            "description": "Bewonder de prachtige bloemententoonstelling"
        },
        {
            "title": "🍺 Brouwerij De Halve Maan",
            "description": "Proef authentieke Gentse bieren"
        },
        {
            "title": "🏞️ Vlaamse Ardennen",
            "description": "Fiets door de glooiende heuvels en pittoreske dorpjes"
        }
    ],
    "West-Vlaanderen": [
        {
            "title": "🏛️ Historisch Centrum Brugge",
            "description": "Wandel door de UNESCO werelderfgoed stad"
        },
        {
            "title": "🌊 Belgische Kust",
            "description": "Geniet van de Noordzee en strandwandelingen"
        },
        {
            "title": "⚔️ In Flanders Fields Museum",
            "description": "Leer over de Eerste Wereldoorlog geschiedenis"
        },
        {
            "title": "🍺 Brugse Brouwerijen",
            "description": "Ontdek de beroemde biertraditie van Brugge"
        }
    ],
    "Vlaams-Brabant": [
        {
            "title": "🎓 Leuven Universiteit",
            "description": "Bezoek een van Europa's oudste universiteiten"
        },
        {
            "title": "🌳 Arboretum Kalmthout",
            "description": "Ontdek de botanische diversiteit"
        },
        {
            "title": "🏰 Kasteel van Gaasbeek",
            "description": "Verken dit prachtige renaissancekasteel"
        },
        {
            "title": "🍺 Stella Artois Brouwerij",
            "description": "Leer over de geschiedenis van dit wereldberoemde bier"
        }
    ],
    "Namen": [
        {
            "title": "🛶 Kajakken op de Maas",
            "description": "Vaar door de prachtige Maasvallei"
        },
        {
            "title": "🕳️ Grotten van Han-sur-Lesse",
            "description": "Ontdek de ondergrondse wonderen"
        },
        {
            "title": "🏞️ Condroz Streek",
            "description": "Wandel door de karakteristieke kalksteenlandschappen"
        },
        {
            "title": "🌲 Ardennen Bossen",
            "description": "Geniet van de uitgestrekte wouden en natuur"
        }
    ],
    "Luik": [
        {
            "title": "🏛️ Paleis der Prinsbisschoppen",
            "description": "Bewonder de gotische architectuur in Luik"
        },
        {
            "title": "⛪ Sint-Pauluskathedraal",
            "description": "Bezoek deze prachtige barokke kathedraal"
        },
        {
            "title": "🌊 Maas Promenade",
            "description": "Wandel langs de rivier door het stadscentrum"
        },
        {
            "title": "🎭 Opéra Royal de Wallonie",
            "description": "Geniet van cultuur in dit historische operagebouw"
        }
    ],
    "Luxemburg": [
        {
            "title": "🏰 Kasteel van Bouillon",
            "description": "Verken een van Europa's oudste burchten"
        },
        {
            "title": "🌲 Semois Vallei",
            "description": "Ontdek de meanderende rivier en bossen"
        },
        {
            "title": "🍺 Abdij van Orval",
            "description": "Proef het beroemde Trappistenbier"
        },
        {
            "title": "🦌 Natuurpark Haute-Sûre",
            "description": "Spot wilde dieren in hun natuurlijke habitat"
        }
    ],
    "Henegouwen": [
        {
            "title": "⛏️ Grand-Hornu UNESCO Site",
            "description": "Ontdek het industriële erfgoed"
        },
        {
            "title": "🏰 Kasteel van Beloeil",
            "description": "Bewonder de 'Versailles van België'"
        },
        {
            "title": "🌸 Pairi Daiza Dierentuin",
            "description": "Bezoek een van Europa's mooiste dierentuinen"
        },
        {
            "title": "🎭 Carnaval van Binche",
            "description": "Ervaar de UNESCO werelderfgoed traditie"
        }
    ],
    "Waals-Brabant": [
        {
            "title": "⚔️ Waterloo Slagveld",
            "description": "Leer over de historische slag van 1815"
        },
        {
            "title": "🏛️ Abdij van Villers",
            "description": "Verken de indrukwekkende cisterciënzer ruïnes"
        },
        {
            "title": "🌳 Forêt de Soignes",
            "description": "Wandel door het 'groene long' van Brussel"
        },
        {
            "title": "🍺 Brasserie Cantillon",
            "description": "Ontdek de traditionele lambiek brouwerij"
        }
    ],
    "Brussel": [
        {
            "title": "🏛️ Grote Markt",
            "description": "Bewonder de UNESCO werelderfgoed Grand-Place"
        },
        {
            "title": "👦 Manneken Pis",
            "description": "Bezoek het beroemde symbool van Brussel"
        },
        {
            "title": "🏰 Koninklijk Paleis",
            "description": "Ontdek de officiële residentie van de koning"
        },
        {
            "title": "🎨 Koninklijke Musea",
            "description": "Geniet van kunst van Vlaamse Primitieven tot moderne kunst"
        }
    ]
}

def get_activities_for_province(province_name):
    """Retourne les activités pour une province donnée"""
    return PROVINCE_ACTIVITIES.get(province_name, PROVINCE_ACTIVITIES.get("Antwerpen", []))

def format_activities_html(activities):
    """Formate les activités en HTML"""
    html = '<div class="activities-grid">\n'
    for activity in activities:
        html += f'''    <div class="activity-item">
        <h3>{activity["title"]}</h3>
        <p>{activity["description"]}</p>
    </div>\n'''
    html += '</div>'
    return html

if __name__ == "__main__":
    # Test
    for province, activities in PROVINCE_ACTIVITIES.items():
        print(f"\n{province}:")
        for activity in activities:
            print(f"  • {activity['title']}: {activity['description']}")
