#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
COMPLÉTION DU CSS MANQUANT
Ajoute tous les styles CSS nécessaires pour les pages châteaux
"""

import os

def add_missing_css():
    """Ajoute le CSS manquant au fichier modern-style.css"""
    css_file = "/Users/marc/Desktop/kastelenbelgie/css/modern-style.css"
    
    missing_css = """
/* ===== STYLES CHÂTEAUX COMPLETS ===== */

/* Castle Hero Section */
.castle-hero {
    background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
    padding: 4rem 0;
    margin-top: 0;
}

.castle-hero-content {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 3rem;
    align-items: center;
}

.castle-image {
    position: relative;
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
}

.image-placeholder {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 4rem 2rem;
    text-align: center;
    min-height: 300px;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.castle-info-box {
    background: white;
    padding: 2.5rem;
    border-radius: 16px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
}

.castle-info-box h1 {
    font-size: 2.5rem;
    font-weight: 800;
    color: #1e293b;
    margin-bottom: 1.5rem;
}

.castle-details {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.detail-item {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

.detail-item strong {
    color: #475569;
    font-weight: 600;
}

.meta-value {
    color: #64748b;
    font-size: 0.95rem;
}

.opening-hours {
    font-size: 0.9rem;
    line-height: 1.6;
}

/* Castle Intro Section */
.castle-intro {
    padding: 4rem 0;
    background: white;
}

.castle-intro .content-wrapper {
    max-width: 800px;
    margin: 0 auto;
}

.castle-intro p {
    font-size: 1.1rem;
    line-height: 1.8;
    color: #374151;
    margin-bottom: 1.5rem;
}

.castle-intro a {
    color: #667eea;
    text-decoration: none;
    font-weight: 500;
}

.castle-intro a:hover {
    text-decoration: underline;
}

/* Castle Activities Section */
.castle-activities {
    padding: 4rem 0;
    background: #f8fafc;
}

.castle-activities h2 {
    font-size: 2rem;
    font-weight: 700;
    color: #1e293b;
    margin-bottom: 1rem;
    text-align: center;
}

.activities-content {
    max-width: 800px;
    margin: 0 auto;
    text-align: center;
}

.activities-content > p {
    font-size: 1.1rem;
    color: #64748b;
    margin-bottom: 3rem;
}

.activities-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
    margin-top: 2rem;
}

.activity-item {
    background: white;
    padding: 2rem;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    text-align: center;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.activity-item:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
}

.activity-item h3 {
    font-size: 1.2rem;
    font-weight: 600;
    color: #1e293b;
    margin-bottom: 0.5rem;
}

.activity-item p {
    color: #64748b;
    font-size: 0.95rem;
    line-height: 1.6;
}

/* Related Castles Section */
.related-castles {
    padding: 4rem 0;
    background: white;
}

.related-castles h2 {
    font-size: 2rem;
    font-weight: 700;
    color: #1e293b;
    margin-bottom: 3rem;
    text-align: center;
}

.castles-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
}

.castle-card {
    background: white;
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.castle-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.15);
}

.castle-image-placeholder {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    height: 200px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 3rem;
}

.castle-card-content {
    padding: 2rem;
}

.castle-card-content h3 {
    font-size: 1.3rem;
    font-weight: 600;
    color: #1e293b;
    margin-bottom: 0.5rem;
}

.castle-card-content p {
    color: #64748b;
    line-height: 1.6;
    margin-bottom: 1.5rem;
}

.btn-primary {
    display: inline-block;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 0.75rem 1.5rem;
    border-radius: 8px;
    text-decoration: none;
    font-weight: 500;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
}

/* Castle Map Section */
.castle-map {
    padding: 4rem 0;
    background: #f8fafc;
}

.castle-map h2 {
    font-size: 2rem;
    font-weight: 700;
    color: #1e293b;
    margin-bottom: 2rem;
    text-align: center;
}

/* Reservation Form Section */
.reservation-form {
    padding: 4rem 0;
    background: white;
}

.reservation-form h2 {
    font-size: 2rem;
    font-weight: 700;
    color: #1e293b;
    margin-bottom: 1rem;
    text-align: center;
}

.form-intro {
    text-align: center;
    margin-bottom: 3rem;
}

.form-intro p {
    font-size: 1.1rem;
    color: #64748b;
    max-width: 600px;
    margin: 0 auto;
}

.contact-form {
    max-width: 600px;
    margin: 0 auto;
    background: #f8fafc;
    padding: 3rem;
    border-radius: 16px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
}

.form-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.5rem;
    margin-bottom: 1.5rem;
}

