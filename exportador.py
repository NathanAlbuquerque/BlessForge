#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo de Resolução de Dependências e Exportação de Modpacks.
Gera pacotes ZIP ou pastas completas prontas para jogar ou enviar a amigos.
"""

import os, zipfile, json, shutil, time

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
EXPORT_DIR = os.path.join(ROOT_DIR, "exportados")
os.makedirs(EXPORT_DIR, exist_ok=True)

from atualizar_catalogo import scan_all

def get_mod_lookups(mods):
    by_file = {}
    by_name = {}
    by_id = {}
    
    for m in mods:
        fn = m['file'].lower()
        by_file[fn] = m
        if m['mod_id']:
            by_id[m['mod_id'].lower()] = m
        by_name[m['name'].lower()] = m
        # Also clean short name
        short = fn.split('-')[0].lower()
        by_name[short] = m
        
    return by_file, by_name, by_id

def find_target_mod(dep_str, mods, by_file, by_name, by_id):
    dep_clean = dep_str.strip().lower()
    if not dep_clean or dep_clean in ('minecraft', 'neoforge', 'forge', 'java', 'fabricloader', 'fabric'):
        return None
        
    if dep_clean in by_id:
        return by_id[dep_clean]
    if dep_clean in by_name:
        return by_name[dep_clean]
    if dep_clean in by_file:
        return by_file[dep_clean]
        
    for m in mods:
        if dep_clean in m['name'].lower() or dep_clean in m['file'].lower() or (m['mod_id'] and dep_clean in m['mod_id'].lower()):
            return m
            
    return None

def resolve_modpack_selection(selected_files, mods=None):
    if mods is None:
        mods, _, _ = scan_all()
        
    by_file, by_name, by_id = get_mod_lookups(mods)
    
    # Track results
    selected_set = set()
    auto_deps_set = set()
    dep_reasons = {} # file -> list of "necessário para X"
    
    # Normalize initial selection
    queue = []
    for f in selected_files:
        f_clean = os.path.basename(f).lower()
        matched = None
        if f_clean in by_file:
            matched = by_file[f_clean]
        else:
            # try finding by name or id
            matched = find_target_mod(f, mods, by_file, by_name, by_id)
            
        if matched and matched['file'] not in selected_set:
            selected_set.add(matched['file'])
            queue.append(matched['file'])

    # Recursively resolve dependencies
    visited = set()
    while queue:
        current_file = queue.pop(0)
        if current_file in visited:
            continue
        visited.add(current_file)
        
        current_mod = by_file.get(current_file.lower())
        if not current_mod:
            continue
            
        for dep in current_mod['resolved_deps']:
            target_mod = find_target_mod(dep, mods, by_file, by_name, by_id)
            if target_mod:
                target_file = target_mod['file']
                if target_file not in selected_set and target_file not in auto_deps_set:
                    auto_deps_set.add(target_file)
                    queue.append(target_file)
                    
                if target_file not in dep_reasons:
                    dep_reasons[target_file] = []
                if current_mod['name'] not in dep_reasons[target_file]:
                    dep_reasons[target_file].append(current_mod['name'])

    total_files = list(selected_set.union(auto_deps_set))
    # Map back to full mod objects
    resolved_mods = [by_file[f.lower()] for f in total_files if f.lower() in by_file]
    resolved_mods.sort(key=lambda m: (m['category'], m['name'].lower()))
    
    return {
        "selected_files": sorted(list(selected_set)),
        "auto_dependencies": sorted(list(auto_deps_set)),
        "total_files": [m['file'] for m in resolved_mods],
        "mods": resolved_mods,
        "dep_reasons": dep_reasons
    }

def generate_manifest_and_readme(preset_name, resolved_result, selected_rps=[], mc_version="1.21.1", loader="NeoForge"):
    mods = resolved_result['mods']
    dep_reasons = resolved_result['dep_reasons']
    auto_deps = set(resolved_result['auto_dependencies'])
    
    # Readme text
    lines = []
    lines.append("=" * 70)
    lines.append(f"📦 MODPACK: {preset_name}")
    lines.append(f"🎮 Minecraft {mc_version} | Loader: {loader}")
    lines.append(f"📅 Gerado em: {time.strftime('%d/%m/%Y %H:%M:%S')}")
    lines.append(f"📊 Total de Mods: {len(mods)} ({len(resolved_result['selected_files'])} escolhidos + {len(auto_deps)} dependências automáticas)")
    lines.append("=" * 70)
    lines.append("\n🛠️ COMO INSTALAR ESTE MODPACK:")
    lines.append("1. Instale o NeoForge 1.21.1 no seu inicializador do Minecraft (ou use Prism / CurseForge / Modrinth).")
    lines.append("2. Extraia os arquivos da pasta 'mods/' para a pasta '.minecraft/mods/' do seu jogo.")
    if selected_rps:
        lines.append("3. Extraia os arquivos da pasta 'resourcepacks/' para '.minecraft/resourcepacks/' e ative-os no menu do jogo.")
    lines.append("4. Inicie o jogo e aproveite!\n")
    lines.append("=" * 70)
    lines.append("📋 LISTA DETALHADA DE MODS INCLUÍDOS:")
    lines.append("=" * 70)
    
    current_cat = None
    for m in mods:
        if m['category'] != current_cat:
            current_cat = m['category']
            lines.append(f"\n[{current_cat}]")
            
        is_auto = m['file'] in auto_deps
        tag = "[Dependência Requerida]" if is_auto else "[Selecionado]"
        reason_str = ""
        if is_auto and m['file'] in dep_reasons:
            reason_str = f" (exigido por: {', '.join(dep_reasons[m['file']])})"
            
        lines.append(f" • {m['name']} (v{m['version'] or '1.21.1'}) {tag}{reason_str}")
        lines.append(f"   Arquivo: {m['file']} | Lado: {m['side']}")
        if m['desc'] and m['desc'] != '---':
            lines.append(f"   Descrição: {m['desc']}")
        if m['url']:
            lines.append(f"   Link: {m['url']}")
            
    if selected_rps:
        lines.append("\n" + "=" * 70)
        lines.append("🎨 PACOTES DE RECURSOS (RESOURCE PACKS):")
        lines.append("=" * 70)
        for rp in selected_rps:
            lines.append(f" • {rp}")
            
    lines.append("\n" + "=" * 70)
    lines.append("Gerado automaticamente pelo Minecraft Mod Menu Suite.")
    lines.append("=" * 70)
    
    readme_text = "\n".join(lines)
    
    # Manifest JSON
    manifest = {
        "modpackName": preset_name,
        "minecraftVersion": mc_version,
        "modLoader": loader,
        "createdAt": time.strftime('%Y-%m-%d %H:%M:%S'),
        "modCount": len(mods),
        "selectedCount": len(resolved_result['selected_files']),
        "autoDepsCount": len(auto_deps),
        "mods": [
            {
                "id": m['mod_id'],
                "name": m['name'],
                "file": m['file'],
                "version": m['version'],
                "category": m['category'],
                "side": m['side'],
                "type": m['type'],
                "isAutoDependency": m['file'] in auto_deps,
                "requiredBy": dep_reasons.get(m['file'], []),
                "url": m['url']
            }
            for m in mods
        ],
        "resourcePacks": selected_rps
    }
    
    return readme_text, manifest

def export_modpack(preset_name, selected_files, include_deps=True, selected_rps=[], export_format="zip"):
    safe_name = "".join(c if c.isalnum() or c in ('-', '_') else '_' for c in preset_name.strip()).strip('_')
    if not safe_name:
        safe_name = f"BlessForge-{time.strftime('%Y%m%d-%H%M%S')}"
        
    mods, all_rps, _ = scan_all()
    
    if include_deps:
        res = resolve_modpack_selection(selected_files, mods)
    else:
        by_file, _, _ = get_mod_lookups(mods)
        sel = [by_file[f.lower()] for f in selected_files if f.lower() in by_file]
        res = {
            "selected_files": selected_files,
            "auto_dependencies": [],
            "total_files": selected_files,
            "mods": sel,
            "dep_reasons": {}
        }
        
    readme_text, manifest = generate_manifest_and_readme(safe_name, res, selected_rps)
    
    if export_format == "zip":
        zip_filename = f"{safe_name}.zip"
        zip_path = os.path.join(EXPORT_DIR, zip_filename)
        
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
            # 1. Add jars to mods/
            for m in res['mods']:
                src_path = m['path']
                if os.path.exists(src_path):
                    z.write(src_path, arcname=f"mods/{m['file']}")
                    
            # 2. Add resource packs
            for rp_name in selected_rps:
                rp_path = os.path.join(ROOT_DIR, "resourcepacks", rp_name)
                if os.path.exists(rp_path):
                    z.write(rp_path, arcname=f"resourcepacks/{rp_name}")
                    
            # 3. Add Readme & Manifest
            z.writestr("LEIA-ME_INSTALACAO.txt", readme_text)
            z.writestr("manifest.json", json.dumps(manifest, indent=2, ensure_ascii=False))
            
        file_size_mb = os.path.getsize(zip_path) / (1024 * 1024)
        return {
            "success": True,
            "format": "zip",
            "name": safe_name,
            "filename": zip_filename,
            "path": zip_path,
            "relative_path": f"exportados/{zip_filename}",
            "size": f"{file_size_mb:.2f} MB",
            "mod_count": len(res['mods']),
            "selected_count": len(res['selected_files']),
            "auto_deps_count": len(res['auto_dependencies']),
            "rp_count": len(selected_rps)
        }
    else:
        # Folder format
        folder_path = os.path.join(EXPORT_DIR, safe_name)
        mods_dest = os.path.join(folder_path, "mods")
        os.makedirs(mods_dest, exist_ok=True)
        
        for m in res['mods']:
            src = m['path']
            if os.path.exists(src):
                shutil.copy2(src, os.path.join(mods_dest, m['file']))
                
        if selected_rps:
            rp_dest = os.path.join(folder_path, "resourcepacks")
            os.makedirs(rp_dest, exist_ok=True)
            for rp_name in selected_rps:
                rp_src = os.path.join(ROOT_DIR, "resourcepacks", rp_name)
                if os.path.exists(rp_src):
                    shutil.copy2(rp_src, os.path.join(rp_dest, rp_name))
                    
        with open(os.path.join(folder_path, "LEIA-ME_INSTALACAO.txt"), 'w', encoding='utf-8') as f:
            f.write(readme_text)
        with open(os.path.join(folder_path, "manifest.json"), 'w', encoding='utf-8') as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)
            
        return {
            "success": True,
            "format": "folder",
            "name": safe_name,
            "path": folder_path,
            "relative_path": f"exportados/{safe_name}",
            "mod_count": len(res['mods']),
            "selected_count": len(res['selected_files']),
            "auto_deps_count": len(res['auto_dependencies']),
            "rp_count": len(selected_rps)
        }

if __name__ == '__main__':
    # Quick CLI test with Create: Gunsmithing
    test_res = resolve_modpack_selection(['create-gunsmithing-1.21.1-1.4.9.jar'])
    print(f"Selected 1 mod, resolved to {len(test_res['total_files'])} total mods:")
    for m in test_res['mods']:
        print(f"  • {m['name']} ({m['file']})")
