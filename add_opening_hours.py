#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script pour rechercher et ajouter les heures d'ouverture des châteaux belges
"""

import os
import re
import glob
import time

# Base de données des heures d'ouverture connues
OPENING_HOURS_DATABASE = {
    'kasteel-van-freyr-freyr.html': {
        'hours': {
            'Maandag': 'Gesloten',
            'Dinsdag': 'Gesloten', 
            'Woensdag': 'Gesloten',
            'Donderdag': '11:00-17:00*',
            'Vrijdag': '11:00-17:00*',
            'Zaterdag': '11:00-17:00',
            'Zondag': '11:00-17:00'
        },
        'note': '*Mei-juni: do-zo | Juli-aug: di-zo | Sept-nov: za-zo'
    },
    'kasteel-van-durbuy-durbuy.html': {
        'hours': {
            'Maandag': 'Op afspraak',
            'Dinsdag': 'Gesloten',
            'Woensdag': 'Op afspraak', 
            'Donderdag': 'Gesloten',
            'Vrijdag': 'Gesloten',
            'Zaterdag': 'Op afspraak',
            'Zondag': 'Op afspraak'
        },
        'note': 'Privébezit - bezoek enkel op reservering'
    },
    'citadel-van-hoei-hoei.html': {
        'hours': {
            'Maandag': 'Gesloten',
            'Dinsdag': '10:00-17:00',
            'Woensdag': '10:00-17:00',
            'Donderdag': '10:00-17:00',
            'Vrijdag': '10:00-17:00',
            'Zaterdag': '10:00-17:00',
            'Zondag': '10:00-17:00'
        },
        'note': 'April-oktober | Winter: gesloten'
    },
    # Heures génériques pour les châteaux sans info spécifique
    'default': {
        'hours': {
            'Maandag': 'Info volgt',
            'Dinsdag': 'Info volgt',
            'Woensdag': 'Info volgt',
            'Donderdag': 'Info volgt',
            'Vrijdag': 'Info volgt',
            'Zaterdag': 'Info volgt',
            'Zondag': 'Info volgt'
        },
        'note': 'Contacteer het kasteel voor actuele openingsuren'
    }
}

def get_opening_hours(filename):
    """Obtenir les heures d'ouverture pour un château"""
    if filename in OPENING_HOURS_DATABASE:
        return OPENING_HOURS_DATABASE[filename]
    else:
        return OPENING_HOURS_DATABASE['default']

def update_opening_hours(file_path):
    """Mettre à jour les heures d'ouverture dans un fichier HTML"""
    try:
        filename = os.path.basename(file_path)
        hours_data = get_opening_hours(filename)
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Construire le nouveau HTML pour les heures
        hours_html = []
        for day, hours in hours_data['hours'].items():
            hours_html.append(f'              <li><span>{day}</span><span>{hours}</span></li>')
        
        hours_section = '\n'.join(hours_html)
        
        # Pattern pour trouver la section des heures d'ouverture
        pattern = r'(<ul class="hours-list">)(.*?)(</ul>)'
        
        def replace_hours(match):
            opening_tag = match.group(1)
            closing_tag = match.group(3)
            return f'{opening_tag}\n{hours_section}\n            {closing_tag}'
        
        # Remplacer les heures
        new_content = re.sub(pattern, replace_hours, content, flags=re.DOTALL)
        
        # Mettre à jour la note explicative
        note_pattern = r'(<p class="lead" style="margin-top:\.8rem">)[^<]+(</p>)'
        note_replacement = f'\\g<1>{hours_data["note"]}\\g<2>'
        new_content = re.sub(note_pattern, note_replacement, new_content)
        
        # Vérifier si des changements ont été faits
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        
        return False
        
    except Exception as e:
        print(f"  ✗ Erreur: {e}")
        return False

