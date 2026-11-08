#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Servidor local para o Minecraft Mod Menu.
Permite sincronizar novos mods e exportar modpacks personalizados (ZIP ou Pasta) com resolução automática de dependências.
"""

import os, sys, json, webbrowser, urllib.parse
from http.server import HTTPServer, SimpleHTTPRequestHandler
import socket

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT_DIR)

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
            
        elif path == '/api/status':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'online': True}).encode('utf-8'))
            return

        elif path == '/api/scan':
            try:
                update_all()
                mods, rps, wishlist = scan_all()
                clean_mods = []
                for m in mods:
                    clean_mods.append({
                        "id": m['mod_id'],
                        "name": m['name'],
                        "file": m['file'],
                        "version": m['version'],
                        "status": m['status'],
                        "location": m['location'],
                        "category": m['category'],
                        "type": m['type'],
                        "side": m['side'],
                        "size": m['size_str'],
                        "url": m['url'],
                        "desc": m['desc'],
                        "deps": m['resolved_deps'],
                        "dependents": m['dependents'],
                        "user_comment": m.get('user_comment', ''),
                        "icon": m.get('icon_path') or ''
                    })
                response_data = {
                    "success": True,
                    "stats": {
                        "active": sum(1 for m in mods if m['status'] == 'ATIVADO'),
                        "disabled": sum(1 for m in mods if m['status'] == 'DESATIVADO'),
                        "total": len(mods),
                        "resourcePacks": len(rps)
                    },
                    "data": {
                        "mods": clean_mods,
                        "resourcePacks": rps,
                        "wishlist": wishlist
                    }
                }
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(response_data, ensure_ascii=False).encode('utf-8'))
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"success": False, "error": str(e)}).encode('utf-8'))
            return

        elif path == '/api/download':
            # Download an exported zip file
            filename = query.get('file', [''])[0]
            # sanitize filename
            safe_filename = os.path.basename(filename)
            file_path = os.path.join(EXPORT_DIR, safe_filename)
            if safe_filename.endswith('.zip') and os.path.exists(file_path):
                file_size = os.path.getsize(file_path)
                self.send_response(200)
                self.send_header('Content-Type', 'application/zip')
                self.send_header('Content-Disposition', f'attachment; filename="{safe_filename}"')
                self.send_header('Content-Length', str(file_size))
                self.end_headers()
                with open(file_path, 'rb') as f:
                    shutil.copyfileobj(f, self.wfile)
                return
            else:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b"Arquivo nao encontrado.")
                return

        return super().do_GET()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length).decode('utf-8')
        try:
            req_data = json.loads(body) if body else {}
        except:
            req_data = {}

        if path == '/api/resolve':
            # Live dependency resolver preview
            files = req_data.get('files', [])
            res = resolve_modpack_selection(files)
            clean_res = {
                "selected_files": res['selected_files'],
                "auto_dependencies": res['auto_dependencies'],
                "total_count": len(res['total_files']),
                "total_files": res['total_files'],
                "dep_reasons": res['dep_reasons']
            }
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(clean_res, ensure_ascii=False).encode('utf-8'))
            return

        elif path == '/api/export':
            preset_name = req_data.get('presetName', 'MeuModpack')
            selected_files = req_data.get('selectedFiles', [])
            include_deps = req_data.get('includeDeps', True)
            selected_rps = req_data.get('selectedRps', [])
            export_format = req_data.get('format', 'zip')

            try:
                res = export_modpack(preset_name, selected_files, include_deps=include_deps, selected_rps=selected_rps, export_format=export_format)
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(res, ensure_ascii=False).encode('utf-8'))
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"success": False, "error": str(e)}).encode('utf-8'))
            return

        self.send_response(404)
        self.end_headers()

def run_server():
    port = find_free_port(8080)
    server_address = ('127.0.0.1', port)
    httpd = HTTPServer(server_address, ModMenuHandler)
    url = f"http://localhost:{port}"
    print(f"\n=======================================================")
    print(f"🚀 Minecraft Mod Menu Server rodando em:")
    print(f"   👉 {url}")
    print(f"=======================================================")
    print(f"Pressione Ctrl+C para encerrar o servidor a qualquer momento.\n")
    
    try:
        webbrowser.open(url)
    except:
        pass
        
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor encerrado.")
        httpd.server_close()

if __name__ == '__main__':
    run_server()
