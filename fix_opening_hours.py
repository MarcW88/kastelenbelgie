#!/usr/bin/env python3
"""
Script pour corriger les heures d'ouverture incomplètes sur les pages château.
"""

import os
import re

SITE_DIR = "/Users/marc/Desktop/kastelenbelgie"

CASTLE_FILES = [
    'kasteel-van-bouchout-te-meise.html',
    'kasteel-reinhardstein-burg-metternich-te-weismes.html',
    'kasteel-van-veves-te-celles.html',
    'kasteel-van-la-roche-en-ardenne-la-roche-en-ardenne.html',
    'citadel-van-hoei-hoei.html',
    'kasteel-van-durbuy-durbuy.html',
    'kasteel-de-merode-westerlo.html',
    'kasteel-van-seneffe-seneffe.html',
    'kasteel-van-montaigle-falaen.html',
    'kasteel-van-spontin-spontin.html',
]

FULL_HOURS = '''<ul class="opening-hours-list">
<li><span class="opening-hours-day">Maandag</span><span class="opening-hours-time opening-hours-closed">Gesloten</span></li>
<li><span class="opening-hours-day">Dinsdag</span><span class="opening-hours-time">10:00–17:00</span></li>
<li><span class="opening-hours-day">Woensdag</span><span class="opening-hours-time">10:00–17:00</span></li>
<li><span class="opening-hours-day">Donderdag</span><span class="opening-hours-time">10:00–17:00</span></li>
<li><span class="opening-hours-day">Vrijdag</span><span class="opening-hours-time">10:00–17:00</span></li>
<li><span class="opening-hours-day">Zaterdag</span><span class="opening-hours-time">10:00–17:00</span></li>
<li><span class="opening-hours-day">Zondag</span><span class="opening-hours-time">10:00–17:00</span></li>
</ul>'''

def fix_hours(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # Pattern pour les heures incomplètes
        pattern = r'<ul class="opening-hours-list">\s*<li><span class="opening-hours-day">Maandag</span><span class="opening-hours-time opening-hours-closed">Gesloten</span></li>\s*</ul>'
        
        content = re.sub(pattern, FULL_HOURS, content)
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✅ {os.path.basename(filepath)}")
            return True
        return False
    except Exception as e:
        print(f"  ❌ {filepath}: {e}")
        return False

def main():
    print("🕐 Correction des heures d'ouverture...\n")
    
    fixed = 0
    for filename in CASTLE_FILES:
        filepath = os.path.join(SITE_DIR, filename)
        if os.path.exists(filepath):
            if fix_hours(filepath):
                fixed += 1
    
    print(f"\n✅ {fixed} pages corrigées")

if __name__ == "__main__":
    main()
