#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo de Resolução de Dependências e Exportação de Modpacks.
Gera pacotes ZIP ou pastas completas prontas para jogar ou enviar a amigos.
"""

import os, zipfile, json, shutil, time

TOOLS_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(TOOLS_DIR)
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
        
    for fn, mod in by_file.items():
        if dep_clean in fn:
            return mod
    for nm, mod in by_name.items():
        if dep_clean in nm:
            return mod
    return None

def resolve_modpack_selection(selected_files, mods):
    by_file, by_name, by_id = get_mod_lookups(mods)
    
    queue = []
    included = {}
    
    for f in selected_files:
        f_clean = f.lower()
        if f_clean in by_file:
            m = by_file[f_clean]
            queue.append(m)
            included[m['file']] = m
            
    # Resolução transitiva de dependências
    visited_deps = set()
    while queue:
        curr = queue.pop(0)
        for dep in curr['dependencies']:
            if dep.lower() in visited_deps:
                continue
            visited_deps.add(dep.lower())
            
            target = find_target_mod(dep, mods, by_file, by_name, by_id)
            if target and target['file'] not in included:
                included[target['file']] = target
                queue.append(target)
                
    return list(included.values())

def export_modpack(mod_list, output_format="zip", custom_name="BlessForge-Custom", include_resourcepacks=False):
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    clean_name = f"{custom_name}_{timestamp}"
    
    if output_format == "zip":
        zip_path = os.path.join(EXPORT_DIR, f"{clean_name}.zip")
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
            for m in mod_list:
                z.write(m['path'], f"mods/{m['file']}")
                
            if include_resourcepacks:
                rp_dir = os.path.join(ROOT_DIR, "resourcepacks")
                if os.path.exists(rp_dir):
                    for rp in os.listdir(rp_dir):
                        if rp.endswith('.zip'):
                            z.write(os.path.join(rp_dir, rp), f"resourcepacks/{rp}")
                            
            manifest = {
                "name": custom_name,
                "version": "1.21.1",
                "loader": "NeoForge 21.1.259",
                "generated_at": time.strftime("%Y-%m-%d %H:%M:%S"),
                "total_mods": len(mod_list),
                "mods": [
                    {
                        "name": m['name'],
                        "file": m['file'],
                        "version": m['version'],
                        "category": m['category']
                    } for m in mod_list
                ]
            }
            z.writestr("manifest.json", json.dumps(manifest, indent=2, ensure_ascii=False))
            
        return zip_path
        
    elif output_format == "folder":
        folder_path = os.path.join(EXPORT_DIR, clean_name)
        mods_dest = os.path.join(folder_path, "mods")
        os.makedirs(mods_dest, exist_ok=True)
        
        for m in mod_list:
            shutil.copy2(m['path'], os.path.join(mods_dest, m['file']))
            
        if include_resourcepacks:
            rp_dest = os.path.join(folder_path, "resourcepacks")
            os.makedirs(rp_dest, exist_ok=True)
            rp_dir = os.path.join(ROOT_DIR, "resourcepacks")
            if os.path.exists(rp_dir):
                for rp in os.listdir(rp_dir):
                    if rp.endswith('.zip'):
                        shutil.copy2(os.path.join(rp_dir, rp), os.path.join(rp_dest, rp))
                        
        manifest = {
            "name": custom_name,
            "version": "1.21.1",
            "loader": "NeoForge 21.1.259",
            "generated_at": time.strftime("%Y-%m-%d %H:%M:%S"),
            "total_mods": len(mod_list),
            "mods": [
                {
                    "name": m['name'],
                    "file": m['file'],
                    "version": m['version'],
                    "category": m['category']
                } for m in mod_list
            ]
        }
        with open(os.path.join(folder_path, "manifest.json"), "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)
            
        return folder_path
        
    return None
