#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assistente Interativo de Exportação de Modpacks — Minecraft 1.21.1 (NeoForge).
Seleciona mods, resolve dependências automaticamente e empacota em .ZIP ou pasta pronta.
"""

import os, sys, time

TOOLS_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, TOOLS_DIR)

from exportador import resolve_modpack_selection, export_modpack, EXPORT_DIR
from atualizar_catalogo import scan_all

PRESETS = {
    "1": {
        "title": "Todos os Mods Ativos (Completo)",
        "desc": "Empacota todos os mods atualmente ativos na pasta mods/",
        "filter": lambda m: m['status'] == 'ATIVADO'
    },
    "2": {
        "title": "Client-Side Only (Para Jogar em Servidores Multiplayer)",
        "desc": "Apenas mods visuais, HUD, áudio e otimização permitidos ao entrar em servidores de terceiros",
        "filter": lambda m: m['side'] == 'Client' and m['status'] == 'ATIVADO'
    },
    "3": {
        "title": "Vanilla+ & Otimização Essencial",
        "desc": "Performance extrema (Sodium, ModernFix, FerriteCore, EntityCulling) + QoL básico (JEI, Waystones, Jade, BetterF3)",
        "filter": lambda m: m['category'] in ('⚡ Otimização & Performance', '🖥️ Interface (UI/HUD) & Controles') or m['file'] in ('waystones-neoforge-1.21.1-21.1.46.jar', 'jei-1.21.1-neoforge-19.57.0.450.jar', 'carryon-neoforge-1.21.1-2.2.6.13.jar')
    },
    "4": {
        "title": "Create & Tecnologia / Automação",
        "desc": "Create + Create: Gunsmithing + todas as armas e dependências de renderização",
        "filter": lambda m: 'create' in m['file'].lower() or 'gun' in m['file'].lower()
    },
    "5": {
        "title": "Aventura, RPG & Dimensões Épicas",
        "desc": "Cataclysm, Twilight Forest, Simply Swords, Dungeons Arise, Armor of the Ages, Bumblezone, Explorify",
        "filter": lambda m: m['category'] in ('🗺️ Aventura, Dimensões & Estruturas', '⚔️ Combate, Armas & Equipamentos')
    },
    "6": {
        "title": "Armazenamento & Logística",
        "desc": "Sophisticated Backpacks, Tom's Simple Storage, InventoryTweak, Bartering Station",
        "filter": lambda m: m['category'] == '🎒 Armazenamento & Inventário'
    }
}

def main():
    print("=" * 70)
    print("   🎮 BLESSFORGE — Assistente de Exportação de Modpacks")
    print("=" * 70)
    print("Escaneando mods disponíveis...")
    mods, rps, _ = scan_all()
    active_mods = [m for m in mods if m['status'] == 'ATIVADO']
    print(f"Total de {len(active_mods)} mods ativos encontrados.")
    print("-" * 70)
    print("Escolha um preset de exportação ou monte o seu:")
    for key, data in sorted(PRESETS.items()):
        print(f" [{key}] {data['title']}")
        print(f"     └─ {data['desc']}")
    print(" [0] Personalizado (Escolher manualmente)")
    print("=" * 70)

    choice = input("\nDigite o número da opção desejada [1]: ").strip() or "1"
    
    selected_files = []
    custom_name = "BlessForge-Custom"
    
    if choice in PRESETS:
        preset = PRESETS[choice]
        custom_name = f"BlessForge-{preset['title'].split()[0]}"
        selected_files = [m['file'] for m in mods if preset['filter'](m)]
    else:
        print("\nLista de Mods Ativos:")
        for idx, m in enumerate(active_mods, 1):
            print(f" {idx:2d}. {m['name']} ({m['file']})")
        raw = input("\nDigite os números dos mods separados por vírgula (ex: 1, 3, 5): ")
        indices = [int(i.strip()) for i in raw.split(',') if i.strip().isdigit()]
        selected_files = [active_mods[i-1]['file'] for i in indices if 1 <= i <= len(active_mods)]
        custom_name = "BlessForge-Custom"

    print(f"\n🔍 Resolvendo dependências automaticamente para {len(selected_files)} mods selecionados...")
    final_mods = resolve_modpack_selection(selected_files, mods)
    print(f"✅ Total após resolução de dependências: {len(final_mods)} mods.")

    fmt_choice = input("\nFormato de Exportação: [1] Arquivo .ZIP  |  [2] Pasta Pronta [1]: ").strip() or "1"
    out_format = "zip" if fmt_choice == "1" else "folder"
    
    rp_choice = input("Incluir Resource Packs no pacote? (s/N): ").strip().lower()
    inc_rp = rp_choice in ('s', 'sim', 'y', 'yes')

    print(f"\n📦 Gerando {out_format.upper()}...")
    out_path = export_modpack(final_mods, output_format=out_format, custom_name=custom_name, include_resourcepacks=inc_rp)
    
    print("\n" + "=" * 70)
    print("🎉 EXPORTAÇÃO CONCLUÍDA COM SUCESSO!")
    print(f"📁 Local: {out_path}")
    print("=" * 70)

if __name__ == '__main__':
    main()
