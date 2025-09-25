#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SCRAPER WIKIPEDIA SPÉCIFIQUE AUX CHÂTEAUX
Recherche UNIQUEMENT du contenu spécifique aux châteaux, pas de contenu générique
"""

import requests
import time
import re
from difflib import SequenceMatcher

class CastleSpecificScraper:
    def __init__(self):
        self.nl_api = "https://nl.wikipedia.org/api.php"
        self.fr_api = "https://fr.wikipedia.org/api.php"
        
    def scrape_castle_specific_content(self, castle_name, province):
        """Recherche du contenu spécifiquement lié au château"""
        print(f"🔍 Recherche spécifique pour: {castle_name}")
        
        # Étape 1: Recherche directe du château
        direct_result = self.search_direct_castle(castle_name, province)
        if direct_result and self.is_castle_specific_content(direct_result['content'], castle_name):
            print(f"  ✅ Contenu spécifique trouvé: {direct_result['source']} ({direct_result['word_count']} mots)")
            return direct_result
        
        # Étape 2: Recherche avec variantes du nom
        variant_result = self.search_castle_variants(castle_name, province)
        if variant_result and self.is_castle_specific_content(variant_result['content'], castle_name):
            print(f"  ✅ Contenu spécifique trouvé via variante: {variant_result['source']} ({variant_result['word_count']} mots)")
            return variant_result
        
        # Étape 3: Recherche dans listes de châteaux
        list_result = self.search_in_castle_lists(castle_name, province)
        if list_result and len(list_result['content']) > 100:
            print(f"  ✅ Contenu trouvé dans liste: {list_result['source']} ({list_result['word_count']} mots)")
            return list_result
        
        print(f"  ❌ Aucun contenu spécifique trouvé pour {castle_name}")
        return None
    
    def search_direct_castle(self, castle_name, province):
        """Recherche directe du château sur Wikipedia"""
        search_terms = self.generate_castle_search_terms(castle_name)
        
        for term in search_terms[:5]:  # Limiter à 5 termes les plus pertinents
            for lang in ['nl', 'fr']:
                api_url = self.nl_api if lang == 'nl' else self.fr_api
                
                try:
                    # Recherche de pages
                    search_params = {
                        'action': 'query',
                        'format': 'json',
                        'list': 'search',
                        'srsearch': term,
                        'srlimit': 5
                    }
                    
                    response = requests.get(api_url, params=search_params, timeout=10)
                    data = response.json()
                    
                    if 'query' in data and 'search' in data['query']:
                        for result in data['query']['search']:
                            page_title = result['title']
                            
                            # Vérifier si c'est vraiment un château
                            if self.is_likely_castle_page(page_title, castle_name):
                                content = self.get_page_content(page_title, lang)
                                if content and len(content) > 200:
                                    return {
                                        'content': content,
                                        'source': f"{page_title} ({lang})",
                                        'word_count': len(content.split()),
                                        'language': lang
                                    }
                    
                    time.sleep(0.5)  # Respecter les limites API
                    
                except Exception as e:
                    print(f"    Erreur recherche {term} ({lang}): {e}")
                    continue
        
        return None
    
    def search_castle_variants(self, castle_name, province):
        """Recherche avec des variantes du nom du château"""
        variants = self.generate_castle_variants(castle_name)
        
        for variant in variants[:3]:
            result = self.search_direct_castle(variant, province)
            if result:
                return result
        
        return None
    
    def search_in_castle_lists(self, castle_name, province):
        """Recherche dans les listes de châteaux"""
        list_terms = [
            f"Lijst van kastelen in {province}",
            f"Kastelen in {province}",
            f"Liste des châteaux de {province}",
            "Lijst van kastelen in België",
            "Liste des châteaux de Belgique"
        ]
        
        for term in list_terms:
            for lang in ['nl', 'fr']:
                api_url = self.nl_api if lang == 'nl' else self.fr_api
                
                try:
                    content = self.get_page_content(term, lang)
                    if content:
                        # Extraire la section spécifique au château
                        castle_section = self.extract_castle_from_list(content, castle_name)
                        if castle_section and len(castle_section) > 100:
                            return {
                                'content': castle_section,
                                'source': f"{term} ({lang})",
                                'word_count': len(castle_section.split()),
                                'language': lang
                            }
                    
                    time.sleep(0.5)
                    
                except Exception as e:
                    continue
        
        return None
    
    def generate_castle_search_terms(self, castle_name):
        """Génère des termes de recherche spécifiques aux châteaux"""
        base_name = castle_name.strip()
        clean_name = self.clean_castle_name(castle_name)
        
        terms = [
            base_name,  # Nom exact
            clean_name,  # Nom nettoyé
        ]
        
        # Variantes linguistiques
        if "kasteel" in base_name.lower():
            french_name = base_name.lower().replace("kasteel", "château").title()
            terms.append(french_name)
        
        if "château" in base_name.lower():
            dutch_name = base_name.lower().replace("château", "kasteel").title()
            terms.append(dutch_name)
        
        return terms
    
    def generate_castle_variants(self, castle_name):
        """Génère des variantes du nom du château"""
        variants = []
        base_name = castle_name.lower()
        
        # Extraire le nom principal
        if "van" in base_name:
            main_part = base_name.split("van")[-1].strip()
            if len(main_part) > 3:
                variants.extend([
                    f"Kasteel {main_part}",
                    f"Château de {main_part}",
                    main_part.title()
                ])
        
        if "de" in base_name:
            main_part = base_name.split("de")[-1].strip()
            if len(main_part) > 3:
                variants.extend([
                    f"Kasteel de {main_part}",
                    f"Château de {main_part}",
                    main_part.title()
                ])
        
        return variants
    
    def clean_castle_name(self, name):
        """Nettoie le nom du château"""
        # Supprimer les mots courants
        common_words = ['kasteel', 'château', 'castle', 'van', 'de', 'du', 'te', 'in']
        words = name.lower().split()
        cleaned_words = [w for w in words if w not in common_words and len(w) > 2]
        return ' '.join(cleaned_words).title()
    
    def is_likely_castle_page(self, page_title, castle_name):
        """Vérifie si la page est probablement sur le château recherché"""
        page_lower = page_title.lower()
        castle_lower = castle_name.lower()
        
        # Mots-clés château
        castle_keywords = ['kasteel', 'château', 'castle', 'burcht', 'slot', 'hof']
        
        # Vérifier si c'est une page de château
        has_castle_keyword = any(keyword in page_lower for keyword in castle_keywords)
        
        # Vérifier la similarité du nom
        similarity = SequenceMatcher(None, page_lower, castle_lower).ratio()
        
        # Extraire les mots principaux du nom du château
        castle_words = [w for w in castle_lower.split() if len(w) > 3 and w not in ['kasteel', 'château', 'castle']]
        has_main_word = any(word in page_lower for word in castle_words)
        
        return (has_castle_keyword and similarity > 0.3) or (has_main_word and similarity > 0.2)
    
    def is_castle_specific_content(self, content, castle_name):
        """Vérifie si le contenu est spécifique au château"""
        content_lower = content.lower()
        castle_lower = castle_name.lower()
        
        # Mots-clés château
        castle_keywords = ['kasteel', 'château', 'castle', 'burcht', 'slot']
        
        # Mots-clés architecture
        architecture_keywords = ['gebouwd', 'architectuur', 'bouw', 'constructie', 'renovatie', 'restauratie']
        
        # Vérifier la présence de mots-clés château
        has_castle_keywords = sum(1 for keyword in castle_keywords if keyword in content_lower) >= 2
        
        # Vérifier la présence de mots-clés architecture
        has_architecture = any(keyword in content_lower for keyword in architecture_keywords)
        
        # Vérifier que ce n'est pas du contenu générique sur une ville
        city_indicators = ['gemeente', 'stad', 'inwoners', 'oppervlakte', 'burgemeester', 'voetbalclub']
        is_city_content = sum(1 for indicator in city_indicators if indicator in content_lower) > 3
        
        # Extraire les mots principaux du château
        castle_words = [w for w in castle_lower.split() if len(w) > 3 and w not in ['kasteel', 'château', 'castle', 'van', 'de']]
        has_castle_name = any(word in content_lower for word in castle_words)
        
        return (has_castle_keywords or has_architecture) and not is_city_content and has_castle_name
    
    def get_page_content(self, page_title, language='nl'):
        """Récupère le contenu d'une page Wikipedia"""
        api_url = self.nl_api if language == 'nl' else self.fr_api
        
        try:
            params = {
                'action': 'query',
                'format': 'json',
                'titles': page_title,
                'prop': 'extracts',
                'exintro': True,
                'explaintext': True,
                'exsectionformat': 'plain'
            }
            
            response = requests.get(api_url, params=params, timeout=10)
            data = response.json()
            
            if 'query' in data and 'pages' in data['query']:
                for page_id, page_data in data['query']['pages'].items():
                    if 'extract' in page_data and page_data['extract']:
                        content = page_data['extract'].strip()
                        if len(content) > 100:
                            return content
            
            return None
            
        except Exception as e:
            print(f"Erreur récupération {page_title}: {e}")
            return None
    
    def extract_castle_from_list(self, list_content, castle_name):
        """Extrait la section spécifique au château depuis une liste"""
        lines = list_content.split('\n')
        castle_section = []
        found_castle = False
        
        # Mots principaux du château
        castle_words = [w.lower() for w in castle_name.split() if len(w) > 3]
        
        for line in lines:
            line_lower = line.lower()
            
            # Vérifier si cette ligne mentionne notre château
            if any(word in line_lower for word in castle_words):
                found_castle = True
                castle_section.append(line)
            elif found_castle and line.strip():
                # Continuer à collecter les lignes suivantes si elles semblent liées
                if any(keyword in line_lower for keyword in ['kasteel', 'château', 'gebouwd', 'eeuw', 'architectuur']):
                    castle_section.append(line)
                else:
                    break
        
        return '\n'.join(castle_section) if castle_section else None
    
    def process_castle_content(self, content, target_words=300):
        """Traite le contenu spécifique au château"""
        if not content:
            return []
        
        # Nettoyer le contenu
        content = re.sub(r'\[.*?\]', '', content)  # Supprimer les références
        content = re.sub(r'\s+', ' ', content).strip()
        
        # Diviser en phrases
        sentences = re.split(r'[.!?]+', content)
        sentences = [s.strip() for s in sentences if len(s.strip()) > 20]
        
        if not sentences:
            return []
        
        # Créer des paragraphes équilibrés
        total_words = sum(len(s.split()) for s in sentences)
        
        if total_words < 100:
            return []
        
        # Diviser en 2-3 paragraphes selon la longueur
        if total_words >= 300:
            # 3 paragraphes
            sentences_per_paragraph = len(sentences) // 3
            paragraphs = []
            
            for i in range(3):
                start_idx = i * sentences_per_paragraph
                if i == 2:  # Dernier paragraphe prend le reste
                    end_idx = len(sentences)
                else:
                    end_idx = (i + 1) * sentences_per_paragraph
                
                paragraph_sentences = sentences[start_idx:end_idx]
                if paragraph_sentences:
                    paragraph = '. '.join(paragraph_sentences) + '.'
                    paragraphs.append(paragraph)
        else:
            # 2 paragraphes
            mid_point = len(sentences) // 2
            paragraphs = [
                '. '.join(sentences[:mid_point]) + '.',
                '. '.join(sentences[mid_point:]) + '.'
            ]
        
        # S'assurer d'avoir au moins 2 paragraphes
        while len(paragraphs) < 2:
            paragraphs.append("Ce château représente un élément important du patrimoine architectural belge.")
        
        return paragraphs[:3]  # Maximum 3 paragraphes

if __name__ == "__main__":
    # Test
    scraper = CastleSpecificScraper()
    result = scraper.scrape_castle_specific_content("Kasteel van Durbuy", "Luxemburg")
    
    if result:
        paragraphs = scraper.process_castle_content(result['content'])
        print(f"\nRésultat: {len(paragraphs)} paragraphes")
        for i, p in enumerate(paragraphs, 1):
            print(f"{i}. {p[:100]}...")
    else:
        print("Aucun contenu spécifique trouvé")
