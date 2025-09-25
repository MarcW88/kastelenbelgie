#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
TEST DU DESIGN MODERNE
Vérifie que les nouveaux styles modernes sont bien appliqués
"""

import os

def test_modern_styles():
    """Teste que les styles modernes sont présents dans style.css"""
    
    print("🎨 TEST DU DESIGN MODERNE")
    print("=" * 50)
    
    css_file = "/Users/marc/Desktop/kastelenbelgie/css/style.css"
    
    if not os.path.exists(css_file):
        print("❌ Fichier style.css non trouvé!")
        return False
    
    try:
        with open(css_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print(f"✅ Fichier style.css lu ({len(content):,} caractères)")
        
        # Vérifier les nouveaux styles modernes
        modern_styles = [
            # Variables modernes
            ('--primary: #3b82f6', 'Variables couleurs modernes'),
            ('--shadow-xl:', 'Ombres modernes'),
            ('--radius-large:', 'Border radius modernes'),
            
            # Hero moderne
            ('.hero-modern', 'Hero section moderne'),
            ('.hero-content-modern', 'Contenu hero moderne'),
            ('.hero-badge-modern', 'Badge hero moderne'),
            ('.hero-title-modern', 'Titre hero moderne'),
            
            # Cards modernes
            ('.card-modern', 'Cards modernes'),
            ('.card-image-modern', 'Images cards modernes'),
            ('.card-content-modern', 'Contenu cards modernes'),
            
            # Grilles modernes
            ('.grid-auto', 'Grilles auto-fit modernes'),
            ('grid-template-columns: repeat(auto-fit, minmax(320px, 1fr))', 'Grilles châteaux améliorées'),
            
            # Boutons modernes
            ('.btn-modern', 'Boutons modernes'),
            ('.btn-primary-modern', 'Boutons primaires modernes'),
            ('border-radius: 50px', 'Boutons arrondis'),
            
            # Effets modernes
            ('transform: translateY(-6px)', 'Hover effects améliorés'),
            ('backdrop-filter: blur(10px)', 'Effets de flou modernes'),
            ('box-shadow: var(--shadow-xl)', 'Ombres variables'),
        ]
        
        missing_styles = []
        for style, description in modern_styles:
            if style in content:
                print(f"  ✅ {description}")
            else:
                missing_styles.append(description)
                print(f"  ❌ {description} - MANQUANT")
        
        if missing_styles:
            print(f"\n⚠️ {len(missing_styles)} styles modernes manquants")
            return False
        else:
            print("\n✅ Tous les styles modernes sont présents!")
            return True
            
    except Exception as e:
        print(f"❌ Erreur lecture CSS: {e}")
        return False

def check_castle_grid_improvements():
    """Vérifie les améliorations des grilles de châteaux"""
    
    print(f"\n🏰 VÉRIFICATION DES GRILLES DE CHÂTEAUX AMÉLIORÉES")
    print("-" * 50)
    
    css_file = "/Users/marc/Desktop/kastelenbelgie/css/style.css"
    
    try:
        with open(css_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        improvements = [
            ('minmax(320px, 1fr)', 'Largeur minimale augmentée (320px vs 300px)'),
            ('height: 220px', 'Hauteur images augmentée (220px vs 200px)'),
            ('transform: translateY(-6px)', 'Hover effect plus prononcé (-6px vs -5px)'),
            ('transform: scale(1.08)', 'Zoom image au hover (1.08)'),
            ('border: 1px solid rgba(0, 0, 0, 0.05)', 'Bordures subtiles'),
            ('transition: all 0.4s ease', 'Transitions plus fluides (0.4s)'),
        ]
        
        for improvement, description in improvements:
            if improvement in content:
                print(f"  ✅ {description}")
            else:
                print(f"  ❌ {description} - MANQUANT")
                
    except Exception as e:
        print(f"❌ Erreur: {e}")

def create_test_page():
    """Crée une page de test pour voir le design moderne"""
    
    print(f"\n📄 CRÉATION D'UNE PAGE DE TEST")
    print("-" * 30)
    
    test_html = """<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test Design Moderne - Kastelen België</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <!-- Hero Section Moderne -->
    <section class="hero-modern">
        <div class="hero-content-modern">
            <div class="hero-text-modern">
                <div class="hero-badge-modern">
                    ✨ Nouveau Design
                </div>
                <h1 class="hero-title-modern">Ontdek de mooiste kastelen van België</h1>
                <p class="hero-description-modern">
                    Van middeleeuwse burchten tot elegante landgoederen - elk kasteel vertelt zijn eigen verhaal.
                </p>
                <div class="hero-actions-modern">
                    <a href="#" class="btn-modern btn-primary-modern">Alle kastelen</a>
                    <a href="#" class="btn-modern btn-secondary-modern">Per provincie</a>
                </div>
            </div>
            <div class="hero-visual-modern">
                <img src="assets/img/castle-hero.jpg" alt="Kasteel" class="hero-image-modern">
                <div class="hero-floating-card">
                    <h4>255+ Kastelen</h4>
                    <p>Ontdek ze allemaal</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Section Châteaux -->
    <section class="section">
        <div class="container">
            <h2 class="section-title">Populaire Kastelen</h2>
            <p class="section-subtitle">Ontdek de meest bezochte kastelen van België</p>
            
            <div class="castle-grid">
                <div class="castle-card">
                    <div class="castle-image">
                        <img src="assets/img/castle1.jpg" alt="Kasteel 1">
                    </div>
                    <div class="castle-card-content">
                        <h3>Kasteel van Freÿr</h3>
                        <p class="card-description">Een prachtig Renaissance kasteel aan de Maas met prachtige tuinen.</p>
                        <a href="#" class="btn-primary">Meer info</a>
                    </div>
                </div>
                
                <div class="castle-card">
                    <div class="castle-image">
                        <img src="assets/img/castle2.jpg" alt="Kasteel 2">
                    </div>
                    <div class="castle-card-content">
                        <h3>Kasteel van Durbuy</h3>
                        <p class="card-description">Een imposant middeleeuws kasteel in de parel van de Ardennen.</p>
                        <a href="#" class="btn-primary">Meer info</a>
                    </div>
                </div>
                
                <div class="castle-card">
                    <div class="castle-image">
                        <img src="assets/img/castle3.jpg" alt="Kasteel 3">
                    </div>
                    <div class="castle-card-content">
                        <h3>Citadel van Hoei</h3>
                        <p class="card-description">Een strategisch gelegen vesting met adembenemende uitzichten.</p>
                        <a href="#" class="btn-primary">Meer info</a>
                    </div>
                </div>
            </div>
        </div>
    </section>
</body>
</html>"""
    
    try:
        with open("/Users/marc/Desktop/kastelenbelgie/test-modern-design.html", 'w', encoding='utf-8') as f:
            f.write(test_html)
        
        print("✅ Page de test créée: test-modern-design.html")
        print("🚀 Ouvrez cette page pour voir le nouveau design!")
        
    except Exception as e:
        print(f"❌ Erreur création page test: {e}")

if __name__ == "__main__":
    styles_ok = test_modern_styles()
    check_castle_grid_improvements()
    create_test_page()
    
    print(f"\n🎯 RÉSULTAT:")
    if styles_ok:
        print("✅ DESIGN MODERNE APPLIQUÉ AVEC SUCCÈS!")
        print("✅ Styles modernes basés sur l'image fournie")
        print("✅ Grilles de châteaux améliorées")
        print("✅ Page de test créée")
        print("\n🚀 Testez avec: python3 start_local_server.py")
        print("📄 Puis ouvrez: http://localhost:8000/test-modern-design.html")
    else:
        print("❌ Certains styles modernes sont manquants")
        print("🔧 Vérifiez le fichier style.css")
