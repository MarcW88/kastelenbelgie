#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script pour ajouter les images des châteaux dans les pages provinces
et ajouter du contenu descriptif avec liens
"""

import os
import re
import glob

def normalize_name_for_image(name):
    """Normalise un nom pour trouver l'image correspondante"""
    name = name.lower()
    name = re.sub(r'[_\-\s]+', '', name)
    return name

def find_castle_image(castle_name, images_dir):
    """Trouve l'image correspondante pour un château"""
    # Normalise le nom du château
    castle_normalized = normalize_name_for_image(castle_name)
    
    # Liste toutes les images disponibles
    image_files = []
    for ext in ['*.jpg', '*.jpeg', '*.png', '*.gif']:
        image_files.extend(glob.glob(os.path.join(images_dir, ext)))
    
    # Essaie de trouver une correspondance
    best_match = None
    best_score = 0
    
    for image_path in image_files:
        image_name = os.path.basename(image_path)
        image_normalized = normalize_name_for_image(os.path.splitext(image_name)[0])
        
        # Correspondance exacte
        if castle_normalized in image_normalized or image_normalized in castle_normalized:
            return image_name
        
        # Correspondance par mots-clés
        castle_words = set(re.split(r'[_\-\s]+', castle_name.lower()))
        image_words = set(re.split(r'[_\-\s]+', os.path.splitext(image_name)[0].lower()))
        
        # Enlève les mots très communs
        common_words = {'kasteel', 'chateau', 'van', 'de', 'het', 'le', 'la', 'du', 'des', 'te', 'in', 'op', 'aan', 'hof'}
        castle_words -= common_words
        image_words -= common_words
        
        if castle_words and image_words:
            intersection = castle_words & image_words
            union = castle_words | image_words
            score = len(intersection) / len(union) if union else 0
            
            if score > best_score and score > 0.4:
                best_score = score
                best_match = image_name
    
    return best_match

