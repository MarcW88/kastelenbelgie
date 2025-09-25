#!/usr/bin/env python3
"""
Script pour moderniser les formulaires en remplaçant les styles inline
par des classes CSS modernes
"""

import os
import re
from pathlib import Path

def add_modern_form_css():
    """Ajoute les styles CSS modernes pour les formulaires"""
    
    modern_form_css = """
/* ===== FORMULAIRES MODERNES ===== */

.form-container {
    max-width: 600px;
    margin: 0 auto;
}

.form-card {
    background: var(--bg-primary);
    padding: 3rem;
    border-radius: var(--radius);
    box-shadow: var(--shadow);
    border: 1px solid rgba(0, 0, 0, 0.05);
}

.form-modern {
    display: grid;
    gap: 1.5rem;
}

.form-group {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

.form-label {
    font-weight: 600;
    color: var(--text);
    font-size: 0.95rem;
}

.form-input,
.form-select,
.form-textarea {
    width: 100%;
    padding: 0.875rem 1rem;
    border: 2px solid #e2e8f0;
    border-radius: var(--radius);
    font-size: 1rem;
    font-family: inherit;
    transition: all 0.2s ease;
    background: var(--bg-primary);
    color: var(--text);
}

.form-input:focus,
.form-select:focus,
.form-textarea:focus {
    outline: none;
    border-color: var(--primary);
    box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    transform: translateY(-1px);
}

.form-input:hover,
.form-select:hover,
.form-textarea:hover {
    border-color: #cbd5e1;
}

.form-textarea {
    resize: vertical;
    min-height: 120px;
    line-height: 1.6;
}

.form-button {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.875rem 2rem;
    background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%);
    color: white;
    border: none;
    border-radius: var(--radius);
    font-weight: 600;
    font-size: 1rem;
    cursor: pointer;
    transition: all 0.2s ease;
    justify-self: start;
}

.form-button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3);
}

.form-button:active {
    transform: translateY(0);
}

.form-disclaimer {
    font-size: 0.875rem;
    color: var(--text-light);
    line-height: 1.5;
    padding: 1rem;
    background: var(--bg-secondary);
    border-radius: var(--radius);
    border-left: 4px solid var(--primary);
}

.form-disclaimer a {
    color: var(--primary);
    text-decoration: none;
    font-weight: 500;
}

.form-disclaimer a:hover {
    text-decoration: underline;
}

/* Animations pour les labels flottants */
.form-group-floating {
    position: relative;
}

.form-group-floating .form-input:focus + .form-label,
.form-group-floating .form-input:not(:placeholder-shown) + .form-label {
    transform: translateY(-1.5rem) scale(0.85);
    color: var(--primary);
}

.form-group-floating .form-label {
    position: absolute;
    top: 0.875rem;
    left: 1rem;
    transition: all 0.2s ease;
    pointer-events: none;
    background: var(--bg-primary);
    padding: 0 0.25rem;
}

/* États de validation */
.form-input.valid {
    border-color: #10b981;
}

.form-input.invalid {
    border-color: #ef4444;
}

.form-error {
    color: #ef4444;
    font-size: 0.875rem;
    margin-top: 0.25rem;
}

.form-success {
    color: #10b981;
    font-size: 0.875rem;
    margin-top: 0.25rem;
}

/* Responsive */
@media (max-width: 768px) {
    .form-card {
        padding: 2rem 1.5rem;
        margin: 1rem;
    }
    
    .form-button {
        width: 100%;
        justify-content: center;
    }
}
"""
    
    return modern_form_css

