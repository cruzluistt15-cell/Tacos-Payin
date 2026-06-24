#!/usr/bin/env python3
"""
Servidor local para Tacos Payín
Corre este archivo y abre http://localhost:8080 en tu navegador.
"""

import http.server
import socketserver
import os
import webbrowser
import threading

PORT = 8080
DIRECTORIO = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORIO, **kwargs)
    
    def log_message(self, format, *args):
        print(f"  [{self.address_string()}] {format % args}")

def abrir_navegador():
    import time
    time.sleep(0.8)
    webbrowser.open(f"http://localhost:{PORT}")

print("=" * 50)
print("  🌮  Tacos Payín – Servidor Local")
print("=" * 50)
print(f"  Abriendo: http://localhost:{PORT}")
print("  Presiona Ctrl+C para detener")
print("=" * 50)

threading.Thread(target=abrir_navegador, daemon=True).start()

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n  Servidor detenido. ¡Hasta pronto! 🌮")
