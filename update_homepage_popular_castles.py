#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MISE À JOUR DE LA HOMEPAGE AVEC CHÂTEAUX POPULAIRES
Ajoute une section de 6 châteaux populaires sur la homepage
"""

from castle_organizer import CastleOrganizer

def update_homepage_popular_castles():
    """Met à jour la homepage avec les châteaux populaires"""
    homepage_file = "/Users/marc/Desktop/kastelenbelgie/index.html"
    
    print("🏠 MISE À JOUR HOMEPAGE AVEC CHÂTEAUX POPULAIRES")
    print("=" * 60)
    
    # Charger les données des châteaux
    organizer = CastleOrganizer()
    organizer.load_castles_data()
    
    # Générer le HTML des châteaux populaires
    popular_html = organizer.generate_popular_castles_html()
    
    try:
        # Lire la homepage actuelle
        with open(homepage_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Créer la section châteaux populaires
        popular_section = f'''
    <!-- Section Châteaux Populaires -->
    <section class="popular-castles-section">
        <div class="container">
            <h2 class="section-title">Populaire Kastelen</h2>
            <p class="section-description">Ontdek de meest bezochte en geliefde kastelen van België</p>
            {popular_html}
        </div>
    </section>
'''
        
        # Chercher où insérer la section (après la section hero)
        if '<section class="hero">' in content:
            # Trouver la fin de la section hero
            hero_end = content.find('</section>', content.find('<section class="hero">'))
            if hero_end != -1:
                hero_end += len('</section>')
                # Insérer la section populaire après le hero
                new_content = content[:hero_end] + popular_section + content[hero_end:]
                
                # Sauvegarder
                with open(homepage_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                print("✅ Homepage mise à jour avec 6 châteaux populaires")
                return True
        
        print("❌ Section hero non trouvée dans la homepage")
        return False
        
    except Exception as e:
        print(f"❌ Erreur: {e}")
        return False

if __name__ == "__main__":
    update_homepage_popular_castles()