def modernize_forms():
    """Modernise les formulaires en remplaçant les styles inline"""
    
    # Répertoire de travail
    base_dir = Path("/Users/marc/Desktop/kastelenbelgie")
    
    print("💅 MODERNISATION DES FORMULAIRES")
    print("=" * 40)
    
    # 1. Ajouter les styles CSS modernes
    css_file = base_dir / "css" / "style.css"
    
    try:
        with open(css_file, 'r', encoding='utf-8') as f:
            css_content = f.read()
        
        # Vérifier si les styles sont déjà présents
        if "FORMULAIRES MODERNES" not in css_content:
            css_content += "\n" + add_modern_form_css()
            
            with open(css_file, 'w', encoding='utf-8') as f:
                f.write(css_content)
            
            print("✅ Styles CSS modernes ajoutés")
        else:
            print("✅ Styles CSS déjà présents")
    
    except Exception as e:
        print(f"❌ Erreur CSS: {e}")
        return
    
    # 2. Moderniser les formulaires HTML
    files_processed = 0
    files_modified = 0
    
    for html_file in base_dir.glob("*.html"):
        # Se concentrer sur les pages avec formulaires
        if html_file.name not in ['contact.html', 'login.html', 'register.html']:
            continue
        
        files_processed += 1
        
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Remplacer les structures de formulaire
            
            # 1. Container du formulaire
            pattern1 = r'<div style="max-width:\s*600px;\s*margin:\s*0\s*auto;">'
            content = re.sub(pattern1, '<div class="form-container">', content)
            
            # 2. Card du formulaire
            pattern2 = r'<div style="background:\s*var\(--white\);\s*padding:\s*3rem;\s*border-radius:\s*var\(--radius\);\s*box-shadow:\s*var\(--shadow\);\s*border:\s*1px\s*solid\s*var\(--border\);">'
            content = re.sub(pattern2, '<div class="form-card">', content)
            
            # 3. Formulaire principal
            pattern3 = r'<form([^>]*)\s*style="display:\s*grid;\s*gap:\s*1\.5rem;">'
            content = re.sub(pattern3, r'<form\1 class="form-modern">', content)
            
            # 4. Labels
            pattern4 = r'<label style="display:\s*block;\s*margin-bottom:\s*0\.5rem;\s*font-weight:\s*600;\s*color:\s*var\(--text\);">'
            content = re.sub(pattern4, '<label class="form-label">', content)
            
            # 5. Inputs
            pattern5 = r'<input([^>]*)\s*style="width:\s*100%;\s*padding:\s*0\.75rem;\s*border:\s*1px\s*solid\s*var\(--border\);\s*border-radius:\s*var\(--radius\);\s*font-size:\s*1rem;">'
            content = re.sub(pattern5, r'<input\1 class="form-input">', content)
            
            # 6. Select
            pattern6 = r'<select([^>]*)\s*style="width:\s*100%;\s*padding:\s*0\.75rem;\s*border:\s*1px\s*solid\s*var\(--border\);\s*border-radius:\s*var\(--radius\);\s*font-size:\s*1rem;">'
            content = re.sub(pattern6, r'<select\1 class="form-select">', content)
            
            # 7. Textarea
            pattern7 = r'<textarea([^>]*)\s*style="width:\s*100%;\s*padding:\s*0\.75rem;\s*border:\s*1px\s*solid\s*var\(--border\);\s*border-radius:\s*var\(--radius\);\s*font-size:\s*1rem;\s*resize:\s*vertical;">'
            content = re.sub(pattern7, r'<textarea\1 class="form-textarea">', content)
            
            # 8. Bouton
            pattern8 = r'<button([^>]*)\s*class="btn-modern\s*btn-primary-modern"\s*style="justify-self:\s*start;">'
            content = re.sub(pattern8, r'<button\1 class="form-button">', content)
            
            # 9. Disclaimer
            pattern9 = r'<div style="font-size:\s*0\.875rem;\s*color:\s*var\(--text-light\);\s*line-height:\s*1\.5;">'
            content = re.sub(pattern9, '<div class="form-disclaimer">', content)
            
            # 10. Groupes de formulaire (divs autour des champs)
            content = re.sub(r'<div>\s*<label', '<div class="form-group"><label', content)
            
            # Vérifier si des modifications ont été faites
            if content != original_content:
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                files_modified += 1
                print(f"✅ {html_file.name} - Formulaire modernisé")
        
        except Exception as e:
            print(f"❌ Erreur avec {html_file.name}: {e}")
    
    print(f"\n📊 RÉSULTATS:")
    print(f"   Fichiers traités: {files_processed}")
    print(f"   Fichiers modifiés: {files_modified}")
    
    if files_modified > 0:
        print(f"\n🎉 Formulaires modernisés!")
        print("   - Styles inline remplacés par classes CSS")
        print("   - Focus states et animations ajoutés")
        print("   - Design moderne et responsive")
        print("   - Meilleure accessibilité")
    else:
        print("\n✨ Formulaires déjà modernes!")

if __name__ == "__main__":
    modernize_forms()