def add_province_content(province_name):
    """Génère le contenu descriptif pour une province"""
    content_map = {
        'Antwerpen': {
            'intro': 'De provincie Antwerpen is een schatgraver voor liefhebbers van historische architectuur. Van imposante waterkastelen tot charmante hoven, deze regio toont de rijke geschiedenis van Vlaanderen door haar diverse kasteelcollectie.',
            'description': 'Ontdek kastelen die eeuwen van geschiedenis vertellen, van middeleeuwse verdedigingswerken tot elegante 19e-eeuwse landhuizen. Elk kasteel in Antwerpen heeft zijn eigen verhaal en architecturale bijzonderheden die de evolutie van de Vlaamse bouwkunst illustreren.'
        },
        'Oost-Vlaanderen': {
            'intro': 'Oost-Vlaanderen herbergt enkele van de meest pittoreske kastelen van België. Deze provincie combineert rijke geschiedenis met prachtige landschappen, waar kastelen als juwelen in het groene landschap liggen.',
            'description': 'Van de imposante kastelen rond Gent tot de verborgen pareltjes in het platteland, Oost-Vlaanderen biedt een diverse collectie die de rijke geschiedenis van deze streek weergeeft. Elk kasteel vertelt het verhaal van adellijke families en architecturale evolutie.'
        },
        'West-Vlaanderen': {
            'intro': 'West-Vlaanderen, met zijn rijke geschiedenis en strategische ligging, huisvest kastelen die getuigen van eeuwen van macht en elegantie. Van kustgebied tot binnenland, elk kasteel heeft zijn unieke charme.',
            'description': 'Ontdek kastelen die de geschiedenis van deze provincie hebben gevormd, van middeleeuwse vestingen tot romantische 19e-eeuwse creaties. West-Vlaanderen toont de diversiteit van de Vlaamse kasteelarchitectuur in al haar glorie.'
        },
        'Limburg': {
            'intro': 'De provincie Limburg verrast met zijn gevarieerde kasteellandschap, van imposante waterkastelen tot charmante landgoederen. Deze regio combineert Nederlandse en Duitse invloeden in haar architecturale erfgoed.',
            'description': 'Limburg biedt een unieke mix van kastelen die de grensligging van deze provincie weerspiegelen. Van de Commanderij van Alden Biesen tot kleinere hoven, elk kasteel draagt bij aan het rijke culturele erfgoed van deze streek.'
        },
        'Vlaams-Brabant': {
            'intro': 'Vlaams-Brabant, het hart van Vlaanderen, herbergt kastelen die de politieke en culturele geschiedenis van de regio weerspiegelen. Van koninklijke residenties tot adellijke landgoederen.',
            'description': 'Deze centrale provincie toont kastelen die eeuwenlang het centrum van macht en cultuur vormden. Van imposante kastelen nabij Brussel tot rustige landgoederen, Vlaams-Brabant biedt een rijke diversiteit aan architecturale schatten.'
        },
        'Namen': {
            'intro': 'De provincie Namen, gelegen in het hart van Wallonië, toont de Franse invloed in haar elegante kastelen en châteaux. Deze regio combineert natuurlijke schoonheid met architecturale pracht.',
            'description': 'Namen biedt spectaculaire kastelen die de Waalse architectuur in al haar glorie tonen. Van het beroemde Kasteel van Freÿr tot verborgen pareltjes langs de Maas, elk kasteel vertelt het verhaal van Waalse elegantie en geschiedenis.'
        },
        'Luik': {
            'intro': 'Luik, met zijn rijke industriële en culturele geschiedenis, herbergt kastelen die de evolutie van deze provincie illustreren. Van middeleeuwse vestingen tot 18e-eeuwse elegantie.',
            'description': 'De provincie Luik toont kastelen die de strategische belangrijkheid van deze regio door de eeuwen heen weerspiegelen. Van de Citadel van Hoei tot charmante landkastelen, elk monument draagt bij aan het rijke erfgoed van deze streek.'
        },
        'Luxemburg': {
            'intro': 'De Belgische provincie Luxemburg, met haar uitgestrekte bossen en heuvels, biedt kastelen die perfect geïntegreerd zijn in het Ardense landschap. Romantiek en geschiedenis gaan hier hand in hand.',
            'description': 'Luxemburg toont kastelen die de charme van de Ardennen belichamen. Van het pittoreske Durbuy tot imposante vestingen, deze provincie biedt kastelen die perfect harmoniëren met de natuurlijke schoonheid van het landschap.'
        },
        'Henegouwen': {
            'intro': 'Henegouwen, een provincie met een rijke industriële en culturele geschiedenis, herbergt kastelen die de Franse architecturale invloed in België tonen. Elegantie en geschiedenis verenigd.',
            'description': 'Deze provincie toont de Franse invloed in de Belgische kasteelarchitectuur. Van het imposante Kasteel van Seneffe tot charmante châteaux, Henegouwen biedt een unieke kijk op de Waalse architecturale traditie.'
        },
        'Waals-Brabant': {
            'intro': 'Waals-Brabant, de jongste provincie van België, combineert de charme van Waalse kastelen met de nabijheid van Brussel. Een unieke mix van culturen en architecturale stijlen.',
            'description': 'Deze provincie toont kastelen die de overgang tussen Vlaanderen en Wallonië illustreren. Van elegante 18e-eeuwse kastelen tot moderne restauraties, Waals-Brabant biedt een diverse collectie architecturale schatten.'
        }
    }
    
    return content_map.get(province_name, {
        'intro': f'De provincie {province_name} herbergt een rijke collectie kastelen die de geschiedenis en cultuur van deze regio weerspiegelen.',
        'description': f'Ontdek de kastelen van {province_name} en laat je verrassen door de architecturale diversiteit en historische rijkdom van deze provincie.'
    })

