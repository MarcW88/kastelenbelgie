#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MONITEUR DE PROGRESSION EN TEMPS RÉEL
Affiche une barre de progression continue pour la génération des châteaux
"""

import os
import time
import glob
from datetime import datetime

def monitor_progress():
    """Monitore la progression de génération des pages châteaux"""
    print("📊 MONITEUR DE PROGRESSION EN TEMPS RÉEL")
    print("=" * 60)
    
    # Compter les fichiers HTML de châteaux existants
    html_files = glob.glob("/Users/marc/Desktop/kastelenbelgie/kasteel-*.html")
    html_files += glob.glob("/Users/marc/Desktop/kastelenbelgie/hof-*.html")
    html_files += glob.glob("/Users/marc/Desktop/kastelenbelgie/het-*.html")
    html_files += glob.glob("/Users/marc/Desktop/kastelenbelgie/de-*.html")
    html_files += glob.glob("/Users/marc/Desktop/kastelenbelgie/sint-*.html")
    html_files += glob.glob("/Users/marc/Desktop/kastelenbelgie/chateau-*.html")
    html_files += glob.glob("/Users/marc/Desktop/kastelenbelgie/burcht-*.html")
    html_files += glob.glob("/Users/marc/Desktop/kastelenbelgie/paleis-*.html")
    html_files += glob.glob("/Users/marc/Desktop/kastelenbelgie/commanderij-*.html")
    html_files += glob.glob("/Users/marc/Desktop/kastelenbelgie/waterkasteel-*.html")
    html_files += glob.glob("/Users/marc/Desktop/kastelenbelgie/waterburcht-*.html")
    html_files += glob.glob("/Users/marc/Desktop/kastelenbelgie/koninklijk-*.html")
    html_files += glob.glob("/Users/marc/Desktop/kastelenbelgie/gaverkasteel-*.html")
    
    # Supprimer les doublons
    html_files = list(set(html_files))
    
    total_expected = 262  # Nombre total de châteaux
    current_count = len(html_files)
    
    print(f"📈 Pages générées: {current_count}/{total_expected}")
    
    # Barre de progression
    progress = (current_count / total_expected) * 100
    bar_length = 50
    filled_length = int(bar_length * current_count // total_expected)
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    
    print(f"🔄 Progression: |{bar}| {progress:.1f}%")
    
    if current_count >= total_expected:
        print("✅ GÉNÉRATION COMPLÈTE !")
    else:
        remaining = total_expected - current_count
        print(f"⏳ Restant: {remaining} châteaux")
    
    print(f"🕒 Dernière vérification: {datetime.now().strftime('%H:%M:%S')}")
    
    # Analyser les derniers fichiers créés
    print("\n📋 DERNIERS CHÂTEAUX GÉNÉRÉS:")
    html_files_with_time = []
    for file in html_files[-10:]:  # 10 derniers fichiers
        try:
            mtime = os.path.getmtime(file)
            filename = os.path.basename(file)
            html_files_with_time.append((filename, mtime))
        except:
            continue
    
    # Trier par date de modification
    html_files_with_time.sort(key=lambda x: x[1], reverse=True)
    
    for i, (filename, mtime) in enumerate(html_files_with_time[:5], 1):
        mod_time = datetime.fromtimestamp(mtime).strftime('%H:%M:%S')
        castle_name = filename.replace('.html', '').replace('-', ' ').title()
        print(f"  {i}. {castle_name} ({mod_time})")
    
    return current_count, total_expected

def continuous_monitor():
    """Moniteur continu avec mise à jour automatique"""
    print("🔄 DÉMARRAGE DU MONITEUR CONTINU")
    print("Appuyez sur Ctrl+C pour arrêter")
    print()
    
    try:
        while True:
            os.system('clear')  # Nettoyer l'écran
            current, total = monitor_progress()
            
            if current >= total:
                print("\n🎉 GÉNÉRATION TERMINÉE !")
                break
            
            print(f"\n⏳ Prochaine vérification dans 10 secondes...")
            time.sleep(10)
            
    except KeyboardInterrupt:
        print("\n\n⏹️ Moniteur arrêté par l'utilisateur")

if __name__ == "__main__":
    # Vérification unique
    monitor_progress()
    
    print("\n" + "=" * 60)
    print("Options:")
    print("1. Vérification unique (terminée)")
    print("2. Pour moniteur continu, relancez avec: python3 progress_monitor.py --continuous")
    
    import sys
    if "--continuous" in sys.argv:
        continuous_monitor()
