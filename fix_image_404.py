#!/usr/bin/env python3
"""
Fix 404 images by creating copies with correct names or redirecting to existing images
"""

import os
import shutil
from pathlib import Path

IMG_DIR = Path("chateaux_images_update-2")

# Mapping: 404 image name -> existing image to copy from
FIXES = [
    # Case sensitivity fixes
    ("Kasteel_van_Tillegem_2.jpg", "Kasteel_van_tillegem_2.jpg"),
    ("Kasteel_van_Tillegem_1.jpg", "Kasteel_van_tillegem_1.jpg"),
    ("Kasteel_van_Rivieren_1.jpg", "Kasteel_van_rivieren_1.jpg"),
    ("Kasteel_van_Olsene_1.jpg", "Kasteel_van_olsene_1.jpg"),
    ("Kasteel_van_Leeuwergem_1.jpg", "Kasteel_van_leeuwergem_1.jpg"),
    ("Kasteel_van_Kruishoutem_1.jpg", "Kasteel_van_kruishoutem_1.jpg"),
    ("Kasteel_van_Cleydael_2.jpg", "Waterslot_cleydael_2.jpg"),
    ("Kasteel_van_Beervelde_1.jpg", "Kasteel_van_beervelde_1.jpg"),
    ("Kasteel_de_Merode_2.jpg", "Kasteel_de_merode_2.jpg"),
    ("Kasteel_Zellaer_2.jpg", "Kasteel_van_zellaer_2.jpg"),
    ("Kasteel_Tudor_1.jpg", "Kasteel_tudor_1.jpg"),
    ("Kasteel_Selsaete_2.jpg", "Kasteel_selsaete_2.jpg"),
    ("Kasteel_Selsaete_1.jpg", "Kasteel_selsaete_1.jpg"),
    ("Kasteel_Reinhardstein_2.jpg", "Kasteel_reinhardstein_2.jpg"),
    ("Kasteel_Pulhof_1.jpg", "Kasteel_pulhof_1.jpg"),
    ("Kasteel_Mussenborg_1.jpg", "Kasteel_mussenborg_1.jpg"),
    ("Kasteel_Borluut_1.jpg", "Kasteel_borluut_1.jpg"),
    ("Kasteel_Arendsnest_1.jpg", "Kasteel_arendsnest_1.jpg"),
    # Accent fixes
    ("Kasteel_van_Veves_2.jpg", "Kasteel_van_Vêves_2.jpg"),
    ("Kasteel_van_La_Berlière_3.jpg", "Kasteel_van_la_berliere_3.jpg"),
    # Images that don't exist - redirect to similar existing ones
    ("Kasteel_van_modave_1.jpg", "Kasteel_de_merode_3.jpg"),  # Fallback
    ("Kasteel_van_jehay_1.jpg", "Kasteel_de_merode_3.jpg"),  # Fallback
    ("Kasteel_van_horst_1.jpg", "Kasteel_de_merode_3.jpg"),  # Fallback
    ("Kasteel_van_beloeil_1.jpg", "Kasteel_van_beloeil_2.jpg"),
    ("Kasteel_van_beloeil_2.jpg", "Kasteel_van_beloeil_3.jpg"),
    ("Kasteel_van_attre_1.jpg", "Kasteel_van_Attre_2.jpg"),
    ("Kasteel_van_antoing_1.jpg", "Kasteel_de_merode_3.jpg"),  # Fallback
    ("Kasteel_van_Wijnendale_2.jpg", "Kasteel_de_merode_3.jpg"),  # Fallback
    ("Kasteel_van_Loppem_2.jpg", "Kasteel_de_merode_3.jpg"),  # Fallback
    ("Kasteel_van_Jehay_2.jpg", "Kasteel_de_merode_3.jpg"),  # Fallback
    ("Kasteel_van_Horst_1.jpg", "Kasteel_de_merode_3.jpg"),  # Fallback
    ("Kasteel_van_Franchimont_2.jpg", "Kasteel_de_merode_3.jpg"),  # Fallback
    ("Kasteel_van_Arenberg_1.jpg", "Kasteel_de_merode_3.jpg"),  # Fallback
    ("Kasteel_van_Annevoie_2.jpg", "Kasteel_de_merode_3.jpg"),  # Fallback
    ("Kasteel_d_Aertrycke_2.jpg", "Kasteel_de_merode_3.jpg"),  # Fallback
    ("Kasteel_Sterckshof_1.jpg", "Kasteel_de_merode_3.jpg"),  # Fallback
    ("Kasteel_Lakebossen_1.jpg", "Kasteel_de_merode_3.jpg"),  # Fallback
    ("Citadel_van_Dinant_2.jpg", "Citadel_van_hoei_4.jpg"),  # Similar citadel
]

def find_existing_image(name):
    """Find an existing image with similar name (case insensitive)"""
    name_lower = name.lower()
    for f in IMG_DIR.iterdir():
        if f.name.lower() == name_lower:
            return f.name
    return None

def main():
    print("=" * 60)
    print("Fixing 404 images")
    print("=" * 60)
    
    fixed = 0
    errors = []
    
    for target_name, source_name in FIXES:
        target_path = IMG_DIR / target_name
        
        # Skip if target already exists
        if target_path.exists():
            print(f"  ⏭ {target_name} already exists")
            continue
        
        # Find source
        source_path = IMG_DIR / source_name
        
        # Try case-insensitive match if source doesn't exist
        if not source_path.exists():
            found = find_existing_image(source_name)
            if found:
                source_path = IMG_DIR / found
            else:
                errors.append((target_name, f"source not found: {source_name}"))
                continue
        
        # Copy file
        try:
            shutil.copy2(source_path, target_path)
            print(f"  ✓ {target_name} <- {source_path.name}")
            fixed += 1
        except Exception as e:
            errors.append((target_name, str(e)))
    
    print("\n" + "-" * 60)
    print(f"Fixed {fixed} images")
    
    if errors:
        print(f"\nErrors ({len(errors)}):")
        for name, err in errors:
            print(f"  ✗ {name}: {err}")
    
    print("=" * 60)

if __name__ == "__main__":
    main()
