#!/usr/bin/env python3
"""
Script pour générer les images du blog "Middeleeuwse Kastelen" avec Stability AI
Nécessite une clé API Stability AI dans la variable d'environnement STABILITY_API_KEY
"""

import os
import requests
from pathlib import Path

# Configuration
STABILITY_API_KEY = os.environ.get("STABILITY_API_KEY")
OUTPUT_DIR = Path(__file__).parent / "blog_images"
OUTPUT_DIR.mkdir(exist_ok=True)

# Prompts pour les 6 images
IMAGES = [
    {
        "filename": "middeleeuwse-kastelen-hero.jpg",
        "prompt": "Horizontal realistic 16:9 image of a medieval castle in Belgium on a rock above a river, with thick stone walls, towers and an inner courtyard. Morning or evening light, soft mist in the valley, no recognizable people. Suitable as hero image for a blog article about medieval castles. Photorealistic, dramatic lighting.",
        "negative_prompt": "text, watermark, logo, people faces, modern elements, cars"
    },
    {
        "filename": "donjon-burcht-citadel-schema.jpg",
        "prompt": "Simple horizontal illustration in neutral colors showing three types of medieval fortifications side by side: on the left a donjon (single residential tower), in the middle a castle with ring wall, towers and courtyard, on the right a citadel as fortified city core. No text, only clear silhouettes in a minimalist style that can be used as a diagram in a blog. Clean architectural illustration style.",
        "negative_prompt": "text, labels, watermark, photorealistic, people"
    },
    {
        "filename": "kasteel-evolutie-timeline.jpg",
        "prompt": "Horizontal illustration in four panels, each with a different type of castle: 1) wooden motte castle on an artificial hill, 2) stone donjon with simple ring wall, 3) complex medieval castle with towers and moats, 4) early modern fortress with low bastions. Neutral color palette, no text, style suitable as infographic-like image in a blog about castle history. Clean illustration style.",
        "negative_prompt": "text, labels, watermark, modern elements"
    },
    {
        "filename": "kasteel-verdediging.jpg",
        "prompt": "Realistic but simplified illustration of a medieval castle showing defensive elements: thick walls, moat, gatehouse with drawbridge, high towers and narrow arrow slits. No text labels in the image, only the visual elements clearly present. Architectural cutaway view showing defense mechanisms. Warm lighting.",
        "negative_prompt": "text, labels, watermark, people, modern elements"
    },
    {
        "filename": "ridderzaal-interieur.jpg",
        "prompt": "Realistic 16:9 illustration of the interior of a medieval great hall in a Belgian castle: large stone room with wooden beams, fireplace, long tables, shields and banners on the wall. A few stylized figures in medieval clothing in the background, without recognizable faces, so the scene remains timeless and neutral. Warm candlelight atmosphere.",
        "negative_prompt": "modern elements, text, watermark, recognizable faces, contemporary clothing"
    },
    {
        "filename": "kastelenroute-ardennen-kaart.jpg",
        "prompt": "Stylized map illustration of the Ardennes with some marked castles: Bouillon, La Roche-en-Ardenne, Reinhardstein and Veves. Green hilly landscape, stylized rivers, small castle pictograms at the locations, no exact map accuracy needed. Horizontal 16:9 image usable as route visual in a blog article. Illustrated travel map style with warm colors.",
        "negative_prompt": "text, labels, photorealistic, satellite view, modern roads"
    }
]


def generate_image(prompt: str, negative_prompt: str, filename: str) -> bool:
    """Génère une image avec Stability AI"""
    
    if not STABILITY_API_KEY:
        print(f"⚠️  STABILITY_API_KEY non définie. Skipping {filename}")
        return False
    
    url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"
    
    headers = {
        "Authorization": f"Bearer {STABILITY_API_KEY}",
        "Content-Type": "application/json",
        "Accept": "image/png"
    }
    
    body = {
        "text_prompts": [
            {"text": prompt, "weight": 1},
            {"text": negative_prompt, "weight": -1}
        ],
        "cfg_scale": 7,
        "height": 640,
        "width": 1536,
        "samples": 1,
        "steps": 30,
        "style_preset": "photographic"
    }
    
    try:
        response = requests.post(url, headers=headers, json=body)
        
        if response.status_code == 200:
            output_path = OUTPUT_DIR / filename
            with open(output_path, "wb") as f:
                f.write(response.content)
            print(f"✅ Généré: {filename}")
            return True
        else:
            print(f"❌ Erreur {response.status_code} pour {filename}: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Exception pour {filename}: {e}")
        return False


def main():
    print("🎨 Génération des images pour le blog Middeleeuwse Kastelen\n")
    
    if not STABILITY_API_KEY:
        print("⚠️  Variable d'environnement STABILITY_API_KEY non définie!")
        print("   Exécutez: export STABILITY_API_KEY='votre-clé-api'")
        print("\n📋 Images à générer manuellement:")
        for img in IMAGES:
            print(f"\n--- {img['filename']} ---")
            print(f"Prompt: {img['prompt']}")
        return
    
    success = 0
    for img in IMAGES:
        if generate_image(img["prompt"], img["negative_prompt"], img["filename"]):
            success += 1
    
    print(f"\n📊 Résultat: {success}/{len(IMAGES)} images générées")
    print(f"📁 Dossier: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
