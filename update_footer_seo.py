#!/usr/bin/env python3
"""
Script pour mettre à jour le footer de toutes les pages HTML avec un footer SEO-optimisé.
Axes travaillés :
1. Structure générale (4 colonnes)
2. Maillage interne (provinces + châteaux populaires)
3. Ancres optimisées
4. Bloc éditorial SEO
"""

import os
import re
from pathlib import Path

# Nouveau footer SEO-optimisé
NEW_FOOTER = '''    <!-- Footer Kastelen België v2.0 -->
    <footer class="footer" style="background: #1E2523; color: #F5F3EF; padding: 0;">
        <div class="container" style="max-width: 1200px; margin: 0 auto; padding: 0 1.5rem;">
            
            <!-- SECTION 1: Branding + Stats -->
            <div class="footer-top" style="display: grid; grid-template-columns: 1.5fr 1fr; gap: 3rem; padding: 3rem 0; border-bottom: 1px solid rgba(255,255,255,0.1);">
                <!-- Brand Column -->
                <div>
                    <h3 style="font-size: 1.4rem; font-weight: 700; margin-bottom: 1rem; color: #F5F3EF;">
                        🏰 Kastelen België
                    </h3>
                    <p style="color: #D4C7B4; line-height: 1.7; margin-bottom: 1.5rem; font-size: 0.95rem;">
                        <strong>Dé gids voor kastelen in België.</strong> Ontdek meer dan 300 kastelen per provincie, 
                        plan je bezoek met praktische info en laat je inspireren door eeuwenoude verhalen 
                        en prachtige foto's uit meer dan duizend jaar Belgische geschiedenis.
                    </p>

                    <!-- Trust Signals -->
                    <div style="display: flex; gap: 2rem; flex-wrap: wrap;">
                        <div style="font-size: 0.85rem; color: #D4C7B4;">
                            <strong style="display: block; color: #C89A3B; font-size: 1.1rem;">300+</strong>
                            Kastelen
                        </div>
                        <div style="font-size: 0.85rem; color: #D4C7B4;">
                            <strong style="display: block; color: #C89A3B; font-size: 1.1rem;">11</strong>
                            Provincies
                        </div>
                        <div style="font-size: 0.85rem; color: #D4C7B4;">
                            <strong style="display: block; color: #C89A3B; font-size: 1.1rem;">1000+</strong>
                            Jaar geschiedenis
                        </div>
                    </div>
                </div>

                <!-- Social + Contact -->
                <div style="background: rgba(255,255,255,0.05); padding: 1.5rem; border-radius: 12px; border: 1px solid rgba(255,255,255,0.1);">
                    <h4 style="color: #F5F3EF; margin-bottom: 1rem; font-size: 1rem;">📬 Contact & Volg Ons</h4>
                    <p style="color: #D4C7B4; font-size: 0.9rem; margin-bottom: 1rem;">
                        Vragen over een kasteel? Suggesties? We horen graag van je!
                    </p>
                    <div style="display: flex; gap: 0.75rem; margin-bottom: 1rem;">
                        <a href="mailto:info@kastelenbelgie.be" style="width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; background: rgba(255,255,255,0.1); border-radius: 50%; color: #F5F3EF; text-decoration: none; transition: background 0.2s;" aria-label="E-mail">📧</a>
                        <a href="https://www.instagram.com/kastelenbelgie" style="width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; background: rgba(255,255,255,0.1); border-radius: 50%; color: #F5F3EF; text-decoration: none; transition: background 0.2s;" aria-label="Instagram">📷</a>
                        <a href="https://www.facebook.com/kastelenbelgie" style="width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; background: rgba(255,255,255,0.1); border-radius: 50%; color: #F5F3EF; text-decoration: none; transition: background 0.2s;" aria-label="Facebook">f</a>
                    </div>
                    <a href="contact.html" style="color: #C89A3B; font-size: 0.9rem; text-decoration: none;">→ Contactformulier</a>
                </div>
            </div>

            <!-- SECTION 2: Navigation Grid -->
            <div class="footer-grid" style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 2rem; padding: 2.5rem 0; border-bottom: 1px solid rgba(255,255,255,0.1);">
                
                <!-- COLUMN 1: Provincies Vlaanderen -->
                <div>
                    <h4 style="color: #F5F3EF; margin-bottom: 1.2rem; font-size: 0.9rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;">Kastelen Vlaanderen</h4>
                    <ul style="list-style: none; padding: 0; margin: 0;">
                        <li style="margin-bottom: 0.6rem;"><a href="antwerpen.html" style="color: #D4C7B4; text-decoration: none; font-size: 0.9rem; transition: color 0.2s;">Kastelen in Antwerpen</a></li>
                        <li style="margin-bottom: 0.6rem;"><a href="vlaams-brabant.html" style="color: #D4C7B4; text-decoration: none; font-size: 0.9rem;">Kastelen in Vlaams-Brabant</a></li>
                        <li style="margin-bottom: 0.6rem;"><a href="oost-vlaanderen.html" style="color: #D4C7B4; text-decoration: none; font-size: 0.9rem;">Kastelen in Oost-Vlaanderen</a></li>
                        <li style="margin-bottom: 0.6rem;"><a href="west-vlaanderen.html" style="color: #D4C7B4; text-decoration: none; font-size: 0.9rem;">Kastelen in West-Vlaanderen</a></li>
                        <li style="margin-bottom: 0.6rem;"><a href="limburg.html" style="color: #D4C7B4; text-decoration: none; font-size: 0.9rem;">Kastelen in Limburg</a></li>
                        <li style="margin-bottom: 0.6rem;"><a href="provinces.html" style="color: #C89A3B; font-weight: 600; text-decoration: none; font-size: 0.9rem;">→ Alle provincies</a></li>
                    </ul>
                </div>

                <!-- COLUMN 2: Provincies Wallonië -->
                <div>
                    <h4 style="color: #F5F3EF; margin-bottom: 1.2rem; font-size: 0.9rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;">Kastelen Wallonië</h4>
                    <ul style="list-style: none; padding: 0; margin: 0;">
                        <li style="margin-bottom: 0.6rem;"><a href="namen.html" style="color: #D4C7B4; text-decoration: none; font-size: 0.9rem;">Kastelen in Namen</a></li>
                        <li style="margin-bottom: 0.6rem;"><a href="luik.html" style="color: #D4C7B4; text-decoration: none; font-size: 0.9rem;">Kastelen in Luik</a></li>
                        <li style="margin-bottom: 0.6rem;"><a href="henegouwen.html" style="color: #D4C7B4; text-decoration: none; font-size: 0.9rem;">Kastelen in Henegouwen</a></li>
                        <li style="margin-bottom: 0.6rem;"><a href="luxemburg.html" style="color: #D4C7B4; text-decoration: none; font-size: 0.9rem;">Kastelen in Luxemburg</a></li>
                        <li style="margin-bottom: 0.6rem;"><a href="waals-brabant.html" style="color: #D4C7B4; text-decoration: none; font-size: 0.9rem;">Kastelen in Waals-Brabant</a></li>
                        <li style="margin-bottom: 0.6rem;"><a href="brussel.html" style="color: #D4C7B4; text-decoration: none; font-size: 0.9rem;">Kastelen in Brussel</a></li>
                    </ul>
                </div>

                <!-- COLUMN 3: Populaire Kastelen -->
                <div>
                    <h4 style="color: #F5F3EF; margin-bottom: 1.2rem; font-size: 0.9rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;">Populaire Kastelen</h4>
                    <ul style="list-style: none; padding: 0; margin: 0;">
                        <li style="margin-bottom: 0.6rem;"><a href="kasteel-van-freyr-freyr.html" style="color: #D4C7B4; text-decoration: none; font-size: 0.9rem;">Kasteel van Freÿr</a></li>
                        <li style="margin-bottom: 0.6rem;"><a href="citadel-van-hoei-hoei.html" style="color: #D4C7B4; text-decoration: none; font-size: 0.9rem;">Citadel van Hoei</a></li>
                        <li style="margin-bottom: 0.6rem;"><a href="kasteel-de-merode-westerlo.html" style="color: #D4C7B4; text-decoration: none; font-size: 0.9rem;">Kasteel de Merode</a></li>
                        <li style="margin-bottom: 0.6rem;"><a href="kasteel-van-durbuy-durbuy.html" style="color: #D4C7B4; text-decoration: none; font-size: 0.9rem;">Kasteel van Durbuy</a></li>
                        <li style="margin-bottom: 0.6rem;"><a href="kasteel-van-bouchout-te-meise.html" style="color: #D4C7B4; text-decoration: none; font-size: 0.9rem;">Kasteel van Bouchout</a></li>
                        <li style="margin-bottom: 0.6rem;"><a href="kasteel-reinhardstein-burg-metternich-te-weismes.html" style="color: #D4C7B4; text-decoration: none; font-size: 0.9rem;">Kasteel Reinhardstein</a></li>
                    </ul>
                </div>

                <!-- COLUMN 4: Blog & Info -->
                <div>
                    <h4 style="color: #F5F3EF; margin-bottom: 1.2rem; font-size: 0.9rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;">Blog & Informatie</h4>
                    <ul style="list-style: none; padding: 0; margin: 0;">
                        <li style="margin-bottom: 0.6rem;"><a href="blog.html" style="color: #D4C7B4; text-decoration: none; font-size: 0.9rem;">📖 Blog</a></li>
                        <li style="margin-bottom: 0.6rem;"><a href="blog-mooiste-kastelen-belgie.html" style="color: #D4C7B4; text-decoration: none; font-size: 0.9rem;">Mooiste kastelen van België</a></li>
                        <li style="margin-bottom: 0.6rem;"><a href="blog-middeleeuwse-kastelen.html" style="color: #D4C7B4; text-decoration: none; font-size: 0.9rem;">Middeleeuwse kastelen</a></li>
                        <li style="margin-bottom: 0.6rem;"><a href="contact.html" style="color: #D4C7B4; text-decoration: none; font-size: 0.9rem;">💬 Contact</a></li>
                        <li style="margin-bottom: 0.6rem;"><a href="privacybeleid.html" style="color: #D4C7B4; text-decoration: none; font-size: 0.9rem;">Privacybeleid</a></li>
                        <li style="margin-bottom: 0.6rem;"><a href="algemene-voorwaarden.html" style="color: #D4C7B4; text-decoration: none; font-size: 0.9rem;">Algemene voorwaarden</a></li>
                    </ul>
                </div>
            </div>

            <!-- SECTION 3: Bottom Bar -->
            <div class="footer-bottom" style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; padding: 2rem 0;">
                <!-- Left: Copyright -->
                <div>
                    <p style="color: #D4C7B4; font-size: 0.85rem; line-height: 1.6; margin: 0;">
                        <strong style="color: #F5F3EF;">© 2024 Kastelen België.</strong> Alle rechten voorbehouden.
                        <br><br>
                        <span style="color: #8A857D;">Op Kastelenbelgie.be vind je meer dan 300 kastelen in België, 
                        netjes gebundeld per provincie met praktische informatie en tips.</span>
                    </p>
                </div>

                <!-- Right: Back to top -->
                <div style="text-align: right;">
                    <p style="color: #8A857D; font-size: 0.85rem; margin: 0 0 0.5rem 0;">
                        Gemaakt met ❤️ voor het Belgische erfgoed
                    </p>
                    <a href="#" style="color: #C89A3B; text-decoration: none; font-size: 0.85rem;">Terug naar boven ↑</a>
                </div>
            </div>
        </div>
    </footer>'''


