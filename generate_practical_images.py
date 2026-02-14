#!/usr/bin/env python3
"""
Script pour générer des images verticales pour la section "praktische informatie"
Format portrait (9:16) pour affichage à droite du texte
"""

import json
import os
import re
from pathlib import Path
import requests

BASE_DIR = Path(__file__).parent
JSON_FILE = BASE_DIR / "practical_blocks.json"
OUTPUT_DIR = BASE_DIR / "images" / "practical"


def load_blocks():
    """Charge les blocs depuis le fichier JSON"""
    with open(JSON_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def build_prompt(block: dict, templates: dict, style: dict) -> str:
    """
    Construit un prompt d'image à partir des données du bloc
    """
    theme = block.get("theme", "bos_pad")
    theme_description = templates.get(theme, templates["bos_pad"])
    
    prompt = f"""A {style['format']} for a tourism website sidebar.

Scene: {theme_description}

Location context: {block['location']}, Belgian Ardennes

Technical requirements:
- {style['lighting']}
- {style['style']}
- Vertical composition suitable for sidebar placement
- Professional quality, inviting atmosphere
- No castle needed, focus on atmosphere and surroundings
"""
    return prompt.strip()


def generate_all_prompts():
    """Génère tous les prompts pour les blocs"""
    data = load_blocks()
    blocks = data["blocks"]
    templates = data["prompt_templates"]
    style = data["style_constants"]

    prompts = []
    for block in blocks:
        prompt = build_prompt(block, templates, style)
        prompts.append({
            "id": block["id"],
            "page": block["page"],
            "castle": block["castle"],
            "current_image": block["current_image"],
            "target_image": block["target_image"],
            "prompt": prompt
        })

    return prompts


def generate_image_stability(prompt: str, output_path: str, api_key: str = None):
    """
    Génère une image verticale via l'API Stability AI
    """
    api_key = api_key or os.environ.get("STABILITY_API_KEY")
    if not api_key:
        print("❌ STABILITY_API_KEY non définie")
        return False

    url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Accept": "image/png"
    }

    # Format vertical 9:16 (768x1344)
    body = {
        "text_prompts": [{"text": prompt, "weight": 1}],
        "cfg_scale": 7,
        "height": 1344,
        "width": 768,
        "samples": 1,
        "steps": 30,
    }

    try:
        response = requests.post(url, headers=headers, json=body)

        if response.status_code == 200:
            Path(output_path).parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, "wb") as f:
                f.write(response.content)
            print(f"✅ Image générée: {output_path}")
            return True
        else:
            print(f"❌ Erreur API: {response.status_code} - {response.text}")
            return False

    except Exception as e:
        print(f"❌ Erreur: {e}")
        return False


def generate_all_images(api_key: str = None):
    """
    Génère toutes les images pour les blocs praktische informatie
    """
    prompts = generate_all_prompts()

    success = 0
    failed = 0

    for p in prompts:
        output_path = BASE_DIR / p["target_image"]

        # Skip si l'image existe déjà
        if output_path.exists():
            print(f"⏭️  Image existe déjà: {p['target_image']}")
            continue

        print(f"\n🎨 Génération: {p['id']}...")
        if generate_image_stability(p["prompt"], str(output_path), api_key):
            success += 1
        else:
            failed += 1

    print(f"\n📊 Résultat: {success} générées, {failed} échouées")


def update_html_images():
    """
    Met à jour les fichiers HTML avec les nouvelles images
    Remplace les images dans la section practical-image
    """
    data = load_blocks()
    blocks = data["blocks"]

    for block in blocks:
        page_path = BASE_DIR / block["page"]
        target_image = block["target_image"]
        current_image = block["current_image"]

        # Vérifier si la nouvelle image existe
        if not (BASE_DIR / target_image).exists():
            print(f"⏭️  Image non générée: {target_image}")
            continue

        # Lire le fichier HTML
        with open(page_path, "r", encoding="utf-8") as f:
            content = f.read()

        original_content = content

        # Pattern: chercher l'image dans practical-image div
        # On cherche <div class="practical-image"> suivi de <img src="...">
        pattern = rf'(<div class="practical-image">\s*<img src="){re.escape(current_image)}("[^>]*>)'
        replacement = rf'\g<1>{target_image}\g<2>'
        
        content, count = re.subn(pattern, replacement, content)
        
        if content != original_content:
            with open(page_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"✅ Mis à jour: {block['page']} - {block['id']}")
        else:
            print(f"⚠️  Pas de changement: {block['page']} - {block['id']}")


def print_prompts(prompts: list):
    """Affiche les prompts de manière lisible"""
    for i, p in enumerate(prompts, 1):
        print(f"\n{'='*60}")
        print(f"📷 Image {i}: {p['id']}")
        print(f"📄 Page: {p['page']}")
        print(f"🏰 Château: {p['castle']}")
        print(f"📁 Fichier cible: {p['target_image']}")
        print(f"\n📝 PROMPT:")
        print("-" * 40)
        print(p['prompt'])
        print("=" * 60)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Génération d'images verticales pour praktische informatie")
    parser.add_argument("--action", choices=["prompts", "generate", "update"], default="prompts",
                       help="Action: prompts (afficher), generate (créer images), update (mettre à jour HTML)")
    parser.add_argument("--api-key", help="Clé API Stability")

    args = parser.parse_args()

    if args.action == "prompts":
        prompts = generate_all_prompts()
        print_prompts(prompts)

    elif args.action == "generate":
        generate_all_images(api_key=args.api_key)

    elif args.action == "update":
        update_html_images()
