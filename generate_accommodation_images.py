#!/usr/bin/env python3
"""
Script pour générer des images optimisées pour les blocs "overnachten"
Utilise les données structurées de accommodation_blocks.json
et génère des prompts pour API d'images (DALL-E, Stability, etc.)
"""

import json
import os
from pathlib import Path

# Configuration
BASE_DIR = Path(__file__).parent
JSON_FILE = BASE_DIR / "accommodation_blocks.json"
OUTPUT_DIR = BASE_DIR / "images" / "cards"


def load_blocks():
    """Charge les blocs depuis le fichier JSON"""
    with open(JSON_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def build_prompt(block: dict, templates: dict, style: dict) -> str:
    """
    Construit un prompt d'image à partir des données du bloc
    
    Args:
        block: Données du bloc (title, location, theme, etc.)
        templates: Templates de description par thème
        style: Constantes de style (format, lighting, etc.)
    
    Returns:
        Prompt complet pour génération d'image (en anglais pour Stability API)
    """
    theme = block.get("theme", "hotels_bb")
    theme_description = templates.get(theme, templates["hotels_bb"])
    
    prompt = f"""A {style['format']} for a tourism website card about accommodation in Belgium.

Scene: {theme_description}

Location context: {block['location']}, Belgium

Technical requirements:
- {style['lighting']}
- {style['style']}
- Suitable as header image for a web card
- Professional quality, inviting for tourists
- Belgian Ardennes atmosphere
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
            "title": block["title"],
            "target_image": block["target_image"],
            "prompt": prompt
        })
    
    return prompts


def save_prompts_to_file(prompts: list, output_file: str = "generated_prompts.json"):
    """Sauvegarde les prompts dans un fichier JSON"""
    output_path = BASE_DIR / output_file
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(prompts, f, indent=2, ensure_ascii=False)
    print(f"✅ {len(prompts)} prompts sauvegardés dans {output_path}")


def print_prompts(prompts: list):
    """Affiche les prompts de manière lisible"""
    for i, p in enumerate(prompts, 1):
        print(f"\n{'='*60}")
        print(f"📷 Image {i}: {p['id']}")
        print(f"📄 Page: {p['page']}")
        print(f"🏷️  Titre: {p['title']}")
        print(f"📁 Fichier cible: {p['target_image']}")
        print(f"\n📝 PROMPT:")
        print("-" * 40)
        print(p['prompt'])
        print("=" * 60)


# ============================================================
# INTÉGRATION API (à adapter selon le service utilisé)
# ============================================================

def generate_image_openai(prompt: str, output_path: str, api_key: str = None):
    """
    Génère une image via l'API OpenAI DALL-E
    
    Nécessite: pip install openai
    """
    try:
        from openai import OpenAI
    except ImportError:
        print("❌ Module openai non installé. Exécutez: pip install openai")
        return False
    
    api_key = api_key or os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("❌ OPENAI_API_KEY non définie")
        return False
    
    client = OpenAI(api_key=api_key)
    
    try:
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1792x1024",
            quality="standard",
            n=1,
        )
        
        image_url = response.data[0].url
        
        # Télécharger l'image
        import requests
        img_response = requests.get(image_url)
        
        # Créer le dossier si nécessaire
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, "wb") as f:
            f.write(img_response.content)
        
        print(f"✅ Image générée: {output_path}")
        return True
        
    except Exception as e:
        print(f"❌ Erreur génération: {e}")
        return False


def generate_image_stability(prompt: str, output_path: str, api_key: str = None):
    """
    Génère une image via l'API Stability AI
    
    Nécessite: pip install stability-sdk
    """
    try:
        import requests
    except ImportError:
        print("❌ Module requests non installé")
        return False
    
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
    
    body = {
        "text_prompts": [{"text": prompt, "weight": 1}],
        "cfg_scale": 7,
        "height": 768,
        "width": 1344,
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


def generate_all_images(api: str = "openai", api_key: str = None):
    """
    Génère toutes les images pour les blocs sans image
    
    Args:
        api: "openai" ou "stability"
        api_key: Clé API (ou utilise variable d'environnement)
    """
    prompts = generate_all_prompts()
    
    generate_func = generate_image_openai if api == "openai" else generate_image_stability
    
    success = 0
    failed = 0
    
    for p in prompts:
        output_path = BASE_DIR / p["target_image"]
        
        # Skip si l'image existe déjà
        if output_path.exists():
            print(f"⏭️  Image existe déjà: {p['target_image']}")
            continue
        
        print(f"\n🎨 Génération: {p['id']}...")
        if generate_func(p["prompt"], str(output_path), api_key):
            success += 1
        else:
            failed += 1
    
    print(f"\n📊 Résultat: {success} générées, {failed} échouées")


def update_html_images():
    """
    Met à jour les fichiers HTML avec les nouvelles images
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
        
        # Remplacer l'ancienne image par la nouvelle
        if current_image in content:
            content = content.replace(current_image, target_image)
            
            with open(page_path, "w", encoding="utf-8") as f:
                f.write(content)
            
            print(f"✅ Mis à jour: {block['page']} - {block['id']}")
        else:
            print(f"⚠️  Image non trouvée dans {block['page']}: {current_image}")


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Génération d'images pour blocs accommodation")
    parser.add_argument("--action", choices=["prompts", "generate", "update"], default="prompts",
                       help="Action: prompts (afficher), generate (créer images), update (mettre à jour HTML)")
    parser.add_argument("--api", choices=["openai", "stability"], default="openai",
                       help="API à utiliser pour la génération")
    parser.add_argument("--api-key", help="Clé API (ou définir OPENAI_API_KEY / STABILITY_API_KEY)")
    parser.add_argument("--save", action="store_true", help="Sauvegarder les prompts dans un fichier JSON")
    
    args = parser.parse_args()
    
    if args.action == "prompts":
        prompts = generate_all_prompts()
        print_prompts(prompts)
        if args.save:
            save_prompts_to_file(prompts)
    
    elif args.action == "generate":
        generate_all_images(api=args.api, api_key=args.api_key)
    
    elif args.action == "update":
        update_html_images()
