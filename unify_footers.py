#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
UNIFICATION DES FOOTERS SUR TOUT LE SITE
Applique le même footer partout avec le style unifié
"""

import glob
import re

def unify_footers():
    """Unifie les footers sur toutes les pages du site"""
    
    print("🦶 UNIFICATION DES FOOTERS SUR TOUT LE SITE")
    print("=" * 60)
    
    # Footer unifié basé sur le style de la homepage
    unified_footer = '''    <footer class="site-footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h3>kastelenbelgie.be</h3>
                    <p>Ontdek de mooiste kastelen van België. Van middeleeuwse burchten tot elegante landgoederen - elk kasteel vertelt zijn eigen verhaal.</p>
                    <div class="social-links">
                        <a href="#" aria-label="Facebook"><i class="fab fa-facebook"></i></a>
                        <a href="#" aria-label="Instagram"><i class="fab fa-instagram"></i></a>
                        <a href="#" aria-label="Twitter"><i class="fab fa-twitter"></i></a>
                    </div>
                </div>
                
                <div class="footer-section">
                    <h3>Kastelen</h3>
                    <ul>
                        <li><a href="kastelen.html">Alle kastelen</a></li>
                        <li><a href="provinces.html">Per provincie</a></li>
                        <li><a href="kaart.html">Kastelenkaart</a></li>
                        <li><a href="blog.html">Kastelen blog</a></li>
                    </ul>
                </div>
                
                <div class="footer-section">
                    <h3>Informatie</h3>
                    <ul>
                        <li><a href="blog.html">Blog</a></li>
                        <li><a href="contact.html">Contact</a></li>
                        <li><a href="#" onclick="alert('Voorwaarden pagina komt binnenkort')">Voorwaarden</a></li>
                        <li><a href="#" onclick="alert('Privacy pagina komt binnenkort')">Privacy</a></li>
                    </ul>
                </div>
                
                <div class="footer-section">
                    <h3>Service</h3>
                    <ul>
                        <li><a href="index.html">Homepage</a></li>
                        <li><a href="blog.html">Alle artikelen</a></li>
                        <li><a href="provinces.html">Provincies</a></li>
                        <li><a href="kastelen.html">Kastelen zoeken</a></li>
                    </ul>
                </div>
            </div>
            
            <div class="footer-bottom">
                <p>&copy; 2024 kastelenbelgie.be. Alle rechten voorbehouden.</p>
                <div class="footer-links">
                    <a href="#" onclick="alert('Voorwaarden pagina komt binnenkort')">Voorwaarden</a>
                    <a href="#" onclick="alert('Privacy pagina komt binnenkort')">Privacy</a>
                    <a href="contact.html">Contact</a>
                </div>
            </div>
        </div>
    </footer>'''
    
    # Trouver tous les fichiers HTML
    html_files = glob.glob("/Users/marc/Desktop/kastelenbelgie/*.html")
    
    updated_count = 0
    
    for html_file in html_files:
        try:
            filename = html_file.split('/')[-1]
            
            # Lire le fichier
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Patterns pour trouver les footers existants
            footer_patterns = [
                r'<footer[^>]*>.*?</footer>',
                r'<!-- Footer -->.*?</footer>',
                r'<div class="footer">.*?</div>\s*</body>',
                r'<section class="footer">.*?</section>'
            ]
            
            content_modified = False
            for pattern in footer_patterns:
                if re.search(pattern, content, re.DOTALL):
                    content = re.sub(pattern, unified_footer, content, flags=re.DOTALL)
                    content_modified = True
                    break
            
            # Si pas de footer existant, l'ajouter avant </body>
            if not content_modified:
                body_end = content.rfind('</body>')
                if body_end != -1:
                    content = content[:body_end] + '\n' + unified_footer + '\n\n' + content[body_end:]
                    content_modified = True
            
            if content_modified:
                # Sauvegarder
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                updated_count += 1
                print(f"✅ {filename}: footer unifié")
            
        except Exception as e:
            print(f"❌ Erreur avec {html_file}: {e}")
            continue
    
    print(f"\n📊 RÉSULTATS:")
    print(f"Pages mises à jour: {updated_count}")

if __name__ == "__main__":
    unify_footers()
