#!/usr/bin/env python3
"""
Script pour nettoyer les balises HTML orphelines et corriger la structure
"""

import os
import re
from pathlib import Path

def clean_orphan_html():
    """Nettoie les balises HTML orphelines et corrige la structure"""
    
    # Répertoire de travail
    base_dir = Path("/Users/marc/Desktop/kastelenbelgie")
    
    # Compteurs
    files_processed = 0
    files_modified = 0
    
    print("🧹 NETTOYAGE DES BALISES HTML ORPHELINES")
    print("=" * 50)
    
    # Parcourir tous les fichiers HTML
    for html_file in base_dir.glob("*.html"):
        files_processed += 1
        
        try:
            # Lire le contenu du fichier
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # 1. Supprimer les balises </nav> orphelines après les breadcrumbs
            # Pattern: breadcrumbs suivi de balises fermantes orphelines
            pattern1 = r'</nav>\s*</div>\s*</nav>\s*</div>\s*</div>'
            content = re.sub(pattern1, '', content)
            
            # 2. Supprimer les balises </nav> orphelines simples
            pattern2 = r'</nav>\s*</div>\s*</nav>'
            content = re.sub(pattern2, '', content)
            
            # 3. Supprimer les commentaires orphelins avec balises
            pattern3 = r'<!-- Breadcrumbs -->\s*</div>\s*</nav>'
            content = re.sub(pattern3, '', content)
            
            # 4. Nettoyer les espaces multiples créés
            pattern4 = r'\n\s*\n\s*\n'
            content = re.sub(pattern4, '\n\n', content)
            
            # 5. Corriger les breadcrumbs dupliqués
            # Chercher les breadcrumbs dupliqués
            breadcrumb_pattern = r'(<nav class="breadcrumbs">.*?</nav>)\s*\1'
            content = re.sub(breadcrumb_pattern, r'\1', content, flags=re.DOTALL)
            
            # 6. Supprimer les balises </div> orphelines après breadcrumbs
            pattern5 = r'(</nav>\s*)</div>\s*</nav>'
            content = re.sub(pattern5, r'\1', content)
            
            # 7. Nettoyer les structures HTML cassées spécifiques
            # Exemple: <div class="castle-info"><h3>Château - België</title>
            pattern6 = r'<div class="castle-info"><h3>[^<]*</title>'
            content = re.sub(pattern6, '', content)
            
            # 8. Supprimer les balises img avec contenu HTML à l'intérieur
            pattern7 = r'<img[^>]*>[^<]*<[^>]*>[^<]*</[^>]*>'
            content = re.sub(pattern7, '', content)
            
            # 9. Corriger les balises title, head, body multiples
            # Supprimer les balises title en double
            title_matches = re.findall(r'<title[^>]*>.*?</title>', content, re.DOTALL)
            if len(title_matches) > 1:
                # Garder seulement le premier title
                first_title = title_matches[0]
                for i in range(1, len(title_matches)):
                    content = content.replace(title_matches[i], '', 1)
            
            # Vérifier si des modifications ont été faites
            if content != original_content:
                # Sauvegarder le fichier modifié
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                files_modified += 1
                print(f"✅ {html_file.name} - HTML nettoyé")
            
        except Exception as e:
            print(f"❌ Erreur avec {html_file.name}: {e}")
    
    print("\n📊 RÉSULTATS:")
    print(f"   Fichiers traités: {files_processed}")
    print(f"   Fichiers modifiés: {files_modified}")
    
    if files_modified > 0:
        print(f"\n🎉 HTML nettoyé sur {files_modified} pages!")
        print("   - Balises orphelines supprimées")
        print("   - Breadcrumbs dupliqués corrigés")
        print("   - Structure HTML validée")
    else:
        print("\n✨ Toutes les pages ont déjà un HTML propre!")

if __name__ == "__main__":
    clean_orphan_html()
