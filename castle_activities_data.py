#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
DONNÉES DES ACTIVITÉS PAR PROVINCE
"""

# Activités par province
PROVINCE_ACTIVITIES = {
    "Antwerpen": [
        {"title": "🏛️ Rubenshuis Antwerpen", "description": "Bezoek het voormalige huis en atelier van Peter Paul Rubens"},
        {"title": "⛪ Onze-Lieve-Vrouwekathedraal", "description": "Bewonder de gotische architectuur en Rubens' meesterwerken"},
        {"title": "🌳 Rivierenhof Park", "description": "Wandel door een van de mooiste parken van Antwerpen"},
        {"title": "🏰 Het Steen Museum", "description": "Ontdek de geschiedenis van Antwerpen in dit historische kasteel"}
    ],
    "Limburg": [
        {"title": "🌲 Nationaal Park Hoge Kempen", "description": "Verken de unieke heide- en boslandschappen"},
        {"title": "⛏️ Mijnmuseum Beringen", "description": "Ontdek de rijke mijnbouwgeschiedenis van Limburg"},
        {"title": "🍎 Fruitstreek Borgloon", "description": "Geniet van de bloesems en fruitboomgaarden"},
        {"title": "🏞️ Voerstreek", "description": "Wandel door de glooiende heuvels van Voeren"}
    ],
    "West-Vlaanderen": [
        {"title": "🏛️ Historisch Centrum Brugge", "description": "Wandel door de UNESCO werelderfgoed stad"},
        {"title": "🌊 Belgische Kust", "description": "Geniet van de Noordzee en strandwandelingen"},
        {"title": "⚔️ In Flanders Fields Museum", "description": "Leer over de Eerste Wereldoorlog geschiedenis"},
        {"title": "🍺 Brugse Brouwerijen", "description": "Ontdek de beroemde biertraditie van Brugge"}
    ],
    "Vlaams-Brabant": [
        {"title": "🎓 Leuven Universiteit", "description": "Bezoek een van Europa's oudste universiteiten"},
        {"title": "🌳 Arboretum Kalmthout", "description": "Ontdek de botanische diversiteit"},
        {"title": "🏰 Kasteel van Gaasbeek", "description": "Verken dit prachtige renaissancekasteel"},
        {"title": "🍺 Stella Artois Brouwerij", "description": "Leer over de geschiedenis van dit wereldberoemde bier"}
    ],
    "Luxemburg": [
        {"title": "🏰 Kasteel van Bouillon", "description": "Verken een van Europa's oudste burchten"},
        {"title": "🌲 Semois Vallei", "description": "Ontdek de meanderende rivier en bossen"},
        {"title": "🍺 Abdij van Orval", "description": "Proef het beroemde Trappistenbier"},
        {"title": "🦌 Natuurpark Haute-Sûre", "description": "Spot wilde dieren in hun natuurlijke habitat"}
    ],
    "Brussel": [
        {"title": "🏛️ Grote Markt", "description": "Bewonder de UNESCO werelderfgoed Grand-Place"},
        {"title": "👦 Manneken Pis", "description": "Bezoek het beroemde symbool van Brussel"},
        {"title": "🏰 Koninklijk Paleis", "description": "Ontdek de officiële residentie van de koning"},
        {"title": "🎨 Koninklijke Musea", "description": "Geniet van kunst van Vlaamse Primitieven tot moderne kunst"}
    ],
    "Oost-Vlaanderen": [
        {"title": "🏰 Gravensteen Gent", "description": "Bezoek de iconische middeleeuwse burcht"},
        {"title": "🎨 Museum voor Schone Kunsten", "description": "Ontdek Vlaamse meesters en moderne kunst"},
        {"title": "🌸 Kasteel van Laarne", "description": "Bewonder dit prachtige waterslot"},
        {"title": "🍺 Gentse Brouwerijen", "description": "Proef lokale bieren in historische setting"}
    ],
    "Namen": [
        {"title": "🏰 Citadel van Namen", "description": "Verken de imposante vesting boven de Maas"},
        {"title": "🌊 Maas en Sambre", "description": "Geniet van boottochtjes op de rivieren"},
        {"title": "🍺 Abdij van Maredsous", "description": "Ontdek de beroemde abdijbieren"},
        {"title": "🌳 Natuurpark Furfooz", "description": "Wandel door prehistorische grotten en bossen"}
    ],
    "Luik": [
        {"title": "🏛️ Paleis van de Prinsbisschoppen", "description": "Bewonder de gotische architectuur"},
        {"title": "🌊 Maas Promenade", "description": "Wandel langs de rivier door het stadscentrum"},
        {"title": "🎵 Opéra Royal de Wallonie", "description": "Geniet van opera en ballet voorstellingen"},
        {"title": "🍺 Val-Dieu Abdij", "description": "Proef authentieke abdijbieren"}
    ],
    "Henegouwen": [
        {"title": "🏰 Kasteel van Beloeil", "description": "Het 'Versailles van België' met prachtige tuinen"},
        {"title": "⛏️ Grand-Hornu", "description": "UNESCO werelderfgoed industrieel complex"},
        {"title": "🎭 Carnaval van Binche", "description": "Ervaar de beroemde UNESCO carnavalstraditie"},
        {"title": "🌳 Pairi Daiza", "description": "Bezoek een van Europa's mooiste dierentuinen"}
    ],
    "Waals-Brabant": [
        {"title": "🎓 Université catholique de Louvain", "description": "Verken de historische universiteitscampus"},
        {"title": "🌳 Domein Solvay", "description": "Wandel door het prachtige kasteelpark"},
        {"title": "🍺 Brasserie de la Senne", "description": "Ontdek lokale craft bieren"},
        {"title": "🏛️ Abdij van Villers", "description": "Bezoek de indrukwekkende cisterciënzer ruïnes"}
    ]
}

def get_activities_for_province(province):
    """Retourne les activités pour une province donnée"""
    return PROVINCE_ACTIVITIES.get(province, PROVINCE_ACTIVITIES.get("Antwerpen", []))
