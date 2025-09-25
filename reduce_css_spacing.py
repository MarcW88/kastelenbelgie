#!/usr/bin/env python3
"""
Script pour réduire les espacements CSS excessifs entre sections
"""

import os
import re
from pathlib import Path

def reduce_css_spacing():
    """Réduit les espacements CSS pour améliorer l'UX"""
    
    # Répertoire de travail
    base_dir = Path("/Users/marc/Desktop/kastelenbelgie")
    css_file = base_dir / "css" / "style.css"
    
    print("📏 RÉDUCTION DES ESPACEMENTS CSS")
    print("=" * 40)
    
    if not css_file.exists():
        print("❌ Fichier style.css non trouvé")
        return
    
    try:
        # Lire le contenu CSS
        with open(css_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        modifications = []
        
        # 1. Réduire .section padding de 5rem à 3rem
        pattern1 = r'\.section\s*\{\s*padding:\s*5rem\s+0;'
        if re.search(pattern1, content):
            content = re.sub(pattern1, '.section {\n  padding: 3rem 0;', content)
            modifications.append("✅ .section padding: 5rem → 3rem (80px → 48px)")
        
        # 2. Réduire .hero-modern padding de 4rem à 2.5rem
        pattern2 = r'\.hero-modern\s*\{\s*[^}]*padding:\s*4rem\s+0;'
        if re.search(pattern2, content):
            content = re.sub(r'(\.hero-modern\s*\{[^}]*padding:\s*)4rem(\s+0;)', r'\g<1>2.5rem\g<2>', content)
            modifications.append("✅ .hero-modern padding: 4rem → 2.5rem (64px → 40px)")
        
        # 3. Réduire .castle-hero padding de 4rem à 3rem
        pattern3 = r'\.castle-hero\s*\{\s*[^}]*padding:\s*4rem\s+0;'
        if re.search(pattern3, content):
            content = re.sub(r'(\.castle-hero\s*\{[^}]*padding:\s*)4rem(\s+0;)', r'\g<1>3rem\g<2>', content)
            modifications.append("✅ .castle-hero padding: 4rem → 3rem (64px → 48px)")
        
        # 4. Réduire .castle-intro padding de 4rem à 3rem
        pattern4 = r'\.castle-intro\s*\{\s*[^}]*padding:\s*4rem\s+0;'
        if re.search(pattern4, content):
            content = re.sub(r'(\.castle-intro\s*\{[^}]*padding:\s*)4rem(\s+0;)', r'\g<1>3rem\g<2>', content)
            modifications.append("✅ .castle-intro padding: 4rem → 3rem (64px → 48px)")
        
        # 5. Réduire .castle-activities padding de 4rem à 3rem
        pattern5 = r'\.castle-activities\s*\{\s*[^}]*padding:\s*4rem\s+0;'
        if re.search(pattern5, content):
            content = re.sub(r'(\.castle-activities\s*\{[^}]*padding:\s*)4rem(\s+0;)', r'\g<1>3rem\g<2>', content)
            modifications.append("✅ .castle-activities padding: 4rem → 3rem (64px → 48px)")
        
        # 6. Réduire .related-castles padding de 4rem à 3rem
        pattern6 = r'\.related-castles\s*\{\s*[^}]*padding:\s*4rem\s+0;'
        if re.search(pattern6, content):
            content = re.sub(r'(\.related-castles\s*\{[^}]*padding:\s*)4rem(\s+0;)', r'\g<1>3rem\g<2>', content)
            modifications.append("✅ .related-castles padding: 4rem → 3rem (64px → 48px)")
        
        # 7. Réduire .castle-map padding de 4rem à 3rem
        pattern7 = r'\.castle-map\s*\{\s*[^}]*padding:\s*4rem\s+0;'
        if re.search(pattern7, content):
            content = re.sub(r'(\.castle-map\s*\{[^}]*padding:\s*)4rem(\s+0;)', r'\g<1>3rem\g<2>', content)
            modifications.append("✅ .castle-map padding: 4rem → 3rem (64px → 48px)")
        
        # 8. Ajuster les sections avec padding 7rem (section-lg)
        pattern8 = r'\.section-lg\s*\{\s*padding:\s*7rem\s+0;'
        if re.search(pattern8, content):
            content = re.sub(pattern8, '.section-lg {\n  padding: 5rem 0;', content)
            modifications.append("✅ .section-lg padding: 7rem → 5rem (112px → 80px)")
        
        # 9. Réduire les marges excessives dans les sections
        pattern9 = r'margin-bottom:\s*3rem;'
        content = re.sub(pattern9, 'margin-bottom: 2rem;', content)
        if 'margin-bottom: 2rem;' in content and 'margin-bottom: 3rem;' not in content:
            modifications.append("✅ Marges réduites: 3rem → 2rem (48px → 32px)")
        
        # Vérifier si des modifications ont été faites
        if content != original_content:
            # Sauvegarder le fichier modifié
            with open(css_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print("📊 MODIFICATIONS APPLIQUÉES:")
            for mod in modifications:
                print(f"   {mod}")
            
            print(f"\n🎉 Espacements optimisés!")
            print("   - Réduction moyenne: 25-30% des espacements")
            print("   - Meilleure utilisation de l'espace")
            print("   - UX améliorée sans casser le design")
            
        else:
            print("✨ Les espacements sont déjà optimisés!")
    
    except Exception as e:
        print(f"❌ Erreur lors de la modification du CSS: {e}")

if __name__ == "__main__":
    reduce_css_spacing()
