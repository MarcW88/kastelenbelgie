#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SERVEUR DE DÉVELOPPEMENT POUR KASTELENBELGIE.BE
Lance un serveur HTTP local pour tester le site
"""

import http.server
import socketserver
import webbrowser
import os
import sys

def start_server(port=8000):
    """Lance le serveur de développement"""
    
    # Changer vers le répertoire du site
    site_dir = "/Users/marc/Desktop/kastelenbelgie"
    os.chdir(site_dir)
    
    print("🏰 SERVEUR DE DÉVELOPPEMENT - KASTELENBELGIE.BE")
    print("=" * 50)
    print(f"📁 Répertoire: {site_dir}")
    print(f"🌐 Port: {port}")
    print(f"🔗 URL: http://localhost:{port}")
    print("=" * 50)
    
    # Configuration du serveur
    handler = http.server.SimpleHTTPRequestHandler
    
    try:
        with socketserver.TCPServer(("", port), handler) as httpd:
            print(f"✅ Serveur démarré sur http://localhost:{port}")
            print("📖 Pages disponibles:")
            print(f"   • Homepage: http://localhost:{port}/")
            print(f"   • Provinces: http://localhost:{port}/provinces.html")
            print(f"   • Blog: http://localhost:{port}/blog.html")
            print(f"   • Contact: http://localhost:{port}/contact.html")
            print(f"   • Kasteel Freÿr: http://localhost:{port}/kasteel-van-freyr-freyr.html")
            print(f"   • Kasteel Bouchout: http://localhost:{port}/kasteel-van-bouchout-te-meise.html")
            print(f"   • Citadel Hoei: http://localhost:{port}/citadel-van-hoei-hoei.html")
            print()
            print("🔍 Fonctionnalités à tester:")
            print("   • Navigation entre les pages")
            print("   • Recherche de châteaux (barre de recherche)")
            print("   • Design responsive (redimensionner la fenêtre)")
            print("   • Formulaire de contact")
            print("   • Breadcrumbs et liens internes")
            print()
            print("⚠️  Pour arrêter le serveur: Ctrl+C")
            print("=" * 50)
            
            # Ouvrir automatiquement le navigateur
            try:
                webbrowser.open(f"http://localhost:{port}")
                print("🌐 Navigateur ouvert automatiquement")
            except:
                print("⚠️  Impossible d'ouvrir le navigateur automatiquement")
                print(f"   Ouvrez manuellement: http://localhost:{port}")
            
            print()
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n🛑 Serveur arrêté par l'utilisateur")
        sys.exit(0)
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"❌ Port {port} déjà utilisé. Essayez un autre port:")
            print(f"   python3 start_dev_server.py {port + 1}")
        else:
            print(f"❌ Erreur: {e}")
        sys.exit(1)

if __name__ == "__main__":
    port = 8000
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("❌ Port invalide. Utilisation du port par défaut 8000")
    
    start_server(port)
