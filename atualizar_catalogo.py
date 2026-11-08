#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de sincronização automática do Minecraft Mod Menu.
Escaneia a pasta por novos mods (.jar), extrai ícones oficiais,
recalcula dependências e atualiza mod_menu.html e MODS_CATALOG.md.
"""

import os, zipfile, json, re, base64

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT_DIR)

ICONS_DIR = os.path.join(ROOT_DIR, "assets", "icons")
os.makedirs(ICONS_DIR, exist_ok=True)
DESAT_DIR = os.path.join(ROOT_DIR, "desativados")
os.makedirs(DESAT_DIR, exist_ok=True)
RP_DIR = os.path.join(ROOT_DIR, "resourcepacks")
os.makedirs(RP_DIR, exist_ok=True)

# Mapeamentos e Aliases
LIB_IDS = {
    'cloth_config', 'cloth-config', 'cloth-config2', 'yacl', 'fzzy_config', 'curios',
    'lionfishapi', 'geckolib', 'playeranimator', 'balm', 'puzzleslib', 'forgeconfigapiport',
    'forgified_fabric_api', 'architectury', 'ftblibrary', 'sophisticatedcore', 'anvianslib',
    'kotlinforforge', 'kotlinlangforge', 'blueprint', 'respackopts', 'mafglib', 'libjf',
    'connector', 'ntgl'
}

CLIENT_FILES = {
    'sodium', 'sodium-extra', 'moreculling', 'immediatelyfast', 'dynamic-fps', 'appleskin',
    'distinguishedpotions', 'betterf3', 'mod menu', 'simplytooltips', 'scribble', 'invmove',
    'mousetweaks', 'forgematica', 'continuity', 'lambdynamiclights', 'sound-physics-remastered',
    'presencefootsteps', 'skin_changer', 'chesttracker', 'improved-inventory-tabs', 'cinematic_respawn',
    'distanthorizons'
}

CURSE_FALLBACKS = {
    'ferritecore': 'https://www.curseforge.com/minecraft/mc-mods/ferritecore-fabric',
    'modernfix': 'https://www.curseforge.com/minecraft/mc-mods/modernfix',
    'sodium': 'https://www.curseforge.com/minecraft/mc-mods/sodium',
    'sodium-extra': 'https://www.curseforge.com/minecraft/mc-mods/sodium-extra',
    'moreculling': 'https://www.curseforge.com/minecraft/mc-mods/more-culling',
    'immediatelyfast': 'https://www.curseforge.com/minecraft/mc-mods/immediatelyfast',
    'toms_storage': 'https://www.curseforge.com/minecraft/mc-mods/toms-storage',
    'sophisticatedbackpacks': 'https://www.curseforge.com/minecraft/mc-mods/sophisticated-backpacks',
    'sophisticatedcore': 'https://www.curseforge.com/minecraft/mc-mods/sophisticated-core',
    'twilightforest': 'https://www.curseforge.com/minecraft/mc-mods/the-twilight-forest',
    'simplyswords': 'https://www.curseforge.com/minecraft/mc-mods/simply-swords',
    'ftbultimine': 'https://www.curseforge.com/minecraft/mc-mods/ftb-ultimine-forge',
    'ftblibrary': 'https://www.curseforge.com/minecraft/mc-mods/ftb-library-forge',
    'ftbranks': 'https://www.curseforge.com/minecraft/mc-mods/ftb-ranks-forge',
    'lootr': 'https://www.curseforge.com/minecraft/mc-mods/lootr',
    'NaturesCompass': 'https://www.curseforge.com/minecraft/mc-mods/natures-compass',
    'gravestone': 'https://www.curseforge.com/minecraft/mc-mods/gravestone-mod',
    'trade-cycling': 'https://www.curseforge.com/minecraft/mc-mods/trade-cycling',
    'BarteringStation': 'https://www.curseforge.com/minecraft/mc-mods/bartering-station',
    'connector': 'https://www.curseforge.com/minecraft/mc-mods/sinytra-connector',
    'continuity': 'https://www.curseforge.com/minecraft/mc-mods/continuity',
    'lambdynamiclights': 'https://www.curseforge.com/minecraft/mc-mods/lambdynamiclights',
    'sound-physics-remastered': 'https://www.curseforge.com/minecraft/mc-mods/sound-physics-remastered',
    'PresenceFootsteps': 'https://www.curseforge.com/minecraft/mc-mods/presence-footsteps',
    'skin_changer': 'https://www.curseforge.com/minecraft/mc-mods/skin-changer',
    'MouseTweaks': 'https://www.curseforge.com/minecraft/mc-mods/mouse-tweaks',
    'InvMove': 'https://www.curseforge.com/minecraft/mc-mods/invmove',
    'SimplyTooltips': 'https://www.curseforge.com/minecraft/mc-mods/simply-tooltips',
    'Scribble': 'https://www.curseforge.com/minecraft/mc-mods/scribble',
    'forgematica': 'https://www.curseforge.com/minecraft/mc-mods/forgematica',
    'respackopts': 'https://www.curseforge.com/minecraft/mc-mods/respackopts',
    'mafglib': 'https://www.curseforge.com/minecraft/mc-mods/mafglib',
    'libjf': 'https://www.curseforge.com/minecraft/mc-mods/libjf',
    'architectury': 'https://www.curseforge.com/minecraft/mc-mods/architectury-api',
    'the-sift': 'https://www.curseforge.com/minecraft/mc-mods/the-sift',
    'jei': 'https://www.curseforge.com/minecraft/mc-mods/jei',
    'blueprint': 'https://www.curseforge.com/minecraft/mc-mods/blueprint',
    'DungeonsArise': 'https://www.curseforge.com/minecraft/mc-mods/when-dungeons-arise',
    'caverns_and_chasms': 'https://www.curseforge.com/minecraft/mc-mods/caverns-and-chasms',
    'DistantHorizons': 'https://www.curseforge.com/minecraft/mc-mods/distant-horizons'
}

ID_ALIASES = {
    'cloth_config': 'Cloth Config API',
    'cloth-config': 'Cloth Config API',
    'cloth-config2': 'Cloth Config API',
    'yacl': 'YetAnotherConfigLib',
    'fzzy_config': 'Fzzy Config',
    'fzzy-config': 'Fzzy Config',
    'curios': 'Curios API',
    'lionfishapi': 'Lionfish API',
    'geckolib': 'GeckoLib',
    'playeranimator': 'playerAnimator',
    'balm': 'Balm',
    'puzzleslib': 'Puzzles Lib',
    'forgeconfigapiport': 'Forge Config API Port',
    'forgified_fabric_api': 'Forgified Fabric API',
    'fabric_api': 'Forgified Fabric API',
    'architectury': 'Architectury API',
    'ftblibrary': 'FTB Library',
    'sophisticatedcore': 'Sophisticated Core',
    'anvianslib': "Anvian's Lib",
    'kotlinforforge': 'Kotlin for Forge',
    'kotlinlangforge': 'KotlinLangForge',
    'blueprint': 'Blueprint',
    'respackopts': 'Respackopts',
    'mafglib': 'MafgLib',
    'libjf': 'LibJF',
    'connector': 'Sinytra Connector',
    'create': 'Create',
    'jei': 'Just Enough Items',
    'emi': 'EMI'
}

def clean_text(t):
    if not t:
        return ""
    return " ".join(t.strip().split())

def extract_icon(jar_path, out_icon_path):
    if os.path.exists(out_icon_path):
        return True
    try:
        with zipfile.ZipFile(jar_path) as z:
            names = z.namelist()
            logo_name = None
            toml_files = [n for n in names if n in ('META-INF/neoforge.mods.toml', 'META-INF/mods.toml')]
            if toml_files:
                content = z.read(toml_files[0]).decode('utf-8', errors='ignore')
                m_logo = re.search(r'logoFile\s*=\s*\"([^\"]+)\"', content)
                if m_logo:
                    logo_name = m_logo.group(1).strip()
            if not logo_name and 'fabric.mod.json' in names:
                try:
                    fj = json.loads(z.read('fabric.mod.json').decode('utf-8', errors='ignore'))
                    logo_name = fj.get('icon')
                    if isinstance(logo_name, dict):
                        logo_name = logo_name.get('128') or logo_name.get('64') or logo_name.get('32') or list(logo_name.values())[0]
                except:
                    pass
            target_entry = None
            if logo_name:
                for n in names:
                    if n.lower() == logo_name.lower() or n.lower().endswith('/' + logo_name.lower()):
                        target_entry = n
                        break
            if not target_entry:
                for cand in ['logo.png', 'icon.png', 'assets/icon.png', 'assets/logo.png', 'pack.png']:
                    for n in names:
                        if n.lower() == cand or n.lower().endswith('/' + cand):
                            target_entry = n
                            break
                    if target_entry:
                        break
            if target_entry:
                with open(out_icon_path, 'wb') as f:
                    f.write(z.read(target_entry))
                return True
    except:
        pass
    return False

def parse_mod_jar(path, is_active):
    fname = os.path.basename(path)
    res = {
        'file': fname,
        'path': path,
        'status': 'ATIVADO' if is_active else 'DESATIVADO',
        'location': fname if is_active else f"desativados/{fname}",
        'mod_id': '',
        'name': '',
        'version': '',
        'desc': '',
        'url': '',
        'deps': [],
        'type': 'Mod',
        'side': 'Both'
    }
    
    # Calculate file size
    try:
        size = os.path.getsize(path)
        if size >= 1024 * 1024:
            res['size_str'] = f"{size / (1024 * 1024):.2f} MB"
        else:
            res['size_str'] = f"{size / 1024:.1f} KB"
    except:
        res['size_str'] = "---"

    try:
        with zipfile.ZipFile(path) as z:
            names = z.namelist()
            toml_files = [n for n in names if n in ('META-INF/neoforge.mods.toml', 'META-INF/mods.toml')]
            fabric_files = [n for n in names if n == 'fabric.mod.json']
            
            if toml_files:
                content = z.read(toml_files[0]).decode('utf-8', errors='ignore')
                m_id = re.search(r'modId\s*=\s*\"([^\"]+)\"', content)
                d_name = re.search(r'displayName\s*=\s*\"([^\"]+)\"', content)
                ver = re.search(r'version\s*=\s*\"([^\"]+)\"', content)
                url = re.search(r'displayURL\s*=\s*\"([^\"]+)\"', content)
                desc_match = re.search(r'description\s*=\s*\'\'\'(.*?)\'\'\'|description\s*=\s*\"\"\"(.*?)\"\"\"|description\s*=\s*\"([^\"]+)\"', content, re.DOTALL)
                
                if m_id: res['mod_id'] = m_id.group(1).strip()
                if d_name: res['name'] = d_name.group(1).strip()
                if ver: res['version'] = ver.group(1).strip()
                if url: res['url'] = url.group(1).strip()
                if desc_match:
                    res['desc'] = clean_text(desc_match.group(1) or desc_match.group(2) or desc_match.group(3) or '')
                    
                dep_blocks = re.findall(r'\[\[dependencies\.[^\]]+\]\](.*?)(?=\[\[|\Z)', content, re.DOTALL)
                for blk in dep_blocks:
                    dep_id = re.search(r'modId\s*=\s*\"([^\"]+)\"', blk)
                    if dep_id:
                        d_val = dep_id.group(1).strip()
                        if d_val not in ('minecraft', 'neoforge', 'forge', 'java'):
                            res['deps'].append(d_val)
                            
            elif fabric_files:
                fj = json.loads(z.read(fabric_files[0]).decode('utf-8', errors='ignore'))
                res['mod_id'] = fj.get('id', '')
                res['name'] = fj.get('name', '')
                res['version'] = fj.get('version', '')
                res['desc'] = clean_text(fj.get('description', ''))
                contact = fj.get('contact', {})
                res['url'] = contact.get('homepage', '') or contact.get('sources', '')
                for dep_id in (fj.get('depends') or {}):
                    if dep_id not in ('minecraft', 'java', 'fabricloader', 'fabric'):
                        res['deps'].append(dep_id)
                        
            elif 'META-INF/MANIFEST.MF' in names:
                mf = z.read('META-INF/MANIFEST.MF').decode('utf-8', errors='ignore')
                title = re.search(r'Implementation-Title:\s*(.+)', mf)
                if title:
                    res['name'] = title.group(1).strip()
    except:
        pass

    # Fallbacks and overrides
    if 'connector' in fname.lower():
        res['name'] = 'Sinytra Connector'
        res['mod_id'] = 'connector'
        res['desc'] = 'Run Fabric mods on NeoForge / Forge'
        res['url'] = 'https://www.curseforge.com/minecraft/mc-mods/sinytra-connector'
    elif 'kotlinforforge' in fname.lower():
        res['name'] = 'Kotlin for Forge'
        res['mod_id'] = 'kotlinforforge'
        res['desc'] = 'Provides Kotlin language support for Forge and NeoForge mods.'
        res['url'] = 'https://www.curseforge.com/minecraft/mc-mods/kotlin-for-forge'
    elif 'ferritecore' in fname.lower():
        res['name'] = 'FerriteCore'
        res['mod_id'] = 'ferritecore'
        res['desc'] = 'Memory usage optimizations for modern Minecraft.'
        res['url'] = 'https://www.curseforge.com/minecraft/mc-mods/ferritecore-fabric'

    if not res['name']:
        res['name'] = fname.split('-')[0].capitalize()
    if not res['desc']:
        res['desc'] = "Sem descrição detalhada disponível."

    # CurseForge URL fallback
    if not res['url'] or 'change.me' in res['url'] or 'example.com' in res['url']:
        for k, v in CURSE_FALLBACKS.items():
            if k.lower() in fname.lower() or k.lower() == res['mod_id'].lower():
                res['url'] = v
                break

    # Classify Type
    mid = res['mod_id'].lower()
    fn_lower = fname.lower()
    if mid in LIB_IDS or 'lib' in fn_lower or 'api' in fn_lower or 'config' in fn_lower:
        res['type'] = 'Lib'
    else:
        res['type'] = 'Mod'

    # Classify Side
    is_client = any(cf in fn_lower or cf in res['name'].lower() for cf in CLIENT_FILES)
    res['side'] = 'Client' if is_client else 'Both'

    # Category
    if any(k in fn_lower or k in res['name'].lower() for k in ['sodium', 'moreculling', 'immediatelyfast', 'modernfix', 'dynamic-fps', 'ferritecore']):
        res['category'] = '⚡ Otimização & Performance'
    elif any(k in fn_lower or k in res['name'].lower() for k in ['create', 'gunsmithing']):
        res['category'] = '⚙️ Tecnologia & Automação'
    elif any(k in fn_lower or k in res['name'].lower() for k in ['backpack', 'toms_storage', 'storage', 'inventorytweak', 'inventory-tabs', 'chesttracker', 'chest']):
        res['category'] = '🎒 Armazenamento & Inventário'
    elif any(k in fn_lower or k in res['name'].lower() for k in ['cataclysm', 'twilightforest', 'twilight forest', 'dungeonsarise', 'dungeon', 'caverns_and_chasms']):
        res['category'] = '🗺️ Aventura, Dimensões & Estruturas'
    elif any(k in fn_lower or k in res['name'].lower() for k in ['simplyswords', 'armoroftheages', 'armor of the ages', 'ntgl', 'upgrader']):
        res['category'] = '⚔️ Combate, Armas & Equipamentos'
    elif any(k in fn_lower or k in res['name'].lower() for k in ['betterf3', 'jade', 'mod menu', 'appleskin', 'distinguished', 'potions', 'simplytooltips', 'scribble', 'invmove', 'mousetweaks', 'forgematica']):
        res['category'] = '🖥️ Interface (UI/HUD) & Controles'
    elif any(k in fn_lower or k in res['name'].lower() for k in ['distanthorizons', 'continuity', 'lambdynamiclights', 'sound-physics', 'presencefootsteps', 'skin_changer', 'symbols_n_stuff']):
        res['category'] = '🎨 Gráficos, Áudio & Imersão'
    elif res['type'] == 'Lib' or any(k in fn_lower or k in res['name'].lower() for k in ['lib', 'api', 'config', 'connector', 'kotlin', 'architectury', 'blueprint', 'respackopts']):
        res['category'] = '📚 Bibliotecas, Frameworks & APIs'
    else:
        res['category'] = '💡 Qualidade de Vida (QoL) & Utilidades'

    # Icon handling
    base_no_ext = os.path.splitext(fname)[0]
    icon_dest = os.path.join(ICONS_DIR, f"{base_no_ext}.png")
    if extract_icon(path, icon_dest) or os.path.exists(icon_dest):
        res['icon_path'] = f"assets/icons/{base_no_ext}.png"
    else:
        res['icon_path'] = None

    # Preserve special user notes
    if 'improved-inventory-tabs' in fname:
        res['user_comment'] = "Não melhorou muito a qualidade de vida, polui a tela e não se adequa muito as ui dos outros mods."
    elif 'chesttracker' in fname:
        res['user_comment'] = "Desativado temporariamente."
    elif 'emi' in fname:
        res['user_comment'] = "Desativado temporariamente para testes com JEI."

    return res

def scan_all():
    root_jars = [os.path.join(ROOT_DIR, f) for f in os.listdir(ROOT_DIR) if f.endswith('.jar')]
    desat_jars = [os.path.join(DESAT_DIR, f) for f in os.listdir(DESAT_DIR) if f.endswith('.jar')]
    
    mods = []
    for p in sorted(root_jars):
        mods.append(parse_mod_jar(p, is_active=True))
    for p in sorted(desat_jars):
        mods.append(parse_mod_jar(p, is_active=False))

    # Name mapping for dependencies
    name_map = {}
    for m in mods:
        if m['mod_id']:
            name_map[m['mod_id'].lower()] = m['name']
        base = m['file'].split('-')[0].lower()
        name_map[base] = m['name']
    name_map.update(ID_ALIASES)

    # Compute dependencies & dependents
    for m in mods:
        resolved = []
        for raw in m['deps']:
            canon = name_map.get(raw.lower(), raw)
            if canon not in resolved and canon.lower() not in ('minecraft', 'neoforge', 'forge', 'java'):
                resolved.append(canon)
        m['resolved_deps'] = resolved
        m['dependents'] = []

    for m in mods:
        m_name = m['name']
        for dep in m['resolved_deps']:
            for target in mods:
                if dep.lower() in target['name'].lower() or target['name'].lower() in dep.lower():
                    if m_name not in target['dependents'] and m_name != target['name']:
                        target['dependents'].append(m_name)

    # Scan Resource Packs
    rps = []
    # Add Fantasy Ores
    rps.append({
        "name": "Fantasy Ores by CesarZorak",
        "file": "Planilha / CurseForge",
        "status": "ATIVADO",
        "url": "https://www.curseforge.com/minecraft/texture-packs/fantasy-ores-by-cesarzorak",
        "desc": "Minérios com estilo visual de fantasia medieval refinada.",
        "icon_path": None
    })
    
    for f in sorted(os.listdir(RP_DIR)):
        if f.endswith('.zip'):
            p = os.path.join(RP_DIR, f)
            base = os.path.splitext(f)[0]
            icon_path = os.path.join(ICONS_DIR, f"{base}.png")
            # Extract pack.png if needed
            if not os.path.exists(icon_path):
                try:
                    with zipfile.ZipFile(p) as z:
                        if 'pack.png' in z.namelist():
                            with open(icon_path, 'wb') as out_f:
                                out_f.write(z.read('pack.png'))
                except:
                    pass
            has_icon = os.path.exists(icon_path)
            
            # Simple descriptions
            desc = "Pacote de textura e recursos."
            if "cave" in f.lower(): desc = "Efeitos sonoros imersivos, ecos e ambientação atmosférica para cavernas."
            elif "enchants" in f.lower(): desc = "Ícones e texturas visuais únicas para cada tipo de encantamento."
            elif "fire" in f.lower(): desc = "Reduz a altura das chamas na tela quando o jogador está em chamas."
            elif "path" in f.lower(): desc = "Conecta texturas de caminhos e estradas de terra perfeitamente."
            elif "3d" in f.lower(): desc = "Modelagem tridimensional sutil para blocos e itens no estilo vanilla."
            
            rps.append({
                "name": base.split(' ')[0] if ' ' in base else base,
                "file": f,
                "status": "PRONTO",
                "url": f"https://www.curseforge.com/minecraft/texture-packs/{base.lower().replace(' ', '-')}",
                "desc": desc,
                "icon_path": f"assets/icons/{base}.png" if has_icon else None
            })

    # Wishlist from ideias_e_links.txt
    wishlist = []
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

    # 1. Update mod_menu.html
    # We update the JSON data inside mod_menu.html
    html_file = os.path.join(ROOT_DIR, 'mod_menu.html')
    if os.path.exists(html_file):
        with open(html_file, 'r', encoding='utf-8') as f:
            html = f.read()
            
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
            
        new_json = json.dumps({
            "mods": clean_mods,
            "resourcePacks": rps,
            "wishlist": wishlist
        }, ensure_ascii=False)
        
        # Replace DATA in html
        html = re.sub(r'const DATA = \{.*?\};\n\n    let currentSelectedMod', f'const DATA = {new_json};\n\n    let currentSelectedMod', html, flags=re.DOTALL)
        # Update header stats counters
        html = re.sub(r'<span id="stat-active">\d+</span>', f'<span id="stat-active">{active_count}</span>', html)
        html = re.sub(r'<span id="stat-disabled">\d+</span>', f'<span id="stat-disabled">{disabled_count}</span>', html)
        html = re.sub(r'<span id="tab-count-mods">\d+</span>', f'<span id="tab-count-mods">{len(mods)}</span>', html)
        
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html)
        print("✅ mod_menu.html atualizado!")

    # 2. Update MODS_CATALOG.md
    md_file = os.path.join(ROOT_DIR, 'MODS_CATALOG.md')
    mods.sort(key=lambda m: (m['category'], 0 if m['status'] == 'ATIVADO' else 1, m['name'].lower()))
    
    categories = sorted(list(set(m['category'] for m in mods)))
    
    md_lines = []
    md_lines.append('# 📦 Catálogo Geral & Organização de Mods — Minecraft 1.21.1 (NeoForge)\n')
    md_lines.append('> [!TIP] 🎮 Interface Visual Interativa (Mod Menu Web) Pronta!')
    md_lines.append('> Criamos uma interface visual completa estilo in-game **Mod Menu** para você explorar seus mods com ícones oficiais extraídos, pesquisa em tempo real (`Ctrl+K`), dependências clicáveis e alternância entre Ativos, Desativados, Resource Packs e Wishlist.')
    md_lines.append('> 🔗 **Para abrir:** Basta dar dois cliques em [mod_menu.html](file:///home/n31415/Games/Minecraft/Ultimate%20Mods/mod_menu.html) no seu navegador!\n')
    
    md_lines.append('## 📊 Resumo da Pasta Organizada\n')
    md_lines.append('| Localização / Status | Quantidade | Descrição |')
    md_lines.append('| :--- | :---: | :--- |')
    md_lines.append(f'| 🟢 **ATIVOS NA RAIZ** (`.`) | **{active_count}** | Mods prontos para copiar/usar no Minecraft |')
    md_lines.append(f'| 🔴 **DESATIVADOS** (`desativados/`) | **{disabled_count}** | Mods isolados (EMI, Chest Tracker, Tabs, Chunky, etc.) |')
    md_lines.append(f'| 🎨 **RESOURCE PACKS** (`resourcepacks/`) | **{len(rps)-1}** | Pacotes visuais e de áudio em formato `.zip` |')
    md_lines.append(f'| **Total Geral** | **{len(mods)}** | **Arquivos JAR únicos catalogados** |\n')
    md_lines.append('---\n')
    
    md_lines.append('## 📑 Índice por Categorias\n')
    for cat in categories:
        count = sum(1 for m in mods if m['category'] == cat)
        slug = cat.lower().replace(' ', '-').replace('&', '').replace('(', '').replace(')', '').replace('⚡', '').replace('⚙️', '').replace('🎒', '').replace('🗺️', '').replace('⚔️', '').replace('💡', '').replace('🖥️', '').replace('🎨', '').replace('📚', '').strip('-')
        md_lines.append(f'- [{cat} ({count} mods)](#{slug})')
    md_lines.append('- [🎨 Resource Packs & Pacotes Visuais](#resource-packs--pacotes-visuais)')
    md_lines.append('- [📌 Mods e Datapacks em Análise / Lista de Desejos](#mods-e-datapacks-em-análise--lista-de-desejos)')
    md_lines.append('\n---\n')

    for cat in categories:
        cat_mods = [m for m in mods if m['category'] == cat]
        md_lines.append(f'## {cat}\n')
        md_lines.append('| Status | Mod / Nome | Arquivo JAR | Lado | Tipo | Dependências | Usado Por (Dependentes) | Descrição & Links |')
        md_lines.append('| :---: | :--- | :--- | :---: | :---: | :--- | :--- | :--- |')
        for m in cat_mods:
            badge = '🟢 Ativo' if m['status'] == 'ATIVADO' else '🔴 Desativado'
            name_md = f"**[{m['name']}]({m['url']})**" if m['url'] else f"**{m['name']}**"
            file_md = f"`{m['file']}`"
            side_md = m['side']
            type_md = m['type']
            deps_str = ', '.join(m['resolved_deps']) if m['resolved_deps'] else '---'
            dependents_str = ', '.join(m['dependents']) if m['dependents'] else '---'
            desc_parts = []
            if m.get('desc') and m['desc'] != '---':
                desc_parts.append(m['desc'])
            if m.get('user_comment'):
                desc_parts.append(f"⚠️ *Nota: {m['user_comment']}*")
            desc_md = '<br>'.join(desc_parts) if desc_parts else '---'
            md_lines.append(f'| {badge} | {name_md} | {file_md} | {side_md} | {type_md} | {deps_str} | {dependents_str} | {desc_md} |')
        md_lines.append('\n---\n')

    text = '\n'.join(md_lines)
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(text)
    print("✅ MODS_CATALOG.md atualizado!")
    
    # Also sync artifact if dir exists
    artifact_path = '/home/n31415/.gemini/antigravity-cli/brain/eadfbbc5-c6da-4701-94e5-5fef22bcbeb7/MODS_CATALOG.md'
    if os.path.exists(os.path.dirname(artifact_path)):
        with open(artifact_path, 'w', encoding='utf-8') as f:
            f.write(text)

    print("\n🎉 Atualização concluída com sucesso! Todos os novos mods e ícones foram sincronizados.")

if __name__ == '__main__':
    update_all()
