#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Geracao e Expansao dos Capitulos 3, 4, 5 e 6 do FTB Quests.
Inclui o tier [Dificuldade: Facil] em cada capitulo para ritmo saudavel de Mundo Eterno,
garantindo distancia minima >= 2.50d entre todos os nos e zero caracteres nao-escapados.
"""

import os
import math
import re

DEST_DIRS = [
    "config/ftbquests/quests/chapters",
    "/home/n31415/Minecraft/config/ftbquests/quests/chapters"
]

def format_snbt(chapter_data):
    lines = ["{"]
    lines.append('\tdefault_hide_dependency_lines: false')
    lines.append(f'\tdefault_quest_shape: "{chapter_data.get("default_quest_shape", "circle")}"')
    lines.append(f'\tfilename: "{chapter_data["filename"]}"')
    lines.append(f'\tgroup: "{chapter_data["group"]}"')
    lines.append('\ticon: {')
    lines.append(f'\t\tid: "{chapter_data["icon"]}"')
    lines.append('\t}')
    lines.append(f'\tid: "{chapter_data["id"]}"')
    lines.append(f'\torder_index: {chapter_data["order_index"]}')
    lines.append(f'\ttitle: "{chapter_data["title"]}"')
    lines.append('\tquests: [')

    for q in chapter_data["quests"]:
        lines.append('\t\t{')
        if "dependencies" in q and q["dependencies"]:
            deps = ', '.join([f'"{d}"' for d in q["dependencies"]])
            lines.append(f'\t\t\tdependencies: [{deps}]')
        
        lines.append('\t\t\tdescription: [')
        for d in q["description"]:
            clean_d = d.replace('"', '\\"')
            if '&' in clean_d:
                raise ValueError(f"ERRO: caractere & proibido na desc da quest {q['id']}: {clean_d}")
            lines.append(f'\t\t\t\t"{clean_d}"')
        lines.append('\t\t\t]')
        
        lines.append('\t\t\ticon: {')
        lines.append(f'\t\t\t\tid: "{q["icon"]}"')
        lines.append('\t\t\t}')
        lines.append(f'\t\t\tid: "{q["id"]}"')
        lines.append(f'\t\t\tshape: "{q.get("shape", "circle")}"')
        lines.append(f'\t\t\tsize: {q.get("size", 1.2):.1f}d')
        
        sub = q.get("subtitle", "")
        if '&' in sub:
            raise ValueError(f"ERRO: caractere & proibido no subtitle da quest {q['id']}")
        lines.append(f'\t\t\tsubtitle: "{sub}"')
        
        # Tasks
        lines.append('\t\t\ttasks: [')
        for t in q["tasks"]:
            lines.append('\t\t\t\t{')
            if t.get("count", 1) > 1:
                lines.append(f'\t\t\t\t\tcount: {t["count"]}L')
            lines.append(f'\t\t\t\t\tid: "{t["id"]}"')
            if t["type"] == "item":
                lines.append('\t\t\t\t\titem: {')
                lines.append('\t\t\t\t\t\tcount: 1')
                lines.append(f'\t\t\t\t\t\tid: "{t["item"]}"')
                lines.append('\t\t\t\t\t}')
            elif t["type"] == "checkmark":
                pass
            lines.append(f'\t\t\t\t\ttitle: "{t.get("title", "")}"')
            lines.append(f'\t\t\t\t\ttype: "{t["type"]}"')
            lines.append('\t\t\t\t}')
        lines.append('\t\t\t]')
        
        # Rewards
        lines.append('\t\t\trewards: [')
        for r in q.get("rewards", []):
            lines.append('\t\t\t\t{')
            if r.get("count", 1) > 1:
                lines.append(f'\t\t\t\t\tcount: {r["count"]}')
            lines.append(f'\t\t\t\t\tid: "{r["id"]}"')
            if r["type"] == "item":
                lines.append('\t\t\t\t\titem: {')
                lines.append('\t\t\t\t\t\tcount: 1')
                lines.append(f'\t\t\t\t\t\tid: "{r["item"]}"')
                lines.append('\t\t\t\t\t}')
            elif r["type"] == "xp_levels":
                lines.append(f'\t\t\t\t\txp_levels: {r.get("xp_levels", 1)}')
            elif r["type"] == "xp":
                lines.append(f'\t\t\t\t\txp: {r.get("xp", 100)}')
            lines.append(f'\t\t\t\t\ttype: "{r["type"]}"')
            lines.append('\t\t\t\t}')
        lines.append('\t\t\t]')
        
        tit = q.get("title", "")
        if '&' in tit:
            raise ValueError(f"ERRO: caractere & proibido no title da quest {q['id']}")
        lines.append(f'\t\t\ttitle: "{tit}"')
        lines.append(f'\t\t\tx: {q["x"]:.1f}d')
        lines.append(f'\t\t\ty: {q["y"]:.1f}d')
        lines.append('\t\t}')
    lines.append('\t]')
    lines.append('}')
    return '\n'.join(lines) + '\n'

def validate_layout(chapter_data):
    quests = chapter_data["quests"]
    min_dist = 999.0
    violators = []
    for i in range(len(quests)):
        for j in range(i + 1, len(quests)):
            q1 = quests[i]
            q2 = quests[j]
            dx = q1["x"] - q2["x"]
            dy = q1["y"] - q2["y"]
            dist = math.hypot(dx, dy)
            if dist < min_dist:
                min_dist = dist
            if dist < 2.49:
                violators.append((q1["title"], q2["title"], dist))
    
    print(f"Capitulo {chapter_data['filename']}: {len(quests)} quests. Menor distancia: {min_dist:.2f}d")
    if violators:
        for v in violators:
            print(f"  [AVISO COLISAO] '{v[0]}' e '{v[1]}' dist: {v[2]:.2f}d")
        raise ValueError(f"Distancia minima menor que 2.50 em {chapter_data['filename']}")

# =====================================================================
# CAPÍTULO 3: TWILIGHT FOREST (32 QUESTS)
# =====================================================================
def get_twilight_data():
    return {
        "filename": "capitulo_3_twilight",
        "group": "1A2B3C4D5E6F7001",
        "id": "1003000000000001",
        "order_index": 3,
        "title": "3. Alem do Dossel (Twilight Forest)",
        "icon": "twilightforest:naga_trophy",
        "quests": [
            # TIER FACIL (8 Quests, y = -3.0d)
            {
                "id": "1003000000000010",
                "title": "Rumo ao Crepusculo Eterno",
                "subtitle": "[Dificuldade: Facil] O ritual sagrado do diamante e das flores",
                "description": [
                    "Para abrir o portal para a dimensao do crepusculo eterno, cave um buraco 2x2 na grama, preencha com agua, cerque as bordas de flores coloridas e atire um diamante la dentro.",
                    "Um raio mistico caira do ceu transformando a agua em um portal violeta encantado!"
                ],
                "icon": "minecraft:diamond",
                "shape": "hexagon",
                "size": 1.5,
                "x": -9.8, "y": -3.0,
                "tasks": [{"id": "1003000000000011", "type": "checkmark", "title": "Abra o Portal do Crepusculo"}],
                "rewards": [
                    {"id": "1003000000000012", "type": "item", "item": "twilightforest:firefly_jar"},
                    {"id": "1003000000000013", "type": "xp_levels", "xp_levels": 3}
                ]
            },
            {
                "id": "1003000000000020",
                "dependencies": ["1003000000000010"],
                "title": "Luzes no Dossel",
                "subtitle": "[Dificuldade: Facil] Capturando vaga-lumes na floresta encantada",
                "description": [
                    "Ao pisar na Twilight Forest, a penumbra e o silencio sao acolhedores. Vaga-lumes luminosos flutuam nos troncos das arvores gigantescas.",
                    "Colete ou prenda um vaga-lume para criar iluminacao organica e comecar a decorar seu primeiro refugio."
                ],
                "icon": "twilightforest:firefly",
                "x": -7.0, "y": -3.0,
                "tasks": [{"id": "1003000000000021", "type": "item", "item": "twilightforest:firefly", "title": "Colete um Vaga-lume"}],
                "rewards": [
                    {"id": "1003000000000022", "type": "item", "item": "twilightforest:firefly_jar", "count": 2},
                    {"id": "1003000000000023", "type": "xp", "xp": 100}
                ]
            },
            {
                "id": "1003000000000030",
                "dependencies": ["1003000000000020"],
                "title": "Mudas Gigantes da Floresta",
                "subtitle": "[Dificuldade: Facil] A silvicultura das arvores colossais",
                "description": [
                    "As arvores de carvalho crepuscular (Twilight Oak) e de dossel (Canopy Tree) fornecem madeiras densas com copas imensas.",
                    "Colete mudas nativas para iniciar seu reflorestamento sustentavel perto do portal."
                ],
                "icon": "twilightforest:twilight_oak_sapling",
                "x": -4.2, "y": -3.0,
                "tasks": [{"id": "1003000000000031", "type": "item", "item": "twilightforest:twilight_oak_sapling", "title": "Obtenha uma Muda de Carvalho Crepuscular"}],
                "rewards": [
                    {"id": "1003000000000032", "type": "item", "item": "twilightforest:canopy_sapling", "count": 2},
                    {"id": "1003000000000033", "type": "xp", "xp": 100}
                ]
            },
            {
                "id": "1003000000000040",
                "dependencies": ["1003000000000030"],
                "title": "Cogumelos do Chao Mistico",
                "subtitle": "[Dificuldade: Facil] A bioluminescencia dos Mushglooms",
                "description": [
                    "Pelo solo umido da floresta brotam cogumelos azuis cintilantes chamados Mushglooms.",
                    "Eles emitem uma luz suave e sao excelentes ingredientes para preparos culinarios e tinturas naturais."
                ],
                "icon": "twilightforest:mushgloom",
                "x": -1.4, "y": -3.0,
                "tasks": [{"id": "1003000000000041", "type": "item", "item": "twilightforest:mushgloom", "count": 4, "title": "Colha Mushglooms"}],
                "rewards": [
                    {"id": "1003000000000042", "type": "item", "item": "minecraft:mushroom_stew", "count": 2},
                    {"id": "1003000000000043", "type": "xp", "xp": 150}
                ]
            },
            {
                "id": "1003000000000050",
                "dependencies": ["1003000000000040"],
                "title": "Penas de Corvo da Floresta",
                "subtitle": "[Dificuldade: Facil] Coleta pacifica com as aves nativas",
                "description": [
                    "Corvos negros e silenciosos empoleiram-se nos galhos baixos. Ao contrario dos monstros do submundo, a fauna do crepusculo e pacifica e graciosa.",
                    "Encontre penas caidas ou interaja com corvos para obter a materia-prima essencial dos mapas magicos."
                ],
                "icon": "twilightforest:raven_feather",
                "x": 1.4, "y": -3.0,
                "tasks": [{"id": "1003000000000051", "type": "item", "item": "twilightforest:raven_feather", "count": 2, "title": "Colete Penas de Corvo"}],
                "rewards": [
                    {"id": "1003000000000052", "type": "item", "item": "minecraft:paper", "count": 8},
                    {"id": "1003000000000053", "type": "xp", "xp": 150}
                ]
            },
            {
                "id": "1003000000000060",
                "dependencies": ["1003000000000050"],
                "title": "Bagas Reluzentes das Cavernas",
                "subtitle": "[Dificuldade: Facil] Colheita de Torchberries sob as colinas",
                "description": [
                    "Penduradas nas raizes subterraneas das colinas ocas crescem bagas incandescentes conhecidas como Torchberries.",
                    "Elas servem tanto para alimentar viajantes quanto para sintetizar tintas arcanas que reagem com energia magica."
                ],
                "icon": "twilightforest:torchberries",
                "x": 4.2, "y": -3.0,
                "tasks": [{"id": "1003000000000061", "type": "item", "item": "twilightforest:torchberries", "count": 6, "title": "Colha Torchberries"}],
                "rewards": [
                    {"id": "1003000000000062", "type": "item", "item": "minecraft:glow_berries", "count": 8},
                    {"id": "1003000000000063", "type": "xp", "xp": 150}
                ]
            },
            {
                "id": "1003000000000070",
                "dependencies": ["1003000000000060"],
                "title": "Raizes Vivas da Terra",
                "subtitle": "[Dificuldade: Facil] Extracao de Live Root nas colinas ocas",
                "description": [
                    "Abaixo do solo fertil, blocos de raiz verde pulsam com seiva mineral. Ao quebrar essas raizes, recolha Liveroots.",
                    "Essa raiz viva pode ser ralada e combinada com metais para criar uma liga magica incomparavel."
                ],
                "icon": "twilightforest:liveroot",
                "x": 7.0, "y": -3.0,
                "tasks": [{"id": "1003000000000071", "type": "item", "item": "twilightforest:liveroot", "count": 4, "title": "Extraia Raizes Vivas (Liveroot)"}],
                "rewards": [
                    {"id": "1003000000000072", "type": "item", "item": "minecraft:iron_ingot", "count": 4},
                    {"id": "1003000000000073", "type": "item", "item": "minecraft:gold_nugget", "count": 16}
                ]
            },
            {
                "id": "1003000000000080",
                "dependencies": ["1003000000000070"],
                "title": "O Talisma de Protecao",
                "subtitle": "[Dificuldade: Facil] O primeiro folego do aventureiro cauteloso",
                "description": [
                    "A floresta recompensa a exploracao paciente. Em baus nas colinas ocas e pequenas ruinas repousam Talismas da Vida (Charm of Life).",
                    "Carregar um talisma no inventario impede um golpe fatal, restaurando sua vida em momentos criticos!"
                ],
                "icon": "twilightforest:charm_of_life_1",
                "x": 9.8, "y": -3.0,
                "tasks": [{"id": "1003000000000081", "type": "item", "item": "twilightforest:charm_of_life_1", "title": "Encontre um Talisma da Vida I"}],
                "rewards": [
                    {"id": "1003000000000082", "type": "item", "item": "minecraft:golden_apple", "count": 2},
                    {"id": "1003000000000083", "type": "xp_levels", "xp_levels": 3}
                ]
            },

            # TIER MEDIA (9 Quests, y = 0.5d)
            {
                "id": "1003000000000090",
                "dependencies": ["1003000000000070"],
                "title": "A Forja da Madeira de Ferro",
                "subtitle": "[Dificuldade: Media] Criando a liga organico-metalica Ironwood",
                "description": [
                    "Combinando raiz viva ralada, ferro e pepitas de ouro numa bancada de trabalho, voce forja lingotes de Ironwood brutos que ja saem da fornalha naturalmente encantados!",
                    "Equipamentos de Ironwood sao a porta de entrada perfeita para o combate estruturado na floresta."
                ],
                "icon": "twilightforest:ironwood_ingot",
                "x": -11.2, "y": 0.5,
                "tasks": [{"id": "1003000000000091", "type": "item", "item": "twilightforest:ironwood_ingot", "count": 4, "title": "Forje Lingotes de Ironwood"}],
                "rewards": [
                    {"id": "1003000000000092", "type": "item", "item": "twilightforest:ironwood_ingot", "count": 4},
                    {"id": "1003000000000093", "type": "xp_levels", "xp_levels": 4}
                ]
            },
            {
                "id": "1003000000000100",
                "dependencies": ["1003000000000050", "1003000000000060"],
                "title": "Cartografia Crepuscular",
                "subtitle": "[Dificuldade: Media] O Mapa Magico que dissipa o nevoeiro",
                "description": [
                    "O Mapa Magico revela a posicao exata das masmorras e lordes protegidos por barreiras arcanas.",
                    "Combine penas de corvo, bagas luminosas e papel para orientar sua rota sem desvios frustrantes."
                ],
                "icon": "twilightforest:magic_map",
                "x": -8.4, "y": 0.5,
                "tasks": [{"id": "1003000000000101", "type": "item", "item": "twilightforest:magic_map", "title": "Crie um Mapa Magico do Crepusculo"}],
                "rewards": [
                    {"id": "1003000000000102", "type": "item", "item": "twilightforest:torchberries", "count": 8},
                    {"id": "1003000000000103", "type": "xp_levels", "xp_levels": 5}
                ]
            },
            {
                "id": "1003000000000110",
                "dependencies": ["1003000000000100"],
                "title": "Magnetismo e Transmutacao",
                "subtitle": "[Dificuldade: Media] Ferramentas alquimicas de prospeccao geologica",
                "description": [
                    "O Po de Transformacao transmuta criaturas da floresta em animais do mundo comum e vice-versa.",
                    "O Íma de Minerios atrai veios inteiros soterrados na rocha diretamente para a superficie, poupando horas de picaretagem no escuro!"
                ],
                "icon": "twilightforest:ore_magnet",
                "x": -5.6, "y": 0.5,
                "tasks": [
                    {"id": "1003000000000111", "type": "item", "item": "twilightforest:ore_magnet", "title": "Obtenha um Íma de Minerios"},
                    {"id": "1003000000000112", "type": "item", "item": "twilightforest:transformation_powder", "count": 8, "title": "Colete Po de Transformacao"}
                ],
                "rewards": [
                    {"id": "1003000000000113", "type": "item", "item": "twilightforest:transformation_powder", "count": 16},
                    {"id": "1003000000000114", "type": "xp_levels", "xp_levels": 6}
                ]
            },
            {
                "id": "1003000000000120",
                "dependencies": ["1003000000000100"],
                "title": "O Colosso do Labirinto: Naga",
                "subtitle": "[Dificuldade: Media] A serpente blindada do jardim de sebes",
                "description": [
                    "A Naga desliza veloz pelo labirinto de sebes. Seus segmentos de cauda vao se soltando conforme ela recebe dano concentrado.",
                    "Ataque a cabeca com saltos cronometrados para triunfar sem sofrer grandes impactos."
                ],
                "icon": "twilightforest:naga_trophy",
                "x": -2.8, "y": 0.5,
                "tasks": [{"id": "1003000000000121", "type": "item", "item": "twilightforest:naga_trophy", "title": "Obtenha o Trofeu da Naga"}],
                "rewards": [
                    {"id": "1003000000000122", "type": "item", "item": "twilightforest:naga_scale", "count": 8},
                    {"id": "1003000000000123", "type": "xp_levels", "xp_levels": 6}
                ]
            },
            {
                "id": "1003000000000130",
                "dependencies": ["1003000000000120"],
                "title": "Armadura de Escamas da Naga",
                "subtitle": "[Dificuldade: Media] Protecao leve e agilidade escorregadia",
                "description": [
                    "Escamas de Naga possuem propriedades repelentes unicas. Ao costura-las em peitorais e perneiras, voce adquire encantamentos nativos de Protecao e Agilidade.",
                    "Um equipamento nobre para quem prefere mobilidade rapida nos combates."
                ],
                "icon": "twilightforest:naga_chestplate",
                "x": 0.0, "y": 0.5,
                "tasks": [{"id": "1003000000000131", "type": "item", "item": "twilightforest:naga_chestplate", "title": "Forje o Peitoral de Naga"}],
                "rewards": [
                    {"id": "1003000000000132", "type": "item", "item": "minecraft:diamond", "count": 2},
                    {"id": "1003000000000133", "type": "xp_levels", "xp_levels": 5}
                ]
            },
            {
                "id": "1003000000000140",
                "dependencies": ["1003000000000120"],
                "title": "O Lich da Torre Obscura",
                "subtitle": "[Dificuldade: Media] O mestre necromante e seus escudos de eter",
                "description": [
                    "No topo da torre de tijolos musgosos reina o Lich. Seus escudos arcanos sao imunes a espadas convencionais.",
                    "Rebata os projeteis magicos do proprio feiticeiro para destruir sua barreira antes de engajar no combate corpo a corpo!"
                ],
                "icon": "twilightforest:lich_trophy",
                "x": 2.8, "y": 0.5,
                "tasks": [{"id": "1003000000000141", "type": "item", "item": "twilightforest:lich_trophy", "title": "Obtenha o Trofeu do Lich"}],
                "rewards": [
                    {"id": "1003000000000142", "type": "item", "item": "minecraft:golden_apple", "count": 3},
                    {"id": "1003000000000143", "type": "xp_levels", "xp_levels": 7}
                ]
            },
            {
                "id": "1003000000000150",
                "dependencies": ["1003000000000140"],
                "title": "Os Cetros Arcanos do Crepusculo",
                "subtitle": "[Dificuldade: Media] Dominando os artefactos magicos do Lich",
                "description": [
                    "O Lich empunhava um dos quatro lendarios cetros: Cetro do Crepusculo, Cetro de Zumbis, Cetro de Escudos ou Cetro de Drenagem.",
                    "Empunhe um desses cetros para usar feitiçaria devastadora contra hordas de monstros."
                ],
                "icon": "twilightforest:twilight_scepter",
                "x": 5.6, "y": 0.5,
                "tasks": [{"id": "1003000000000151", "type": "item", "item": "twilightforest:twilight_scepter", "title": "Conquiste um Cetro Magico"}],
                "rewards": [
                    {"id": "1003000000000152", "type": "item", "item": "minecraft:ender_pearl", "count": 4},
                    {"id": "1003000000000153", "type": "xp_levels", "xp_levels": 5}
                ]
            },
            {
                "id": "1003000000000160",
                "dependencies": ["1003000000000140"],
                "title": "O Minotauro do Labirinto",
                "subtitle": "[Dificuldade: Media] A fera furiosa do submundo de estalactites",
                "description": [
                    "Abaixo dos pantanos ergue-se o labirinto de dois andares. Em seu centro reside o Minoshroom empunhando um machado colossale de diamante.",
                    "Derrote o lorde bovino para provar sua forca e destravar os ingredientes das receitas ancestrais."
                ],
                "icon": "twilightforest:minoshroom_trophy",
                "x": 8.4, "y": 0.5,
                "tasks": [{"id": "1003000000000161", "type": "item", "item": "twilightforest:minoshroom_trophy", "title": "Obtenha o Trofeu do Minoshroom"}],
                "rewards": [
                    {"id": "1003000000000162", "type": "item", "item": "twilightforest:meef_stroganoff", "count": 2},
                    {"id": "1003000000000163", "type": "xp_levels", "xp_levels": 6}
                ]
            },
            {
                "id": "1003000000000170",
                "dependencies": ["1003000000000160"],
                "title": "O Machado do Minotauro",
                "subtitle": "[Dificuldade: Media] Dano devastador durante arrancadas ferozes",
                "description": [
                    "O Machado de Diamante do Minotauro e famoso por causar dano colossal quando empunhado enquanto corre em direcao ao adversario.",
                    "A ferramenta perfeita para abrir caminhos atraves de hordas inimigas."
                ],
                "icon": "twilightforest:diamond_minotaur_axe",
                "x": 11.2, "y": 0.5,
                "tasks": [{"id": "1003000000000171", "type": "item", "item": "twilightforest:diamond_minotaur_axe", "title": "Empunhe o Machado do Minotauro"}],
                "rewards": [
                    {"id": "1003000000000172", "type": "item", "item": "minecraft:diamond", "count": 3},
                    {"id": "1003000000000173", "type": "xp_levels", "xp_levels": 6}
                ]
            },

            # TIER DIFICIL (9 Quests, y = 4.0d)
            {
                "id": "1003000000000180",
                "dependencies": ["1003000000000150"],
                "title": "O Leque de Penas do Pavao",
                "subtitle": "[Dificuldade: Dificil] Rajadas de vento e repulsao em area",
                "description": [
                    "O Peacock Feather Fan canaliza o vento da copa das arvores para arremessar inimigos para longe com forca monumental.",
                    "Excelente para controlar grupos em beiras de abismos e torres."
                ],
                "icon": "twilightforest:peacock_feather_fan",
                "x": -11.2, "y": 4.0,
                "tasks": [{"id": "1003000000000181", "type": "item", "item": "twilightforest:peacock_feather_fan", "title": "Adquira o Peacock Feather Fan"}],
                "rewards": [
                    {"id": "1003000000000182", "type": "item", "item": "minecraft:feather", "count": 16},
                    {"id": "1003000000000183", "type": "xp_levels", "xp_levels": 5}
                ]
            },
            {
                "id": "1003000000000190",
                "dependencies": ["1003000000000160"],
                "title": "Maca e Corrente Demolidora",
                "subtitle": "[Dificuldade: Dificil] A arma de quebra-escudo das profundezas",
                "description": [
                    "A maca com corrente (Block and Chain) e uma arma pesadissima recuperada dos gigantes do submundo.",
                    "Arremesse o bloco macico para quebrar escudos de defensores e atordoar alvos blindados."
                ],
                "icon": "twilightforest:block_and_chain",
                "x": -8.4, "y": 4.0,
                "tasks": [{"id": "1003000000000191", "type": "item", "item": "twilightforest:block_and_chain", "title": "Obtenha a Maca e Corrente"}],
                "rewards": [
                    {"id": "1003000000000192", "type": "item", "item": "minecraft:iron_block", "count": 2},
                    {"id": "1003000000000193", "type": "xp_levels", "xp_levels": 6}
                ]
            },
            {
                "id": "1003000000000200",
                "dependencies": ["1003000000000160"],
                "title": "A Hidra Flamejante dos Pantanos",
                "subtitle": "[Dificuldade: Dificil] O terror de sete cabecas do pantano ardente",
                "description": [
                    "No coracao do pantano de fogo, a Hidra cospe chamas e bolas de fogo incandescentes.",
                    "Quando uma cabeca abre a boca para rugir ou disparar, mire seus projeteis exatamente no interior para causar dano critico!"
                ],
                "icon": "twilightforest:hydra_trophy",
                "x": -5.6, "y": 4.0,
                "tasks": [{"id": "1003000000000201", "type": "item", "item": "twilightforest:hydra_trophy", "title": "Obtenha o Trofeu da Hidra"}],
                "rewards": [
                    {"id": "1003000000000202", "type": "item", "item": "twilightforest:hydra_chop", "count": 5},
                    {"id": "1003000000000203", "type": "xp_levels", "xp_levels": 8}
                ]
            },
            {
                "id": "1003000000000210",
                "dependencies": ["1003000000000200"],
                "title": "Sangue Ardente da Hidra",
                "subtitle": "[Dificuldade: Dificil] O fluido incandescente para ligas termicas",
                "description": [
                    "O sangue da besta morta ferve a temperaturas vulcanicas. Ele e o ingrediente lendario para a forja dos lingotes de fogo.",
                    "Manuseie com cuidado antes de introduzir nas matrizes de ferro."
                ],
                "icon": "twilightforest:fiery_blood",
                "x": -2.8, "y": 4.0,
                "tasks": [{"id": "1003000000000211", "type": "item", "item": "twilightforest:fiery_blood", "count": 4, "title": "Recolha Sangue da Hidra"}],
                "rewards": [
                    {"id": "1003000000000212", "type": "item", "item": "minecraft:blaze_rod", "count": 8},
                    {"id": "1003000000000213", "type": "xp_levels", "xp_levels": 7}
                ]
            },
            {
                "id": "1003000000000220",
                "dependencies": ["1003000000000210"],
                "title": "Forja da Armadura Flamejante",
                "subtitle": "[Dificuldade: Dificil] Fiery Ingot e a fusao termica suprema",
                "description": [
                    "Ao fundir o sangue da Hidra com ferro refinado, nascem os Lingotes de Fogo (Fiery Ingot).",
                    "Armas forjadas desse material incendeiam permanentemente os alvos e a armadura repele ataques com labaredas retaliatorias."
                ],
                "icon": "twilightforest:fiery_ingot",
                "x": 0.0, "y": 4.0,
                "tasks": [{"id": "1003000000000221", "type": "item", "item": "twilightforest:fiery_ingot", "count": 4, "title": "Forje Lingotes de Fogo"}],
                "rewards": [
                    {"id": "1003000000000222", "type": "item", "item": "twilightforest:fiery_ingot", "count": 2},
                    {"id": "1003000000000223", "type": "xp_levels", "xp_levels": 8}
                ]
            },
            {
                "id": "1003000000000230",
                "dependencies": ["1003000000000140"],
                "title": "A Tumba dos Cavaleiros Fantasmas",
                "subtitle": "[Dificuldade: Dificil] Batalha de espectros na Fortaleza das Trevas",
                "description": [
                    "Nas profundezas da Floresta Sombria repousa a tumba de seis cavaleiros esqueleto espectrais.",
                    "Eles atacam coordenadamente arremessando armas fantasmas. Derrote todos para dissipar a maldicao da tumba!"
                ],
                "icon": "twilightforest:knight_phantom_trophy",
                "x": 2.8, "y": 4.0,
                "tasks": [{"id": "1003000000000231", "type": "item", "item": "twilightforest:knight_phantom_trophy", "title": "Obtenha o Trofeu dos Cavaleiros"}],
                "rewards": [
                    {"id": "1003000000000232", "type": "item", "item": "twilightforest:phantom_helmet"},
                    {"id": "1003000000000233", "type": "xp_levels", "xp_levels": 8}
                ]
            },
            {
                "id": "1003000000000240",
                "dependencies": ["1003000000000230"],
                "title": "Metal dos Cavaleiros Espectrais",
                "subtitle": "[Dificuldade: Dificil] O Knightmetal e as armas fantasmagoricas",
                "description": [
                    "O Knightmetal e extraido dos fragmentos de armaduras deixados pelos guerreiros caidos.",
                    "Com ele voce forja picaretas que danificam inimigos que tentam te interromper e espadas velozes como fantasmas."
                ],
                "icon": "twilightforest:knightmetal_ingot",
                "x": 5.6, "y": 4.0,
                "tasks": [{"id": "1003000000000241", "type": "item", "item": "twilightforest:knightmetal_ingot", "count": 4, "title": "Forje Lingotes de Knightmetal"}],
                "rewards": [
                    {"id": "1003000000000242", "type": "item", "item": "twilightforest:knightmetal_ingot", "count": 4},
                    {"id": "1003000000000243", "type": "xp_levels", "xp_levels": 7}
                ]
            },
            {
                "id": "1003000000000250",
                "dependencies": ["1003000000000230"],
                "title": "O Ur-Ghast da Torre Escura",
                "subtitle": "[Dificuldade: Dificil] O senhor dos tentaculos mecânicos nas nuvens",
                "description": [
                    "No ápice da gigantesca Torre Escura flutua o Ur-Ghast em meio a tempestade de raios e lagrimas carmim.",
                    "Ative os alçapoes com carminite para capturar servos ghasts e disparar ondas de choque letais contra o monarca!"
                ],
                "icon": "twilightforest:ur_ghast_trophy",
                "x": 8.4, "y": 4.0,
                "tasks": [{"id": "1003000000000251", "type": "item", "item": "twilightforest:ur_ghast_trophy", "title": "Obtenha o Trofeu do Ur-Ghast"}],
                "rewards": [
                    {"id": "1003000000000252", "type": "item", "item": "minecraft:ghast_tear", "count": 8},
                    {"id": "1003000000000253", "type": "xp_levels", "xp_levels": 9}
                ]
            },
            {
                "id": "1003000000000260",
                "dependencies": ["1003000000000250"],
                "title": "Lagrimas Ardentes do Vazio",
                "subtitle": "[Dificuldade: Dificil] A essencia liquida da tristeza celestial",
                "description": [
                    "As Fiery Tears do Ur-Ghast sao o equivalente aéreo do sangue da Hidra. Possuem uma afinidade mágica potente para criação de armaduras de fogo e encantos supremos.",
                    "Colete o frasco de lágrimas para completar a progressão da Torre Escura."
                ],
                "icon": "twilightforest:fiery_tears",
                "x": 11.2, "y": 4.0,
                "tasks": [{"id": "1003000000000261", "type": "item", "item": "twilightforest:fiery_tears", "count": 2, "title": "Recolha Lagrimas Ardentes"}],
                "rewards": [
                    {"id": "1003000000000262", "type": "item", "item": "twilightforest:fiery_ingot", "count": 2},
                    {"id": "1003000000000263", "type": "xp_levels", "xp_levels": 8}
                ]
            },

            # TIER EXTREMA (6 Quests, y = 7.5d)
            {
                "id": "1003000000000270",
                "dependencies": ["1003000000000200", "1003000000000250"],
                "title": "O Yeti Alfa da Geleira",
                "subtitle": "[Dificuldade: Extrema] O guardiao furioso das cavernas de gelo",
                "description": [
                    "Dentro da caverna congelada de quatro entradas vive o colossal Yeti Alfa. Quando ele ruge e se enfurece, estalactites pontiagudas caem do teto!",
                    "Esquive-se das estalactites e contra-ataque durante os breves intervalos de fadiga do monstro."
                ],
                "icon": "twilightforest:alpha_yeti_trophy",
                "x": -8.4, "y": 7.5,
                "tasks": [{"id": "1003000000000271", "type": "item", "item": "twilightforest:alpha_yeti_trophy", "title": "Obtenha o Trofeu do Yeti Alfa"}],
                "rewards": [
                    {"id": "1003000000000272", "type": "item", "item": "twilightforest:alpha_yeti_fur", "count": 6},
                    {"id": "1003000000000273", "type": "xp_levels", "xp_levels": 9}
                ]
            },
            {
                "id": "1003000000000280",
                "dependencies": ["1003000000000270"],
                "title": "Pelagem do Yeti e Armadura Termica",
                "subtitle": "[Dificuldade: Extrema] Isolamento contra o frio absoluto",
                "description": [
                    "A pelagem do Yeti Alfa permite criar vestes que congelam oponentes que te atacam corpo a corpo.",
                    "Essencial para suportar a nevasca implacavel do Palacio de Aurora."
                ],
                "icon": "twilightforest:alpha_yeti_fur",
                "x": -5.6, "y": 7.5,
                "tasks": [{"id": "1003000000000281", "type": "item", "item": "twilightforest:alpha_yeti_fur", "count": 4, "title": "Forje Traje com Pelagem de Yeti"}],
                "rewards": [
                    {"id": "1003000000000282", "type": "item", "item": "minecraft:packed_ice", "count": 32},
                    {"id": "1003000000000283", "type": "xp_levels", "xp_levels": 8}
                ]
            },
            {
                "id": "1003000000000290",
                "dependencies": ["1003000000000270"],
                "title": "A Rainha da Neve da Torre Glacial",
                "subtitle": "[Dificuldade: Extrema] A soberana dos cristais e do gelo vivo",
                "description": [
                    "No ápice do Palacio de Aurora aguarda a Snow Queen, protegida por um escudo rotativo de cristais de gelo e voando sobre um bloco flutuante.",
                    "Foque seus ataques quando ela descer para esmagar o chao, destruindo sua guarda com arcos precisos!"
                ],
                "icon": "twilightforest:snow_queen_trophy",
                "x": -2.8, "y": 7.5,
                "tasks": [{"id": "1003000000000291", "type": "item", "item": "twilightforest:snow_queen_trophy", "title": "Obtenha o Trofeu da Rainha da Neve"}],
                "rewards": [
                    {"id": "1003000000000292", "type": "item", "item": "minecraft:diamond_block", "count": 1},
                    {"id": "1003000000000293", "type": "xp_levels", "xp_levels": 10}
                ]
            },
            {
                "id": "1003000000000300",
                "dependencies": ["1003000000000290"],
                "title": "O Arco Glacial Perfurante",
                "subtitle": "[Dificuldade: Extrema] Disparos que congelam a alma dos inimigos",
                "description": [
                    "O Ice Bow da Rainha dispara flechas cobertas de gelo magico que congelam o alvo no lugar por preciosos segundos.",
                    "Uma arma tatica inestimavel para o controle de chefes hiper-velozes."
                ],
                "icon": "twilightforest:ice_bow",
                "x": 0.0, "y": 7.5,
                "tasks": [{"id": "1003000000000301", "type": "item", "item": "twilightforest:ice_bow", "title": "Adquira o Arco de Gelo"}],
                "rewards": [
                    {"id": "1003000000000302", "type": "item", "item": "minecraft:spectral_arrow", "count": 32},
                    {"id": "1003000000000303", "type": "xp_levels", "xp_levels": 8}
                ]
            },
            {
                "id": "1003000000000310",
                "dependencies": ["1003000000000290"],
                "title": "A Picareta do Gigante das Nuvens",
                "subtitle": "[Dificuldade: Extrema] Mineracao colossal em escala monumental",
                "description": [
                    "Nas nuvens acima do planalto vivem gigantes empunhando ferramentas monumentais. A Giant's Pickaxe consegue quebrar blocos 4x4 de uma so vez!",
                    "Uma dadiva fabulosa para abrir espacos gigantescos em construcoes subterraneas."
                ],
                "icon": "twilightforest:giant_pickaxe",
                "x": 2.8, "y": 7.5,
                "tasks": [{"id": "1003000000000311", "type": "item", "item": "twilightforest:giant_pickaxe", "title": "Recupere a Picareta do Gigante"}],
                "rewards": [
                    {"id": "1003000000000312", "type": "item", "item": "minecraft:netherite_scrap", "count": 2},
                    {"id": "1003000000000313", "type": "xp_levels", "xp_levels": 10}
                ]
            },
            {
                "id": "1003000000000320",
                "dependencies": ["1003000000000310"],
                "title": "A Lampada das Cinzas Eternas",
                "subtitle": "[Dificuldade: Extrema] O artefato supremo para queimar as roseiras de espinhos",
                "description": [
                    "A Lamp of Cinders abriga uma chama ancestral capaz de reduzir a cinzas os densos espinhos que cercam o Castelo Final.",
                    "Voce alcancou o ponto mais avancado do Crepusculo Eterno. Guarde sua lampada como simbolo da sua soberania sobre a floresta!"
                ],
                "icon": "twilightforest:lamp_of_cinders",
                "shape": "diamond",
                "size": 1.5,
                "x": 5.6, "y": 7.5,
                "tasks": [{"id": "1003000000000321", "type": "item", "item": "twilightforest:lamp_of_cinders", "title": "Conquiste a Lampada das Cinzas"}],
                "rewards": [
                    {"id": "1003000000000322", "type": "item", "item": "minecraft:nether_star", "count": 1},
                    {"id": "1003000000000323", "type": "xp_levels", "xp_levels": 15}
                ]
            }
        ]
    }

# =====================================================================
# CAPÍTULO 4: THE BUMBLEZONE (29 QUESTS)
# =====================================================================
def get_bumblezone_data():
    return {
        "filename": "capitulo_4_bumblezone",
        "group": "1A2B3C4D5E6F7001",
        "id": "1004000000000001",
        "order_index": 4,
        "title": "4. No Coracao da Colmeia (The Bumblezone)",
        "icon": "the_bumblezone:bee_bread",
        "quests": [
            # TIER FACIL (8 Quests, y = -3.0d)
            {
                "id": "1004000000000010",
                "title": "Rumo a Colmeia Cosmica",
                "subtitle": "[Dificuldade: Facil] O salto quantico atraves do favo",
                "description": [
                    "Para entrar no reino sagrado das abelhas, localize qualquer colmeia repleta de mel (ou Ninho de Abelhas) e atire uma perola de ender diretamente contra ela.",
                    "Voce encolhera milagrosamente e despertara imerso em galerias de puro nectar e ambar cintilante!"
                ],
                "icon": "minecraft:ender_pearl",
                "shape": "hexagon",
                "size": 1.5,
                "x": -9.8, "y": -3.0,
                "tasks": [{"id": "1004000000000011", "type": "checkmark", "title": "Teleporte-se para The Bumblezone"}],
                "rewards": [
                    {"id": "1004000000000012", "type": "item", "item": "minecraft:glass_bottle", "count": 8},
                    {"id": "1004000000000013", "type": "xp_levels", "xp_levels": 3}
                ]
            },
            {
                "id": "1004000000000020",
                "dependencies": ["1004000000000010"],
                "title": "Os Favos Porosos do Solo",
                "subtitle": "[Dificuldade: Facil] A arquitetura esponjosa da colmeia",
                "description": [
                    "Ao descer pelas galerias, repare que as paredes sao feitas de blocos de favo poroso que absorvem quedas e amortecem seus passos.",
                    "Colete amostras para estudar sua composicao e construir estruturas acusticas e macias."
                ],
                "icon": "the_bumblezone:porous_honeycomb_block",
                "x": -7.0, "y": -3.0,
                "tasks": [{"id": "1004000000000021", "type": "item", "item": "the_bumblezone:porous_honeycomb_block", "count": 8, "title": "Colete Blocos de Favo Poroso"}],
                "rewards": [
                    {"id": "1004000000000022", "type": "item", "item": "minecraft:honey_bottle", "count": 4},
                    {"id": "1004000000000023", "type": "xp", "xp": 100}
                ]
            },
            {
                "id": "1004000000000030",
                "dependencies": ["1004000000000020"],
                "title": "A Cera Protetora das Abelhas",
                "subtitle": "[Dificuldade: Facil] Isolamento impermeavel e artesanato puro",
                "description": [
                    "A cera secretada pelas operarias (Beehive Beeswax) e ultra maleavel e serve para confeccionar velas, tijolos ornamentados e selar recipientes.",
                    "Mantenha sempre um estoque na sua bolsa para os artesanatos refinados do formigueiro de mel."
                ],
                "icon": "the_bumblezone:beehive_beeswax",
                "x": -4.2, "y": -3.0,
                "tasks": [{"id": "1004000000000031", "type": "item", "item": "the_bumblezone:beehive_beeswax", "count": 6, "title": "Colete Cera de Abelha"}],
                "rewards": [
                    {"id": "1004000000000032", "type": "item", "item": "minecraft:candle", "count": 4},
                    {"id": "1004000000000033", "type": "xp", "xp": 120}
                ]
            },
            {
                "id": "1004000000000040",
                "dependencies": ["1004000000000030"],
                "title": "Agua com Acucar Revigorante",
                "subtitle": "[Dificuldade: Facil] A bebida favorita das operarias cansadas",
                "description": [
                    "Misturando acucar cristal em garrafas de agua limpa voce prepara Sugar Water Bottles.",
                    "Beber essa infusao regenera sua energia com agilidade, e oferecer as abelhas ganha imediatamente sua admiracao e gratidao!"
                ],
                "icon": "the_bumblezone:sugar_water_bottle",
                "x": -1.4, "y": -3.0,
                "tasks": [{"id": "1004000000000041", "type": "item", "item": "the_bumblezone:sugar_water_bottle", "count": 4, "title": "Prepare Garrafas de Agua com Acucar"}],
                "rewards": [
                    {"id": "1004000000000042", "type": "item", "item": "minecraft:sugar", "count": 16},
                    {"id": "1004000000000043", "type": "xp", "xp": 150}
                ]
            },
            {
                "id": "1004000000000050",
                "dependencies": ["1004000000000040"],
                "title": "O Pao de Mel Nutritivo (Bee Bread)",
                "subtitle": "[Dificuldade: Facil] Superalimento proteico fermentado na colmeia",
                "description": [
                    "O Bee Bread e produzido atraves da fermentacao natural do polen com gotas de mel.",
                    "Cada mordida sacia profundamente a fome do viajante, tornando-o o alimento de campo perfeito para quem passa longas jornadas explorando."
                ],
                "icon": "the_bumblezone:bee_bread",
                "x": 1.4, "y": -3.0,
                "tasks": [{"id": "1004000000000051", "type": "item", "item": "the_bumblezone:bee_bread", "count": 4, "title": "Obtenha Pao de Abelha (Bee Bread)"}],
                "rewards": [
                    {"id": "1004000000000052", "type": "item", "item": "the_bumblezone:bee_bread", "count": 8},
                    {"id": "1004000000000053", "type": "xp", "xp": 150}
                ]
            },
            {
                "id": "1004000000000060",
                "dependencies": ["1004000000000050"],
                "title": "Tufos de Polen no Ar",
                "subtitle": "[Dificuldade: Facil] Polinizacao acelerada em escala mistica",
                "description": [
                    "Pollen Puffs flutuam pelas flores gigantes e cantos da colmeia. Atire um Pollen Puff em lavouras para fertilizar o solo instantaneamente como farinha de osso em massa!",
                    "Excelente para suas plantacoes automatizadas sem nenhum esforco."
                ],
                "icon": "the_bumblezone:pollen_puff",
                "x": 4.2, "y": -3.0,
                "tasks": [{"id": "1004000000000061", "type": "item", "item": "the_bumblezone:pollen_puff", "count": 6, "title": "Colete Tufos de Polen (Pollen Puff)"}],
                "rewards": [
                    {"id": "1004000000000062", "type": "item", "item": "minecraft:bone_meal", "count": 16},
                    {"id": "1004000000000063", "type": "xp", "xp": 150}
                ]
            },
            {
                "id": "1004000000000070",
                "dependencies": ["1004000000000060"],
                "title": "Navegacao por Docura",
                "subtitle": "[Dificuldade: Facil] A Bussola de Mel que aponta para maravilhas",
                "description": [
                    "A Honey Compass sincroniza seus magnetos de nectar para apontar diretamente para colmeias e santuarios secretos.",
                    "Nunca mais se sinta perdido nas infinitas galerias de cera."
                ],
                "icon": "the_bumblezone:honey_compass",
                "x": 7.0, "y": -3.0,
                "tasks": [{"id": "1004000000000071", "type": "item", "item": "the_bumblezone:honey_compass", "title": "Crie a Honey Compass"}],
                "rewards": [
                    {"id": "1004000000000072", "type": "item", "item": "the_bumblezone:sugar_water_bottle", "count": 4},
                    {"id": "1004000000000073", "type": "xp_levels", "xp_levels": 3}
                ]
            },
            {
                "id": "1004000000000080",
                "dependencies": ["1004000000000070"],
                "title": "Capacete de Abelha Sem Ferrao",
                "subtitle": "[Dificuldade: Facil] O primeiro equipamento mimetico da colmeia",
                "description": [
                    "Confeccionado com ceras especiais, o Stingless Bee Helmet faz com que as abelhas te vejam como um aliado benevolente.",
                    "Evite olhares de reprovacao e explore em total harmonia com os enxames."
                ],
                "icon": "the_bumblezone:stingless_bee_helmet_1",
                "x": 9.8, "y": -3.0,
                "tasks": [{"id": "1004000000000081", "type": "item", "item": "the_bumblezone:stingless_bee_helmet_1", "title": "Forje o Capacete de Abelha Sem Ferrao"}],
                "rewards": [
                    {"id": "1004000000000082", "type": "item", "item": "the_bumblezone:beehive_beeswax", "count": 8},
                    {"id": "1004000000000083", "type": "xp_levels", "xp_levels": 4}
                ]
            },

            # TIER MEDIA (8 Quests, y = 0.5d)
            {
                "id": "1004000000000090",
                "dependencies": ["1004000000000030"],
                "title": "Nos de Cera Luminescente",
                "subtitle": "[Dificuldade: Media] Iluminacao de ambar sem queimar oxigenio",
                "description": [
                    "Luminescent Wax Nodes sao nos de cera brilhante que emitem fotons continuos mesmo debaixo d'agua e em correntes de ar viscoso.",
                    "Perfeitos para sinalizar tuneis e criar estacoes subterraneas seguras."
                ],
                "icon": "the_bumblezone:luminescent_wax_node",
                "x": -9.8, "y": 0.5,
                "tasks": [{"id": "1004000000000091", "type": "item", "item": "the_bumblezone:luminescent_wax_node", "count": 4, "title": "Colete Nos de Cera Luminescente"}],
                "rewards": [
                    {"id": "1004000000000092", "type": "item", "item": "the_bumblezone:luminescent_wax_node", "count": 8},
                    {"id": "1004000000000093", "type": "xp_levels", "xp_levels": 4}
                ]
            },
            {
                "id": "1004000000000100",
                "dependencies": ["1004000000000090"],
                "title": "Fragmentos do Cristal de Mel",
                "subtitle": "[Dificuldade: Media] Minerando geodos de mel petrificado",
                "description": [
                    "Em cavernas profundas, o mel se cristaliza em estalactites densas com resistencia de pedras preciosas.",
                    "Extraia Honey Crystal Shards para forjar escudos refratarios e ferramentas duraveis."
                ],
                "icon": "the_bumblezone:honey_crystal_shards",
                "x": -7.0, "y": 0.5,
                "tasks": [{"id": "1004000000000101", "type": "item", "item": "the_bumblezone:honey_crystal_shards", "count": 8, "title": "Minerar Fragmentos de Cristal de Mel"}],
                "rewards": [
                    {"id": "1004000000000102", "type": "item", "item": "the_bumblezone:honey_crystal_shards", "count": 8},
                    {"id": "1004000000000103", "type": "xp_levels", "xp_levels": 5}
                ]
            },
            {
                "id": "1004000000000110",
                "dependencies": ["1004000000000100"],
                "title": "O Escudo Cristalino de Mel",
                "subtitle": "[Dificuldade: Media] Defesa gelatinosa que desacelera projeteis",
                "description": [
                    "O Honey Crystal Shield absorve impactos e gruda ataques fisicos, reduzindo a velocidade dos agressores.",
                    "Uma protecao confiavel para repelir vespas agressivas e monstros venenosos."
                ],
                "icon": "the_bumblezone:honey_crystal_shield",
                "x": -4.2, "y": 0.5,
                "tasks": [{"id": "1004000000000111", "type": "item", "item": "the_bumblezone:honey_crystal_shield", "title": "Forje o Escudo de Cristal de Mel"}],
                "rewards": [
                    {"id": "1004000000000112", "type": "item", "item": "minecraft:golden_carrot", "count": 8},
                    {"id": "1004000000000113", "type": "xp_levels", "xp_levels": 5}
                ]
            },
            {
                "id": "1004000000000120",
                "dependencies": ["1004000000000050"],
                "title": "Sopa de Mel Reconfortante",
                "subtitle": "[Dificuldade: Media] Refeicao quente para climas viscosos",
                "description": [
                    "A Bee Soup une caldos de vegetais ricos com geleia real, nutrindo o corpo com rapidez incomparavel.",
                    "Tenha tigelas preparadas antes de descer as fendas mais profundas da dimensao."
                ],
                "icon": "the_bumblezone:bee_soup",
                "x": -1.4, "y": 0.5,
                "tasks": [{"id": "1004000000000121", "type": "item", "item": "the_bumblezone:bee_soup", "count": 2, "title": "Prepare Sopa de Mel"}],
                "rewards": [
                    {"id": "1004000000000122", "type": "item", "item": "the_bumblezone:bee_soup", "count": 4},
                    {"id": "1004000000000123", "type": "xp_levels", "xp_levels": 4}
                ]
            },
            {
                "id": "1004000000000130",
                "dependencies": ["1004000000000100"],
                "title": "Botas da Abelha Carpinteira",
                "subtitle": "[Dificuldade: Media] Escalada aderente em superficies escorregadias",
                "description": [
                    "As Carpenter Bee Boots permitem que o portador suba e se fixe em paredes de favos pegajosos com estabilidade absoluta.",
                    "Nunca mais escorregue acidentalmente em cascatas de mel!"
                ],
                "icon": "the_bumblezone:carpenter_bee_boots_1",
                "x": 1.4, "y": 0.5,
                "tasks": [{"id": "1004000000000131", "type": "item", "item": "the_bumblezone:carpenter_bee_boots_1", "title": "Forje as Botas de Abelha Carpinteira"}],
                "rewards": [
                    {"id": "1004000000000132", "type": "item", "item": "minecraft:slime_ball", "count": 8},
                    {"id": "1004000000000133", "type": "xp_levels", "xp_levels": 5}
                ]
            },
            {
                "id": "1004000000000140",
                "dependencies": ["1004000000000130"],
                "title": "Perneiras da Abelha Operaria",
                "subtitle": "[Dificuldade: Media] Mobilidade e resistencia ao acido da colmeia",
                "description": [
                    "Costuradas com peles polinizadas, as Honey Bee Leggings complementam o traje concedendo reducao de dano contra venenos e acido de ferroes.",
                    "Indispensaveis para explorar ninhos de vespas."
                ],
                "icon": "the_bumblezone:honey_bee_leggings_1",
                "x": 4.2, "y": 0.5,
                "tasks": [{"id": "1004000000000141", "type": "item", "item": "the_bumblezone:honey_bee_leggings_1", "title": "Forje as Perneiras de Abelha Operaria"}],
                "rewards": [
                    {"id": "1004000000000142", "type": "item", "item": "minecraft:iron_ingot", "count": 6},
                    {"id": "1004000000000143", "type": "xp_levels", "xp_levels": 5}
                ]
            },
            {
                "id": "1004000000000150",
                "dependencies": ["1004000000000140"],
                "title": "Peitoral Protetor da Colmeia",
                "subtitle": "[Dificuldade: Media] Armadura quitinosa com asas integradas",
                "description": [
                    "O Bumble Bee Chestplate confere defesa massiva e melhora o planeio com asas aerodinamicas da colmeia.",
                    "Combine as quatro pecas para usufruir de beneficios de simpatia com a colonia inteira."
                ],
                "icon": "the_bumblezone:bumble_bee_chestplate_1",
                "x": 7.0, "y": 0.5,
                "tasks": [{"id": "1004000000000151", "type": "item", "item": "the_bumblezone:bumble_bee_chestplate_1", "title": "Forje o Peitoral de Abelha"}],
                "rewards": [
                    {"id": "1004000000000152", "type": "item", "item": "the_bumblezone:honey_crystal_shards", "count": 8},
                    {"id": "1004000000000153", "type": "xp_levels", "xp_levels": 6}
                ]
            },
            {
                "id": "1004000000000160",
                "dependencies": ["1004000000000030"],
                "title": "Velas Aromaticas Alquimicas",
                "subtitle": "[Dificuldade: Media] Aromatizadores que pacificam os ares",
                "description": [
                    "A Potion Candle queima liberando vapores alquimicos suaves que concedem efeitos beneficos para todos os jogadores ao redor.",
                    "Acenda uma vela em sua base na colmeia para respirar tranquilo e recarregar suas energias."
                ],
                "icon": "the_bumblezone:potion_candle",
                "x": 9.8, "y": 0.5,
                "tasks": [{"id": "1004000000000161", "type": "item", "item": "the_bumblezone:potion_candle", "title": "Crie uma Vela de Pocao (Potion Candle)"}],
                "rewards": [
                    {"id": "1004000000000162", "type": "item", "item": "minecraft:blaze_powder", "count": 4},
                    {"id": "1004000000000163", "type": "xp_levels", "xp_levels": 5}
                ]
            },

            # TIER DIFICIL (9 Quests, y = 4.0d)
            {
                "id": "1004000000000170",
                "dependencies": ["1004000000000150"],
                "title": "Audiencia com a Rainha Abelha",
                "subtitle": "[Dificuldade: Dificil] Negociacoes e trocas de tributos reais",
                "description": [
                    "Em seu trono colossal repousa a majestosa Bee Queen. Ela e pacifica por natureza, mas exige tributos dignos em troca de reliquias arcanas.",
                    "Faca trocas com a Rainha oferecendo nectares raros e pecas de armadura para receber presentes inestimaveis!"
                ],
                "icon": "the_bumblezone:bee_stinger",
                "x": -11.2, "y": 4.0,
                "tasks": [{"id": "1004000000000171", "type": "item", "item": "the_bumblezone:bee_stinger", "count": 2, "title": "Obtenha Ferroes de Abelha Raros"}],
                "rewards": [
                    {"id": "1004000000000172", "type": "item", "item": "minecraft:gold_block", "count": 2},
                    {"id": "1004000000000173", "type": "xp_levels", "xp_levels": 7}
                ]
            },
            {
                "id": "1004000000000180",
                "dependencies": ["1004000000000170"],
                "title": "O Canhao de Abelhas (Bee Cannon)",
                "subtitle": "[Dificuldade: Dificil] Artilharia viva alimentada por enxames",
                "description": [
                    "O Bee Cannon e uma das armas mais irreverentes e poderosas da colmeia. Ele dispara abelhas enfurecidas teleguiadas em direcao a qualquer agressor!",
                    "Trate suas municoes com carinho e veja as hordas inimigas sucumbirem ao enxame zumbidor."
                ],
                "icon": "the_bumblezone:bee_cannon",
                "x": -8.4, "y": 4.0,
                "tasks": [{"id": "1004000000000181", "type": "item", "item": "the_bumblezone:bee_cannon", "title": "Construa o Canhao de Abelhas"}],
                "rewards": [
                    {"id": "1004000000000182", "type": "item", "item": "the_bumblezone:sugar_water_bottle", "count": 8},
                    {"id": "1004000000000183", "type": "xp_levels", "xp_levels": 7}
                ]
            },
            {
                "id": "1004000000000190",
                "dependencies": ["1004000000000170"],
                "title": "Tijolos de Cera Ancestral",
                "subtitle": "[Dificuldade: Dificil] Monumentos e santuarios das velhas dinastias",
                "description": [
                    "Estruturas em ruinas espalhadas pela dimensao foram erguidas com Ancient Wax Bricks, um material indestrutivel por chamas convencionais.",
                    "Explore os altares para desvendar os segredos dos ancestrais da colmeia."
                ],
                "icon": "the_bumblezone:ancient_wax_bricks",
                "x": -5.6, "y": 4.0,
                "tasks": [{"id": "1004000000000191", "type": "item", "item": "the_bumblezone:ancient_wax_bricks", "count": 16, "title": "Colete Tijolos de Cera Ancestral"}],
                "rewards": [
                    {"id": "1004000000000192", "type": "item", "item": "minecraft:emerald", "count": 12},
                    {"id": "1004000000000193", "type": "xp_levels", "xp_levels": 6}
                ]
            },
            {
                "id": "1004000000000200",
                "dependencies": ["1004000000000190"],
                "title": "A Essencia das Abelhas",
                "subtitle": "[Dificuldade: Dificil] A destilacao concentrada do espirito coletivo",
                "description": [
                    "A Essence of the Bees e o extrato supremo de fertilidade e vida vegetal. Ela repara equipamentos biologicos e cura enxames instantaneamente.",
                    "Guarde com extrema reverencia este elixir dourado."
                ],
                "icon": "the_bumblezone:essence_of_the_bees",
                "x": -2.8, "y": 4.0,
                "tasks": [{"id": "1004000000000201", "type": "item", "item": "the_bumblezone:essence_of_the_bees", "title": "Conquiste a Essencia das Abelhas"}],
                "rewards": [
                    {"id": "1004000000000202", "type": "item", "item": "the_bumblezone:essence_of_the_bees", "count": 1},
                    {"id": "1004000000000203", "type": "xp_levels", "xp_levels": 8}
                ]
            },
            {
                "id": "1004000000000210",
                "dependencies": ["1004000000000200"],
                "title": "O Casulo Sagrado de Mel",
                "subtitle": "[Dificuldade: Dificil] Incubacao e renascimento na colmeia",
                "description": [
                    "Nos santuarios da Rainha encontram-se Honey Cocoons. Ao serem abertos com ferramentas delicadas, revelam criaturas raras e tesouros esquecidos.",
                    "Cuide dos casulos para preservar a linhagem real."
                ],
                "icon": "the_bumblezone:honey_cocoon",
                "x": 0.0, "y": 4.0,
                "tasks": [{"id": "1004000000000211", "type": "item", "item": "the_bumblezone:honey_cocoon", "title": "Resgate um Casulo de Mel (Honey Cocoon)"}],
                "rewards": [
                    {"id": "1004000000000212", "type": "item", "item": "the_bumblezone:bee_bread", "count": 6},
                    {"id": "1004000000000213", "type": "xp_levels", "xp_levels": 7}
                ]
            },
            {
                "id": "1004000000000220",
                "dependencies": ["1004000000000190"],
                "title": "A Super Vela dos Santuarios",
                "subtitle": "[Dificuldade: Dificil] O fogo perene que ilumina kilometros de favos",
                "description": [
                    "A Super Candle e forjada a partir de ceras ancestrais refinadas. Seu raio de iluminacao dissipa a escuridao mesmo nas maiores cavernas abertas.",
                    "Um artefato decorativo e funcional digno de mestres construtores."
                ],
                "icon": "the_bumblezone:super_candle",
                "x": 2.8, "y": 4.0,
                "tasks": [{"id": "1004000000000221", "type": "item", "item": "the_bumblezone:super_candle", "title": "Crie uma Super Vela"}],
                "rewards": [
                    {"id": "1004000000000222", "type": "item", "item": "minecraft:glowstone", "count": 16},
                    {"id": "1004000000000223", "type": "xp_levels", "xp_levels": 6}
                ]
            },
            {
                "id": "1004000000000230",
                "dependencies": ["1004000000000150"],
                "title": "O Manto Translucido da Rainha",
                "subtitle": "[Dificuldade: Dificil] As asas celestiais de quitina pura",
                "description": [
                    "Ao consagrar seu peitoral de abelha com tecidos de quitina translucida perante a Rainha, voce forja o Bumble Bee Chestplate Translucido.",
                    "Sua velocidade no ar atinge novos patamares de elegancia e liberdade."
                ],
                "icon": "the_bumblezone:bumble_bee_chestplate_trans_1",
                "x": 5.6, "y": 4.0,
                "tasks": [{"id": "1004000000000231", "type": "item", "item": "the_bumblezone:bumble_bee_chestplate_trans_1", "title": "Forje o Manto Translucido da Rainha"}],
                "rewards": [
                    {"id": "1004000000000232", "type": "item", "item": "minecraft:feather", "count": 32},
                    {"id": "1004000000000233", "type": "xp_levels", "xp_levels": 8}
                ]
            },
            {
                "id": "1004000000000240",
                "dependencies": ["1004000000000170"],
                "title": "O Banquete dos Campeoes",
                "subtitle": "[Dificuldade: Dificil] Preparando oferendas gastronomicas reais",
                "description": [
                    "A Rainha reconhece chefs dedicados. Prepare um farto carregamento de Bee Bread e sopas para abastecer a despensa real em epocas de seca.",
                    "O pacto de lealdade sera recompensado com acesso irrestrito aos tesouros mais profundos."
                ],
                "icon": "the_bumblezone:bee_bread",
                "x": 8.4, "y": 4.0,
                "tasks": [{"id": "1004000000000241", "type": "item", "item": "the_bumblezone:bee_bread", "count": 16, "title": "Entregue 16 Paes de Abelha"}],
                "rewards": [
                    {"id": "1004000000000242", "type": "item", "item": "the_bumblezone:sugar_water_bottle", "count": 16},
                    {"id": "1004000000000243", "type": "xp_levels", "xp_levels": 7}
                ]
            },
            {
                "id": "1004000000000250",
                "dependencies": ["1004000000000210"],
                "title": "A Cura das Larvas da Colmeia",
                "subtitle": "[Dificuldade: Dificil] Preservando o futuro da especie",
                "description": [
                    "Muitos favos de criacao sao contaminados por fungos e parasitas externos. Use agua doce enriquecida e essencia para revitalizar os blocos de criacao (Brood Blocks).",
                    "A harmonia ecologica da colmeia depende do seu cuidado paternal."
                ],
                "icon": "the_bumblezone:honey_cocoon",
                "x": 11.2, "y": 4.0,
                "tasks": [{"id": "1004000000000251", "type": "checkmark", "title": "Revitalize um Berçario da Colmeia"}],
                "rewards": [
                    {"id": "1004000000000252", "type": "item", "item": "minecraft:honey_block", "count": 8},
                    {"id": "1004000000000253", "type": "xp_levels", "xp_levels": 7}
                ]
            },

            # TIER EXTREMA (4 Quests, y = 7.5d)
            {
                "id": "1004000000000260",
                "dependencies": ["1004000000000230"],
                "title": "O Colosso Alado: Beehemoth",
                "subtitle": "[Dificuldade: Extrema] Domando a maior criatura dos ceus de mel",
                "description": [
                    "O Beehemoth e a majestosa abelha gigante capaz de carregar cavaleiros em seu dorso. Para doma-lo, alimente-o pacientemente com agua adocada e amizade constante.",
                    "Uma vez domado, coloque uma sela e voe com controle impecavel pelas alturas infinitas da dimensao!"
                ],
                "icon": "the_bumblezone:sugar_water_bottle",
                "shape": "hexagon",
                "size": 1.4,
                "x": -4.2, "y": 7.5,
                "tasks": [{"id": "1004000000000261", "type": "checkmark", "title": "Dome e Cavalgue um Beehemoth"}],
                "rewards": [
                    {"id": "1004000000000262", "type": "item", "item": "minecraft:saddle"},
                    {"id": "1004000000000263", "type": "xp_levels", "xp_levels": 10}
                ]
            },
            {
                "id": "1004000000000270",
                "dependencies": ["1004000000000180"],
                "title": "A Furia da Colmeia Superada",
                "subtitle": "[Dificuldade: Extrema] Sobrevivendo ao Wrath of the Hive nivel maximo",
                "description": [
                    "Perturbar favos proibidos ou agredir a realeza desperta o terrível efeito Wrath of the Hive. O ceu escurece em carmesim e milhares de abelhas vorazes emergem das paredes!",
                    "Sobreviva a toda a duracao do efeito sem morrer para provar sua invulnerabilidade suprema."
                ],
                "icon": "the_bumblezone:bee_stinger",
                "x": -1.4, "y": 7.5,
                "tasks": [{"id": "1004000000000271", "type": "checkmark", "title": "Sobreviva ao Wrath of the Hive Maximo"}],
                "rewards": [
                    {"id": "1004000000000272", "type": "item", "item": "minecraft:totem_of_undying"},
                    {"id": "1004000000000273", "type": "xp_levels", "xp_levels": 12}
                ]
            },
            {
                "id": "1004000000000280",
                "dependencies": ["1004000000000190"],
                "title": "O Labirinto do Templo de Cera",
                "subtitle": "[Dificuldade: Extrema] Desafiando os guardioes milenares",
                "description": [
                    "No santuario subterraneo mais profundo aguarda o Labirinto de Cera Antiga. Armadilhas de teia de mel, lavas doces e sentinelas velozes guardam a camara final.",
                    "Conquiste o nucleo do labirinto e receba as honrarias da corte das abelhas."
                ],
                "icon": "the_bumblezone:ancient_wax_bricks",
                "x": 1.4, "y": 7.5,
                "tasks": [{"id": "1004000000000281", "type": "checkmark", "title": "Conquiste o Labirinto do Templo"}],
                "rewards": [
                    {"id": "1004000000000282", "type": "item", "item": "minecraft:netherite_ingot", "count": 2},
                    {"id": "1004000000000283", "type": "xp_levels", "xp_levels": 12}
                ]
            },
            {
                "id": "1004000000000290",
                "dependencies": ["1004000000000260", "1004000000000270", "1004000000000280"],
                "title": "O Mestre do Nectar Cosmico",
                "subtitle": "[Dificuldade: Extrema] A soberania pacifica do Mundo Eterno",
                "description": [
                    "Voce alcancou a compreensao total da simbiose com as abelhas. A colmeia nao e um lugar para saquear com pressa, mas sim um lar acolhedor de infinita docura.",
                    "Receba o titulo de Guardiao Supremo do Ambar e desfrute da sua jornada eterna!"
                ],
                "icon": "the_bumblezone:essence_of_the_bees",
                "shape": "diamond",
                "size": 1.5,
                "x": 4.2, "y": 7.5,
                "tasks": [{"id": "1004000000000291", "type": "checkmark", "title": "Consagre-se Mestre do Nectar"}],
                "rewards": [
                    {"id": "1004000000000292", "type": "item", "item": "minecraft:nether_star", "count": 1},
                    {"id": "1004000000000293", "type": "xp_levels", "xp_levels": 15}
                ]
            }
        ]
    }

# =====================================================================
# CAPÍTULO 5: O ARSENAL LENDÁRIO (29 QUESTS)
# =====================================================================
def get_arsenal_data():
    return {
        "filename": "capitulo_5_arsenal",
        "group": "1A2B3C4D5E6F7001",
        "id": "1005000000000001",
        "order_index": 5,
        "title": "5. O Arsenal Lendario (Simply Swords e Armaduras)",
        "icon": "simplyswords:iron_longsword",
        "quests": [
            # TIER FACIL (8 Quests, y = -3.0d)
            {
                "id": "1005000000000010",
                "title": "A Filosofia do Armeiro",
                "subtitle": "[Dificuldade: Facil] Cada lamina reflete uma postura de alma",
                "description": [
                    "O combate tradicional do Minecraft com espadas genericas e limitado. Com o Simply Swords e Armor of the Ages, seu arsenal ganha estilos marciais historicos e taticas unicas:",
                    "• Espadas longas fornecem alcance extendido;",
                    "• Rapieiras concedem sequencias de golpes ultra-rapidas;",
                    "• Claymores varrem hordas inteiras em arcos abertos.",
                    "Descubra cada postura sem pressa e eleja suas laminas favoritas!"
                ],
                "icon": "minecraft:iron_sword",
                "shape": "hexagon",
                "size": 1.5,
                "x": -9.8, "y": -3.0,
                "tasks": [{"id": "1005000000000011", "type": "checkmark", "title": "Inicie o Caminho do Armeiro"}],
                "rewards": [
                    {"id": "1005000000000012", "type": "item", "item": "minecraft:iron_ingot", "count": 8},
                    {"id": "1005000000000013", "type": "xp_levels", "xp_levels": 3}
                ]
            },
            {
                "id": "1005000000000020",
                "dependencies": ["1005000000000010"],
                "title": "A Pedra de Amolar do Aprendiz",
                "subtitle": "[Dificuldade: Facil] Manutencao de fio e purificacao de metais",
                "description": [
                    "Um verdadeiro guerreiro sabe que lamina cega e perigo certo. Tenha um Rebolo (Grindstone) em sua forja para remover impurezas e reciclar encantamentos antigos em pura experiencia.",
                    "A forja bem cuidada e a base de todo arsenal formidavel."
                ],
                "icon": "minecraft:grindstone",
                "x": -7.0, "y": -3.0,
                "tasks": [{"id": "1005000000000021", "type": "item", "item": "minecraft:grindstone", "title": "Construa um Rebolo"}],
                "rewards": [
                    {"id": "1005000000000022", "type": "item", "item": "minecraft:iron_ingot", "count": 4},
                    {"id": "1005000000000023", "type": "xp", "xp": 100}
                ]
            },
            {
                "id": "1005000000000030",
                "dependencies": ["1005000000000020"],
                "title": "Espada Longa de Ferro (Longsword)",
                "subtitle": "[Dificuldade: Facil] Alcance estendido e equilibrio impecavel",
                "description": [
                    "A Longsword foi projetada para manter inimigos fora da distancia de golpe padrao. Seu alcance superior permite golpear rastejantes e esqueletos antes que alcancem voce.",
                    "Forje sua primeira espada longa basica de ferro."
                ],
                "icon": "simplyswords:iron_longsword",
                "x": -4.2, "y": -3.0,
                "tasks": [{"id": "1005000000000031", "type": "item", "item": "simplyswords:iron_longsword", "title": "Forje uma Longsword de Ferro"}],
                "rewards": [
                    {"id": "1005000000000032", "type": "item", "item": "minecraft:leather", "count": 8},
                    {"id": "1005000000000033", "type": "xp", "xp": 150}
                ]
            },
            {
                "id": "1005000000000040",
                "dependencies": ["1005000000000020"],
                "title": "Rapieira de Ferro Veloz (Rapier)",
                "subtitle": "[Dificuldade: Facil] Velocidade cirurgica e estocadas consecutivas",
                "description": [
                    "A Rapier possui taxa de ataque altissima. Ao atingir o alvo em sequencia ininterrupta, desfere dano acumulativo devastador.",
                    "Excelente para jogadores que apreciam ritmo rapido e agilidade de esquiva."
                ],
                "icon": "simplyswords:iron_rapier",
                "x": -1.4, "y": -3.0,
                "tasks": [{"id": "1005000000000041", "type": "item", "item": "simplyswords:iron_rapier", "title": "Forje uma Rapieira de Ferro"}],
                "rewards": [
                    {"id": "1005000000000042", "type": "item", "item": "minecraft:iron_nugget", "count": 16},
                    {"id": "1005000000000043", "type": "xp", "xp": 150}
                ]
            },
            {
                "id": "1005000000000050",
                "dependencies": ["1005000000000020"],
                "title": "Par de Sais de Ferro Ageis (Sai)",
                "subtitle": "[Dificuldade: Facil] Combate de empunhadura dupla e desvio letal",
                "description": [
                    "O Sai e uma adaga de tres pontas oriental de manuseio duplo. Ele concede ataques rapidos como o relampago em combates a queima-roupa.",
                    "Forje um par de Sais de ferro para treinar suas combinacoes marciais."
                ],
                "icon": "simplyswords:iron_sai",
                "x": 1.4, "y": -3.0,
                "tasks": [{"id": "1005000000000051", "type": "item", "item": "simplyswords:iron_sai", "title": "Forje um Sai de Ferro"}],
                "rewards": [
                    {"id": "1005000000000052", "type": "item", "item": "minecraft:flint", "count": 8},
                    {"id": "1005000000000053", "type": "xp", "xp": 150}
                ]
            },
            {
                "id": "1005000000000060",
                "dependencies": ["1005000000000020"],
                "title": "Alabarda de Ferro de Infantaria",
                "subtitle": "[Dificuldade: Facil] A forca da haste contra cavaleiros e hordas",
                "description": [
                    "A Halberd une uma cabeca de machado com uma ponta perfurante montada sobre uma longa haste de madeira.",
                    "Capaz de quebrar escudos e repelir inimigos com violencia descomunal."
                ],
                "icon": "simplyswords:iron_halberd",
                "x": 4.2, "y": -3.0,
                "tasks": [{"id": "1005000000000061", "type": "item", "item": "simplyswords:iron_halberd", "title": "Forje uma Alabarda de Ferro"}],
                "rewards": [
                    {"id": "1005000000000062", "type": "item", "item": "minecraft:stick", "count": 16},
                    {"id": "1005000000000063", "type": "xp", "xp": 150}
                ]
            },
            {
                "id": "1005000000000070",
                "dependencies": ["1005000000000020"],
                "title": "Lanca de Ferro Perfurante (Spear)",
                "subtitle": "[Dificuldade: Facil] Dominio do espaco com estocadas lineares",
                "description": [
                    "A Spear foi a arma mais dominante de todas as eras antigas por uma razao simples: alcanca o inimigo muito antes dele poder te tocar.",
                    "Mantenha monstros perigosos a distancia de seguranca com precisao impecavel."
                ],
                "icon": "simplyswords:iron_spear",
                "x": 7.0, "y": -3.0,
                "tasks": [{"id": "1005000000000071", "type": "item", "item": "simplyswords:iron_spear", "title": "Forje uma Lanca de Ferro"}],
                "rewards": [
                    {"id": "1005000000000072", "type": "item", "item": "minecraft:oak_log", "count": 8},
                    {"id": "1005000000000073", "type": "xp", "xp": 150}
                ]
            },
            {
                "id": "1005000000000080",
                "dependencies": ["1005000000000020"],
                "title": "Claymore de Ferro Devastadora",
                "subtitle": "[Dificuldade: Facil] A grande lamina de duas maos das terras altas",
                "description": [
                    "A Claymore possui arco de varredura massivo. Um unico golpe bem posicionado atinge e arremessa para tras tres ou quatro monstros simultaneamente.",
                    "Perfeita para momentos em que voce se ve cercado em cavernas escuras."
                ],
                "icon": "simplyswords:iron_claymore",
                "x": 9.8, "y": -3.0,
                "tasks": [{"id": "1005000000000081", "type": "item", "item": "simplyswords:iron_claymore", "title": "Forje uma Claymore de Ferro"}],
                "rewards": [
                    {"id": "1005000000000082", "type": "item", "item": "minecraft:iron_ingot", "count": 4},
                    {"id": "1005000000000083", "type": "xp_levels", "xp_levels": 3}
                ]
            },

            # TIER MEDIA (8 Quests, y = 0.5d)
            {
                "id": "1005000000000090",
                "dependencies": ["1005000000000030"],
                "title": "Katana de Ferro e Disciplina",
                "subtitle": "[Dificuldade: Media] Cortes em saque rapido (Iaijutsu)",
                "description": [
                    "A Katana une curvatura perfeita e borda ultra-fina. Seus ataques criticos causam sangramentos profundos que enfraquecem chefes com o tempo.",
                    "Uma obra de arte oriental forjada na sua propria bigorna."
                ],
                "icon": "simplyswords:iron_katana",
                "x": -9.8, "y": 0.5,
                "tasks": [{"id": "1005000000000091", "type": "item", "item": "simplyswords:iron_katana", "title": "Forje uma Katana de Ferro"}],
                "rewards": [
                    {"id": "1005000000000092", "type": "item", "item": "minecraft:gold_ingot", "count": 4},
                    {"id": "1005000000000093", "type": "xp_levels", "xp_levels": 5}
                ]
            },
            {
                "id": "1005000000000100",
                "dependencies": ["1005000000000030"],
                "title": "Lamina Dupla Giratoria (Twinblade)",
                "subtitle": "[Dificuldade: Media] O torvelinho cortante de duas pontas",
                "description": [
                    "A Twinblade e empunhada no centro, girando como a helice de um moinho. Ao correr e atacar, voce se torna um furacao imune a flechas.",
                    "Domine o movimento giratorio para surpreender agressores velozes."
                ],
                "icon": "simplyswords:iron_twinblade",
                "x": -7.0, "y": 0.5,
                "tasks": [{"id": "1005000000000101", "type": "item", "item": "simplyswords:iron_twinblade", "title": "Forje uma Twinblade de Ferro"}],
                "rewards": [
                    {"id": "1005000000000102", "type": "item", "item": "minecraft:iron_ingot", "count": 6},
                    {"id": "1005000000000103", "type": "xp_levels", "xp_levels": 5}
                ]
            },
            {
                "id": "1005000000000110",
                "dependencies": ["1005000000000040"],
                "title": "Cutelo Pirata Veloz (Cutlass)",
                "subtitle": "[Dificuldade: Media] Destreza nos conveses e esquivas acrobaticas",
                "description": [
                    "O Cutlass e leve, rapido e desenhado para duelos dinamicos. Permite manobras evasivas imediatas apos cada golpe desferido.",
                    "Sinta-se o capitao dos sete mares explorando as costas do mundo."
                ],
                "icon": "simplyswords:iron_cutlass",
                "x": -4.2, "y": 0.5,
                "tasks": [{"id": "1005000000000111", "type": "item", "item": "simplyswords:iron_cutlass", "title": "Forje um Cutlass de Ferro"}],
                "rewards": [
                    {"id": "1005000000000112", "type": "item", "item": "minecraft:lapis_lazuli", "count": 16},
                    {"id": "1005000000000113", "type": "xp_levels", "xp_levels": 5}
                ]
            },
            {
                "id": "1005000000000120",
                "dependencies": ["1005000000000060"],
                "title": "Glaive de Guerra dos Generais",
                "subtitle": "[Dificuldade: Media] Potencia cortante montada em haste balanceada",
                "description": [
                    "A Warglaive une lamina de alfanje a haste de impacto, conferindo varreduras aereas que acertam monstros voadores e alvos terrestres em sincronia.",
                    "A arma favorita das vanguardas imperiais."
                ],
                "icon": "simplyswords:iron_warglaive",
                "x": -1.4, "y": 0.5,
                "tasks": [{"id": "1005000000000121", "type": "item", "item": "simplyswords:iron_warglaive", "title": "Forje uma Warglaive de Ferro"}],
                "rewards": [
                    {"id": "1005000000000122", "type": "item", "item": "minecraft:diamond", "count": 2},
                    {"id": "1005000000000123", "type": "xp_levels", "xp_levels": 6}
                ]
            },
            {
                "id": "1005000000000130",
                "dependencies": ["1005000000000010"],
                "title": "A Tabua Runica Arcana",
                "subtitle": "[Dificuldade: Media] O molde sagrado para fundir laminas unicas",
                "description": [
                    "A Runic Tablet e um molde antigo encontrado em baus de masmorras ou sintetizado com gemas e diamantes.",
                    "Ela desbloqueia a infusao de almas elementais para transformar espadas comuns nas místicas armas de lenda!"
                ],
                "icon": "simplyswords:runic_tablet",
                "x": 1.4, "y": 0.5,
                "tasks": [{"id": "1005000000000131", "type": "item", "item": "simplyswords:runic_tablet", "title": "Obtenha uma Tabua Runica (Runic Tablet)"}],
                "rewards": [
                    {"id": "1005000000000132", "type": "item", "item": "minecraft:diamond", "count": 3},
                    {"id": "1005000000000133", "type": "xp_levels", "xp_levels": 6}
                ]
            },
            {
                "id": "1005000000000140",
                "dependencies": ["1005000000000010"],
                "title": "Peitoral de Placas de Ferro Reforcado",
                "subtitle": "[Dificuldade: Media] A armadura de transicao para a Idade do Aco",
                "description": [
                    "Antes de herdar as armaduras das grandes civilizacoes historicas, forje o Iron Plate Armor Chestplate do Armor of the Ages.",
                    "Sua couraca protege os orgaos vitais e prepara seu corpo para suportar o peso dos conjuntos miticos."
                ],
                "icon": "armoroftheages:iron_plate_armor_chest",
                "x": 4.2, "y": 0.5,
                "tasks": [{"id": "1005000000000141", "type": "item", "item": "armoroftheages:iron_plate_armor_chest", "title": "Forje o Peitoral de Placas de Ferro"}],
                "rewards": [
                    {"id": "1005000000000142", "type": "item", "item": "minecraft:iron_block", "count": 1},
                    {"id": "1005000000000143", "type": "xp_levels", "xp_levels": 5}
                ]
            },
            {
                "id": "1005000000000150",
                "dependencies": ["1005000000000140"],
                "title": "Armadura do Centuriao Romano",
                "subtitle": "[Dificuldade: Media] A gloria inquebravel das legioes de Roma",
                "description": [
                    "Inspirada na armadura dos comandantes da legiao romana, a armadura de Centuriao confere firmeza disciplinada e resistencia contra empurrao.",
                    "Cerque-se de camaradas e avance em formacao de tartaruga invicta."
                ],
                "icon": "armoroftheages:centurion_armor_chest",
                "x": 7.0, "y": 0.5,
                "tasks": [{"id": "1005000000000151", "type": "item", "item": "armoroftheages:centurion_armor_chest", "title": "Forje o Peitoral de Centuriao"}],
                "rewards": [
                    {"id": "1005000000000152", "type": "item", "item": "minecraft:gold_ingot", "count": 6},
                    {"id": "1005000000000153", "type": "xp_levels", "xp_levels": 6}
                ]
            },
            {
                "id": "1005000000000160",
                "dependencies": ["1005000000000140"],
                "title": "Armadura Leve Japonesa",
                "subtitle": "[Dificuldade: Media] O tecido encouraçado dos nobres samurais",
                "description": [
                    "A Japanese Light Armor prioriza flexibilidade e esquivas rapidas sem sacrificar a resistencia contra flechas.",
                    "O par perfeito para guerreiros que empunham katanas e nodachis."
                ],
                "icon": "armoroftheages:japanese_light_armor_chest",
                "x": 9.8, "y": 0.5,
                "tasks": [{"id": "1005000000000161", "type": "item", "item": "armoroftheages:japanese_light_armor_chest", "title": "Forje a Armadura Leve Japonesa"}],
                "rewards": [
                    {"id": "1005000000000162", "type": "item", "item": "minecraft:leather", "count": 12},
                    {"id": "1005000000000163", "type": "xp_levels", "xp_levels": 6}
                ]
            },

            # TIER DIFICIL (9 Quests, y = 4.0d)
            {
                "id": "1005000000000170",
                "dependencies": ["1005000000000150"],
                "title": "A Armadura Sagrada do Paladino",
                "subtitle": "[Dificuldade: Dificil] Bencaos de luz para combater a escuridao",
                "description": [
                    "A Holy Armor (Paladino) e forjada sob preces e oracoes. Ela repele mortos-vivos com auras luminosas e reduz drasticamente o dano de maldicoes e wither.",
                    "Sua couraca dourada e uma fortaleza contra o mal."
                ],
                "icon": "armoroftheages:holy_armor_chest",
                "x": -11.2, "y": 4.0,
                "tasks": [{"id": "1005000000000171", "type": "item", "item": "armoroftheages:holy_armor_chest", "title": "Forje o Peitoral Sagrado (Holy Armor)"}],
                "rewards": [
                    {"id": "1005000000000172", "type": "item", "item": "minecraft:golden_apple", "count": 2},
                    {"id": "1005000000000173", "type": "xp_levels", "xp_levels": 8}
                ]
            },
            {
                "id": "1005000000000180",
                "dependencies": ["1005000000000160"],
                "title": "A Armadura Samourai O-Yoroi",
                "subtitle": "[Dificuldade: Dificil] A grande armadura pesada do xogunato",
                "description": [
                    "A O-Yoroi e a obra-prima da metalurgia e amarracao feudal japonesa. Placas laqueadas de ferro endurecido resistem a cortes devastadores de bestas colossais.",
                    "A armadura definitiva para quem segue o codigo do Bushido."
                ],
                "icon": "armoroftheages:o_yoroi_armor_chest",
                "x": -8.4, "y": 4.0,
                "tasks": [{"id": "1005000000000181", "type": "item", "item": "armoroftheages:o_yoroi_armor_chest", "title": "Forje a Armadura O-Yoroi"}],
                "rewards": [
                    {"id": "1005000000000182", "type": "item", "item": "minecraft:diamond", "count": 4},
                    {"id": "1005000000000183", "type": "xp_levels", "xp_levels": 8}
                ]
            },
            {
                "id": "1005000000000190",
                "dependencies": ["1005000000000140"],
                "title": "A Armadura Cerimonial de Anubis",
                "subtitle": "[Dificuldade: Dificil] O guardiao dourado do submundo do Nilo",
                "description": [
                    "Inspirada na divindade chacal do antigo Egito, a armadura de Anubis concede resistencia a necroses e melhora o dano de estocada contra alvos amaldicoados.",
                    "Caminhe pelas dunas com a presenca de um deus."
                ],
                "icon": "armoroftheages:anubis_armor_chest",
                "x": -5.6, "y": 4.0,
                "tasks": [{"id": "1005000000000191", "type": "item", "item": "armoroftheages:anubis_armor_chest", "title": "Forje o Peitoral de Anubis"}],
                "rewards": [
                    {"id": "1005000000000192", "type": "item", "item": "minecraft:emerald_block", "count": 2},
                    {"id": "1005000000000193", "type": "xp_levels", "xp_levels": 8}
                ]
            },
            {
                "id": "1005000000000200",
                "dependencies": ["1005000000000140"],
                "title": "A Armadura do Deus do Trovao: Raijin",
                "subtitle": "[Dificuldade: Dificil] O poder dos tambores celestes tempestuosos",
                "description": [
                    "A armadura de Raijin ressoa com eletricidade estatica pura. Cada golpe sofrido descarrega faiscas retaliatorias nos atacantes ao redor.",
                    "Sinta os trovoes obedecerem a sua vontade em meio as tempestades."
                ],
                "icon": "armoroftheages:raijin_armor_chest",
                "x": -2.8, "y": 4.0,
                "tasks": [{"id": "1005000000000201", "type": "item", "item": "armoroftheages:raijin_armor_chest", "title": "Forje a Armadura de Raijin"}],
                "rewards": [
                    {"id": "1005000000000202", "type": "item", "item": "minecraft:lightning_rod", "count": 2},
                    {"id": "1005000000000203", "type": "xp_levels", "xp_levels": 8}
                ]
            },
            {
                "id": "1005000000000210",
                "dependencies": ["1005000000000140"],
                "title": "A Armadura Alada de Quetzalcoatl",
                "subtitle": "[Dificuldade: Dificil] A serpente emplumada dos templos solares",
                "description": [
                    "Inspirada na deidade das civilizacoes mesoamericanas, a Quetzalcoatl Armor reduz gravidade em saltos e confere velocidade espetacular em selvas e montanhas.",
                    "Um tributo a liberdade e ao esplendor do sol."
                ],
                "icon": "armoroftheages:quetzalcoatl_armor_chest",
                "x": 0.0, "y": 4.0,
                "tasks": [{"id": "1005000000000211", "type": "item", "item": "armoroftheages:quetzalcoatl_armor_chest", "title": "Forje a Armadura de Quetzalcoatl"}],
                "rewards": [
                    {"id": "1005000000000212", "type": "item", "item": "minecraft:gold_block", "count": 2},
                    {"id": "1005000000000213", "type": "xp_levels", "xp_levels": 8}
                ]
            },
            {
                "id": "1005000000000220",
                "dependencies": ["1005000000000130"],
                "title": "Lamina Lendaria: Soulpyre",
                "subtitle": "[Dificuldade: Dificil] A pira ardente das almas imortais",
                "description": [
                    "A Soulpyre e uma espada mistica imbuida com fogo espectral azul. Seus golpes incendeiam inimigos com chamas de almas que ignoram parte da armadura fisica.",
                    "Forje ou recupere esta reliquia das cinzas antigas."
                ],
                "icon": "simplyswords:soulpyre",
                "x": 2.8, "y": 4.0,
                "tasks": [{"id": "1005000000000221", "type": "item", "item": "simplyswords:soulpyre", "title": "Obtenha a Lamina Soulpyre"}],
                "rewards": [
                    {"id": "1005000000000222", "type": "item", "item": "minecraft:soul_campfire", "count": 2},
                    {"id": "1005000000000223", "type": "xp_levels", "xp_levels": 9}
                ]
            },
            {
                "id": "1005000000000230",
                "dependencies": ["1005000000000130"],
                "title": "Lamina Lendaria: Stormbringer",
                "subtitle": "[Dificuldade: Dificil] O arauto das tempestades e vendavais",
                "description": [
                    "A Stormbringer canaliza correntes atmosfericas para disparar laminas de vacuo a cada varredura de combate, acertando alvos distantes sem gasto de flechas.",
                    "O poder do tufao ao alcance dos seus punhos."
                ],
                "icon": "simplyswords:stormbringer",
                "x": 5.6, "y": 4.0,
                "tasks": [{"id": "1005000000000231", "type": "item", "item": "simplyswords:stormbringer", "title": "Obtenha a Lamina Stormbringer"}],
                "rewards": [
                    {"id": "1005000000000232", "type": "item", "item": "minecraft:prismarine_shard", "count": 16},
                    {"id": "1005000000000233", "type": "xp_levels", "xp_levels": 9}
                ]
            },
            {
                "id": "1005000000000240",
                "dependencies": ["1005000000000130"],
                "title": "Lamina Lendaria: Frostfall",
                "subtitle": "[Dificuldade: Dificil] O sopro polar que petrifica os mares",
                "description": [
                    "Frostfall congela instantaneamente a agua sob os pes do guerreiro e envolve os inimigos em casulos de gelo comprimido.",
                    "Ideal para anular chefes velozes que tentam flanquear sua posicao."
                ],
                "icon": "simplyswords:frostfall",
                "x": 8.4, "y": 4.0,
                "tasks": [{"id": "1005000000000241", "type": "item", "item": "simplyswords:frostfall", "title": "Obtenha a Lamina Frostfall"}],
                "rewards": [
                    {"id": "1005000000000242", "type": "item", "item": "minecraft:blue_ice", "count": 8},
                    {"id": "1005000000000243", "type": "xp_levels", "xp_levels": 9}
                ]
            },
            {
                "id": "1005000000000250",
                "dependencies": ["1005000000000130"],
                "title": "Lamina Lendaria: Sunfire",
                "subtitle": "[Dificuldade: Dificil] A radiacao solar que purifica corrupcoes",
                "description": [
                    "Sunfire e a contraparte da luz celestial. Ela cega momentaneamente oponentes com flashes solares no inicio dos golpes criticos.",
                    "Uma dadiva majestosa para qualquer explorador das trevas."
                ],
                "icon": "simplyswords:sunfire",
                "x": 11.2, "y": 4.0,
                "tasks": [{"id": "1005000000000251", "type": "item", "item": "simplyswords:sunfire", "title": "Obtenha a Lamina Sunfire"}],
                "rewards": [
                    {"id": "1005000000000252", "type": "item", "item": "minecraft:glowstone", "count": 32},
                    {"id": "1005000000000253", "type": "xp_levels", "xp_levels": 9}
                ]
            },

            # TIER EXTREMA (4 Quests, y = 7.5d)
            {
                "id": "1005000000000260",
                "dependencies": ["1005000000000220"],
                "title": "Lamina Lendaria: Twisted Blade",
                "subtitle": "[Dificuldade: Extrema] A distorcao da realidade espiralada",
                "description": [
                    "A Twisted Blade distorce o tecido do espaco, puxando os inimigos mais distantes para o raio de impacto imediato da sua espada.",
                    "Nenhum arqueiro ou feiticeiro escapa do seu raio de gravidade."
                ],
                "icon": "simplyswords:twisted_blade",
                "x": -4.2, "y": 7.5,
                "tasks": [{"id": "1005000000000261", "type": "item", "item": "simplyswords:twisted_blade", "title": "Domine a Twisted Blade"}],
                "rewards": [
                    {"id": "1005000000000262", "type": "item", "item": "minecraft:ender_eye", "count": 4},
                    {"id": "1005000000000263", "type": "xp_levels", "xp_levels": 10}
                ]
            },
            {
                "id": "1005000000000270",
                "dependencies": ["1005000000000220"],
                "title": "Lamina Lendaria: Soulstealer",
                "subtitle": "[Dificuldade: Extrema] O vampirismo das forcas vitais",
                "description": [
                    "A temida Soulstealer consome as almas dos inimigos abatidos, restaurando diretamente a vida e a saciedade do seu portador a cada golpe fatal.",
                    "Com ela em maos, voce e praticamente imortal diante de hordas infinitas."
                ],
                "icon": "simplyswords:soulstealer",
                "x": -1.4, "y": 7.5,
                "tasks": [{"id": "1005000000000271", "type": "item", "item": "simplyswords:soulstealer", "title": "Domine a Soulstealer"}],
                "rewards": [
                    {"id": "1005000000000272", "type": "item", "item": "minecraft:wither_skeleton_skull", "count": 2},
                    {"id": "1005000000000273", "type": "xp_levels", "xp_levels": 12}
                ]
            },
            {
                "id": "1005000000000280",
                "dependencies": ["1005000000000230"],
                "title": "Lamina Lendaria: Arcanethyst",
                "subtitle": "[Dificuldade: Extrema] A ressonancia dos cristais arcanos",
                "description": [
                    "Forjada a partir de geodes de ametista pura sob pressoes colossais, a Arcanethyst emite pulsos sonoros que atordoam e quebram armaduras de chefes antigos.",
                    "A harmonia perfeita entre geologia e magia marcial."
                ],
                "icon": "simplyswords:arcanethyst",
                "x": 1.4, "y": 7.5,
                "tasks": [{"id": "1005000000000281", "type": "item", "item": "simplyswords:arcanethyst", "title": "Domine a Arcanethyst"}],
                "rewards": [
                    {"id": "1005000000000282", "type": "item", "item": "minecraft:amethyst_block", "count": 8},
                    {"id": "1005000000000283", "type": "xp_levels", "xp_levels": 12}
                ]
            },
            {
                "id": "1005000000000290",
                "dependencies": ["1005000000000230"],
                "title": "Lamina Lendaria: Thunderbrand",
                "subtitle": "[Dificuldade: Extrema] O relampago personificado em aco mistico",
                "description": [
                    "A lendaria Thunderbrand convoca raios celestiais reais sobre o alvo durante combates ao ar livre. Sob ceus de chuva, seu poder e simplesmente catastrofico!",
                    "Voce alcancou a maestria suprema sobre o Arsenal Lendario do BlessForge."
                ],
                "icon": "simplyswords:thunderbrand",
                "shape": "diamond",
                "size": 1.5,
                "x": 4.2, "y": 7.5,
                "tasks": [{"id": "1005000000000291", "type": "item", "item": "simplyswords:thunderbrand", "title": "Domine a Thunderbrand"}],
                "rewards": [
                    {"id": "1005000000000292", "type": "item", "item": "minecraft:nether_star", "count": 1},
                    {"id": "1005000000000293", "type": "xp_levels", "xp_levels": 15}
                ]
            }
        ]
    }

# =====================================================================
# CAPÍTULO 6: O FIM DOS TITÃS (30 QUESTS)
# =====================================================================
def get_cataclysm_data():
    return {
        "filename": "capitulo_6_cataclysm",
        "group": "1A2B3C4D5E6F7001",
        "id": "1006000000000001",
        "order_index": 6,
        "title": "6. O Fim dos Titas (L_Ender's Cataclysm)",
        "icon": "cataclysm:monstrous_horn",
        "quests": [
            # TIER FACIL (7 Quests, y = -3.0d)
            {
                "id": "1006000000000010",
                "title": "Ecos de Eras Esquecidas",
                "subtitle": "[Dificuldade: Facil] Os vestigios arqueologicos dos antigos cataclismos",
                "description": [
                    "O mundo em que voce pisa e o resultado de cataclismos colossais travados milenios antes da sua chegada.",
                    "Monumentos submersos, forjas soterradas na lava e templos sob as dunas escondem sentinelas adormecidas.",
                    "Antes de enfrentar essas forcas titanicas, e crucial comecar pela arqueologia calma: estudar materiais, provar alimentos das profundezas e preparar seu corpo com cautela."
                ],
                "icon": "minecraft:ancient_debris",
                "shape": "hexagon",
                "size": 1.5,
                "x": -8.4, "y": -3.0,
                "tasks": [{"id": "1006000000000011", "type": "checkmark", "title": "Estude a Historia dos Titas"}],
                "rewards": [
                    {"id": "1006000000000012", "type": "item", "item": "minecraft:golden_apple", "count": 2},
                    {"id": "1006000000000013", "type": "xp_levels", "xp_levels": 3}
                ]
            },
            {
                "id": "1006000000000020",
                "dependencies": ["1006000000000010"],
                "title": "Carne de Caranguejo de Ametista",
                "subtitle": "[Dificuldade: Facil] Nutricao hiperenergetica das praias e fendas",
                "description": [
                    "Nas praias e proximidades de geodos litoraneos habitam os Amethyst Crabs. Sua carne e suculenta e fornece saturacao prolongada.",
                    "Cozinhe a carne de caranguejo para manter sua stamina estavel durante longas caminhadas arqueologicas."
                ],
                "icon": "cataclysm:amethyst_crab_meat",
                "x": -5.6, "y": -3.0,
                "tasks": [{"id": "1006000000000021", "type": "item", "item": "cataclysm:amethyst_crab_meat", "count": 4, "title": "Obtenha Carne de Amethyst Crab"}],
                "rewards": [
                    {"id": "1006000000000022", "type": "item", "item": "cataclysm:blessed_amethyst_crab_meat", "count": 2},
                    {"id": "1006000000000023", "type": "xp", "xp": 100}
                ]
            },
            {
                "id": "1006000000000030",
                "dependencies": ["1006000000000020"],
                "title": "A Carapaca do Caranguejo de Ametista",
                "subtitle": "[Dificuldade: Facil] Placas quitinosas para reforco inicial",
                "description": [
                    "A carapaca dura desses crustaceos combina cristais de quartzo e minerais marinhos. Ela serve como base para reparos preliminares e forja de acessorios defensivos.",
                    "Colete carapacas para estudar a resistencia dos materiais do Cataclysm."
                ],
                "icon": "cataclysm:amethyst_crab_shell",
                "x": -2.8, "y": -3.0,
                "tasks": [{"id": "1006000000000031", "type": "item", "item": "cataclysm:amethyst_crab_shell", "count": 2, "title": "Colete Carapacas de Caranguejo"}],
                "rewards": [
                    {"id": "1006000000000032", "type": "item", "item": "minecraft:amethyst_shard", "count": 8},
                    {"id": "1006000000000033", "type": "xp", "xp": 120}
                ]
            },
            {
                "id": "1006000000000040",
                "dependencies": ["1006000000000010"],
                "title": "Pedacos de Coral dos Oceanos",
                "subtitle": "[Dificuldade: Facil] Minerais biologicos das cidades submersas",
                "description": [
                    "Nos recifes proximos a Sunken City repousam blocos de Coral Chunks. Eles sao ricos em calcario endurecido sob pressao abissal.",
                    "Recolha fragmentos de coral para sintetizar compostos de endurecimento de escudos."
                ],
                "icon": "cataclysm:coral_chunk",
                "x": 0.0, "y": -3.0,
                "tasks": [{"id": "1006000000000041", "type": "item", "item": "cataclysm:coral_chunk", "count": 4, "title": "Colete Coral Chunks"}],
                "rewards": [
                    {"id": "1006000000000042", "type": "item", "item": "minecraft:prismarine_crystals", "count": 8},
                    {"id": "1006000000000043", "type": "xp", "xp": 120}
                ]
            },
            {
                "id": "1006000000000050",
                "dependencies": ["1006000000000030"],
                "title": "O Cinto do Iniciante (Belt of Beginner)",
                "subtitle": "[Dificuldade: Facil] Acessorios ergonomicos para amortecer impactos",
                "description": [
                    "O Belt of Beginner e um acessorio criado especificamente para viajantes prudentes. Ele absorve trancos de quedas e distribui o peso da sua armadura com suavidade.",
                    "Equipe-o no seu slot Curios para explorar as ruinas com seguranca."
                ],
                "icon": "cataclysm:belt_of_beginner",
                "x": 2.8, "y": -3.0,
                "tasks": [{"id": "1006000000000051", "type": "item", "item": "cataclysm:belt_of_beginner", "title": "Adquira o Belt of Beginner"}],
                "rewards": [
                    {"id": "1006000000000052", "type": "item", "item": "minecraft:leather", "count": 8},
                    {"id": "1006000000000053", "type": "xp_levels", "xp_levels": 3}
                ]
            },
            {
                "id": "1006000000000060",
                "dependencies": ["1006000000000040"],
                "title": "Peixe-Leao do Abismo Oceanico",
                "subtitle": "[Dificuldade: Facil] Ictiologia das fossas abissais",
                "description": [
                    "O Lionfish nada tranquilamente ao redor das colunas de Azure Seastone. Embora seus espinhos exijam cuidado, ele e vital para elixires de visao noturna e respiracao aquatica.",
                    "Pesque ou capture um exemplar para suas analises alquimicas."
                ],
                "icon": "cataclysm:lionfish",
                "x": 5.6, "y": -3.0,
                "tasks": [{"id": "1006000000000061", "type": "item", "item": "cataclysm:lionfish", "title": "Capture um Peixe-Leao"}],
                "rewards": [
                    {"id": "1006000000000062", "type": "item", "item": "minecraft:pufferfish", "count": 2},
                    {"id": "1006000000000063", "type": "xp", "xp": 150}
                ]
            },
            {
                "id": "1006000000000070",
                "dependencies": ["1006000000000050"],
                "title": "O Aco Negro dos Antigos",
                "subtitle": "[Dificuldade: Facil] A liga metalica que sustentou civilizacoes perdidas",
                "description": [
                    "O Black Steel e o metal estrutural do Cataclysm. Ele e denso, negro como a noite e infinitamente superior ao ferro comum.",
                    "Colete ou forje lingotes de Black Steel para dar inicio ao seu arsenal resistente a impactos titanicos."
                ],
                "icon": "cataclysm:black_steel_ingot",
                "x": 8.4, "y": -3.0,
                "tasks": [{"id": "1006000000000071", "type": "item", "item": "cataclysm:black_steel_ingot", "count": 4, "title": "Forje Lingotes de Black Steel"}],
                "rewards": [
                    {"id": "1006000000000072", "type": "item", "item": "cataclysm:black_steel_ingot", "count": 4},
                    {"id": "1006000000000073", "type": "xp_levels", "xp_levels": 4}
                ]
            },

            # TIER MEDIA (7 Quests, y = 0.5d)
            {
                "id": "1006000000000080",
                "dependencies": ["1006000000000070"],
                "title": "A Picareta de Aco Negro",
                "subtitle": "[Dificuldade: Media] Minando as rochas endurecidas das catacumbas",
                "description": [
                    "A Black Steel Pickaxe possui durabilidade extraordinaria e velocidade de mineracao capaz de furar as muralhas das cidadelas ancestrais sem sofrer desgaste subito.",
                    "Sua melhor companheira para escavacoes profundas."
                ],
                "icon": "cataclysm:black_steel_pickaxe",
                "x": -8.4, "y": 0.5,
                "tasks": [{"id": "1006000000000081", "type": "item", "item": "cataclysm:black_steel_pickaxe", "title": "Forje a Picareta de Black Steel"}],
                "rewards": [
                    {"id": "1006000000000082", "type": "item", "item": "minecraft:diamond", "count": 3},
                    {"id": "1006000000000083", "type": "xp_levels", "xp_levels": 5}
                ]
            },
            {
                "id": "1006000000000090",
                "dependencies": ["1006000000000070"],
                "title": "A Espada de Aco Negro",
                "subtitle": "[Dificuldade: Media] Corte denso contra monstros couraçados",
                "description": [
                    "A Black Steel Sword golpeia com a massa inercial de um martelo e a afiacao de uma navalha. Essencial para perfurar carapacas de Deeplings e Koboletons.",
                    "Prepare sua espada antes de invadir as primeiras câmaras."
                ],
                "icon": "cataclysm:black_steel_sword",
                "x": -5.6, "y": 0.5,
                "tasks": [{"id": "1006000000000091", "type": "item", "item": "cataclysm:black_steel_sword", "title": "Forje a Espada de Black Steel"}],
                "rewards": [
                    {"id": "1006000000000092", "type": "item", "item": "minecraft:iron_block", "count": 1},
                    {"id": "1006000000000093", "type": "xp_levels", "xp_levels": 5}
                ]
            },
            {
                "id": "1006000000000100",
                "dependencies": ["1006000000000070"],
                "title": "O Escudo Targe de Aco Negro",
                "subtitle": "[Dificuldade: Media] Parrying e bloqueio de ondas de choque",
                "description": [
                    "O Black Steel Targe e um escudo circular balanceado que permite aparar ataques fisicos com precisao milimetrica, desestabilizando atacantes.",
                    "Treine seu tempo de bloqueio contra ataques pesados."
                ],
                "icon": "cataclysm:black_steel_targe",
                "x": -2.8, "y": 0.5,
                "tasks": [{"id": "1006000000000101", "type": "item", "item": "cataclysm:black_steel_targe", "title": "Forje o Escudo Targe de Black Steel"}],
                "rewards": [
                    {"id": "1006000000000102", "type": "item", "item": "minecraft:golden_apple", "count": 2},
                    {"id": "1006000000000103", "type": "xp_levels", "xp_levels": 5}
                ]
            },
            {
                "id": "1006000000000110",
                "dependencies": ["1006000000000040"],
                "title": "Fragmentos de Coral Cristalizado",
                "subtitle": "[Dificuldade: Media] As formacoes brilhantes da Sunken City",
                "description": [
                    "Nas profundezas da Sunken City, o coral sofreu cristalizacao piezoeletrica, gerando os Crystallized Coral Fragments.",
                    "Eles sao a fonte primordial para confeccionar arpoes e armaduras do oceano profundo."
                ],
                "icon": "cataclysm:crystallized_coral_fragments",
                "x": 0.0, "y": 0.5,
                "tasks": [{"id": "1006000000000111", "type": "item", "item": "cataclysm:crystallized_coral_fragments", "count": 6, "title": "Colete Fragmentos de Coral Cristalizado"}],
                "rewards": [
                    {"id": "1006000000000112", "type": "item", "item": "cataclysm:crystallized_coral_fragments", "count": 6},
                    {"id": "1006000000000113", "type": "xp_levels", "xp_levels": 6}
                ]
            },
            {
                "id": "1006000000000120",
                "dependencies": ["1006000000000010"],
                "title": "Tempestade de Areia Engarrafada",
                "subtitle": "[Dificuldade: Media] O turbilhao das piramides e templos do deserto",
                "description": [
                    "A Sandstorm In A Bottle aprisiona um redemoinho eterno do deserto. Ao ser aberta em salto, impulsiona o aventureiro a grandes alturas com um duplo salto de vento!",
                    "Mobilidade vertical perfeita para explorar ruinas elevadas."
                ],
                "icon": "cataclysm:sandstorm_in_a_bottle",
                "x": 2.8, "y": 0.5,
                "tasks": [{"id": "1006000000000121", "type": "item", "item": "cataclysm:sandstorm_in_a_bottle", "title": "Encontre a Tempestade em Garrafa"}],
                "rewards": [
                    {"id": "1006000000000122", "type": "item", "item": "minecraft:sand", "count": 32},
                    {"id": "1006000000000123", "type": "xp_levels", "xp_levels": 6}
                ]
            },
            {
                "id": "1006000000000130",
                "dependencies": ["1006000000000050"],
                "title": "Botas Resistentes das Profundezas",
                "subtitle": "[Dificuldade: Media] Sturdy Boots e a ancoragem no solo",
                "description": [
                    "As Sturdy Boots possuem sola pesada magnetizada que impede que ondas de choque ou golpes colossais arremessem voce contra paredes ou abismos.",
                    "Essenciais para enfrentar gigantes que produzem tremores de terra."
                ],
                "icon": "cataclysm:sturdy_boots",
                "x": 5.6, "y": 0.5,
                "tasks": [{"id": "1006000000000131", "type": "item", "item": "cataclysm:sturdy_boots", "title": "Equipe as Sturdy Boots"}],
                "rewards": [
                    {"id": "1006000000000132", "type": "item", "item": "minecraft:iron_ingot", "count": 6},
                    {"id": "1006000000000133", "type": "xp_levels", "xp_levels": 6}
                ]
            },
            {
                "id": "1006000000000140",
                "dependencies": ["1006000000000050"],
                "title": "Luvas Aderentes dos Exploradores",
                "subtitle": "[Dificuldade: Media] Sticky Gloves e a escalada de monumentos",
                "description": [
                    "As Sticky Gloves permitem subir e se dependurar nas cornijas das masmorras monumentais sem precisar empilhar terra ou blocos deselegantes.",
                    "Suba com agilidade natural para flanquear sentinelas."
                ],
                "icon": "cataclysm:sticky_gloves",
                "x": 8.4, "y": 0.5,
                "tasks": [{"id": "1006000000000141", "type": "item", "item": "cataclysm:sticky_gloves", "title": "Equipe as Sticky Gloves"}],
                "rewards": [
                    {"id": "1006000000000142", "type": "item", "item": "minecraft:slime_ball", "count": 8},
                    {"id": "1006000000000143", "type": "xp_levels", "xp_levels": 6}
                ]
            },

            # TIER DIFICIL (8 Quests, y = 4.0d)
            {
                "id": "1006000000000150",
                "dependencies": ["1006000000000080"],
                "title": "A Chave Misteriosa dos Santuarios",
                "subtitle": "[Dificuldade: Dificil] Strange Key e os portais selados",
                "description": [
                    "A Strange Key e um mecanismo esculpido com runas de pedra estelar. Ela destranca as portas de selo das masmorras onde os titas hibernam.",
                    "Localize uma chave inspecionando baus de sentinelas de elite."
                ],
                "icon": "cataclysm:strange_key",
                "x": -9.8, "y": 4.0,
                "tasks": [{"id": "1006000000000151", "type": "item", "item": "cataclysm:strange_key", "title": "Obtenha a Strange Key"}],
                "rewards": [
                    {"id": "1006000000000152", "type": "item", "item": "minecraft:diamond", "count": 4},
                    {"id": "1006000000000153", "type": "xp_levels", "xp_levels": 7}
                ]
            },
            {
                "id": "1006000000000160",
                "dependencies": ["1006000000000120"],
                "title": "O Colar do Deserto Ancestral",
                "subtitle": "[Dificuldade: Dificil] Protecao calorica contra as areias causticantes",
                "description": [
                    "O Necklace of the Desert e uma joia cerimonial encontrada nas profundezas das piramides amaldicoadas. Ele dissipa efeitos de queima e reduz a sede do calor.",
                    "Um amuleto essencial antes de invadir a arena do Ancient Remnant."
                ],
                "icon": "cataclysm:necklace_of_the_desert",
                "x": -7.0, "y": 4.0,
                "tasks": [{"id": "1006000000000161", "type": "item", "item": "cataclysm:necklace_of_the_desert", "title": "Recupere o Colar do Deserto"}],
                "rewards": [
                    {"id": "1006000000000162", "type": "item", "item": "minecraft:gold_block", "count": 2},
                    {"id": "1006000000000163", "type": "xp_levels", "xp_levels": 8}
                ]
            },
            {
                "id": "1006000000000170",
                "dependencies": ["1006000000000150"],
                "title": "O Olho das Chamas Ardentes",
                "subtitle": "[Dificuldade: Dificil] Flame Eye: O radar da Fortaleza Ardente do Nether",
                "description": [
                    "O Flame Eye pulsa em direcao as muralhas de basalto negro da Burning Arena no Nether, onde Ignis guarda sua corte de fogo.",
                    "Siga a trajetoria do olho para localizar o santuario sem errar caminhos no submundo."
                ],
                "icon": "cataclysm:flame_eye",
                "x": -4.2, "y": 4.0,
                "tasks": [{"id": "1006000000000171", "type": "item", "item": "cataclysm:flame_eye", "title": "Forje ou Encontre o Flame Eye"}],
                "rewards": [
                    {"id": "1006000000000172", "type": "item", "item": "minecraft:blaze_rod", "count": 8},
                    {"id": "1006000000000173", "type": "xp_levels", "xp_levels": 8}
                ]
            },
            {
                "id": "1006000000000180",
                "dependencies": ["1006000000000150"],
                "title": "O Olho das Profundezas Abissais",
                "subtitle": "[Dificuldade: Dificil] Abyss Eye: A bussola da Sunken City",
                "description": [
                    "O Abyss Eye detecta a pressao barometrica e aponta diretamente para a fosso central da Sunken City, covil do Leviathan.",
                    "Prepare elixires de respiracao aquatica e guie-se atraves das profundezas oceanicas."
                ],
                "icon": "cataclysm:abyss_eye",
                "x": -1.4, "y": 4.0,
                "tasks": [{"id": "1006000000000181", "type": "item", "item": "cataclysm:abyss_eye", "title": "Forje ou Encontre o Abyss Eye"}],
                "rewards": [
                    {"id": "1006000000000182", "type": "item", "item": "minecraft:prismarine", "count": 16},
                    {"id": "1006000000000183", "type": "xp_levels", "xp_levels": 8}
                ]
            },
            {
                "id": "1006000000000190",
                "dependencies": ["1006000000000150"],
                "title": "O Olho Mecanico da Cidadela",
                "subtitle": "[Dificuldade: Dificil] Mech Eye: Rastreando a Fabrica Esquecida",
                "description": [
                    "O Mech Eye emite pulsos de ondas eletromagneticas que sintonizam a frequencia da Fabrica Antiga soterrada, morada de The Harbinger.",
                    "Siga o zumbido mecânico para descobrir o complexo subterraneo."
                ],
                "icon": "cataclysm:mech_eye",
                "x": 1.4, "y": 4.0,
                "tasks": [{"id": "1006000000000191", "type": "item", "item": "cataclysm:mech_eye", "title": "Forje ou Encontre o Mech Eye"}],
                "rewards": [
                    {"id": "1006000000000192", "type": "item", "item": "minecraft:redstone_block", "count": 4},
                    {"id": "1006000000000193", "type": "xp_levels", "xp_levels": 8}
                ]
            },
            {
                "id": "1006000000000200",
                "dependencies": ["1006000000000150"],
                "title": "O Olho Monstruoso do Subsolo",
                "subtitle": "[Dificuldade: Dificil] Monstrous Eye: O coracao de Netherite petrificado",
                "description": [
                    "O Monstrous Eye pulsa com a batida cardiaca pesada da Netherite Monstrosity. Ele indica a forja vulcanica soterrada no Nether onde ela repousa.",
                    "Aproxime-se apenas quando estiver munido de pocoes de resistencia maxima a fogo."
                ],
                "icon": "cataclysm:monstrous_eye",
                "x": 4.2, "y": 4.0,
                "tasks": [{"id": "1006000000000201", "type": "item", "item": "cataclysm:monstrous_eye", "title": "Forje ou Encontre o Monstrous Eye"}],
                "rewards": [
                    {"id": "1006000000000202", "type": "item", "item": "minecraft:netherrack", "count": 64},
                    {"id": "1006000000000203", "type": "xp_levels", "xp_levels": 8}
                ]
            },
            {
                "id": "1006000000000210",
                "dependencies": ["1006000000000150"],
                "title": "O Olho do Deserto Antigo",
                "subtitle": "[Dificuldade: Dificil] Desert Eye: A tumba esquecida do Ancient Remnant",
                "description": [
                    "O Desert Eye gira com magnetismo de areia, indicando a piramide colossal enterrada sob as tempestades do deserto.",
                    "La dentro aguardam mumias, armadilhas de queda e a sentinela fóssil."
                ],
                "icon": "cataclysm:desert_eye",
                "x": 7.0, "y": 4.0,
                "tasks": [{"id": "1006000000000211", "type": "item", "item": "cataclysm:desert_eye", "title": "Forje ou Encontre o Desert Eye"}],
                "rewards": [
                    {"id": "1006000000000212", "type": "item", "item": "minecraft:chiseled_sandstone", "count": 16},
                    {"id": "1006000000000213", "type": "xp_levels", "xp_levels": 8}
                ]
            },
            {
                "id": "1006000000000220",
                "dependencies": ["1006000000000150"],
                "title": "O Olho do Vazio Cosmico",
                "subtitle": "[Dificuldade: Dificil] Void Eye: Rumo a Cidadela Flutuante do The End",
                "description": [
                    "Nas ilhas remotas do End ergue-se a Ruined Citadel, guardada pelo Ender Guardian. O Void Eye indica a rota espacial atraves das ilhas do vazio.",
                    "Leve foguetes, asas de elitra ou blocos suficientes para a travessia."
                ],
                "icon": "cataclysm:void_eye",
                "x": 9.8, "y": 4.0,
                "tasks": [{"id": "1006000000000221", "type": "item", "item": "cataclysm:void_eye", "title": "Forje ou Encontre o Void Eye"}],
                "rewards": [
                    {"id": "1006000000000222", "type": "item", "item": "minecraft:ender_pearl", "count": 16},
                    {"id": "1006000000000223", "type": "xp_levels", "xp_levels": 9}
                ]
            },

            # TIER EXTREMA (8 Quests, y = 7.5d)
            {
                "id": "1006000000000230",
                "dependencies": ["1006000000000200"],
                "title": "A Monstruosidade de Netherite",
                "subtitle": "[Dificuldade: Extrema] O colosso de metal fundido do Soul Blacksmith",
                "description": [
                    "A Netherite Monstrosity empunha um martelo que pulveriza rochas e descarrega ondas de choque de magma no solo.",
                    "Atraia a besta para areas abertas e desvie dos disparos de lava antes de castiga-la com golpes criticos!"
                ],
                "icon": "cataclysm:monstrous_horn",
                "shape": "hexagon",
                "size": 1.4,
                "x": -9.8, "y": 7.5,
                "tasks": [{"id": "1006000000000231", "type": "item", "item": "cataclysm:monstrous_horn", "title": "Obtenha o Monstrous Horn"}],
                "rewards": [
                    {"id": "1006000000000232", "type": "item", "item": "minecraft:netherite_ingot", "count": 2},
                    {"id": "1006000000000233", "type": "xp_levels", "xp_levels": 12}
                ]
            },
            {
                "id": "1006000000000240",
                "dependencies": ["1006000000000230"],
                "title": "A Forja Infernal Desperta",
                "subtitle": "[Dificuldade: Extrema] O martelo monumental de impacto vulcanico",
                "description": [
                    "Com o chifre da monstruosidade forja-se a Infernal Forge. Cada golpe no chao levanta pedras incandescentes que esmagam grupos de inimigos com fisica realista!",
                    "Uma das armas pesadas mais iconicas de toda a historia dos mods."
                ],
                "icon": "cataclysm:infernal_forge",
                "x": -7.0, "y": 7.5,
                "tasks": [{"id": "1006000000000241", "type": "item", "item": "cataclysm:infernal_forge", "title": "Forje a Infernal Forge"}],
                "rewards": [
                    {"id": "1006000000000242", "type": "item", "item": "minecraft:netherite_block", "count": 1},
                    {"id": "1006000000000243", "type": "xp_levels", "xp_levels": 12}
                ]
            },
            {
                "id": "1006000000000250",
                "dependencies": ["1006000000000170"],
                "title": "Ignis: O Cavaleiro do Fogo Eterno",
                "subtitle": "[Dificuldade: Extrema] O duelista supremo da Burning Arena",
                "description": [
                    "Ignis e um mestre da esgrima flamejante. Suas investidas aereas desenham arcos incandescentes e ele desvia de flechas com facilidade desconcertante.",
                    "Encare-o em combate corpo a corpo com escudo resistente e tempos de aparo perfeitos."
                ],
                "icon": "cataclysm:burning_ashes",
                "shape": "hexagon",
                "size": 1.4,
                "x": -4.2, "y": 7.5,
                "tasks": [{"id": "1006000000000251", "type": "item", "item": "cataclysm:burning_ashes", "title": "Obtenha as Cinzas Ardentes de Ignis"}],
                "rewards": [
                    {"id": "1006000000000252", "type": "item", "item": "minecraft:netherite_ingot", "count": 2},
                    {"id": "1006000000000253", "type": "xp_levels", "xp_levels": 12}
                ]
            },
            {
                "id": "1006000000000260",
                "dependencies": ["1006000000000250"],
                "title": "A Lamina Devastadora: Incinerator",
                "subtitle": "[Dificuldade: Extrema] A grande espada forjada no fogo sagrado",
                "description": [
                    "A espada empunhada por Ignis agora e sua. A Incinerator projeta ondas de calor que cortam armaduras e incineram tudo a sua frente com elegancia mortal.",
                    "O trofeu supremo dos duelos do submundo."
                ],
                "icon": "cataclysm:the_incinerator",
                "x": -1.4, "y": 7.5,
                "tasks": [{"id": "1006000000000261", "type": "item", "item": "cataclysm:the_incinerator", "title": "Empunhe The Incinerator"}],
                "rewards": [
                    {"id": "1006000000000262", "type": "item", "item": "minecraft:blaze_rod", "count": 16},
                    {"id": "1006000000000263", "type": "xp_levels", "xp_levels": 12}
                ]
            },
            {
                "id": "1006000000000270",
                "dependencies": ["1006000000000190"],
                "title": "The Harbinger: A Calamidade Mecanica",
                "subtitle": "[Dificuldade: Extrema] O guardiao cibernetico da Fabrica Perdida",
                "description": [
                    "O Harbinger dispara misseis teleguiados, rajadas de laser mortais e ondas eletromagneticas que desestabilizam escudos.",
                    "Use pilares e a arquitetura da fábrica como cobertura para desviar dos lasers antes de engajar no ataque."
                ],
                "icon": "cataclysm:emp",
                "shape": "hexagon",
                "size": 1.4,
                "x": 1.4, "y": 7.5,
                "tasks": [{"id": "1006000000000271", "type": "item", "item": "cataclysm:emp", "title": "Obtenha o Nucleo EMP do Harbinger"}],
                "rewards": [
                    {"id": "1006000000000272", "type": "item", "item": "minecraft:netherite_scrap", "count": 4},
                    {"id": "1006000000000273", "type": "xp_levels", "xp_levels": 12}
                ]
            },
            {
                "id": "1006000000000280",
                "dependencies": ["1006000000000180"],
                "title": "The Leviathan: O Terror do Abismo",
                "subtitle": "[Dificuldade: Extrema] O senhor das profundezas da Sunken City",
                "description": [
                    "O colossal Leviathan nada em circulos ao redor do altar abissal. Quando ele ruge, ondas gravitacionais sugam o jogador em direcao a sua bocarra gigante!",
                    "Nade com velocidade usando nadadeiras ou tridente para atingir seus pontos fracos nas costas."
                ],
                "icon": "cataclysm:abyssal_sacrifice",
                "shape": "hexagon",
                "size": 1.4,
                "x": 4.2, "y": 7.5,
                "tasks": [{"id": "1006000000000281", "type": "item", "item": "cataclysm:abyssal_sacrifice", "title": "Conquiste o Tributo do Abismo"}],
                "rewards": [
                    {"id": "1006000000000282", "type": "item", "item": "minecraft:heart_of_the_sea", "count": 1},
                    {"id": "1006000000000283", "type": "xp_levels", "xp_levels": 15}
                ]
            },
            {
                "id": "1006000000000290",
                "dependencies": ["1006000000000210"],
                "title": "Maledictus: A Maldicao Espectral",
                "subtitle": "[Dificuldade: Extrema] O fantasma amaldicoado dos templos sombrios",
                "description": [
                    "Maledictus vagueia pelas catacumbas invocando espectros e prendendo a alma do jogador em correntes de sombras que restringem o movimento.",
                    "Quebre as correntes com ataques fisicos rapidos para manter-se livre e triunfar!"
                ],
                "icon": "cataclysm:cursed_tombstone",
                "shape": "hexagon",
                "size": 1.4,
                "x": 7.0, "y": 7.5,
                "tasks": [{"id": "1006000000000291", "type": "item", "item": "cataclysm:cursed_tombstone", "title": "Obtenha a Lapide Amaldicoada"}],
                "rewards": [
                    {"id": "1006000000000292", "type": "item", "item": "minecraft:echo_shard", "count": 4},
                    {"id": "1006000000000293", "type": "xp_levels", "xp_levels": 12}
                ]
            },
            {
                "id": "1006000000000300",
                "dependencies": ["1006000000000220", "1006000000000240", "1006000000000260", "1006000000000270", "1006000000000280"],
                "title": "O Guardiao do Fim: Ender Guardian",
                "subtitle": "[Dificuldade: Extrema] A sentinela suprema do vazio cosmico",
                "description": [
                    "No topo da Ruined Citadel aguarda o mais formidavel dos titas: o Ender Guardian. Ele manipula a gravidade, abre fendas no espaco e desfere socos que quebram o proprio ar!",
                    "Ao derrota-lo, voce encerra a era dos titas e se consagra como a lenda viva absoluta do Mundo Eterno!"
                ],
                "icon": "cataclysm:void_core",
                "shape": "diamond",
                "size": 1.6,
                "x": 9.8, "y": 7.5,
                "tasks": [{"id": "1006000000000301", "type": "item", "item": "cataclysm:void_core", "title": "Conquiste o Void Core do Ender Guardian"}],
                "rewards": [
                    {"id": "1006000000000302", "type": "item", "item": "minecraft:nether_star", "count": 2},
                    {"id": "1006000000000303", "type": "xp_levels", "xp_levels": 20}
                ]
            }
        ]
    }

# =====================================================================
# EXECUÇÃO PRINCIPAL
# =====================================================================
def main():
    chapters = [
        get_twilight_data(),
        get_bumblezone_data(),
        get_arsenal_data(),
        get_cataclysm_data()
    ]
    
    total_quests = 0
    print("=== EXPANDINDO CAPÍTULOS 3, 4, 5 E 6 COM TIER FÁCIL E ESPAÇAMENTO AMPLO ===")
    
    for ch in chapters:
        validate_layout(ch)
        snbt_text = format_snbt(ch)
        
        # Verificacao de seguranca contra &
        if '&' in snbt_text:
            raise ValueError(f"FALHA GRAVE: '&' encontrado no capitulo {ch['filename']}")
        
        total_quests += len(ch["quests"])
        
        for dest in DEST_DIRS:
            os.makedirs(dest, exist_ok=True)
            path = os.path.join(dest, f"{ch['filename']}.snbt")
            with open(path, "w", encoding="utf-8") as f:
                f.write(snbt_text)
            print(f"Salvo: {path}")

    print(f"\nSUCESSO! 4 capitulos gerados e validados perfeitamente.")
    print(f"Total de quests adicionadas nos capitulos 3, 4, 5 e 6: {total_quests}")

if __name__ == "__main__":
    main()