def update_province_page(file_path, images_dir):
    """Met à jour une page province avec images et contenu"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extrait le nom de la province
        province_match = re.search(r'<h1>Kastelen in ([^<]+)</h1>', content)
        if not province_match:
            return False, "Nom de province non trouvé"
        
        province_name = province_match.group(1)
        
        # Ajoute le contenu descriptif
        province_content = add_province_content(province_name)
        
        # Trouve la section après les stats
        stats_pattern = r'(<div class="stats">.*?</div>\s*</div>\s*</section>)'
        
        new_section = f'''\\1
    
    <section class="section province-intro">
      <div class="container">
        <div class="province-content">
          <p class="lead">{province_content['intro']}</p>
          <p>{province_content['description']}</p>
          <div class="province-navigation">
            <a href="index.html" class="btn btn-secondary">← Terug naar homepage</a>
            <a href="provinces.html" class="btn btn-ghost">Alle provincies →</a>
          </div>
        </div>
      </div>
    </section>'''
        
        # Ajoute la section si elle n'existe pas déjà
        if 'province-intro' not in content:
            content = re.sub(stats_pattern, new_section, content, flags=re.DOTALL)
        
        # Remplace les placeholders d'images par de vraies images
        castle_cards = re.findall(r'<a class="castle-card" href="([^"]+)"[^>]*>.*?<h3>([^<]+)</h3>', content, re.DOTALL)
        
        images_added = 0
        for castle_link, castle_name in castle_cards:
            # Trouve l'image correspondante
            castle_image = find_castle_image(castle_name, images_dir)
            
            if castle_image:
                # Remplace le gradient par l'image
                old_pattern = f'(<a class="castle-card" href="{re.escape(castle_link)}"[^>]*>\\s*)<div class="castle-media gradient-[0-9]"></div>'
                new_image = f'\\1<div class="castle-media"><img src="./chateaux_images/{castle_image}" alt="{castle_name}" class="castle-image"></div>'
                
                new_content = re.sub(old_pattern, new_image, content)
                if new_content != content:
                    content = new_content
                    images_added += 1
        
        # Écrit le fichier mis à jour
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True, f"Contenu ajouté, {images_added} images intégrées"
        
    except Exception as e:
        return False, f"Erreur: {e}"

def add_province_css():
    """Ajoute le CSS pour les pages provinces"""
    css_code = '''
/* Province pages */
.province-intro {
  background: #f8fafc;
  border-top: 1px solid #e2e8f0;
}

.province-content {
  max-width: 800px;
  margin: 0 auto;
  text-align: center;
}

.province-content .lead {
  font-size: 1.1rem;
  margin-bottom: 1.5rem;
}

.province-navigation {
  margin-top: 2rem;
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
}

.castle-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.castle-card:hover .castle-image {
  transform: scale(1.05);
}

@media (max-width: 640px) {
  .province-navigation {
    flex-direction: column;
    align-items: center;
  }
}'''
    
    css_file = '/Users/marc/Desktop/kastelenbelgie/css/style.css'
    
    try:
        with open(css_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if '/* Province pages */' not in content:
            with open(css_file, 'a', encoding='utf-8') as f:
                f.write(css_code)
            return True
        
        return False
        
    except Exception as e:
        print(f"Erreur CSS: {e}")
        return False

def main():
    """Fonction principale"""
    print("=== MISE À JOUR PAGES PROVINCES ===")
    
    images_dir = '/Users/marc/Desktop/kastelenbelgie/chateaux_images'
    
    # Ajoute le CSS
    print("Ajout du CSS pour les pages provinces...")
    if add_province_css():
        print("  ✓ CSS ajouté")
    else:
        print("  ○ CSS déjà présent")
    
    # Trouve toutes les pages provinces
    province_files = [
        '/Users/marc/Desktop/kastelenbelgie/antwerpen.html',
        '/Users/marc/Desktop/kastelenbelgie/oost-vlaanderen.html',
        '/Users/marc/Desktop/kastelenbelgie/west-vlaanderen.html',
        '/Users/marc/Desktop/kastelenbelgie/limburg.html',
        '/Users/marc/Desktop/kastelenbelgie/vlaams-brabant.html',
        '/Users/marc/Desktop/kastelenbelgie/namen.html',
        '/Users/marc/Desktop/kastelenbelgie/luik.html',
        '/Users/marc/Desktop/kastelenbelgie/luxemburg.html',
        '/Users/marc/Desktop/kastelenbelgie/henegouwen.html',
        '/Users/marc/Desktop/kastelenbelgie/waals-brabant.html'
    ]
    
    # Filtre les fichiers qui existent
    existing_files = [f for f in province_files if os.path.exists(f)]
    print(f"Trouvé {len(existing_files)} pages provinces")
    
    success_count = 0
    total_images = 0
    
    for file_path in existing_files:
        filename = os.path.basename(file_path)
        success, message = update_province_page(file_path, images_dir)
        
        if success:
            print(f"  ✓ {filename}: {message}")
            success_count += 1
            # Extrait le nombre d'images du message
            if "images intégrées" in message:
                images_count = int(message.split()[2])
                total_images += images_count
        else:
            print(f"  ✗ {filename}: {message}")
    
    print(f"\n=== RÉSULTAT ===")
    print(f"Pages provinces traitées: {len(existing_files)}")
    print(f"Pages mises à jour avec succès: {success_count}")
    print(f"Total images de châteaux ajoutées: {total_images}")
    print("Les pages provinces sont maintenant enrichies!")

if __name__ == "__main__":
    main()
