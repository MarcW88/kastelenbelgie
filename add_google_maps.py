#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
AJOUT DE CARTES GOOGLE MAPS
Remplace les placeholders de cartes par de vraies cartes Google Maps
"""

import os
import re
import glob

def get_castle_info_from_page(content):
    """Extrait les informations du château depuis la page"""
    # Extraire le nom du château
    title_match = re.search(r'<title>([^|]+)', content)
    castle_name = title_match.group(1).strip() if title_match else "Château"
    
    # Extraire l'adresse
    address_match = re.search(r'<span class="meta-value">([^<]+(?:<br[^>]*>[^<]+)?)</span>', content)
    address = ""
    if address_match:
        address = address_match.group(1).replace('<br>', ', ').replace('<br/>', ', ').strip()
        # Nettoyer l'adresse
        address = re.sub(r'<[^>]+>', '', address)
    
    # Extraire la province
    province_match = re.search(r'<span class="meta-value">([^<]+)</span>', content)
    province = province_match.group(1).strip() if province_match else ""
    
    return castle_name, address, province

def create_google_maps_embed(castle_name, address, province):
    """Crée le code d'intégration Google Maps"""
    # Construire la requête de recherche
    if address and address != "Info volgt":
        search_query = f"{castle_name}, {address}"
    else:
        search_query = f"{castle_name}, {province}, Belgium"
    
    # Encoder pour URL
    search_query_encoded = search_query.replace(' ', '+').replace(',', '%2C')
    
    maps_html = f'''
            <div class="map-container">
                <div class="map-header">
                    <h3>📍 Locatie van {castle_name}</h3>
                    <p><strong>Adres:</strong> {address if address and address != "Info volgt" else f"{castle_name}, {province}"}</p>
                </div>
                <div class="google-map">
                    <iframe 
                        src="https://www.google.com/maps/embed/v1/place?key=YOUR_API_KEY&q={search_query_encoded}"
                        width="100%" 
                        height="400" 
                        style="border:0;" 
                        allowfullscreen="" 
                        loading="lazy" 
                        referrerpolicy="no-referrer-when-downgrade">
                    </iframe>
                </div>
                <div class="map-actions">
                    <a href="https://www.google.com/maps/search/{search_query_encoded}" target="_blank" class="btn-secondary">
                        🗺️ Open in Google Maps
                    </a>
                    <a href="https://www.google.com/maps/dir//{search_query_encoded}" target="_blank" class="btn-secondary">
                        🚗 Routebeschrijving
                    </a>
                </div>
            </div>'''
    
    return maps_html

def update_map_section(content, castle_name, address, province):
    """Met à jour la section carte"""
    maps_html = create_google_maps_embed(castle_name, address, province)
    
    # Chercher et remplacer la section map
    patterns = [
        r'(<section class="castle-map">.*?<div class="container">)(.*?)(</div>\s*</section>)',
        r'(<section class="map-section">.*?<div class="container">)(.*?)(</div>\s*</section>)',
        r'(<div class="map-container">)(.*?)(</div>)'
    ]
    
    for pattern in patterns:
        if re.search(pattern, content, flags=re.DOTALL):
            new_content = re.sub(pattern, f'\\1{maps_html}\\3', content, flags=re.DOTALL)
            return new_content
    
    return content

