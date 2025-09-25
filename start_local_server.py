#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SERVEUR LOCAL POUR TESTER LE SITE
Démarre un serveur HTTP local pour tester l'affichage des grilles
"""

import http.server
import socketserver
import webbrowser
import threading
import time

def start_server():
    """Démarre un serveur HTTP local"""
    PORT = 8000
    
    class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
        def end_headers(self):
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Expires', '0')
            super().end_headers()
    
    try:
        with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
            print(f"🌐 Serveur démarré sur http://localhost:{PORT}")
            print(f"📱 Pages à tester:")
            print(f"   • Homepage: http://localhost:{PORT}/index.html")
            print(f"   • Antwerpen: http://localhost:{PORT}/antwerpen.html")
            print(f"   • Château exemple: http://localhost:{PORT}/kasteel-van-freyr-freyr.html")
            print(f"\n🎯 VÉRIFICATIONS À FAIRE:")
            print(f"   1. Les châteaux s'affichent-ils en 3 colonnes sur antwerpen.html ?")
            print(f"   2. Les hover effects fonctionnent-ils ?")
            print(f"   3. Le design est-il responsive ?")
            print(f"\n⏹️  Appuyez sur Ctrl+C pour arrêter le serveur")
            
            # Ouvrir automatiquement la page Antwerpen
            def open_browser():
                time.sleep(1)
                webbrowser.open(f'http://localhost:{PORT}/antwerpen.html')
            
            threading.Thread(target=open_browser, daemon=True).start()
            
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n🛑 Serveur arrêté")
    except Exception as e:
        print(f"❌ Erreur serveur: {e}")

if __name__ == "__main__":
    print("🚀 DÉMARRAGE DU SERVEUR LOCAL POUR TEST")
    print("=" * 50)
    start_server()