def update_footer_in_file(filepath):
    """Met à jour le footer dans un fichier HTML."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern pour trouver le footer existant (plusieurs variantes possibles)
        # On cherche de <!-- Footer --> ou <footer jusqu'à </footer>
        patterns = [
            r'<!-- Footer Kastelen België v2\.0 -->.*?<footer class="footer"[^>]*>.*?</footer>',
            r'<!-- Footer.*?-->.*?<footer class="footer"[^>]*>.*?</footer>',
            r'<!-- Footer uniforme -->.*?<footer class="footer"[^>]*>.*?</footer>',
            r'<!-- Footer SEO-optimisé -->.*?<footer class="footer"[^>]*>.*?</footer>',
            r'<footer class="footer"[^>]*>.*?</footer>',
        ]
        
        new_content = content
        replaced = False
        
        for pattern in patterns:
            if re.search(pattern, new_content, re.DOTALL):
                new_content = re.sub(pattern, NEW_FOOTER, new_content, flags=re.DOTALL)
                replaced = True
                break
        
        if replaced and new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        elif not replaced:
            print(f"  ⚠️  Pas de footer trouvé dans: {filepath}")
            return False
        else:
            return False  # Pas de changement nécessaire
            
    except Exception as e:
        print(f"  ❌ Erreur avec {filepath}: {e}")
        return False


def main():
    """Parcourt tous les fichiers HTML et met à jour les footers."""
    project_dir = Path(__file__).parent
    html_files = list(project_dir.glob('*.html'))
    
    print(f"🏰 Mise à jour du footer SEO pour {len(html_files)} fichiers HTML...")
    print("=" * 60)
    
    updated = 0
    skipped = 0
    errors = 0
    
    for html_file in sorted(html_files):
        # Ignorer les fichiers de test
        if 'test' in html_file.name.lower():
            skipped += 1
            continue
            
        result = update_footer_in_file(html_file)
        if result:
            print(f"  ✅ {html_file.name}")
            updated += 1
        elif result is False:
            errors += 1
    
    print("=" * 60)
    print(f"✅ Fichiers mis à jour: {updated}")
    print(f"⏭️  Fichiers ignorés: {skipped}")
    print(f"⚠️  Erreurs/non trouvés: {errors}")
    print("\n🎉 Footer SEO appliqué avec succès!")


if __name__ == "__main__":
    main()
