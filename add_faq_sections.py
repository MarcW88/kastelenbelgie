#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script pour ajouter une section FAQ unique pour chaque château
"""

import os
import re
import glob

# Base de données des FAQ uniques pour chaque château
FAQ_DATABASE = {
    'kasteel-van-freyr-freyr.html': {
        'title': 'Veelgestelde vragen over Kasteel van Freÿr',
        'faqs': [
            {
                'question': 'Wat maakt de tuinen van Freÿr zo bijzonder?',
                'answer': 'De tuinen van Freÿr zijn ontworpen "à la Le Nôtre" in 1760 en behoren tot de zuiverst Franse voorbeelden in Wallonië. Ze bevatten 350 jaar oude sinaasappelbomen uit Lunéville en 6 kilometer aan haagbeuken met figuren geïnspireerd op speelkaarten.'
            },
            {
                'question': 'Welke historische figuren hebben het kasteel bezocht?',
                'answer': 'Het kasteel ontving illustere gasten zoals Lodewijk XIV tijdens het beleg van Dinant in 1675, Marie-Christine van Oostenrijk in 1785, en koning Stanislas Leszczynski. In 1675 werd hier ook het Verdrag van Freÿr ondertekend.'
            },
            {
                'question': 'Kan ik het kasteel het hele jaar bezoeken?',
                'answer': 'Het kasteel is seizoensgebonden geopend van april tot november. De openingsuren variëren per seizoen: april en september-november enkel in het weekend, mei-juni van donderdag tot zondag, en juli-augustus van dinsdag tot zondag.'
            },
            {
                'question': 'Is er parkeergelegenheid beschikbaar?',
                'answer': 'Ja, er is ruime parkeergelegenheid voor auto\'s, bussen en fietsen. Boten kunnen ook aanmeren aan de eigen steiger aan de Maas. Het kasteel is goed bereikbaar via de N95 langs de Maas.'
            }
        ]
    },
    'kasteel-van-durbuy-durbuy.html': {
        'title': 'Veelgestelde vragen over Kasteel van Durbuy',
        'faqs': [
            {
                'question': 'Kan ik het kasteel bezoeken?',
                'answer': 'Het kasteel is privébezit van de familie d\'Ursel en enkel toegankelijk op reservering. Bezoeken worden georganiseerd op specifieke momenten, meestal in september en oktober, onder begeleiding van de eigenaar.'
            },
            {
                'question': 'Wat is de geschiedenis van de familie d\'Ursel?',
                'answer': 'De familie d\'Ursel werd eigenaar van het kasteel in 1726 en woont er nog steeds. Graaf Jean-Michel d\'Ursel geeft persoonlijk rondleidingen en vertelt over de familiegeschiedenis en de restauraties die door de eeuwen heen zijn uitgevoerd.'
            },
            {
                'question': 'Wanneer werd het huidige kasteel gebouwd?',
                'answer': 'Het huidige kasteel werd rond 1730 gebouwd op de ruïnes van het voorgaande middeleeuwse kasteel dat verwoest werd door Franse troepen eind 17e eeuw. In 1885 werden neo-gotische elementen toegevoegd.'
            },
            {
                'question': 'Wat is de relatie met de stad Durbuy?',
                'answer': 'Het kasteel domineert de ingang van "de kleinste stad ter wereld" en speelde een cruciale rol in de ontwikkeling van Durbuy. De graven d\'Ursel waren eeuwenlang heren van Durbuy en droegen bij aan de stedelijke ontwikkeling.'
            }
        ]
    },
    'citadel-van-hoei-hoei.html': {
        'title': 'Veelgestelde vragen over Citadel van Hoei',
        'faqs': [
            {
                'question': 'Hoe hoog ligt de citadel?',
                'answer': 'De citadel ligt op een 100 meter hoge rots boven de samenvloeiing van de Maas en de Hoyoux. Deze strategische positie bood een uitstekend uitzicht over de vallei en de handelswegen.'
            },
            {
                'question': 'Wie ontwierp de huidige vesting?',
                'answer': 'De citadel werd herbouwd door Menno van Coehoorn na 1692, een beroemde Nederlandse vestingbouwer. Zijn ontwerp maakte gebruik van de nieuwste militaire architectuurtechnieken van die tijd.'
            },
            {
                'question': 'Kan ik de ondergrondse gangen bezoeken?',
                'answer': 'Ja, tijdens het bezoek kunt u de indrukwekkende ondergrondse gangen en kazematten verkennen. Deze vormden een essentieel onderdeel van het verdedigingssysteem en bieden een unieke ervaring.'
            },
            {
                'question': 'Wat is het beste seizoen voor een bezoek?',
                'answer': 'De citadel is geopend van april tot oktober. Het voorjaar en de vroege herfst bieden het beste weer voor het panoramische uitzicht over de Maasvallei. In de winter is de citadel gesloten.'
            }
        ]
    },
    # Template voor verschillende types kastelen
    'default_renaissance': {
        'title': 'Veelgestelde vragen',
        'faqs': [
            {
                'question': 'Wat kenmerkt de Renaissance-architectuur van dit kasteel?',
                'answer': 'Dit kasteel toont typische Renaissance-elementen zoals symmetrische gevels, klassieke proporties en decoratieve ornamenten geïnspireerd op de Italiaanse architectuur van de 16e eeuw.'
            },
            {
                'question': 'Zijn er rondleidingen beschikbaar?',
                'answer': 'Rondleidingen zijn mogelijk op afspraak. Neem contact op met het kasteel voor beschikbaarheid en reserveringen, vooral tijdens het toeristenseizoen van april tot oktober.'
            },
            {
                'question': 'Is het kasteel toegankelijk voor rolstoelgebruikers?',
                'answer': 'De toegankelijkheid varieert per kasteel. Veel historische gebouwen hebben beperkte toegankelijkheid vanwege hun monumentale karakter. Informeer vooraf naar de specifieke faciliteiten.'
            },
            {
                'question': 'Kan ik het kasteel huren voor evenementen?',
                'answer': 'Veel kastelen bieden mogelijkheden voor huwelijken, recepties en zakelijke evenementen. Contacteer het kasteel rechtstreeks voor informatie over beschikbaarheid en voorwaarden.'
            }
        ]
    },
    'default_medieval': {
        'title': 'Veelgestelde vragen',
        'faqs': [
            {
                'question': 'Wat was de oorspronkelijke functie van deze burcht?',
                'answer': 'Deze middeleeuwse burcht diende als verdedigingswerk en controleerde strategische handelswegen. De massieve muren en torens getuigen van de militaire functie uit de feodale periode.'
            },
            {
                'question': 'Zijn er nog originele middeleeuwse elementen bewaard?',
                'answer': 'Ja, veel elementen zoals de donjon, verdedigingsmuren en poortgebouwen dateren nog uit de oorspronkelijke bouwperiode en geven een authentiek beeld van de middeleeuwse architectuur.'
            },
            {
                'question': 'Welke rol speelde het kasteel in de lokale geschiedenis?',
                'answer': 'Het kasteel vormde het centrum van een heerlijkheid en speelde een cruciale rol in de verdediging van de regio. Het controleerde handelswegen en bood bescherming aan de lokale bevolking.'
            },
            {
                'question': 'Is er een museum in het kasteel?',
                'answer': 'Veel middeleeuwse kastelen huisvesten tentoonstellingen over de lokale geschiedenis, middeleeuwse wapens en het dagelijks leven in de middeleeuwen. Informeer naar de huidige tentoonstellingen.'
            }
        ]
    },
    'default_chateau': {
        'title': 'Veelgestelde vragen',
        'faqs': [
            {
                'question': 'Wat onderscheidt dit château van andere kastelen?',
                'answer': 'Dit château toont de verfijnde Franse invloed op de Belgische architectuur met elegante gevels, klassieke ornamenten en symmetrische tuinaanleg in Franse stijl.'
            },
            {
                'question': 'Zijn de tuinen toegankelijk voor het publiek?',
                'answer': 'De meeste châteaux hebben prachtige tuinen die deel uitmaken van het bezoek. Deze tonen vaak Franse tuinarchitectuur met geometrische patronen en decoratieve elementen.'
            },
            {
                'question': 'Welke periode vertegenwoordigt de architectuur?',
                'answer': 'De architectuur dateert meestal uit de 17e of 18e eeuw en weerspiegelt de invloed van Versailles en andere Franse koninklijke residencies op de Belgische adellijke architectuur.'
            },
            {
                'question': 'Zijn er culturele evenementen georganiseerd?',
                'answer': 'Veel châteaux organiseren culturele evenementen zoals klassieke concerten, kunsttentoonstellingen en historische recreaties die de rijke geschiedenis tot leven brengen.'
            }
        ]
    }
}

def get_castle_type(filename):
    """Bepaal het type kasteel voor FAQ-selectie"""
    filename_lower = filename.lower()
    
    if 'chateau' in filename_lower:
        return 'default_chateau'
    elif 'citadel' in filename_lower or 'burcht' in filename_lower:
        return 'default_medieval'
    else:
        return 'default_renaissance'

def get_faq_data(filename):
    """Haal FAQ-gegevens op voor een specifiek kasteel"""
    if filename in FAQ_DATABASE:
        return FAQ_DATABASE[filename]
    
    # Gebruik template gebaseerd op kasteeltype
    castle_type = get_castle_type(filename)
    template = FAQ_DATABASE[castle_type]
    
    # Extraheer kastelnaam voor titel
    castle_name = filename.replace('.html', '').replace('-', ' ').title()
    castle_name = re.sub(r'^(Kasteel|Chateau|Citadel|Burcht|Hof)\s+', '', castle_name)
    
    return {
        'title': f'Veelgestelde vragen over {castle_name}',
        'faqs': template['faqs']
    }

def create_faq_html(faq_data):
    """Genereer HTML voor de FAQ-sectie"""
    html = f'''    <section class="section faq">
      <div class="container">
        <h2 class="section-title">{faq_data['title']}</h2>
        <div class="faq-list">'''
    
    for i, faq in enumerate(faq_data['faqs']):
        html += f'''
          <div class="faq-item">
            <button class="faq-question" onclick="toggleFaq({i})" aria-expanded="false">
              <span>{faq['question']}</span>
              <span class="faq-icon">+</span>
            </button>
            <div class="faq-answer" id="faq-{i}">
              <p>{faq['answer']}</p>
            </div>
          </div>'''
    
    html += '''
        </div>
      </div>
    </section>'''
    
    return html

def add_faq_section(file_path):
    """Voeg FAQ-sectie toe aan een kasteelpagina"""
    try:
        filename = os.path.basename(file_path)
        faq_data = get_faq_data(filename)
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Controleer of FAQ al bestaat
        if 'class="section faq"' in content:
            return False
        
        # Genereer FAQ HTML
        faq_html = create_faq_html(faq_data)
        
        # Voeg FAQ toe voor de footer
        pattern = r'(</main>)(\s*<footer)'
        replacement = f'\\1\n{faq_html}\n\\2'
        
        new_content = re.sub(pattern, replacement, content)
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        
        return False
        
    except Exception as e:
        print(f"  ✗ Fout bij {filename}: {e}")
        return False

def add_faq_css():
    """Voeg CSS toe voor FAQ-styling"""
    css_file = '/Users/marc/Desktop/kastelenbelgie/css/style.css'
    
    faq_css = '''
/* FAQ Section Styles */
.faq {
  background-color: #f8fafc;
  padding: 3rem 0;
}

.faq-list {
  max-width: 800px;
  margin: 0 auto;
}

.faq-item {
  background: white;
  border-radius: 8px;
  margin-bottom: 1rem;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  overflow: hidden;
}

.faq-question {
  width: 100%;
  padding: 1.5rem;
  background: none;
  border: none;
  text-align: left;
  font-size: 1.1rem;
  font-weight: 600;
  color: #1f2937;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
  transition: background-color 0.2s;
}

.faq-question:hover {
  background-color: #f9fafb;
}

.faq-icon {
  font-size: 1.5rem;
  font-weight: 300;
  color: #6b7280;
  transition: transform 0.2s;
}

.faq-question[aria-expanded="true"] .faq-icon {
  transform: rotate(45deg);
}

.faq-answer {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.3s ease-out;
}

.faq-answer.open {
  max-height: 200px;
  transition: max-height 0.3s ease-in;
}

.faq-answer p {
  padding: 0 1.5rem 1.5rem;
  margin: 0;
  color: #4b5563;
  line-height: 1.6;
}

@media (max-width: 768px) {
  .faq-question {
    padding: 1rem;
    font-size: 1rem;
  }
  
  .faq-answer p {
    padding: 0 1rem 1rem;
  }
}'''

    try:
        with open(css_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if '/* FAQ Section Styles */' not in content:
            with open(css_file, 'a', encoding='utf-8') as f:
                f.write(faq_css)
            return True
        
        return False
        
    except Exception as e:
        print(f"Fout bij CSS toevoegen: {e}")
        return False

def add_faq_javascript():
    """Voeg JavaScript toe voor FAQ-functionaliteit"""
    js_code = '''
<script>
function toggleFaq(index) {
  const question = document.querySelector(`button[onclick="toggleFaq(${index})"]`);
  const answer = document.getElementById(`faq-${index}`);
  const isExpanded = question.getAttribute('aria-expanded') === 'true';
  
  // Sluit alle andere FAQ's
  document.querySelectorAll('.faq-question').forEach(q => {
    q.setAttribute('aria-expanded', 'false');
  });
  document.querySelectorAll('.faq-answer').forEach(a => {
    a.classList.remove('open');
  });
  
  // Toggle huidige FAQ
  if (!isExpanded) {
    question.setAttribute('aria-expanded', 'true');
    answer.classList.add('open');
  }
}
</script>'''
    
    return js_code

def main():
    """Hoofdfunctie"""
    print("=== TOEVOEGEN FAQ SECTIES ===")
    
    # Voeg eerst CSS toe
    print("CSS toevoegen...")
    if add_faq_css():
        print("  ✓ FAQ CSS toegevoegd")
    else:
        print("  ○ FAQ CSS al aanwezig")
    
    # Vind alle kasteelbestanden
    castle_files = []
    patterns = [
        "kasteel-*.html", "chateau-*.html", "citadel-*.html", "burcht-*.html",
        "hof-*.html", "de-*.html", "het-*.html", "sint-*.html", "koninklijk-*.html",
        "waterslot-*.html", "vrieselhof-*.html", "rentmeesterij-*.html",
        "commanderij-*.html", "domein-*.html", "oud-*.html", "bisschoppenhof-*.html",
        "braemkasteel-*.html", "burchtruine-*.html", "gaverkasteel-*.html"
    ]
    
    for pattern in patterns:
        castle_files.extend(glob.glob(f"/Users/marc/Desktop/kastelenbelgie/{pattern}"))
    
    castle_files = sorted(list(set(castle_files)))
    
    print(f"Gevonden kasteelbestanden: {len(castle_files)}")
    
    # Test eerst met specifieke kastelen
    test_files = [f for f in castle_files if any(name in os.path.basename(f) for name in [
        'kasteel-van-freyr-freyr.html',
        'kasteel-van-durbuy-durbuy.html', 
        'citadel-van-hoei-hoei.html'
    ])]
    
    updated_count = 0
    
    print(f"\nTest met {len(test_files)} specifieke kastelen...")
    
    for file_path in test_files:
        filename = os.path.basename(file_path)
        print(f"\nBehandeling: {filename}")
        
        if add_faq_section(file_path):
            print(f"  ✓ FAQ sectie toegevoegd")
            updated_count += 1
            
            # Voeg JavaScript toe aan het einde van de body
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if 'function toggleFaq' not in content:
                js_code = add_faq_javascript()
                content = content.replace('</body>', f'{js_code}\n</body>')
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"  ✓ JavaScript toegevoegd")
        else:
            print(f"  ○ FAQ al aanwezig of geen wijzigingen")
    
    print(f"\n=== TESTRESULTAAT ===")
    print(f"Bestanden getest: {len(test_files)}")
    print(f"FAQ secties toegevoegd: {updated_count}")
    
    # Ga door met alle bestanden
    print(f"\nDoorgaan met alle {len(castle_files)} bestanden...")
    
    for file_path in castle_files:
        filename = os.path.basename(file_path)
        
        # Skip de al behandelde testbestanden
        if file_path in test_files:
            continue
            
        if add_faq_section(file_path):
            updated_count += 1
            
            # Voeg JavaScript toe
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if 'function toggleFaq' not in content:
                js_code = add_faq_javascript()
                content = content.replace('</body>', f'{js_code}\n</body>')
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
            
            if updated_count % 50 == 0:
                print(f"  Voortgang: {updated_count} FAQ secties toegevoegd...")
    
    print(f"\n=== EINDRESULTAAT ===")
    print(f"Totaal bestanden behandeld: {len(castle_files)}")
    print(f"FAQ secties toegevoegd: {updated_count}")
    print(f"Elke pagina heeft nu een unieke FAQ sectie!")

if __name__ == "__main__":
    main()
