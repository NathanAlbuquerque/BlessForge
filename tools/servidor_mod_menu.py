#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Servidor local para o Minecraft Mod Menu.
Permite sincronizar novos mods e exportar modpacks personalizados (ZIP ou Pasta) com resolução automática de dependências.
"""

import os, sys, json, webbrowser, urllib.parse
from http.server import HTTPServer, SimpleHTTPRequestHandler
import socket

TOOLS_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(TOOLS_DIR)
os.chdir(ROOT_DIR)
sys.path.insert(0, TOOLS_DIR)

from atualizar_catalogo import scan_all, update_all
from exportador import resolve_modpack_selection, export_modpack, EXPORT_DIR

def find_free_port(start_port=8080):
    port = start_port
    while port < 9000:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('127.0.0.1', port)) != 0:
                return port
        port += 1
    return 8080

class ModMenuHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        query = urllib.parse.parse_qs(parsed.query)

        if path == '/' or path == '/index.html':
            self.path = '/mod_menu.html'
            return super().do_GET()

        elif path == '/api/sync':
            try:
                update_all()
                mods, rps, wishlist = scan_all()
                self.send_response(200)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.end_headers()
                res = json.dumps({"status": "ok", "message": "Catálogo sincronizado com sucesso!", "count": len(mods)})
                self.wfile.write(res.encode('utf-8'))
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.end_headers()
                res = json.dumps({"status": "error", "message": str(e)})
                self.wfile.write(res.encode('utf-8'))
            return

        elif path == '/api/export':
            try:
                fmt = query.get('format', ['zip'])[0]
                name = query.get('name', ['BlessForge-Custom'])[0]
                inc_rp = query.get('rps', ['0'])[0] == '1'
                files_raw = query.get('files', [''])[0]
                
                mods, rps, _ = scan_all()
                if files_raw:
                    selected = [f.strip() for f in files_raw.split(',') if f.strip()]
                    final_mods = resolve_modpack_selection(selected, mods)
                else:
                    final_mods = [m for m in mods if m['status'] == 'ATIVADO']

                out_path = export_modpack(final_mods, output_format=fmt, custom_name=name, include_resourcepacks=inc_rp)
                
                self.send_response(200)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.end_headers()
                res = json.dumps({
                    "status": "ok",
                    "file": os.path.basename(out_path),
                    "path": out_path,
                    "total_mods": len(final_mods)
                })
                self.wfile.write(res.encode('utf-8'))
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.end_headers()
                res = json.dumps({"status": "error", "message": str(e)})
                self.wfile.write(res.encode('utf-8'))
            return

        return super().do_GET()

def start_server():
    port = find_free_port(8080)
    server_address = ('127.0.0.1', port)
    httpd = HTTPServer(server_address, ModMenuHandler)
    url = f"http://127.0.0.1:{port}/"
    print("=" * 65)
    print("   🎮 BLESSFORGE — Servidor Local do Mod Menu")
    print("=" * 65)
    print(f" Servidor iniciado em: {url}")
    print(" Sincronização em tempo real e exportador habilitados.")
    print(" Pressione Ctrl+C no terminal para encerrar.")
    print("=" * 65)
    webbrowser.open(url)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor encerrado.")

if __name__ == '__main__':
    start_server()
