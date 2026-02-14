#!/usr/bin/env python3
"""
Script pour mettre à jour UNIQUEMENT les images de la section overnachten (ticket-card-image)
Ne touche pas aux sections hero, activities ou gallery
"""

import re
from pathlib import Path

BASE_DIR = Path(__file__).parent

# Mapping: (page, old_image) -> new_image
# Uniquement pour les images dans ticket-card avec class="ticket-card-image"
REPLACEMENTS = {
    "kasteel-van-durbuy-durbuy.html": [
        ("chateau_image_update_3/kasteel_durbuy_2.jpg", "images/cards/durbuy-hotels-oude-stad.jpg"),
        ("chateau_image_update_3/kasteel_durbuy_4.jpg", "images/cards/durbuy-chalets.jpg"),
        ("chateau_image_update_3/kasteel_durbuy_6.jpg", "images/cards/durbuy-adventure-valley.jpg"),
    ],
    "kasteel-van-deulin-deulin-fronville.html": [
        ("chateaux_images_update-2/Kasteel_van_Deulin_5.jpg", "images/cards/deulin-events.jpg"),
        ("chateaux_images_update-2/Kasteel_van_Deulin_3.jpg", "images/cards/deulin-hotels.jpg"),
        ("chateaux_images_update-2/Kasteel_van_Deulin_4.jpg", "images/cards/deulin-vakantiewoningen.jpg"),
    ],
    "kasteel-van-mirwart-mirwart-saint-hubert.html": [
        ("chateaux_images_update-2/Kasteel_van_Mirwart_3.jpg", "images/cards/mirwart-kasteel.jpg"),
        ("chateaux_images_update-2/Kasteel_van_Mirwart_4.jpg", "images/cards/mirwart-hotels.jpg"),
        ("chateaux_images_update-2/Kasteel_van_Mirwart_5.jpg", "images/cards/mirwart-natuurhuisjes.jpg"),
    ],
    "kasteel-van-longchamps-longchamps-bertogne.html": [
        ("chateaux_images_update-2/Kasteel_van_longchamps_6.jpg", "images/cards/longchamps-kasteel.jpg"),
        ("chateaux_images_update-2/Kasteel_van_longchamps_4.jpg", "images/cards/longchamps-gites.jpg"),
        ("chateaux_images_update-2/Kasteel_van_longchamps_5.jpg", "images/cards/longchamps-vakantiewoningen.jpg"),
    ],
    "kasteel-van-porcheresse-daverdisse.html": [
        ("chateaux_images_update-2/Kasteel_van_Porcheresse_4.jpg", "images/cards/porcheresse-kasteel.jpg"),
        ("chateaux_images_update-2/Kasteel_van_Porcheresse_3.jpg", "images/cards/porcheresse-gites.jpg"),
        ("chateaux_images_update-2/Kasteel_van_Porcheresse_5.jpg", "images/cards/porcheresse-vakantiewoningen.jpg"),
    ],
    "kasteel-van-orval-villers-devant-orval.html": [
        ("chateaux_images_update-2/Kasteel_van_Orval_6.jpg", "images/cards/orval-gites.jpg"),
        ("chateaux_images_update-2/Kasteel_van_Orval_4.jpg", "images/cards/orval-florenville.jpg"),
        ("chateaux_images_update-2/Kasteel_van_Orval_5.jpg", "images/cards/orval-semois.jpg"),
    ],
}


def update_ticket_card_images():
    """
    Remplace les images UNIQUEMENT dans les balises avec class="ticket-card-image"
    """
    for page, replacements in REPLACEMENTS.items():
        page_path = BASE_DIR / page
        
        if not page_path.exists():
            print(f"⚠️  Page non trouvée: {page}")
            continue
        
        with open(page_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        original_content = content
        changes = 0
        
        for old_img, new_img in replacements:
            # Pattern: <img src="OLD" ... class="ticket-card-image">
            # On cherche spécifiquement les images avec class="ticket-card-image"
            pattern = rf'(<img\s+src="){re.escape(old_img)}("[^>]*class="ticket-card-image"[^>]*>)'
            replacement = rf'\g<1>{new_img}\g<2>'
            
            new_content, count = re.subn(pattern, replacement, content)
            if count > 0:
                content = new_content
                changes += count
            else:
                # Essayer l'ordre inverse (class avant src)
                pattern2 = rf'(<img[^>]*class="ticket-card-image"[^>]*src="){re.escape(old_img)}("[^>]*>)'
                new_content, count = re.subn(pattern2, replacement, content)
                if count > 0:
                    content = new_content
                    changes += count
        
        if content != original_content:
            with open(page_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"✅ {page}: {changes} image(s) mise(s) à jour dans section overnachten")
        else:
            print(f"⏭️  {page}: aucun changement")


if __name__ == "__main__":
    print("🔄 Mise à jour des images de la section overnachten uniquement...\n")
    update_ticket_card_images()
    print("\n✅ Terminé!")
