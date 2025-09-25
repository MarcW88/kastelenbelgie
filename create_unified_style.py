#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CRÉATION D'UN STYLE.CSS UNIFIÉ
Fusionne tous les CSS en un seul fichier style.css
"""

import os
import glob
import re

def create_unified_css():
    """Crée un style.css unifié avec tous les styles"""
    
    print("🎨 CRÉATION D'UN STYLE.CSS UNIFIÉ")
    print("=" * 50)
    
    # CSS files à fusionner (dans l'ordre de priorité)
    css_files = [
        '/Users/marc/Desktop/kastelenbelgie/css/unified-style.css',
        '/Users/marc/Desktop/kastelenbelgie/css/modern-style.css',
        '/Users/marc/Desktop/kastelenbelgie/css/style-new.css',
        '/Users/marc/Desktop/kastelenbelgie/css/style.css'
    ]
    
    unified_content = """/* STYLE.CSS UNIFIÉ - KASTELENBELGIE.BE */
/* Fichier CSS unique pour tout le site */
/* Généré automatiquement - NE PAS MODIFIER MANUELLEMENT */

"""
    
    for css_file in css_files:
        if os.path.exists(css_file):
            try:
                with open(css_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Nettoyer le contenu
                content = clean_css_content(content, os.path.basename(css_file))
                
                unified_content += f"\n/* ========== {os.path.basename(css_file).upper()} ========== */\n"
                unified_content += content + "\n\n"
                
                print(f"✅ Fusionné: {os.path.basename(css_file)}")
                
            except Exception as e:
                print(f"❌ Erreur avec {css_file}: {e}")
        else:
            print(f"⚠️ Fichier non trouvé: {css_file}")
    
    # Ajouter les styles spécifiques manquants
    unified_content += get_missing_styles()
    
    # Sauvegarder le CSS unifié
    output_file = '/Users/marc/Desktop/kastelenbelgie/css/style.css'
    
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(unified_content)
        
        print(f"✅ CSS unifié créé: {output_file}")
        return True
        
    except Exception as e:
        print(f"❌ Erreur création CSS unifié: {e}")
        return False

def clean_css_content(content, filename):
    """Nettoie le contenu CSS"""
    
    # Supprimer les commentaires de début de fichier
    content = re.sub(r'/\*[^*]*STYLE CSS[^*]*\*/', '', content, flags=re.IGNORECASE)
    content = re.sub(r'/\*[^*]*Design basé[^*]*\*/', '', content)
    content = re.sub(r'/\*[^*]*Combinaison[^*]*\*/', '', content)
    
    # Supprimer les doublons de variables CSS
    if filename != 'unified-style.css':
        content = re.sub(r':root\s*{[^}]*}', '', content, flags=re.DOTALL)
    
    # Nettoyer les espaces multiples
    content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
    
    return content.strip()

def get_missing_styles():
    """Retourne les styles manquants essentiels"""
    
    return """
/* ========== STYLES SPÉCIFIQUES SUPPLÉMENTAIRES ========== */

/* Correction grilles châteaux - PRIORITÉ ABSOLUE */
.castle-grid {
    display: grid !important;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)) !important;
    gap: 2rem !important;
    margin-top: 2rem !important;
}

.castle-card {
    background: white !important;
    border-radius: 18px !important;
    overflow: hidden !important;
    box-shadow: 0 4px 20px rgba(0,0,0,0.08) !important;
    transition: all 0.3s ease !important;
    display: block !important;
}

.castle-card:hover {
    transform: translateY(-5px) !important;
    box-shadow: 0 8px 30px rgba(0,0,0,0.15) !important;
    text-decoration: none !important;
}

.castle-card .castle-image {
    height: 200px !important;
    overflow: hidden !important;
}

.castle-card .castle-image img {
    width: 100% !important;
    height: 100% !important;
    object-fit: cover !important;
    transition: transform 0.3s ease !important;
}

.castle-card:hover .castle-image img {
    transform: scale(1.05) !important;
}

.castle-card-content {
    padding: 1.5rem !important;
}

.castle-card h3 {
    font-size: 1.1rem !important;
    font-weight: 600 !important;
    margin-bottom: 0.5rem !important;
    line-height: 1.3 !important;
}

/* Responsive grilles châteaux */
@media (max-width: 768px) {
    .castle-grid {
        grid-template-columns: 1fr !important;
        gap: 1.5rem !important;
    }
    
    .castle-card .castle-image {
        height: 160px !important;
    }
}

/* Fin des styles spécifiques */
"""

def update_all_html_files():
    """Met à jour tous les fichiers HTML pour utiliser style.css"""
    
    print("\n🔄 MISE À JOUR DES LIENS CSS DANS TOUS LES FICHIERS HTML")
    print("=" * 60)
    
    html_files = glob.glob("/Users/marc/Desktop/kastelenbelgie/*.html")
    updated_count = 0
    
    for html_file in html_files:
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Remplacer tous les liens CSS par style.css
            original_content = content
            
            # Patterns de remplacement
            css_patterns = [
                r'<link rel="stylesheet" href="css/modern-style\.css">',
                r'<link rel="stylesheet" href="css/unified-style\.css">',
                r'<link rel="stylesheet" href="css/style-new\.css">',
                r'<link rel="stylesheet" href="css/style\.css">'
            ]
            
            for pattern in css_patterns:
                content = re.sub(pattern, '<link rel="stylesheet" href="css/style.css">', content)
            
            if content != original_content:
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                updated_count += 1
                
        except Exception as e:
            print(f"❌ Erreur avec {html_file}: {e}")
            continue
    
    print(f"✅ {updated_count} fichiers HTML mis à jour")
    return updated_count

if __name__ == "__main__":
    print("🚀 UNIFICATION COMPLÈTE DU CSS")
    print("=" * 40)
    print("OBJECTIF: UN SEUL style.css POUR TOUT LE SITE")
    print()
    
    # Étape 1: Créer le CSS unifié
    if create_unified_css():
        # Étape 2: Mettre à jour tous les HTML
        updated_count = update_all_html_files()
        
        print(f"\n🎉 UNIFICATION TERMINÉE!")
        print(f"✅ CSS unifié créé: css/style.css")
        print(f"✅ {updated_count} pages HTML mises à jour")
        print(f"✅ Toutes les pages utilisent maintenant css/style.css")
        print(f"\n🎯 RÉSULTAT: UN SEUL FICHIER CSS POUR TOUT LE SITE!")
    else:
        print("❌ Échec de l'unification")