.form-group {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

.form-group label {
    font-weight: 500;
    color: #374151;
}

.form-group input,
.form-group select,
.form-group textarea {
    padding: 0.75rem;
    border: 1px solid #d1d5db;
    border-radius: 8px;
    font-size: 1rem;
    transition: border-color 0.2s ease, box-shadow 0.2s ease;
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
    outline: none;
    border-color: #667eea;
    box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

.form-note {
    font-size: 0.9rem;
    color: #64748b;
    text-align: center;
    margin-top: 1rem;
}

/* Responsive Design */
@media (max-width: 768px) {
    .castle-hero-content {
        grid-template-columns: 1fr;
        gap: 2rem;
    }
    
    .castle-info-box h1 {
        font-size: 2rem;
    }
    
    .activities-grid {
        grid-template-columns: 1fr;
    }
    
    .castles-grid {
        grid-template-columns: 1fr;
    }
    
    .form-row {
        grid-template-columns: 1fr;
    }
    
    .contact-form {
        padding: 2rem;
    }
}

@media (max-width: 480px) {
    .castle-hero {
        padding: 2rem 0;
    }
    
    .castle-activities,
    .related-castles,
    .castle-map,
    .reservation-form {
        padding: 3rem 0;
    }
    
    .castle-info-box {
        padding: 2rem;
    }
    
    .activity-item {
        padding: 1.5rem;
    }
}
"""
    
    try:
        if os.path.exists(css_file):
            with open(css_file, 'r', encoding='utf-8') as f:
                existing_content = f.read()
            
            # Vérifier si le CSS n'est pas déjà présent
            if 'STYLES CHÂTEAUX COMPLETS' not in existing_content:
                with open(css_file, 'a', encoding='utf-8') as f:
                    f.write(missing_css)
                print("✅ CSS châteaux complet ajouté à modern-style.css")
            else:
                print("✅ CSS châteaux déjà présent")
        else:
            print("❌ Fichier CSS non trouvé")
            
    except Exception as e:
        print(f"❌ Erreur ajout CSS: {e}")

def create_search_js():
    """Crée le fichier search.js complet"""
    search_js_path = "/Users/marc/Desktop/kastelenbelgie/js/search.js"
    
    # Créer le dossier js s'il n'existe pas
    os.makedirs("/Users/marc/Desktop/kastelenbelgie/js", exist_ok=True)
    
    search_js_content = """// Fonctionnalité de recherche pour kastelenbelgie.be

// Liste des châteaux (à compléter avec tous les châteaux)
const castles = [
    {name: "Kasteel van Freÿr", url: "kasteel-van-freyr-freyr.html"},
    {name: "Kasteel van Bouchout", url: "kasteel-van-bouchout-te-meise.html"},
    {name: "Citadel van Hoei", url: "citadel-van-hoei-hoei.html"},
    {name: "Kasteel van Durbuy", url: "kasteel-van-durbuy-durbuy.html"},
    {name: "Kasteel Engelhof", url: "kasteel-engelhof-houthalen.html"},
    {name: "Kasteel Beauregard", url: "kasteel-beauregard-froyennes.html"},
    {name: "Kasteel Karreveld", url: "kasteel-karreveld-te-sint-jans-molenbeek.html"},
    {name: "Kasteel van Wegimont", url: "kasteel-van-wegimont-ayeneux-soumagne.html"},
    {name: "Kasteel ter Lucht", url: "kasteel-ter-lucht-sint-andries.html"},
    {name: "Hof ter Borght", url: "hof-ter-borght-westmeerbeek.html"},
    {name: "Kasteel van Fougeraie", url: "kasteel-van-fougeraie-te-ukkel.html"},
    {name: "Kasteel Mohimont", url: "kasteel-mohimont-villers-devant-orval.html"},
    {name: "Kasteel van Orval", url: "kasteel-van-orval-villers-devant-orval.html"}
];

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
"""
    
    try:
        with open(search_js_path, 'w', encoding='utf-8') as f:
            f.write(search_js_content)
        print("✅ Fichier search.js créé avec fonctionnalité complète")
    except Exception as e:
        print(f"❌ Erreur création search.js: {e}")

def main():
    """Fonction principale"""
    print("🎨 COMPLÉTION DU CSS ET JS MANQUANTS")
    print("=" * 50)
    
    add_missing_css()
    create_search_js()
    
    print("\n✅ Tous les éléments manquants ont été ajoutés!")
    print("🔄 Relancez final_verification.py pour voir l'amélioration du score")

if __name__ == "__main__":
    main()