def add_maps_css():
    """Ajoute le CSS pour les cartes"""
    css_file = "/Users/marc/Desktop/kastelenbelgie/css/modern-style.css"
    
    css_to_add = """
/* Google Maps Integration */
.map-container {
    background: white;
    border-radius: 16px;
    padding: 2rem;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
    margin: 2rem 0;
}

.map-header {
    text-align: center;
    margin-bottom: 2rem;
}

.map-header h3 {
    font-size: 1.5rem;
    font-weight: 700;
    color: #1e293b;
    margin-bottom: 0.5rem;
}

.map-header p {
    color: #64748b;
    font-size: 1rem;
}

.google-map {
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    margin-bottom: 1.5rem;
}

.google-map iframe {
    width: 100%;
    height: 400px;
    border: none;
}

.map-actions {
    display: flex;
    gap: 1rem;
    justify-content: center;
    flex-wrap: wrap;
}

.map-actions .btn-secondary {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.75rem 1.5rem;
    background: #f1f5f9;
    color: #475569;
    text-decoration: none;
    border-radius: 8px;
    font-weight: 500;
    transition: all 0.2s ease;
}

.map-actions .btn-secondary:hover {
    background: #e2e8f0;
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

/* Responsive */
@media (max-width: 768px) {
    .map-container {
        padding: 1.5rem;
        margin: 1rem 0;
    }
    
    .google-map iframe {
        height: 300px;
    }
    
    .map-actions {
        flex-direction: column;
        align-items: center;
    }
    
    .map-actions .btn-secondary {
        width: 100%;
        justify-content: center;
    }
}
"""
    
    try:
        if os.path.exists(css_file):
            with open(css_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if 'Google Maps Integration' not in content:
                with open(css_file, 'a', encoding='utf-8') as f:
                    f.write(css_to_add)
                print("✅ CSS Google Maps ajouté")
            else:
                print("✅ CSS Google Maps déjà présent")
        else:
            print("⚠️ Fichier CSS non trouvé")
    except Exception as e:
        print(f"❌ Erreur ajout CSS: {e}")

def add_google_maps_to_all_pages():
    """Ajoute Google Maps à toutes les pages châteaux"""
    castle_files = []
    
    # Chercher tous les fichiers de châteaux
    patterns = ['kasteel-*.html', 'chateau-*.html', 'citadel-*.html', 'burcht-*.html']
    for pattern in patterns:
        castle_files.extend(glob.glob(f"/Users/marc/Desktop/kastelenbelgie/{pattern}"))
    
    print(f"🗺️ AJOUT DE GOOGLE MAPS À {len(castle_files)} PAGES")
    print("=" * 60)
    
    updated_count = 0
    
    for i, filepath in enumerate(castle_files, 1):
        filename = os.path.basename(filepath)
        print(f"\n[{i}/{len(castle_files)}] Traitement de {filename}")
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extraire les informations du château
            castle_name, address, province = get_castle_info_from_page(content)
            
            print(f"  Château: {castle_name}")
            print(f"  Adresse: {address if address else 'Non spécifiée'}")
            print(f"  Province: {province}")
            
            # Vérifier si une section map existe
            if 'castle-map' not in content and 'map-section' not in content and 'map-container' not in content:
                print(f"  ⚠️ Section map non trouvée")
                continue
            
            # Mettre à jour la section map
            new_content = update_map_section(content, castle_name, address, province)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                updated_count += 1
                print(f"  ✅ Google Maps ajouté")
            else:
                print(f"  ⚠️ Aucune modification")
                
        except Exception as e:
            print(f"  ❌ Erreur: {e}")
    
    print(f"\n✅ TERMINÉ: {updated_count} pages mises à jour avec Google Maps")
    print("\n📝 NOTE IMPORTANTE:")
    print("Pour que les cartes fonctionnent, vous devez:")
    print("1. Obtenir une clé API Google Maps")
    print("2. Remplacer 'YOUR_API_KEY' dans les iframes")
    print("3. Activer l'API Maps Embed dans Google Cloud Console")

def create_api_key_replacement_script():
    """Crée un script pour remplacer la clé API"""
    script_content = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
REMPLACEMENT DE LA CLÉ API GOOGLE MAPS
Remplace YOUR_API_KEY par votre vraie clé API
"""

import os
import glob

def replace_api_key(api_key):
    """Remplace la clé API dans tous les fichiers"""
    if not api_key or api_key == "YOUR_API_KEY":
        print("❌ Veuillez fournir une vraie clé API")
        return
    
    castle_files = []
    patterns = ['kasteel-*.html', 'chateau-*.html', 'citadel-*.html', 'burcht-*.html']
    for pattern in patterns:
        castle_files.extend(glob.glob(f"/Users/marc/Desktop/kastelenbelgie/{pattern}"))
    
    updated_count = 0
    
    for filepath in castle_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if 'YOUR_API_KEY' in content:
                new_content = content.replace('YOUR_API_KEY', api_key)
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                updated_count += 1
        except Exception as e:
            print(f"Erreur avec {filepath}: {e}")
    
    print(f"✅ {updated_count} fichiers mis à jour avec la clé API")

if __name__ == "__main__":
    # Remplacez par votre vraie clé API Google Maps
    API_KEY = "YOUR_GOOGLE_MAPS_API_KEY_HERE"
    replace_api_key(API_KEY)
'''
    
    with open("/Users/marc/Desktop/kastelenbelgie/replace_maps_api_key.py", 'w', encoding='utf-8') as f:
        f.write(script_content)
    
    print("✅ Script de remplacement de clé API créé: replace_maps_api_key.py")

def main():
    """Fonction principale"""
    print("🗺️ INTÉGRATION GOOGLE MAPS")
    print("=" * 50)
    
    # Ajouter le CSS nécessaire
    add_maps_css()
    
    # Ajouter Google Maps aux pages
    add_google_maps_to_all_pages()
    
    # Créer le script de remplacement de clé API
    create_api_key_replacement_script()

if __name__ == "__main__":
    main()
