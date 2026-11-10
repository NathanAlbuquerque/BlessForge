#!/usr/bin/env python3
import re
import os

coords = {
    # Main Spine (Eixo horizontal Y = 0.0)
    "1001000000000010": (-11.0, 0.0),   # Madeira
    "1001000000000020": (-8.5, 0.0),    # Crafting Table
    "1001000000000030": (-6.0, 0.0),    # Fornalha
    "1001000000000040": (-6.0, 2.5),    # Mudas
    "1001000000000310": (-3.0, 0.0),    # Ferro
    "1001000000000320": (0.0, 0.0),     # Escudo
    "1001000000000330": (0.0, 2.5),     # Cobre
    "1001000000000340": (3.0, 0.0),     # Diamante
    "1001000000000610": (12.0, 0.0),    # Upgrader
    "1001000000000620": (14.5, 0.0),    # Pioneiro Consagrado

    # Ramo Arquitetura (Y negativo, esquerda)
    "1001000000000110": (-6.0, -3.0),   # Cobblestone
    "1001000000000120": (-3.5, -4.5),   # Stonecutter
    "1001000000000130": (-3.5, -2.5),   # Cama
    "1001000000000140": (-1.5, -3.5),   # Lanterna

    # Ramo Sustento & Felino (Y positivo, esquerda)
    "1001000000000210": (-8.5, 3.5),    # Trigo
    "1001000000000220": (-8.5, 6.0),    # Pomar
    "1001000000000230": (-6.0, 5.0),    # Pecuária
    "1001000000000240": (-3.5, 5.0),    # Gato

    # Ramo Inventário Inteligente (Y positivo, centro-direita)
    "1001000000000410": (3.0, 3.5),     # Mochila
    "1001000000000420": (5.5, 4.5),     # Auto-coleta
    "1001000000000430": (5.5, 2.5),     # Mochila Ferro
    "1001000000000440": (8.5, 3.5),     # Tom Storage

    # Ramo Mobilidade Sem Tédio (Y positivo, inferior-direita)
    "1001000000000510": (3.0, 7.0),     # Tirolesa
    "1001000000000520": (5.5, 7.0),     # Nature Compass
    "1001000000000530": (5.5, 9.5),     # Waystone
    "1001000000000540": (8.5, 8.5),     # Bound Scroll

    # Trilha Perigo Médio (Y negativo, centro-topo)
    "1001000000000710": (1.0, -2.5),    # Esqueletos
    "1001000000000720": (-1.0, -5.5),   # Creepers
    "1001000000000730": (1.5, -5.0),    # Aranhas
    "1001000000000740": (1.0, -7.5),    # Bruxa
    "1001000000000750": (3.5, -2.5),    # Prata
    "1001000000000760": (6.0, -2.5),    # Claymore
    "1001000000000770": (3.8, -4.8),    # Afogados
    "1001000000000780": (6.0, -4.8),    # Patrulha
    "1001000000000790": (-1.0, -8.0),   # Spawner
    "1001000000000800": (8.5, -2.5),    # Armadura Completa

    # Trilha Difícil
    "1001000000000810": (6.0, -7.2),    # Posto Avançado
    "1001000000000820": (6.0, -9.5),    # Raid
    "1001000000000830": (8.5, -4.8),    # Tábua Rúnica
    "1001000000000840": (11.0, -4.8),   # Trial Chamber
    "1001000000000850": (11.0, -7.2),   # Breeze

    # Trilha Extrema
    "1001000000000860": (8.5, -9.5),    # Ominous Mace
    "1001000000000870": (13.5, -7.2),   # Warden
}

def update_chapter(filepath):
    print("Atualizando coordenadas em:", filepath)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Split quests by top-level quest objects
    # Note: quest objects are indented with \t\t{ inside quests: [ ... ]
    # We can search for each quest id and update its x and y lines
    for qid, (new_x, new_y) in coords.items():
        # Match quest block starting from id: "qid" until the next x and y
        # We can locate id: "qid" and replace x: ...d and y: ...d within that quest block
        pattern = re.compile(
            r'(id:\s*\"' + qid + r'\"[\s\S]*?)(x:\s*[-\d\.]+d\s*\n\s*y:\s*[-\d\.]+d)',
            re.MULTILINE
        )
        def repl(match):
            prefix = match.group(1)
            # Find indentation of x line
            indent = "\t\t\t"
            return f"{prefix}x: {new_x}d\n{indent}y: {new_y}d"

        content, count = pattern.subn(repl, content, count=1)
        if count == 0:
            print(f"AVISO: Quest {qid} não encontrada pelo padrão!")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print("Concluído com sucesso:", filepath)

target1 = "/home/n31415/Games/Minecraft/Ultimate Mods/config/ftbquests/quests/chapters/capitulo_1_pioneiro.snbt"
target2 = "/home/n31415/Minecraft/config/ftbquests/quests/chapters/capitulo_1_pioneiro.snbt"

update_chapter(target1)
update_chapter(target2)
