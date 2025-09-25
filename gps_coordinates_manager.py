#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
GESTIONNAIRE DE COORDONNÉES GPS POUR CHÂTEAUX
Intègre les coordonnées depuis chateaux_coord.csv
"""

import csv
import os
from urllib.parse import urlparse

class GPSCoordinatesManager:
    def __init__(self, coord_file_path):
        self.coord_file = coord_file_path
        self.coordinates_data = self._load_coordinates()
    
    def _load_coordinates(self):
        """Charge les coordonnées depuis le fichier CSV"""
        if not os.path.exists(self.coord_file):
            print(f"❌ Fichier de coordonnées non trouvé: {self.coord_file}")
            return {}
        
        coordinates = {}
        
        try:
            with open(self.coord_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    url = row.get('URL', '').strip()
                    lat = row.get('LAT', '').strip()
                    lng = row.get('LNG', '').strip()
                    geo_status = row.get('GEO_STATUS', '').strip()
                    
                    # Ne garder que les coordonnées valides
                    if url and lat and lng and geo_status == 'OK':
                        try:
                            lat_float = float(lat)
                            lng_float = float(lng)
                            
                            # Vérifier que les coordonnées sont dans une plage raisonnable pour la Belgique
                            if (49.0 <= lat_float <= 52.0) and (2.0 <= lng_float <= 7.0):
                                coordinates[url] = {
                                    'lat': lat_float,
                                    'lng': lng_float,
                                    'title': row.get('Title', ''),
                                    'province': row.get('Provincie', ''),
                                    'address': row.get('ADRESSE', '')
                                }
                        except ValueError:
                            continue
            
            print(f"📍 {len(coordinates)} coordonnées GPS chargées")
            return coordinates
            
        except Exception as e:
            print(f"❌ Erreur lors du chargement des coordonnées: {e}")
            return {}
    
    def get_coordinates(self, castle_url):
        """Récupère les coordonnées pour une URL de château"""
        if not castle_url:
            return None
        
        # Normaliser l'URL
        normalized_url = castle_url.strip().rstrip('/')
        
        # Recherche exacte
        if normalized_url in self.coordinates_data:
            coords = self.coordinates_data[normalized_url]
            return {
                'lat': coords['lat'],
                'lng': coords['lng'],
                'address': coords['address'],
                'has_coordinates': True
            }
        
        # Recherche par correspondance partielle
        url_path = urlparse(normalized_url).path
        for stored_url, coords in self.coordinates_data.items():
            stored_path = urlparse(stored_url).path
            if url_path == stored_path:
                return {
                    'lat': coords['lat'],
                    'lng': coords['lng'],
                    'address': coords['address'],
                    'has_coordinates': True
                }
        
        return {
            'lat': None,
            'lng': None,
            'address': '',
            'has_coordinates': False
        }
    
    def generate_google_maps_embed(self, castle_name, castle_url, address=""):
        """Génère l'URL d'embed Google Maps"""
        coords = self.get_coordinates(castle_url)
        
        if coords['has_coordinates']:
            # Utiliser les coordonnées GPS précises
            lat, lng = coords['lat'], coords['lng']
            embed_url = f"https://www.google.com/maps/embed/v1/view?key=YOUR_API_KEY&center={lat},{lng}&zoom=15&maptype=roadmap"
            
            return {
                'embed_url': embed_url,
                'search_url': f"https://www.google.com/maps/search/{lat},{lng}",
                'directions_url': f"https://www.google.com/maps/dir//{lat},{lng}",
                'coordinates': {'lat': lat, 'lng': lng},
                'address': coords['address'] or address,
                'has_precise_location': True
            }
        else:
            # Utiliser l'adresse ou le nom du château
            search_query = address if address else f"{castle_name}, Belgique"
            encoded_query = search_query.replace(' ', '%20')
            
            embed_url = f"https://www.google.com/maps/embed/v1/place?key=YOUR_API_KEY&q={encoded_query}"
            
            return {
                'embed_url': embed_url,
                'search_url': f"https://www.google.com/maps/search/{encoded_query}",
                'directions_url': f"https://www.google.com/maps/dir//{encoded_query}",
                'coordinates': None,
                'address': address,
                'has_precise_location': False
            }
    
    def get_nearby_castles(self, castle_url, radius_km=50, max_results=5):
        """Trouve les châteaux à proximité"""
        coords = self.get_coordinates(castle_url)
        
        if not coords['has_coordinates']:
            return []
        
        import math
        
        def calculate_distance(lat1, lng1, lat2, lng2):
            """Calcule la distance entre deux points GPS en km"""
            R = 6371  # Rayon de la Terre en km
            
            dlat = math.radians(lat2 - lat1)
            dlng = math.radians(lng2 - lng1)
            
            a = (math.sin(dlat/2) * math.sin(dlat/2) + 
                 math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * 
                 math.sin(dlng/2) * math.sin(dlng/2))
            
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
            return R * c
        
        nearby_castles = []
        base_lat, base_lng = coords['lat'], coords['lng']
        
        for url, castle_data in self.coordinates_data.items():
            if url == castle_url:  # Exclure le château actuel
                continue
            
            distance = calculate_distance(
                base_lat, base_lng,
                castle_data['lat'], castle_data['lng']
            )
            
            if distance <= radius_km:
                nearby_castles.append({
                    'title': castle_data['title'],
                    'url': url,
                    'distance': round(distance, 1),
                    'province': castle_data['province'],
                    'coordinates': {
                        'lat': castle_data['lat'],
                        'lng': castle_data['lng']
                    }
                })
        
        # Trier par distance
        nearby_castles.sort(key=lambda x: x['distance'])
        return nearby_castles[:max_results]

# Test de la classe
if __name__ == "__main__":
    coord_file = "/Users/marc/Desktop/kastelenbelgie/chateaux_coord.csv"
    gps_manager = GPSCoordinatesManager(coord_file)
    
    # Test avec quelques châteaux
    test_urls = [
        "https://kastelenbelgie.be/nl/kasteel-van-freyr-freyr/",
        "https://kastelenbelgie.be/nl/kasteel-beauregard-froyennes/",
        "https://kastelenbelgie.be/nl/hof-ter-borght-westmeerbeek/"
    ]
    
    for url in test_urls:
        print(f"\n🏰 Test pour: {url}")
        
        # Récupérer les coordonnées
        coords = gps_manager.get_coordinates(url)
        print(f"  📍 Coordonnées: {coords}")
        
        # Générer la carte
        maps_data = gps_manager.generate_google_maps_embed("Test Castle", url, "Test Address")
        print(f"  🗺️ Carte: {maps_data['has_precise_location']}")
        
        # Trouver les châteaux à proximité
        nearby = gps_manager.get_nearby_castles(url, 30, 3)
        print(f"  🏰 Châteaux à proximité: {len(nearby)}")
        for castle in nearby:
            print(f"    - {castle['title']} ({castle['distance']} km)")
