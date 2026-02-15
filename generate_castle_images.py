#!/usr/bin/env python3
"""
Generate castle images for kastelenbelgie.be using Stability AI
"""

import os
import requests
import base64
from pathlib import Path

# Stability AI API key - set as environment variable
API_KEY = os.environ.get("STABILITY_API_KEY")

# Output directory
OUTPUT_DIR = Path("stability_images")
OUTPUT_DIR.mkdir(exist_ok=True)

# Image prompts for each region/theme
PROMPTS = {
    # Provinces
    "antwerpen": "Beautiful medieval castle in Antwerp Belgium, red brick architecture, surrounded by green gardens, sunny day, photorealistic, 4k",
    "namen": "Majestic castle on a hill in Namur Belgium, overlooking the Meuse river, stone walls, dramatic sky, photorealistic, 4k",
    "oost-vlaanderen": "Historic Gravensteen-style castle in Ghent East Flanders Belgium, medieval fortress with moat, photorealistic, 4k",
    "luik": "Impressive citadel fortress in Liège Belgium, stone fortifications on hilltop, panoramic view, photorealistic, 4k",
    "limburg": "Romantic water castle in Limburg Belgium, surrounded by moat and trees, peaceful atmosphere, photorealistic, 4k",
    
    # Regions
    "vlaanderen": "Elegant Flemish castle in Flanders Belgium, Renaissance architecture, beautiful gardens, sunny day, photorealistic, 4k",
    "wallonie": "Dramatic castle in the Walloon Ardennes Belgium, forest setting, medieval stone architecture, misty atmosphere, photorealistic, 4k",
    "brussel": "Royal Palace of Laeken style castle in Brussels Belgium, neoclassical architecture, manicured gardens, photorealistic, 4k",
    "ardennen": "Rugged medieval fortress castle in Belgian Ardennes, perched on rocky cliff, dense forest, dramatic lighting, photorealistic, 4k",
    "kust": "Coastal castle manor near Belgian coast, elegant architecture, sea breeze atmosphere, sunny day, photorealistic, 4k",
    "henegouwen": "Grand château in Hainaut Belgium, French-style architecture, large estate grounds, photorealistic, 4k",
    
    # Types
    "bezoek": "Welcoming castle museum in Belgium, open gates, visitors exploring, beautiful architecture, sunny day, photorealistic, 4k",
    "overnachten": "Luxurious castle hotel in Belgium, romantic atmosphere, elegant interior visible, evening lighting, photorealistic, 4k",
    "evenement": "Magnificent castle wedding venue in Belgium, decorated for celebration, romantic gardens, golden hour, photorealistic, 4k",
    "wandeling": "Castle with extensive parkland in Belgium, walking paths through gardens, autumn colors, peaceful atmosphere, photorealistic, 4k",
}

def generate_image(prompt: str, output_name: str):
    """Generate an image using Stability AI SDXL"""
    
    if not API_KEY:
        print("Error: STABILITY_API_KEY environment variable not set")
        return False
    
    url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    payload = {
        "text_prompts": [
            {
                "text": prompt,
                "weight": 1.0
            },
            {
                "text": "blurry, low quality, distorted, ugly, cartoon, anime, drawing",
                "weight": -1.0
            }
        ],
        "cfg_scale": 7,
        "width": 1024,
        "height": 768,
        "samples": 1,
        "steps": 30,
        "style_preset": "photographic"
    }
    
    print(f"Generating: {output_name}...")
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        
        if response.status_code == 200:
            data = response.json()
            for i, image in enumerate(data["artifacts"]):
                img_data = base64.b64decode(image["base64"])
                output_path = OUTPUT_DIR / f"{output_name}.jpg"
                with open(output_path, "wb") as f:
                    f.write(img_data)
                print(f"  ✓ Saved: {output_path}")
            return True
        else:
            print(f"  ✗ Error {response.status_code}: {response.text}")
            return False
            
    except Exception as e:
        print(f"  ✗ Exception: {e}")
        return False

def main():
    print("=" * 50)
    print("Generating castle images for kastelenbelgie.be")
    print("=" * 50)
    
    if not API_KEY:
        print("\n⚠️  Please set STABILITY_API_KEY environment variable:")
        print("   export STABILITY_API_KEY='your-api-key-here'")
        print("\nThen run this script again.")
        return
    
    success_count = 0
    total = len(PROMPTS)
    
    for name, prompt in PROMPTS.items():
        if generate_image(prompt, name):
            success_count += 1
    
    print("\n" + "=" * 50)
    print(f"Generated {success_count}/{total} images")
    print(f"Images saved to: {OUTPUT_DIR.absolute()}")
    print("=" * 50)

if __name__ == "__main__":
    main()
