#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Extração Automática de Metadados e Sincronização do Catálogo BlessForge.
Lê os arquivos .jar em mods/ e desativados/, extrai ícones para assets/icons/,
gera o MODS_CATALOG.md em docs/ e atualiza o mod_menu.html interativo.
"""

import os
import zipfile
import re
import json
import shutil
from pathlib import Path

# Configura caminhos baseado na raiz do projeto (um nível acima de tools/)
TOOLS_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(TOOLS_DIR)
os.chdir(ROOT_DIR)

MODS_DIR = os.path.join(ROOT_DIR, "mods")
DESAT_DIR = os.path.join(ROOT_DIR, "desativados")
RP_DIR = os.path.join(ROOT_DIR, "resourcepacks")
DOCS_DIR = os.path.join(ROOT_DIR, "docs")
ASSETS_DIR = os.path.join(ROOT_DIR, "assets")
ICONS_DIR = os.path.join(ASSETS_DIR, "icons")

os.makedirs(MODS_DIR, exist_ok=True)
os.makedirs(DESAT_DIR, exist_ok=True)
os.makedirs(RP_DIR, exist_ok=True)
os.makedirs(DOCS_DIR, exist_ok=True)
os.makedirs(ICONS_DIR, exist_ok=True)

def parse_toml(text):
    data = {}
    current_section = data
    current_key = None
    
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if line.startswith('[[') and line.endswith(']]'):
            sec = line[2:-2].strip()
            parts = sec.split('.')
            d = data
            for p in parts[:-1]:
                d = d.setdefault(p, {})
            current_section = {}
            d.setdefault(parts[-1], []).append(current_section)
        elif line.startswith('[') and line.endswith(']'):
            sec = line[1:-1].strip()
            parts = sec.split('.')
            d = data
            for p in parts:
                d = d.setdefault(p, {})
            current_section = d
        elif '=' in line:
            k, v = line.split('=', 1)
            k = k.strip()
            v = v.strip().strip('"').strip("'")
            current_section[k] = v
    return data

def extract_icon(jar_path, out_icon_path):
    if os.path.exists(out_icon_path):
        return True
    try:
        with zipfile.ZipFile(jar_path, 'r') as z:
            logo_name = None
            if "META-INF/neoforge.mods.toml" in z.namelist():
                toml_text = z.read("META-INF/neoforge.mods.toml").decode('utf-8', errors='ignore')
                for line in toml_text.splitlines():
                    if 'logoFile' in line and '=' in line:
                        logo_name = line.split('=', 1)[1].strip().strip('"').strip("'")
                        break
            elif "META-INF/mods.toml" in z.namelist():
                toml_text = z.read("META-INF/mods.toml").decode('utf-8', errors='ignore')
                for line in toml_text.splitlines():
                    if 'logoFile' in line and '=' in line:
                        logo_name = line.split('=', 1)[1].strip().strip('"').strip("'")
                        break

            candidates = []
            if logo_name:
                candidates.extend([logo_name, logo_name.lstrip('/'), f"assets/{logo_name}"])
            candidates.extend(['icon.png', 'logo.png', 'pack.png', 'assets/icon.png', 'assets/logo.png'])
            
            for c in candidates:
                for item in z.namelist():
                    if item.lower() == c.lower() or item.lower().endswith('/' + c.lower()):
                        with open(out_icon_path, 'wb') as f:
                            f.write(z.read(item))
                        return True
            for item in z.namelist():
                if item.lower().endswith('.png') and any(k in item.lower() for k in ['icon', 'logo', 'pack']):
                    with open(out_icon_path, 'wb') as f:
                        f.write(z.read(item))
                    return True
    except Exception:
        pass
    return False

def inspect_jar(path, is_active=True):
    fname = os.path.basename(path)
    rel_path = f"mods/{fname}" if is_active else f"desativados/{fname}"
    info = {
        'file': fname,
        'path': path,
        'location': rel_path,
        'status': 'ATIVADO' if is_active else 'DESATIVADO',
        'name': fname,
        'mod_id': '',
        'version': '',
        'desc': '',
        'authors': '',
        'url': '',
        'side': 'Both',
        'type': 'Mod',
        'dependencies': [],
        'dependents': [],
        'category': '💡 Qualidade de Vida (QoL) & Utilidades',
        'icon': None,
        'size_mb': round(os.path.getsize(path) / (1024 * 1024), 2)
    }

    base_no_ext = os.path.splitext(fname)[0]
    icon_dest = os.path.join(ICONS_DIR, f"{base_no_ext}.png")
    if extract_icon(path, icon_dest) or os.path.exists(icon_dest):
        info['icon'] = f"assets/icons/{base_no_ext}.png"

    try:
        with zipfile.ZipFile(path, 'r') as z:
            names = z.namelist()
            if "META-INF/neoforge.mods.toml" in names or "META-INF/mods.toml" in names:
                toml_file = "META-INF/neoforge.mods.toml" if "META-INF/neoforge.mods.toml" in names else "META-INF/mods.toml"
                t_content = z.read(toml_file).decode('utf-8', errors='ignore')
                t_data = parse_toml(t_content)
                
                mods_list = t_data.get('mods', [])
                if isinstance(mods_list, list) and len(mods_list) > 0:
                    m = mods_list[0]
                    info['name'] = m.get('displayName', info['name'])
                    info['mod_id'] = m.get('modId', '')
                    info['version'] = m.get('version', '')
                    info['desc'] = m.get('description', '').replace('\n', ' ').strip()
                    info['authors'] = m.get('authors', '')
                    info['url'] = m.get('displayURL', '')
                
                deps_dict = t_data.get('dependencies', {})
                all_deps = []
                for mod_key, dep_list in deps_dict.items():
                    if isinstance(dep_list, list):
                        for dep in dep_list:
                            dep_id = dep.get('modId')
                            dep_type = dep.get('type', 'required')
                            dep_side = dep.get('side', 'BOTH')
                            if dep_id and dep_id not in ['minecraft', 'neoforge', 'forge', 'java']:
                                all_deps.append(dep_id)
                            if dep_side == 'CLIENT':
                                info['side'] = 'Client'
                            elif dep_side == 'SERVER':
                                info['side'] = 'Server'
                info['dependencies'] = list(dict.fromkeys(all_deps))
            elif "fabric.mod.json" in names:
                f_data = json.loads(z.read("fabric.mod.json").decode('utf-8', errors='ignore'))
                info['name'] = f_data.get('name', info['name'])
                info['mod_id'] = f_data.get('id', '')
                info['version'] = f_data.get('version', '')
                info['desc'] = f_data.get('description', '')
                info['side'] = f_data.get('environment', 'both').capitalize()
                deps = f_data.get('depends', {})
                info['dependencies'] = [k for k in deps.keys() if k not in ['minecraft', 'fabricloader', 'java']]
    except Exception:
        pass

    # Categorização inteligente
    fn_lower = fname.lower()
    desc_lower = info['desc'].lower()
    name_lower = info['name'].lower()
    all_text = f"{fn_lower} {name_lower} {desc_lower}"

    if any(k in all_text for k in ['sodium', 'culling', 'fps', 'ferritecore', 'modernfix', 'immediatelyfast', 'badoptimizations', 'entityculling', 'spark']):
        info['category'] = '⚡ Otimização & Performance'
    elif any(k in all_text for k in ['create', 'gunsmithing']):
        info['category'] = '⚙️ Tecnologia & Automação'
    elif any(k in all_text for k in ['sword', 'armor', 'weapon', 'simplyswords', 'armoroftheages', 'gun lib', 'ntgl']):
        info['category'] = '⚔️ Combate, Armas & Equipamentos'
    elif any(k in all_text for k in ['storage', 'backpack', 'tweak', 'bartering']):
        info['category'] = '🎒 Armazenamento & Inventário'
    elif any(k in all_text for k in ['dungeon', 'twilight', 'cataclysm', 'sift', 'caverns', 'tectonic', 'terralith', 'bumblezone', 'explorify', 't_and_t', 'towns']):
        info['category'] = '🗺️ Aventura, Dimensões & Estruturas'
    elif any(k in all_text for k in ['sound', 'ambient', 'footsteps', 'music', 'visual', 'cinematic', 'continuity', 'dynamiclights']):
        info['category'] = '🎨 Gráficos, Áudio & Imersão'
    elif any(k in all_text for k in ['betterf3', 'jade', 'menu', 'invmove', 'tooltip', 'appleskin', 'potions', 'litematica', 'forgematica', 'scribble', 'traveler']):
        info['category'] = '🖥️ Interface (UI/HUD) & Controles'
    elif any(k in all_text for k in ['api', 'lib', 'cloth', 'architectury', 'puzzles', 'u_team', 'kotlin', 'fzzy', 'geckolib', 'balm', 'curios', 'blueprint', 'lithostitched', 'cristel', 'resourceful', 'yung']):
        info['category'] = '📚 Bibliotecas, Frameworks & APIs'
        info['type'] = 'Lib'

    return info

def scan_all():
    mods = []
    # Mods ativos em mods/
    active_jars = [os.path.join(MODS_DIR, f) for f in os.listdir(MODS_DIR) if f.endswith('.jar')]
    for j in sorted(active_jars):
        mods.append(inspect_jar(j, is_active=True))

    # Mods desativados em desativados/
    if os.path.exists(DESAT_DIR):
        desat_jars = [os.path.join(DESAT_DIR, f) for f in os.listdir(DESAT_DIR) if f.endswith('.jar')]
        for j in sorted(desat_jars):
            mods.append(inspect_jar(j, is_active=False))

    # Resolução de dependências inversas (dependents)
    mod_id_map = {m['mod_id'].lower(): m for m in mods if m['mod_id']}
    name_map = {m['name'].lower(): m for m in mods}
    file_map = {m['file'].lower(): m for m in mods}

    for m in mods:
        for dep in m['dependencies']:
            d_clean = dep.lower()
            target = mod_id_map.get(d_clean) or name_map.get(d_clean) or file_map.get(d_clean)
            if target and m['name'] not in target['dependents']:
                target['dependents'].append(m['name'])

    # Resource packs
    rps = []
    if os.path.exists(RP_DIR):
        for f in sorted(os.listdir(RP_DIR)):
            if not f.endswith('.zip'):
                continue
            p = os.path.join(RP_DIR, f)
            base = os.path.splitext(f)[0]
            icon_path = os.path.join(ICONS_DIR, f"{base}.png")
            desc = "Resource pack para melhorias visuais e de interface."
            try:
                with zipfile.ZipFile(p, 'r') as z:
                    if 'pack.png' in z.namelist() and not os.path.exists(icon_path):
                        with open(icon_path, 'wb') as out_f:
                            out_f.write(z.read('pack.png'))
                    if 'pack.mcmeta' in z.namelist():
                        meta = json.loads(z.read('pack.mcmeta').decode('utf-8', errors='ignore'))
                        desc = meta.get('pack', {}).get('description', desc)
                        if isinstance(desc, dict):
                            desc = desc.get('text', str(desc))
            except Exception:
                pass

            has_icon = os.path.exists(icon_path)
            rps.append({
                "name": base,
                "file": f,
                "url": f"https://www.curseforge.com/minecraft/texture-packs/{base.lower().replace(' ', '-')}",
                "desc": desc,
                "icon_path": f"assets/icons/{base}.png" if has_icon else None
            })

    # Wishlist de docs/ideias_e_links.txt ou raiz
    wishlist = []
    ideias_file = os.path.join(DOCS_DIR, 'ideias_e_links.txt')
    if not os.path.exists(ideias_file):
        ideias_file = os.path.join(ROOT_DIR, 'ideias_e_links.txt')
        
    if os.path.exists(ideias_file):
        with open(ideias_file, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                raw = line.strip()
                if raw.startswith('http'):
                    slug = raw.rstrip('/').split('/')[-1]
                    name = slug.replace('-', ' ').title()
                    wtype = 'Datapack' if 'data-pack' in raw else ('Resource Pack' if 'texture-pack' in raw else 'Mod')
                    wishlist.append({
                        "name": name,
                        "type": wtype,
                        "url": raw,
                        "desc": f"{wtype} anotado para avaliação."
                    })
                elif raw and not raw.startswith('Pensando'):
                    wishlist.append({
                        "name": raw,
                        "type": "Mod/Ideia",
                        "url": "",
                        "desc": "Ideia ou mod citado nas anotações."
                    })

    return mods, rps, wishlist

def update_all():
    print("🔍 Escaneando diretório e analisando metadados dos mods...")
    mods, rps, wishlist = scan_all()
    
    active_count = sum(1 for m in mods if m['status'] == 'ATIVADO')
    disabled_count = sum(1 for m in mods if m['status'] == 'DESATIVADO')
    print(f"📊 Encontrados: {len(mods)} mods ({active_count} ativos, {disabled_count} desativados), {len(rps)} resource packs, {len(wishlist)} itens na wishlist.")

    # 1. Atualiza mod_menu.html
    html_file = os.path.join(ROOT_DIR, 'mod_menu.html')
    if os.path.exists(html_file):
        with open(html_file, 'r', encoding='utf-8') as f:
            html = f.read()

        clean_mods = []
        for m in mods:
            clean_mods.append({
                "name": m['name'],
                "file": m['file'],
                "location": m['location'],
                "status": m['status'],
                "category": m['category'],
                "side": m['side'],
                "type": m['type'],
                "version": m['version'],
                "mod_id": m['mod_id'],
                "url": m['url'] or f"https://www.curseforge.com/minecraft/mc-mods/{m['file'].split('-')[0].lower()}",
                "desc": m['desc'] or "Mod para Minecraft 1.21.1 NeoForge.",
                "icon_path": m['icon'],
                "dependencies": m['dependencies'],
                "dependents": m['dependents']
            })
            
        new_json = json.dumps({
            "mods": clean_mods,
            "resourcePacks": rps,
            "wishlist": wishlist
        }, ensure_ascii=False)
        
        html = re.sub(r'const DATA = \{.*?\};\n\n    let currentSelectedMod', f'const DATA = {new_json};\n\n    let currentSelectedMod', html, flags=re.DOTALL)
        html = re.sub(r'<span class="stat-badge" id="count-active">.*?</span>', f'<span class="stat-badge" id="count-active">🟢 {active_count} Ativos</span>', html)
        html = re.sub(r'<span class="stat-badge" id="count-disabled">.*?</span>', f'<span class="stat-badge" id="count-disabled">🔴 {disabled_count} Desativados</span>', html)
        html = re.sub(r'<span class="stat-badge" id="count-rps">.*?</span>', f'<span class="stat-badge" id="count-rps">🎨 {len(rps)} Resource Packs</span>', html)
        
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html)
        print("✅ mod_menu.html atualizado!")

    # 2. Gera docs/MODS_CATALOG.md
    categories = sorted(list(set(m['category'] for m in mods)))
    
    md_lines = []
    md_lines.append('# 📦 Catálogo Geral & Organização de Mods — Minecraft 1.21.1 (NeoForge)\n')
    md_lines.append('> [!TIP] 🎮 Interface Visual Interativa (Mod Menu Web) Pronta!')
    md_lines.append('> Criamos uma interface visual completa estilo in-game **Mod Menu** para você explorar seus mods com ícones oficiais extraídos, pesquisa em tempo real (`Ctrl+K`), dependências clicáveis e alternância entre Ativos, Desativados, Resource Packs e Wishlist.')
    md_lines.append('> 🔗 **Para abrir:** Execute `./abrir_mod_menu.sh` ou abra [mod_menu.html](../mod_menu.html) no navegador!\n')
    
    md_lines.append('## 📊 Resumo da Pasta Organizada\n')
    md_lines.append('| Localização / Status | Quantidade | Descrição |')
    md_lines.append('| :--- | :---: | :--- |')
    md_lines.append(f'| 🟢 **ATIVOS** (`mods/`) | **{active_count}** | Mods prontos para copiar/usar no Minecraft |')
    md_lines.append(f'| 🔴 **DESATIVADOS** (`desativados/`) | **{disabled_count}** | Mods isolados para teste ou backup |')
    md_lines.append(f'| 🎨 **RESOURCE PACKS** (`resourcepacks/`) | **{len(rps)}** | Pacotes visuais e de áudio em formato `.zip` |')
    md_lines.append(f'| **Total Geral** | **{len(mods)}** | **Arquivos JAR únicos catalogados** |\n')
    md_lines.append('---\n')
    
    md_lines.append('## 📑 Índice por Categorias\n')
    for cat in categories:
        cat_count = sum(1 for m in mods if m['category'] == cat)
        cat_id = cat.lower().replace(' ', '-').replace('&', '').replace('(', '').replace(')', '').replace('⚡', '').replace('⚔️', '').replace('⚙️', '').replace('🎒', '').replace('🎨', '').replace('💡', '').replace('📚', '').replace('🖥️', '').replace('🗺️', '').strip('-')
        md_lines.append(f'- [{cat} ({cat_count} mods)](#{cat_id})')
    md_lines.append('- [🎨 Resource Packs & Pacotes Visuais](#resource-packs--pacotes-visuais)')
    md_lines.append('- [📌 Mods e Datapacks em Análise / Lista de Desejos](#mods-e-datapacks-em-análise--lista-de-desejos)\n')
    md_lines.append('---\n')

    for cat in categories:
        md_lines.append(f'## {cat}\n')
        md_lines.append('| Status | Mod / Nome | Arquivo JAR | Lado | Tipo | Dependências | Usado Por (Dependentes) | Descrição & Links |')
        md_lines.append('| :---: | :--- | :--- | :---: | :---: | :--- | :--- | :--- |')
        cat_mods = [m for m in mods if m['category'] == cat]
        for m in sorted(cat_mods, key=lambda x: x['name'].lower()):
            st = '🟢 Ativo' if m['status'] == 'ATIVADO' else '🔴 Desativado'
            name_cell = f"**[{m['name']}]({m['url']})**" if m['url'] else f"**{m['name']}**"
            deps_cell = ', '.join(m['dependencies']) if m['dependencies'] else '---'
            dep_by_cell = ', '.join(m['dependents']) if m['dependents'] else '---'
            desc_cell = m['desc'][:160] + ('...' if len(m['desc']) > 160 else '') if m['desc'] else '---'
            md_lines.append(f"| {st} | {name_cell} | `{m['file']}` | {m['side']} | {m['type']} | {deps_cell} | {dep_by_cell} | {desc_cell} |")
        md_lines.append('\n---\n')

    # Seção Resource Packs
    md_lines.append('## 🎨 Resource Packs & Pacotes Visuais\n')
    md_lines.append('| Pacote / Nome | Arquivo ZIP | Descrição & Links |')
    md_lines.append('| :--- | :--- | :--- |')
    for rp in rps:
        md_lines.append(f"| **[{rp['name']}]({rp['url']})** | `{rp['file']}` | {rp['desc']} |")
    md_lines.append('\n---\n')

    # Seção Wishlist
    md_lines.append('## 📌 Mods e Datapacks em Análise / Lista de Desejos\n')
    md_lines.append('| Nome / Recurso | Tipo | Link / Referência | Descrição / Objetivo |')
    md_lines.append('| :--- | :---: | :--- | :--- |')
    for item in wishlist:
        link_str = f"[{item['name']}]({item['url']})" if item['url'] else item['name']
        md_lines.append(f"| **{item['name']}** | `{item['type']}` | {link_str} | {item['desc']} |")
    md_lines.append('\n')

    md_content = '\n'.join(md_lines)
    
    # Salva em docs/
    md_file = os.path.join(DOCS_DIR, 'MODS_CATALOG.md')
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(md_content)
    print("✅ docs/MODS_CATALOG.md atualizado!")

    # Atualiza artifact se existir
    artifact_path = "/home/n31415/.gemini/antigravity-cli/brain/eadfbbc5-c6da-4701-94e5-5fef22bcbeb7/MODS_CATALOG.md"
    if os.path.exists(os.path.dirname(artifact_path)):
        with open(artifact_path, 'w', encoding='utf-8') as f:
            f.write(md_content)

    print("\n🎉 Atualização concluída com sucesso! Todos os novos mods e ícones foram sincronizados.")

if __name__ == '__main__':
    update_all()
