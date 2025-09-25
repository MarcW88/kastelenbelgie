#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SYSTÈME DE MATCHING D'IMAGES POUR CHÂTEAUX
Trouve les images correspondantes avec seuil de similarité de 50%
"""

import os
import re
from difflib import SequenceMatcher
from urllib.parse import urlparse

class CastleImageMatcher:
    def __init__(self, images_directory):
        self.images_dir = images_directory
        self.image_files = self._load_image_files()
    
    def _load_image_files(self):
        """Charge la liste des fichiers d'images disponibles"""
        if not os.path.exists(self.images_dir):
            print(f"❌ Dossier d'images non trouvé: {self.images_dir}")
            return []
        
        image_files = []
        for filename in os.listdir(self.images_dir):
            if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp')):
                # Extraire le nom de base (sans numéro et extension)
                base_name = re.sub(r'_\d+\.(jpg|jpeg|png|gif|webp)$', '', filename, flags=re.IGNORECASE)
                image_files.append({
                    'filename': filename,
                    'base_name': base_name,
                    'full_path': os.path.join(self.images_dir, filename)
                })
        
        print(f"📸 {len(image_files)} images chargées depuis {self.images_dir}")
        return image_files
    
    def similarity(self, a, b):
        """Calcule la similarité entre deux chaînes"""
        return SequenceMatcher(None, a.lower(), b.lower()).ratio()
    
    def normalize_name(self, name):
        """Normalise un nom pour la comparaison"""
        # Convertir en minuscules
        normalized = name.lower()
        
        # Supprimer les mots communs
        common_words = ['kasteel', 'château', 'castle', 'van', 'de', 'du', 'der', 'het', 'le', 'la', 'te', 'in']
        for word in common_words:
            normalized = re.sub(rf'\b{word}\b', '', normalized)
        
        # Remplacer les caractères spéciaux
        normalized = re.sub(r'[àáâãäå]', 'a', normalized)
        normalized = re.sub(r'[èéêë]', 'e', normalized)
        normalized = re.sub(r'[ìíîï]', 'i', normalized)
        normalized = re.sub(r'[òóôõö]', 'o', normalized)
        normalized = re.sub(r'[ùúûü]', 'u', normalized)
        normalized = re.sub(r'[ç]', 'c', normalized)
        normalized = re.sub(r'[ñ]', 'n', normalized)
        
        # Supprimer les caractères non-alphanumériques sauf espaces et tirets
        normalized = re.sub(r'[^a-z0-9\s\-]', '', normalized)
        
        # Normaliser les espaces et tirets
        normalized = re.sub(r'[\s\-]+', '_', normalized)
        normalized = normalized.strip('_')
        
        return normalized
    
    def extract_castle_name_from_url(self, url):
        """Extrait le nom du château depuis l'URL"""
        url_path = urlparse(url).path
        filename = url_path.split('/')[-2] if url_path.endswith('/') else url_path.split('/')[-1]
        
        # Supprimer les préfixes et suffixes courants
        filename = re.sub(r'^(kasteel-|château-|castle-)', '', filename)
        filename = re.sub(r'(-te-|-in-|-van-|-de-|-du-)', '-', filename)
        
        return filename.replace('-', '_')
    
    def find_matching_images(self, castle_name, castle_url="", threshold=0.5):
        """Trouve les images correspondant au château"""
        if not self.image_files:
            return []
        
        # Préparer les noms de recherche
        search_names = [self.normalize_name(castle_name)]
        
        if castle_url:
            url_name = self.extract_castle_name_from_url(castle_url)
            search_names.append(self.normalize_name(url_name))
        
        # Rechercher les correspondances
        matches = []
        
        for search_name in search_names:
            for image_info in self.image_files:
                image_base = self.normalize_name(image_info['base_name'])
                
                # Calculer la similarité
                similarity_score = self.similarity(search_name, image_base)
                
                if similarity_score >= threshold:
                    # Éviter les doublons
                    if not any(m['filename'] == image_info['filename'] for m in matches):
                        matches.append({
                            'filename': image_info['filename'],
                            'full_path': image_info['full_path'],
                            'similarity': similarity_score,
                            'search_term': search_name,
                            'image_base': image_base
                        })
        
        # Trier par similarité décroissante
        matches.sort(key=lambda x: x['similarity'], reverse=True)
        
        return matches[:6]  # Maximum 6 images
    
    def get_best_image(self, castle_name, castle_url="", threshold=0.5):
        """Retourne la meilleure image pour un château"""
        matches = self.find_matching_images(castle_name, castle_url, threshold)
        
        if matches:
            best_match = matches[0]
            print(f"  🖼️ Image trouvée: {best_match['filename']} (similarité: {best_match['similarity']:.2f})")
            return best_match
        
        print(f"  ❌ Aucune image trouvée pour {castle_name}")
        return None
    
    def get_related_castle_images(self, province, exclude_castle="", max_images=3):
        """Trouve des images de châteaux reliés pour une province"""
        # Mots-clés par province pour filtrer les images
        province_keywords = {
            'Antwerpen': ['antwerpen', 'anvers', 'merksem', 'brasschaat', 'kapellen'],
            'Limburg': ['limburg', 'hasselt', 'genk', 'bilzen', 'tongeren'],
            'Oost-Vlaanderen': ['gent', 'aalst', 'dendermonde', 'lokeren', 'sint_niklaas'],
            'West-Vlaanderen': ['brugge', 'kortrijk', 'oostende', 'roeselare', 'ieper'],
            'Vlaams-Brabant': ['leuven', 'vilvoorde', 'aarschot', 'tienen', 'diest'],
            'Brussel': ['brussel', 'brussels', 'bruxelles', 'uccle', 'ixelles'],
            'Waals-Brabant': ['wavre', 'nivelles', 'braine', 'waterloo', 'ottignies'],
            'Namen': ['namur', 'namen', 'dinant', 'gembloux', 'ciney'],
            'Luik': ['liege', 'luik', 'verviers', 'seraing', 'herstal'],
            'Henegouwen': ['mons', 'charleroi', 'tournai', 'mouscron', 'la_louviere'],
            'Luxemburg': ['arlon', 'bastogne', 'marche', 'virton', 'neufchateau']
        }
        
        keywords = province_keywords.get(province, [province.lower()])
        exclude_normalized = self.normalize_name(exclude_castle) if exclude_castle else ""
        
        related_images = []
        
        for image_info in self.image_files:
            image_base = self.normalize_name(image_info['base_name'])
            
            # Éviter l'image du château actuel
            if exclude_normalized and self.similarity(exclude_normalized, image_base) > 0.7:
                continue
            
            # Vérifier si l'image correspond à la province
            for keyword in keywords:
                if keyword in image_base or any(k in image_base for k in keywords):
                    related_images.append({
                        'filename': image_info['filename'],
                        'full_path': image_info['full_path'],
                        'base_name': image_info['base_name']
                    })
                    break
        
        # Retourner un échantillon aléatoire
        import random
        if len(related_images) > max_images:
            related_images = random.sample(related_images, max_images)
        
        return related_images

# Test de la classe
if __name__ == "__main__":
    images_dir = "/Users/marc/Desktop/kastelenbelgie/chateaux_images_update-2"
    matcher = CastleImageMatcher(images_dir)
    
    # Test avec quelques châteaux
    test_cases = [
        ("Kasteel van Freyr", "https://kastelenbelgie.be/nl/kasteel-van-freyr-freyr/"),
        ("Kasteel Beauregard", "https://kastelenbelgie.be/nl/kasteel-beauregard-froyennes/"),
        ("Hof ter Borght", "https://kastelenbelgie.be/nl/hof-ter-borght-westmeerbeek/")
    ]
    
    for castle_name, castle_url in test_cases:
        print(f"\n🏰 Test pour: {castle_name}")
        
        # Trouver la meilleure image
        best_image = matcher.get_best_image(castle_name, castle_url, 0.5)
        
        # Trouver toutes les images correspondantes
        all_matches = matcher.find_matching_images(castle_name, castle_url, 0.3)
        print(f"  📸 {len(all_matches)} images trouvées au total")
        
        for match in all_matches[:3]:
            print(f"    - {match['filename']} (similarité: {match['similarity']:.2f})")
