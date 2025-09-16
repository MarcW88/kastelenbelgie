#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script pour analyser les textes d'introduction des châteaux et identifier les contenus dupliqués
"""

import os
import re
import glob
from collections import defaultdict
import hashlib

def extract_intro_text(file_path):
    """Extraire le texte d'introduction d'une page de château"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Chercher la section intro
        intro_pattern = r'<div class="intro">(.*?)</div>'
        intro_match = re.search(intro_pattern, content, re.DOTALL)
        
        if intro_match:
            intro_html = intro_match.group(1)
            
            # Extraire les paragraphes
            paragraphs = re.findall(r'<p>\s*(.*?)\s*</p>', intro_html, re.DOTALL)
            
            # Nettoyer le texte
            clean_paragraphs = []
            for p in paragraphs:
                # Supprimer les balises HTML
                clean_text = re.sub(r'<[^>]+>', '', p)
                # Nettoyer les espaces
                clean_text = ' '.join(clean_text.split())
                if clean_text.strip():
                    clean_paragraphs.append(clean_text.strip())
            
            return clean_paragraphs
        
        return []
        
    except Exception as e:
        print(f"Erreur lors de l'extraction de {file_path}: {e}")
        return []

def get_text_hash(text):
    """Générer un hash pour identifier les textes similaires"""
    return hashlib.md5(text.lower().encode()).hexdigest()

def analyze_duplicates(castle_files):
    """Analyser les doublons dans les textes d'introduction"""
    
    text_to_files = defaultdict(list)
    file_to_text = {}
    
    print("=== ANALYSE DES TEXTES D'INTRODUCTION ===\n")
    
    for file_path in castle_files:
        filename = os.path.basename(file_path)
        intro_paragraphs = extract_intro_text(file_path)
        
        if intro_paragraphs:
            # Combiner tous les paragraphes
            full_text = ' '.join(intro_paragraphs)
            text_hash = get_text_hash(full_text)
            
            text_to_files[text_hash].append(filename)
            file_to_text[filename] = {
                'text': full_text,
                'paragraphs': intro_paragraphs,
                'hash': text_hash
            }
        else:
            print(f"⚠️  Pas de texte d'intro trouvé: {filename}")
    
    # Identifier les doublons
    duplicates = {hash_val: files for hash_val, files in text_to_files.items() if len(files) > 1}
    
    print(f"Pages analysées: {len(castle_files)}")
    print(f"Pages avec texte d'intro: {len(file_to_text)}")
    print(f"Groupes de doublons trouvés: {len(duplicates)}\n")
    
    # Afficher les doublons
    if duplicates:
        print("=== DOUBLONS DÉTECTÉS ===\n")
        for i, (hash_val, files) in enumerate(duplicates.items(), 1):
            print(f"Groupe {i} ({len(files)} pages):")
            for filename in files[:3]:  # Afficher max 3 exemples
                print(f"  - {filename}")
            if len(files) > 3:
                print(f"  ... et {len(files) - 3} autres")
            
            # Afficher le texte
            sample_text = file_to_text[files[0]]['text'][:200]
            print(f"  Texte: {sample_text}...")
            print()
    
    # Analyser les textes génériques
    print("=== TEXTES GÉNÉRIQUES DÉTECTÉS ===\n")
    generic_keywords = [
        'ce château', 'cette forteresse', 'cet édifice',
        'situé en belgique', 'patrimoine belge', 'architecture remarquable',
        'histoire fascinante', 'témoigne du passé', 'exemple typique'
    ]
    
    generic_files = []
    for filename, data in file_to_text.items():
        text_lower = data['text'].lower()
        generic_score = sum(1 for keyword in generic_keywords if keyword in text_lower)
        
        if generic_score >= 2 or len(data['text']) < 100:
            generic_files.append((filename, generic_score, len(data['text'])))
    
    if generic_files:
        print(f"Pages avec texte générique ({len(generic_files)}):")
        for filename, score, length in sorted(generic_files, key=lambda x: x[1], reverse=True)[:10]:
            print(f"  - {filename} (score: {score}, longueur: {length})")
    
    return file_to_text, duplicates, generic_files

def main():
    """Fonction principale"""
    
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
    
    # Analyser les textes
    file_to_text, duplicates, generic_files = analyze_duplicates(castle_files)
    
    # Sauvegarder les résultats pour usage ultérieur
    print("\n=== RECOMMANDATIONS ===")
    print("1. Remplacer les textes dupliqués par du contenu unique")
    print("2. Enrichir les textes génériques avec des informations spécifiques")
    print("3. Rechercher des informations historiques et architecturales uniques")
    print("4. Ajouter des détails sur la localisation, l'époque, les propriétaires")

if __name__ == "__main__":
    main()
