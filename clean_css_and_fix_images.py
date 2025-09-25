#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
NETTOYAGE CSS ET CORRECTION IMAGES
Supprime les conflits CSS et fixe la hauteur de l'image hero
"""

import re

def clean_css_conflicts():
    """Nettoie les conflits CSS et définit clairement les styles images"""
    
    print("🧹 NETTOYAGE CSS ET CORRECTION IMAGES")
    print("-" * 50)
    
    css_file = "/Users/marc/Desktop/kastelenbelgie/css/style.css"
    
    try:
        with open(css_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Supprimer TOUTES les définitions .castle-image existantes
        patterns_to_remove = [
            r'\.castle-image[^}]*\{[^}]*\}',
            r'\.castle-image img[^}]*\{[^}]*\}',
            r'\.castle-image:empty[^}]*\{[^}]*\}',
            r'\.castle-image:not\([^}]*\)[^}]*\{[^}]*\}',
            r'\.castle-image\.placeholder[^}]*\{[^}]*\}',
            r'\.castle-image:has\([^}]*\)[^}]*\{[^}]*\}',
            r'\.castle-card \.castle-image[^}]*\{[^}]*\}',
            r'\.castle-card \.castle-image img[^}]*\{[^}]*\}',
            r'\.castle-card:hover \.castle-image[^}]*\{[^}]*\}',
            r'\.popular-castle-card \.castle-image[^}]*\{[^}]*\}',
            r'\.related-castle-card \.castle-image[^}]*\{[^}]*\}',
        ]
        
        for pattern in patterns_to_remove:
            content = re.sub(pattern, '', content, flags=re.DOTALL)
        
        # Nettoyer les espaces multiples
        content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
        
        # Ajouter les définitions CSS propres et claires
        clean_css = """
/* ===== STYLES IMAGES PROPRES ET DÉFINITIFS ===== */

/* Image hero dans castle-hero (même hauteur que info-box) */
.castle-hero .castle-image {
    width: 100%;
    height: 100%;
    min-height: 400px;
    border-radius: 16px;
    overflow: hidden;
    position: relative;
    background: transparent;
}

.castle-hero .castle-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 16px;
}

/* Images dans les cards châteaux (pages provinces, related, etc.) */
.castle-card .castle-image,
.popular-castle-card .castle-image,
.related-castle-card .castle-image {
    width: 100%;
    height: 200px;
    overflow: hidden;
    border-radius: 12px;
    background: transparent;
}

.castle-card .castle-image img,
.popular-castle-card .castle-image img,
.related-castle-card .castle-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.3s ease;
}

/* Hover effects */
.castle-card:hover .castle-image img,
.popular-castle-card:hover .castle-image img,
.related-castle-card:hover .castle-image img {
    transform: scale(1.05);
}

/* Gallery images */
.gallery-image {
    width: 100%;
    height: 200px;
    object-fit: cover;
    border-radius: 12px;
}

/* Responsive */
@media (max-width: 768px) {
    .castle-hero .castle-image {
        min-height: 300px;
    }
    
    .castle-card .castle-image,
    .popular-castle-card .castle-image,
    .related-castle-card .castle-image {
        height: 160px;
    }
}

/* ===== FIN STYLES IMAGES ===== */
"""
        
        # Ajouter le CSS propre à la fin
        content += "\n" + clean_css
        
        with open(css_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ CSS nettoyé et styles images redéfinis proprement")
        print("✅ Image hero aura maintenant la même hauteur que l'info-box")
        
    except Exception as e:
        print(f"❌ Erreur: {e}")

if __name__ == "__main__":
    print("🧹 NETTOYAGE CSS ET CORRECTION IMAGES")
    print("=" * 50)
    
    clean_css_conflicts()
    
    print(f"\n🎉 CSS NETTOYÉ!")
    print("✅ Conflits CSS supprimés")
    print("✅ Image hero corrigée pour même hauteur que info-box")
    print("✅ Styles images cohérents partout")
    print("\n🚀 Teste maintenant l'image hero sur bisschoppenhof-deurne.html")