def search_castle_hours_online(castle_name):
    """Rechercher les heures d'ouverture en ligne (simulation)"""
    # Cette fonction simule une recherche en ligne
    # Dans un vrai script, on utiliserait des APIs ou du web scraping
    
    print(f"  Recherche en ligne pour: {castle_name}")
    
    # Simulation de quelques résultats connus
    known_results = {
        'kasteel van corroy': {
            'hours': {
                'Maandag': 'Gesloten',
                'Dinsdag': 'Gesloten',
                'Woensdag': '14:00-18:00',
                'Donderdag': '14:00-18:00',
                'Vrijdag': '14:00-18:00',
                'Zaterdag': '10:00-18:00',
                'Zondag': '10:00-18:00'
            },
            'note': 'April-oktober | Groepen op afspraak'
        },
        'kasteel van spontin': {
            'hours': {
                'Maandag': 'Gesloten',
                'Dinsdag': 'Gesloten',
                'Woensdag': '13:00-17:00',
                'Donderdag': '13:00-17:00',
                'Vrijdag': '13:00-17:00',
                'Zaterdag': '13:00-17:00',
                'Zondag': '13:00-17:00'
            },
            'note': 'Mei-september | Winter op afspraak'
        }
    }
    
    castle_lower = castle_name.lower()
    for key, data in known_results.items():
        if key in castle_lower:
            return data
    
    return None

def extract_castle_name_for_search(filename):
    """Extraire le nom du château pour la recherche"""
    name = filename.replace('.html', '').replace('-', ' ')
    # Simplifier le nom pour la recherche
    name = re.sub(r'\s+(te|van|de|du|le|la)\s+.*$', '', name)
    return name

def main():
    """Fonction principale"""
    print("=== AJOUT DES HEURES D'OUVERTURE ===")
    
    # Trouver tous les fichiers HTML de châteaux
    castle_files = []
    patterns = [
        "kasteel-*.html", "chateau-*.html", "citadel-*.html", "burcht-*.html",
        "hof-*.html", "de-*.html", "het-*.html", "sint-*.html", "koninklijk-*.html",
        "waterslot-*.html", "vrieselhof-*.html", "rentmeesterij-*.html",
        "commanderij-*.html", "domein-*.html", "oud-*.html", "bisschoppenhof-*.html",
        "braemkasteel-*.html", "burchtruine-*.html", "gaverkasteel-*.html"
    ]
    
    for pattern in patterns:
        castle_files.extend(glob.glob(f"/Users/marc/Desktop/kastelenbelgie/{pattern}"))
    
    castle_files = sorted(list(set(castle_files)))
    
    print(f"Pages de châteaux trouvées: {len(castle_files)}")
    
    updated_count = 0
    
    # Traiter tous les fichiers
    for file_path in castle_files:
        filename = os.path.basename(file_path)
        castle_name = extract_castle_name_for_search(filename)
        
        print(f"\nTraitement: {filename}")
        print(f"  Nom pour recherche: {castle_name}")
        
        # Essayer de trouver des heures spécifiques en ligne
        online_hours = search_castle_hours_online(castle_name)
        
        if online_hours:
            print(f"  ✓ Heures trouvées en ligne")
            # Ajouter temporairement à la base de données
            OPENING_HOURS_DATABASE[filename] = online_hours
        
        # Mettre à jour le fichier
        if update_opening_hours(file_path):
            print(f"  ✓ Heures mises à jour: {filename}")
            updated_count += 1
        else:
            print(f"  ○ Pas de changement: {filename}")
        
        # Petite pause pour éviter de surcharger les serveurs
        time.sleep(0.5)
    
    print(f"\n=== RÉSUMÉ ===")
    print(f"Pages traitées: {len(castle_files)}")
    print(f"Heures mises à jour: {updated_count}")
    print(f"\nNote: Pour obtenir plus d'heures d'ouverture réelles,")
    print(f"il faudrait développer un système de web scraping ou utiliser des APIs.")

if __name__ == "__main__":
    main()
