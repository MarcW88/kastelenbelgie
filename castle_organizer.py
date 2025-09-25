#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ORGANISATEUR DE CHÂTEAUX PAR PROVINCE
Organise les châteaux par province et trouve leurs images
"""

import csv
import os
import glob
from difflib import SequenceMatcher
from image_matcher import CastleImageMatcher

class CastleOrganizer:
    def __init__(self):
        self.image_matcher = CastleImageMatcher("/Users/marc/Desktop/kastelenbelgie/chateaux_images_update-2")
        self.castles_by_province = {}
        self.popular_castles = [
            "Kasteel van Freÿr",
            "Kasteel van Durbuy", 
            "Citadel van hoei",
            "Kasteel de merode",
            "Kasteel van Bouchout",
            "Waterslot cleydael"
        ]
    
    def load_castles_data(self):
        """Charge les données des châteaux depuis le CSV"""
        csv_file = "/Users/marc/Desktop/kastelenbelgie/chateaux_opening_hours - chateaux_opening_hours.csv"
        
        try:
            with open(csv_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                
                for row in reader:
                    title = row.get('Title', '')
                    url = row.get('URL', '')
                    province = row.get('Provincie', '')
                    
                    # Ignorer les pages d'index
                    if any(skip in title.lower() for skip in ['kastelen per provincie', 'kastelen in', 'home', 'kaart']):
                        continue
                    
                    if province not in self.castles_by_province:
                        self.castles_by_province[province] = []
                    
                    # Trouver l'image correspondante
                    image_info = self.image_matcher.get_best_image(title, url, 0.5)
                    
                    castle_data = {
                        'title': title,
                        'url': url,
                        'province': province,
                        'image': image_info['filename'] if image_info else None,
                        'image_similarity': image_info['similarity'] if image_info else 0,
                        'filename': self.get_filename_from_url(url)
                    }
                    
                    self.castles_by_province[province].append(castle_data)
        
        except Exception as e:
            print(f"Erreur chargement données: {e}")
    
    def get_filename_from_url(self, url):
        """Extrait le nom du fichier depuis l'URL"""
        from urllib.parse import urlparse
        url_path = urlparse(url).path
        filename = url_path.split('/')[-2] if url_path.endswith('/') else url_path.split('/')[-1]
        return filename if filename else "kasteel"
    
    def get_popular_castles_data(self):
        """Récupère les données des châteaux populaires"""
        popular_data = []
        
        for province_castles in self.castles_by_province.values():
            for castle in province_castles:
                if any(popular in castle['title'] for popular in self.popular_castles):
                    popular_data.append(castle)
                    if len(popular_data) >= 6:
                        break
            if len(popular_data) >= 6:
                break
        
        # Compléter avec d'autres châteaux si nécessaire
        if len(popular_data) < 6:
            for province_castles in self.castles_by_province.values():
                for castle in province_castles:
                    if castle not in popular_data and castle['image']:
                        popular_data.append(castle)
                        if len(popular_data) >= 6:
                            break
                if len(popular_data) >= 6:
                    break
        
        return popular_data[:6]
    
    def generate_province_castle_list_html(self, province):
        """Génère le HTML pour la liste des châteaux d'une province"""
        if province not in self.castles_by_province:
            return ""
        
        castles = self.castles_by_province[province]
        html = '<div class="castle-grid">\n'
        
        for castle in castles:
            image_src = f"chateaux_images_update-2/{castle['image']}" if castle['image'] else "assets/placeholder-castle-card.svg"
            
            html += f'''
                <div class="castle-card">
                    <div class="castle-image">
                        <img src="{image_src}" alt="{castle['title']}" loading="lazy">
                    </div>
                    <div class="castle-card-content">
                        <h3>{castle['title']}</h3>
                        <p class="card-description">Ontdek dit prachtige kasteel in {province}</p>
                        <a href="{castle['filename']}.html" class="btn-primary">Meer info</a>
                    </div>
                </div>
            '''
        
        html += '</div>\n'
        return html
    
    def generate_popular_castles_html(self):
        """Génère le HTML pour les châteaux populaires de la homepage"""
        popular_castles = self.get_popular_castles_data()
        
        html = '<div class="popular-castles-grid">\n'
        
        for castle in popular_castles:
            image_src = f"chateaux_images_update-2/{castle['image']}" if castle['image'] else "assets/placeholder-castle-card.svg"
            
            html += f'''
                <div class="popular-castle-card">
                    <div class="castle-image">
                        <img src="{image_src}" alt="{castle['title']}" loading="lazy">
                    </div>
                    <div class="castle-card-content">
                        <h3>{castle['title']}</h3>
                        <p class="card-description">{castle['province']}</p>
                        <a href="{castle['filename']}.html" class="btn-primary">Bezoek kasteel</a>
                    </div>
                </div>
            '''
        
        html += '</div>\n'
        return html
    
    def get_related_castles_in_province(self, current_castle_title, province, max_castles=3):
        """Récupère des châteaux liés dans la même province"""
        if province not in self.castles_by_province:
            return []
        
        related_castles = []
        province_castles = self.castles_by_province[province]
        
        # Filtrer le château actuel et prendre ceux avec images
        for castle in province_castles:
            if (castle['title'] != current_castle_title and 
                castle['image'] and 
                len(related_castles) < max_castles):
                related_castles.append(castle)
        
        return related_castles
    
    def print_statistics(self):
        """Affiche les statistiques"""
        print("📊 STATISTIQUES DES CHÂTEAUX PAR PROVINCE")
        print("=" * 50)
        
        total_castles = 0
        total_with_images = 0
        
        for province, castles in self.castles_by_province.items():
            with_images = sum(1 for c in castles if c['image'])
            total_castles += len(castles)
            total_with_images += with_images
            
            print(f"{province}: {len(castles)} châteaux ({with_images} avec images)")
        
        print(f"\nTotal: {total_castles} châteaux")
        print(f"Avec images: {total_with_images} ({total_with_images/total_castles*100:.1f}%)")
        
        popular = self.get_popular_castles_data()
        print(f"\nChâteaux populaires sélectionnés: {len(popular)}")
        for castle in popular:
            print(f"  - {castle['title']} ({castle['province']})")

if __name__ == "__main__":
    organizer = CastleOrganizer()
    organizer.load_castles_data()
    organizer.print_statistics()
