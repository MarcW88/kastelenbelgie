#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SCRAPER WIKIPEDIA AVANCÉ POUR CHÂTEAUX
Recherche approfondie et contenu unique 300+ mots minimum
"""

import requests
import time
import re
from difflib import SequenceMatcher
from urllib.parse import quote

class AdvancedWikipediaScraper:
    def __init__(self):
        self.fr_api = "https://fr.wikipedia.org/w/api.php"
        self.nl_api = "https://nl.wikipedia.org/w/api.php"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'KastelenBelgie/1.0 (contact@kastelenbelgie.be)'
        })
    
    def similarity(self, a, b):
        """Calcule la similarité entre deux chaînes"""
        return SequenceMatcher(None, a.lower(), b.lower()).ratio()
    
    def clean_castle_name(self, name):
        """Nettoie le nom du château pour la recherche"""
        # Supprimer les mots communs
        common_words = ['kasteel', 'château', 'castle', 'van', 'de', 'du', 'der', 'het', 'le', 'la']
        words = name.lower().split()
        cleaned_words = [w for w in words if w not in common_words and len(w) > 2]
        return ' '.join(cleaned_words)
    
    def generate_search_terms(self, castle_name, province="", city=""):
        """Génère une liste de termes de recherche optimisés"""
        base_name = castle_name.strip()
        cleaned_name = self.clean_castle_name(castle_name)
        
        search_terms = []
        
        # Termes de base - PRIORITÉ AUX NOMS SIMPLES
        search_terms.extend([
            cleaned_name,  # Nom simple en premier (ex: "Durbuy")
            base_name,
            f"kasteel {cleaned_name}",
            f"château {cleaned_name}",
            f"castle {cleaned_name}"
        ])
        
        # Avec localisation
        if province:
            search_terms.extend([
                f"{cleaned_name} {province}",
                f"{base_name} {province}",
                f"château {cleaned_name} {province}"
            ])
        
        if city:
            search_terms.extend([
                f"{cleaned_name} {city}",
                f"{base_name} {city}"
            ])
        
        # Variantes orthographiques
        if "kasteel" in base_name.lower():
            french_variant = base_name.lower().replace("kasteel", "château")
            search_terms.append(french_variant)
        
        # Extraire juste le nom de la ville/lieu depuis le nom du château
        if "van" in base_name.lower():
            city_part = base_name.lower().split("van")[-1].strip()
            if len(city_part) > 3:
                search_terms.insert(0, city_part)  # Priorité haute
        
        # Supprimer les doublons et garder l'ordre (plus spécifique d'abord)
        seen = set()
        unique_terms = []
        for term in search_terms:
            if term.lower() not in seen:
                seen.add(term.lower())
                unique_terms.append(term)
        
        return unique_terms
    
    def search_wikipedia_pages(self, search_terms, language='nl'):
        """Recherche des pages sur Wikipedia"""
        api_url = self.nl_api if language == 'nl' else self.fr_api
        
        for term in search_terms[:10]:  # Limiter à 10 termes
            try:
                params = {
                    'action': 'query',
                    'format': 'json',
                    'list': 'search',
                    'srsearch': term,
                    'srlimit': 5,
                    'srwhat': 'text'
                }
                
                response = self.session.get(api_url, params=params, timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    search_results = data.get('query', {}).get('search', [])
                    
                    # Filtrer les résultats pertinents
                    for result in search_results:
                        title = result['title']
                        snippet = result.get('snippet', '')
                        
                        # Vérifier la pertinence
                        if self.is_castle_related(title, snippet):
                            similarity_score = self.similarity(term, title)
                            if similarity_score > 0.2:  # Seuil de similarité réduit
                                return title, language, similarity_score
                
                time.sleep(0.5)  # Respecter les limites
                
            except Exception as e:
                print(f"Erreur recherche {term}: {e}")
                continue
        
        return None, None, 0
    
    def is_castle_related(self, title, snippet):
        """Vérifie si le résultat est lié à un château"""
        castle_keywords = [
            'château', 'kasteel', 'castle', 'fort', 'forteresse', 
            'burcht', 'slot', 'manor', 'manoir', 'palais', 'palace'
        ]
        
        text = f"{title} {snippet}".lower()
        return any(keyword in text for keyword in castle_keywords)
    
    def get_full_wikipedia_content(self, page_title, language='nl'):
        """Récupère le contenu complet d'une page Wikipedia"""
        api_url = self.nl_api if language == 'nl' else self.fr_api
        
        try:
            # Récupérer le contenu complet
            params = {
                'action': 'query',
                'format': 'json',
                'titles': page_title,
                'prop': 'extracts|pageimages',
                'exintro': False,  # Récupérer tout l'article
                'explaintext': True,
                'exsectionformat': 'plain',
                'piprop': 'original'
            }
            
            response = self.session.get(api_url, params=params, timeout=15)
            if response.status_code == 200:
                data = response.json()
                pages = data.get('query', {}).get('pages', {})
                
                for page_id, page_info in pages.items():
                    if 'extract' in page_info:
                        content = page_info['extract']
                        image_url = page_info.get('pageimages', {}).get('original', {}).get('source', '')
                        
                        return {
                            'content': content,
                            'image_url': image_url,
                            'title': page_title,
                            'language': language,
                            'word_count': len(content.split())
                        }
            
            return None
            
        except Exception as e:
            print(f"Erreur récupération contenu {page_title}: {e}")
            return None
    
    def process_wikipedia_content(self, content, target_words=300):
        """Traite et optimise le contenu Wikipedia pour atteindre 300+ mots"""
        if not content:
            return []
        
        # Nettoyer le contenu plus agressivement
        content = re.sub(r'\[.*?\]', '', content)  # Supprimer les références
        content = re.sub(r'\(.*?\)', '', content)  # Supprimer les parenthèses
        content = re.sub(r'\s+', ' ', content).strip()  # Normaliser les espaces
        
        # Diviser en phrases (plus permissif)
        sentences = re.split(r'[.!?]+', content)
        sentences = [s.strip() for s in sentences if len(s.strip()) > 15]  # Seuil plus bas
        
        if not sentences:
            return []
        
        # Prendre TOUT le contenu disponible pour atteindre 300+ mots
        total_words = sum(len(s.split()) for s in sentences)
        
        if total_words < 50:
            # Vraiment pas assez de contenu
            return []
        
        # Créer des paragraphes plus longs pour atteindre 300+ mots
        if total_words >= target_words:
            # Diviser en 3 paragraphes équilibrés
            words_per_paragraph = total_words // 3
            paragraphs = []
            current_paragraph = []
            current_word_count = 0
            
            for sentence in sentences:
                sentence_words = len(sentence.split())
                current_paragraph.append(sentence)
                current_word_count += sentence_words
                
                # Finaliser le paragraphe quand on atteint la taille cible
                if current_word_count >= words_per_paragraph and len(paragraphs) < 2:
                    paragraph_text = '. '.join(current_paragraph) + '.'
                    paragraphs.append(paragraph_text)
                    current_paragraph = []
                    current_word_count = 0
            
            # Ajouter le dernier paragraphe avec tout le reste
            if current_paragraph:
                paragraph_text = '. '.join(current_paragraph) + '.'
                paragraphs.append(paragraph_text)
        else:
            # Contenu plus court, créer 2 paragraphes plus longs
            mid_point = len(sentences) // 2
            paragraphs = [
                '. '.join(sentences[:mid_point]) + '.',
                '. '.join(sentences[mid_point:]) + '.'
            ]
        
        # S'assurer d'avoir au moins 2 paragraphes
        while len(paragraphs) < 2:
            if len(paragraphs) == 1:
                # Diviser le premier paragraphe en deux
                first_sentences = paragraphs[0].split('. ')
                if len(first_sentences) > 2:
                    mid = len(first_sentences) // 2
                    paragraphs = [
                        '. '.join(first_sentences[:mid]) + '.',
                        '. '.join(first_sentences[mid:])
                    ]
                else:
                    paragraphs.append("Dit monument vormt een belangrijk onderdeel van het Belgische erfgoed.")
            else:
                paragraphs.append("Deze historische site blijft een belangrijke getuige van het verleden.")
        
        return paragraphs[:3]  # Maximum 3 paragraphes
    
    def translate_to_dutch(self, text):
        """Traduit le texte français en néerlandais (traduction basique)"""
        # Dictionnaire de traduction des mots clés château
        translations = {
            'château': 'kasteel',
            'Château': 'Kasteel',
            'château de': 'kasteel van',
            'Château de': 'Kasteel van',
            'château du': 'kasteel van de',
            'Château du': 'Kasteel van de',
            'forteresse': 'vesting',
            'architecture': 'architectuur',
            'siècle': 'eeuw',
            'siècles': 'eeuwen',
            'histoire': 'geschiedenis',
            'historique': 'historisch',
            'construction': 'bouw',
            'bâtiment': 'gebouw',
            'édifice': 'gebouw',
            'monument': 'monument',
            'patrimoine': 'erfgoed',
            'visiteurs': 'bezoekers',
            'visite': 'bezoek',
            'aujourd\'hui': 'vandaag de dag',
            'actuellement': 'momenteel',
            'propriétaire': 'eigenaar',
            'famille': 'familie',
            'période': 'periode',
            'époque': 'tijdperk',
            'style': 'stijl',
            'gothique': 'gotisch',
            'renaissance': 'renaissance',
            'baroque': 'barok',
            'médiéval': 'middeleeuws',
            'médiévale': 'middeleeuwse',
            'région': 'regio',
            'province': 'provincie',
            'commune': 'gemeente',
            'ville': 'stad',
            'village': 'dorp',
            'Belgique': 'België',
            'belge': 'Belgisch',
            'français': 'Frans',
            'française': 'Franse',
            'flamand': 'Vlaams',
            'flamande': 'Vlaamse',
            'wallon': 'Waals',
            'wallonne': 'Waalse'
        }
        
        # Appliquer les traductions
        translated_text = text
        for french, dutch in translations.items():
            translated_text = translated_text.replace(french, dutch)
        
        return translated_text
    
    def scrape_castle_info(self, castle_name, province="", city=""):
        """Fonction principale pour scraper les informations d'un château"""
        print(f"🔍 Recherche Wikipedia pour: {castle_name}")
        
        # Générer les termes de recherche
        search_terms = self.generate_search_terms(castle_name, province, city)
        print(f"  📝 Termes de recherche: {search_terms[:3]}...")
        
        # Rechercher d'abord en néerlandais
        page_title, language, similarity = self.search_wikipedia_pages(search_terms, 'nl')
        
        # Si pas trouvé en néerlandais, essayer en français
        if not page_title:
            page_title, language, similarity = self.search_wikipedia_pages(search_terms, 'fr')
        
        if page_title:
            print(f"  ✅ Trouvé: {page_title} ({language}) - Similarité: {similarity:.2f}")
            
            # Récupérer le contenu complet
            wiki_data = self.get_full_wikipedia_content(page_title, language)
            
            if wiki_data and wiki_data['word_count'] > 20:
                # Traiter le contenu
                paragraphs = self.process_wikipedia_content(wiki_data['content'], 300)
                
                # Si le contenu est en français, le traduire en néerlandais
                if language == 'fr':
                    print(f"  🔄 Traduction FR → NL en cours...")
                    paragraphs = [self.translate_to_dutch(p) for p in paragraphs]
                
                total_words = sum(len(p.split()) for p in paragraphs)
                print(f"  📄 Contenu généré: {total_words} mots en {len(paragraphs)} paragraphes")
                
                return {
                    'paragraphs': paragraphs,
                    'source_title': page_title,
                    'source_language': language,
                    'word_count': total_words,
                    'image_url': wiki_data.get('image_url', ''),
                    'similarity_score': similarity
                }
        
        print(f"  ❌ Pas trouvé sur Wikipedia")
        return None

# Test de la classe
if __name__ == "__main__":
    scraper = AdvancedWikipediaScraper()
    
    # Test avec quelques châteaux
    test_castles = [
        ("Kasteel van Freyr", "Namen", "Hastière"),
        ("Kasteel van Durbuy", "Luxemburg", "Durbuy"),
        ("Kasteel Beauregard", "Henegouwen", "Froyennes")
    ]
    
    for castle_name, province, city in test_castles:
        print(f"\n{'='*60}")
        result = scraper.scrape_castle_info(castle_name, province, city)
        if result:
            print(f"Résultat pour {castle_name}:")
            for i, paragraph in enumerate(result['paragraphs'], 1):
                print(f"Paragraphe {i}: {paragraph[:100]}...")
        time.sleep(2)
