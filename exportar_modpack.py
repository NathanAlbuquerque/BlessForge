#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assistente Interativo de Exportação de Modpacks — Minecraft 1.21.1 (NeoForge).
Seleciona mods, resolve dependências automaticamente e empacota em .ZIP ou pasta pronta.
"""

import os, sys, time
from exportador import resolve_modpack_selection, export_modpack, EXPORT_DIR
from atualizar_catalogo import scan_all

PRESETS = {
    "1": {
        "title": "Todos os Mods Ativos (Completo)",
        "desc": "Empacota todos os 74 mods atualmente ativos na raiz",
        "filter": lambda m: m['status'] == 'ATIVADO'
    },
    "2": {
        "title": "Client-Side Only (Para Jogar em Servidores Multiplayer)",
        "desc": "Apenas mods visuais, HUD, áudio e otimização permitidos ao entrar em servidores de terceiros",
        "filter": lambda m: m['side'] == 'Client' and m['status'] == 'ATIVADO'
    },
    "3": {
        "title": "Vanilla+ & Otimização Essencial",
        "desc": "Performance extrema (Sodium, ModernFix, FerriteCore) + QoL básico (JEI, Waystones, Jade, BetterF3)",
        "filter": lambda m: m['category'] in ('⚡ Otimização & Performance', '🖥️ Interface (UI/HUD) & Controles') or m['file'] in ('waystones-neoforge-1.21.1-21.1.46.jar', 'jei-1.21.1-neoforge-19.57.0.450.jar', 'carryon-neoforge-1.21.1-2.2.6.13.jar')
    },
    "4": {
        "title": "Create & Tecnologia / Automação",
        "desc": "Create + Create: Gunsmithing + todas as armas e dependências de renderização",
        "filter": lambda m: 'create' in m['file'].lower() or 'gun' in m['file'].lower()
    },
    "5": {
        "title": "Aventura, RPG & Dimensões Épicas",
        "desc": "L_Ender's Cataclysm, Twilight Forest, Simply Swords, Dungeons Arise, Armor of the Ages",
        "filter": lambda m: m['category'] in ('🗺️ Aventura, Dimensões & Estruturas', '⚔️ Combate, Armas & Equipamentos')
    },
    "6": {
        "title": "Armazenamento & Logística",
        "desc": "Sophisticated Backpacks, Tom's Simple Storage, InventoryTweak, Bartering Station",
        "filter": lambda m: m['category'] == '🎒 Armazenamento & Inventário' or 'storage' in m['file'].lower()
    }
}

def main():
    print("\n" + "=" * 65)
    print("📦 BLESSFORGE — GERADOR E EXPORTADOR DE MODPACKS (1.21.1 NEOFORGE)")
    print("=" * 65)
    
    mods, rps, _ = scan_all()
    active_mods = [m for m in mods if m['status'] == 'ATIVADO']
    print(f"Modoteca carregada: {len(active_mods)} mods ativos disponíveis.")
    print("\nEscolha como deseja selecionar os mods:")
    print("  [1-6] Escolher um Preset Recomendado:")
    for key, p in PRESETS.items():
        print(f"        {key}. {p['title']}")
        print(f"           ↳ {p['desc']}")
    print("  [7]   Seleção Manual (escolher mods um a um)")
    print("  [0]   Sair")
    
    choice = input("\nDigite a opção desejada: ").strip()
    if choice == "0":
        print("Operação cancelada.")
        return
        
    selected_files = []
    preset_name = "MeuModpack"
    
    if choice in PRESETS:
        p = PRESETS[choice]
        preset_name = p['title'].split('(')[0].strip().replace(' ', '-').replace('&', 'e')
        selected_files = [m['file'] for m in mods if p['filter'](m)]
        print(f"\n✅ Preset '{p['title']}' selecionado ({len(selected_files)} mods iniciais).")
        
    elif choice == "7":
        preset_name = input("Nome do seu modpack (ex: BlessForge-Amigos): ").strip() or "BlessForge-Custom"
        print("\nLista de mods disponíveis:")
        for idx, m in enumerate(active_mods):
            print(f"  [{idx+1:2d}] {m['name']} ({m['file']}) - {m['category']}")
            
        print("\nDigite os números dos mods desejados separados por espaço ou vírgula (ex: 1, 4, 12):")
        raw_picks = input("Números: ").strip()
        picks = [int(p.strip()) for p in raw_picks.replace(',', ' ').split() if p.strip().isdigit()]
        for p in picks:
            if 1 <= p <= len(active_mods):
                selected_files.append(active_mods[p-1]['file'])
        print(f"\n✅ {len(selected_files)} mods selecionados manualmente.")
    else:
        print("Opção inválida.")
        return
        
    if not selected_files:
        print("Nenhum mod selecionado. Abortando.")
        return
        
    # Resolution
    print("\n🔍 Analisando árvore de dependências...")
    res = resolve_modpack_selection(selected_files, mods)
    auto_count = len(res['auto_dependencies'])
    print(f"📊 Resultado da Resolução:")
    print(f"   • Mods selecionados diretamente: {len(res['selected_files'])}")
    print(f"   • Dependências automáticas incluídas: {auto_count}")
    if auto_count > 0:
        for dep_file in res['auto_dependencies']:
            reasons = res['dep_reasons'].get(dep_file, [])
            reason_str = f" (exigido por: {', '.join(reasons)})" if reasons else ""
            print(f"     ➕ {dep_file}{reason_str}")
    print(f"   • Total final: {len(res['total_files'])} mods no pacote.")
    
    # Resource packs option
    selected_rps = []
    rp_zips = [f for f in os.listdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "resourcepacks")) if f.endswith('.zip')]
    if rp_zips:
        print("\nDeseja incluir pacotes de texturas/som (Resource Packs)?")
        print("  [1] Sim, incluir todos")
        print("  [2] Não, apenas os mods")
        rp_choice = input("Opção [1/2, padrão 2]: ").strip()
        if rp_choice == "1":
            selected_rps = rp_zips
            print(f"✅ {len(selected_rps)} Resource Packs incluídos.")
            
    # Format option
    print("\nEm qual formato deseja exportar?")
    print("  [1] Arquivo .ZIP comprimido (Ideal para enviar no Discord/Drive para amigos)")
    print("  [2] Pasta Pronta no disco (Ideal para copiar direto para .minecraft/mods)")
    fmt_choice = input("Opção [1/2, padrão 1]: ").strip()
    export_fmt = "folder" if fmt_choice == "2" else "zip"
    
    print("\n⚙️ Empacotando modpack...")
    result = export_modpack(preset_name, selected_files, include_deps=True, selected_rps=selected_rps, export_format=export_fmt)
    
    print("\n" + "=" * 65)
    print("🎉 MODPACK EXPORTADO COM SUCESSO!")
    print("=" * 65)
    if export_fmt == "zip":
        print(f"📦 Arquivo ZIP: {result['path']}")
        print(f"📊 Tamanho: {result['size']} | Mods: {result['mod_count']} | Resource Packs: {result['rp_count']}")
        print(f"👉 Envie este arquivo .zip para seus amigos. Ele já inclui o 'LEIA-ME_INSTALACAO.txt' com instruções!")
    else:
        print(f"📁 Pasta gerada: {result['path']}")
        print(f"👉 Copie o conteúdo de '{result['path']}/mods/' direto para a sua pasta .minecraft/mods/")
    print("=" * 65 + "\n")

if __name__ == '__main__':
    main()
