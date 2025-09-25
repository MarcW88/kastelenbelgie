#!/usr/bin/env python3
"""
Script pour compléter la liste de recherche avec tous les châteaux du site
"""

import os
import re
from pathlib import Path
from bs4 import BeautifulSoup

def extract_castle_info(html_file):
    """Extrait le nom et l'URL d'un château depuis son fichier HTML"""
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        # Extraire le nom depuis le title
        title_tag = soup.find('title')
        if title_tag:
            title = title_tag.get_text()
            # Nettoyer le titre (enlever " | kastelenbelgie.be")
            name = title.replace(' | kastelenbelgie.be', '').strip()
        else:
            # Fallback: utiliser le nom du fichier
            name = html_file.stem.replace('-', ' ').title()
        
        # URL relative
        url = html_file.name
        
        return {"name": name, "url": url}
    
    except Exception as e:
        print(f"⚠️  Erreur avec {html_file.name}: {e}")
        return None

def complete_search_list():
    """Génère la liste complète des châteaux pour search.js"""
    
    # Répertoire de travail
    base_dir = Path("/Users/marc/Desktop/kastelenbelgie")
    
    print("🔍 GÉNÉRATION DE LA LISTE COMPLÈTE DE RECHERCHE")
    print("=" * 55)
    
    castles = []
    
    # Parcourir tous les fichiers HTML
    for html_file in base_dir.glob("*.html"):
        # Ignorer les pages non-châteaux
        if html_file.name in ['index.html', 'contact.html', 'blog.html', 'provinces.html', 
                             'antwerpen.html', 'limburg.html', 'oost-vlaanderen.html', 
                             'west-vlaanderen.html', 'vlaams-brabant.html', 'namen.html',
                             'luxemburg.html', 'luik.html', 'henegouwen.html', 'waals-brabant.html',
                             'admin.html', 'dashboard.html', 'login.html', 'register.html']:
            continue
        
        # Ignorer les articles de blog
        if html_file.name.startswith('blog-'):
            continue
            
        # Extraire les informations du château
        castle_info = extract_castle_info(html_file)
        if castle_info:
            castles.append(castle_info)
    
    # Trier par nom
    castles.sort(key=lambda x: x['name'])
    
    print(f"📊 {len(castles)} châteaux trouvés")
    
    # Générer le nouveau contenu JavaScript
    js_content = '''// Fonctionnalité de recherche pour kastelenbelgie.be

// Liste complète des châteaux (générée automatiquement)
const castles = [
'''
    
    for castle in castles:
        js_content += f'    {{name: "{castle["name"]}", url: "{castle["url"]}"}},\n'
    
    js_content += '''];

// Fonction de recherche
function searchCastles(query) {
    if (!query || query.length < 2) {
        return [];
    }
    
    const searchTerm = query.toLowerCase();
    return castles.filter(castle => 
        castle.name.toLowerCase().includes(searchTerm)
    ).slice(0, 8); // Limiter à 8 résultats
}

// Affichage des résultats
function displaySearchResults(results) {
    const resultsContainer = document.getElementById('search-results');
    
    if (!resultsContainer) {
        return;
    }
    
    if (results.length === 0) {
        resultsContainer.style.display = 'none';
        return;
    }
    
    resultsContainer.innerHTML = results.map(castle => `
        <div class="search-result-item">
            <a href="${castle.url}">
                <span class="castle-icon">🏰</span>
                <span class="castle-name">${castle.name}</span>
            </a>
        </div>
    `).join('');
    
    resultsContainer.style.display = 'block';
}

// Initialisation de la recherche
function initializeSearch() {
    const searchInput = document.getElementById('search-input');
    const searchResults = document.getElementById('search-results');
    
    if (!searchInput) {
        return;
    }
    
    // Créer le conteneur de résultats s'il n'existe pas
    if (!searchResults) {
        const resultsDiv = document.createElement('div');
        resultsDiv.id = 'search-results';
        resultsDiv.className = 'search-results';
        searchInput.parentNode.appendChild(resultsDiv);
    }
    
    // Event listener pour la saisie
    searchInput.addEventListener('input', function(e) {
        const query = e.target.value;
        const results = searchCastles(query);
        displaySearchResults(results);
    });
    
    // Masquer les résultats quand on clique ailleurs
    document.addEventListener('click', function(e) {
        if (!e.target.closest('.search-box')) {
            const resultsContainer = document.getElementById('search-results');
            if (resultsContainer) {
                resultsContainer.style.display = 'none';
            }
        }
    });
    
    // Empêcher la fermeture quand on clique dans la search box
    const searchBox = document.querySelector('.search-box');
    if (searchBox) {
        searchBox.addEventListener('click', function(e) {
            e.stopPropagation();
        });
    }
}

// Styles CSS pour les résultats de recherche
const searchStyles = `
.search-box {
    position: relative;
}

.search-results {
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
    z-index: 1000;
    max-height: 300px;
    overflow-y: auto;
    display: none;
}

.search-result-item {
    border-bottom: 1px solid #f1f5f9;
}

.search-result-item:last-child {
    border-bottom: none;
}

.search-result-item a {
    display: flex;
    align-items: center;
    padding: 0.75rem 1rem;
    text-decoration: none;
    color: #374151;
    transition: background-color 0.2s ease;
}

.search-result-item a:hover {
    background-color: #f8fafc;
}

.castle-icon {
    margin-right: 0.75rem;
    font-size: 1.2rem;
}

.castle-name {
    font-weight: 500;
}

.search-input {
    width: 100%;
    padding: 0.5rem 1rem;
    border: 1px solid #d1d5db;
    border-radius: 6px;
    font-size: 0.9rem;
    transition: border-color 0.2s ease, box-shadow 0.2s ease;
}

.search-input:focus {
    outline: none;
    border-color: #667eea;
    box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

@media (max-width: 768px) {
    .search-results {
        left: -100px;
        right: -100px;
    }
}
`;

// Ajouter les styles CSS
function addSearchStyles() {
    const styleSheet = document.createElement('style');
    styleSheet.textContent = searchStyles;
    document.head.appendChild(styleSheet);
}

// Initialiser quand le DOM est chargé
document.addEventListener('DOMContentLoaded', function() {
    addSearchStyles();
    initializeSearch();
});
'''
    
    # Sauvegarder le nouveau fichier search.js
    search_js_path = base_dir / "js" / "search.js"
    
    try:
        with open(search_js_path, 'w', encoding='utf-8') as f:
            f.write(js_content)
        
        print(f"✅ search.js mis à jour avec {len(castles)} châteaux")
        print(f"   Ancien: 13 châteaux")
        print(f"   Nouveau: {len(castles)} châteaux")
        print(f"   Amélioration: +{len(castles) - 13} châteaux")
        
    except Exception as e:
        print(f"❌ Erreur lors de la sauvegarde: {e}")
    
    print("\n🎉 Barre de recherche maintenant complète!")
    print("   - Recherche dans tous les châteaux du site")
    print("   - Résultats en temps réel")
    print("   - Interface moderne avec icônes")

if __name__ == "__main__":
    complete_search_list()
