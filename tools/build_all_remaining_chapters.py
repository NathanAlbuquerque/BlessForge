#!/usr/bin/env python3
import os
import math
import re

print("=== CONSTRUINDO TODOS OS CAPÍTULOS RESTANTES (3, 4, 5 E 6) ===")

# =====================================================================
# CAPÍTULO 3: TWILIGHT FOREST (22 QUESTS)
# =====================================================================
TWILIGHT_SNBT = """{
	default_hide_dependency_lines: false
	default_quest_shape: "circle"
	filename: "capitulo_3_twilight"
	group: "1A2B3C4D5E6F7001"
	icon: {
		id: "twilightforest:naga_trophy"
	}
	id: "1003000000000001"
	order_index: 3
	title: "3. Alem do Dossel (Twilight Forest)"
	quests: [
		{
			description: [
				"Para abrir o portal para a dimensao do crepusculo eterno, cave um buraco 2x2 na grama, preencha com agua, cerque as bordas de flores coloridas e atire um diamante la dentro."
				"Um raio místico caira do ceu transformando a agua em um portal violeta encantado!"
			]
			icon: {
				id: "minecraft:diamond"
			}
			id: "1003000000000010"
			shape: "hexagon"
			size: 1.5d
			subtitle: "O ritual sagrado do diamante e das flores"
			tasks: [
				{
					id: "1003000000000011"
					title: "Abra o Portal do Crepusculo"
					type: "checkmark"
				}
			]
			rewards: [
				{
					id: "1003000000000012"
					item: {
						count: 1
						id: "twilightforest:magic_map"
					}
					type: "item"
				}
				{
					id: "1003000000000013"
					type: "xp_levels"
					xp_levels: 5
				}
			]
			title: "Rumo ao Crepusculo Eterno"
			x: -11.0d
			y: 0.0d
		}
		{
			dependencies: ["1003000000000010"]
			description: [
				"O Mapa Magico revela biomas encantados e os icones dos lordes sombrios protegidos por barreiras magicas."
				"Combine penas de corvo, bagas reluzentes e papel para orientar sua jornada com precisao absoluta."
			]
			icon: {
				id: "twilightforest:magic_map"
			}
			id: "1003000000000020"
			shape: "circle"
			size: 1.2d
			subtitle: "A cartografia arcana da floresta"
			tasks: [
				{
					id: "1003000000000021"
					item: {
						count: 1
						id: "twilightforest:magic_map"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 8
					id: "1003000000000022"
					item: {
						count: 1
						id: "twilightforest:torchberries"
					}
					type: "item"
				}
				{
					id: "1003000000000023"
					type: "xp_levels"
					xp_levels: 5
				}
			]
			title: "O Mapeamento do Crepusculo"
			x: -8.5d
			y: 0.0d
		}
		{
			dependencies: ["1003000000000020"]
			description: [
				"Nas colinas ocas do Crepusculo descansam minerios raros e baus repletos de amuletos protetores."
				"O Amuleto da Vida (Charm of Life) salva voce da morte iminente, restaurando coracoes no momento critico!"
			]
			icon: {
				id: "twilightforest:charm_of_life_2"
			}
			id: "1003000000000030"
			shape: "circle"
			size: 1.1d
			subtitle: "[Dificuldade: Media] Protecao milagrosa nas masmorras das colinas ocas"
			tasks: [
				{
					id: "1003000000000031"
					item: {
						count: 1
						id: "twilightforest:charm_of_life_2"
					}
					type: "item"
				}
			]
			rewards: [
				{
					id: "1003000000000032"
					item: {
						count: 1
						id: "twilightforest:charm_of_keeping_3"
					}
					type: "item"
				}
				{
					id: "1003000000000033"
					type: "xp_levels"
					xp_levels: 6
				}
			]
			title: "O Amuleto da Salvacao"
			x: -8.5d
			y: 2.5d
		}
		{
			dependencies: ["1003000000000020"]
			description: [
				"Combinando ferro bruto, ouro e madeira viva, forje o Ironwood — um metal impregnado de forca vegetal que ja nasce pre-encantado!"
				"Armaduras e ferramentas de Ironwood oferecem durabilidade excelente sem custos de bigorna."
			]
			icon: {
				id: "twilightforest:ironwood_ingot"
			}
			id: "1003000000000040"
			shape: "circle"
			size: 1.1d
			subtitle: "[Dificuldade: Media] A fusao botanica de ferro e magia da terra"
			tasks: [
				{
					count: 8L
					id: "1003000000000041"
					item: {
						count: 1
						id: "twilightforest:ironwood_ingot"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 8
					id: "1003000000000042"
					item: {
						count: 1
						id: "twilightforest:ironwood_ingot"
					}
					type: "item"
				}
				{
					id: "1003000000000043"
					type: "xp_levels"
					xp_levels: 6
				}
			]
			title: "Metal Botanico: Ironwood"
			x: -6.0d
			y: 2.5d
		}
		{
			dependencies: ["1003000000000020"]
			description: [
				"Folhas místicas colhidas nos baus das masmorras subterraneas podem ser prensadas em Lingotes de Folhaco (Steeleaf)."
				"O Steeleaf confere velocidade de corte surpreendente e encantamentos de alta sinergia."
			]
			icon: {
				id: "twilightforest:steeleaf_ingot"
			}
			id: "1003000000000050"
			shape: "circle"
			size: 1.1d
			subtitle: "[Dificuldade: Media] O aco vegetal do dossel sombrio"
			tasks: [
				{
					count: 8L
					id: "1003000000000051"
					item: {
						count: 1
						id: "twilightforest:steeleaf_ingot"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 8
					id: "1003000000000052"
					item: {
						count: 1
						id: "twilightforest:steeleaf_ingot"
					}
					type: "item"
				}
				{
					id: "1003000000000053"
					type: "xp_levels"
					xp_levels: 6
				}
			]
			title: "Aco das Folhas: Steeleaf"
			x: -3.5d
			y: 2.5d
		}
		{
			dependencies: ["1003000000000020"]
			description: [
				"O primeiro guardiao da progressao repousa em um patio cercado de pedra musgosa."
				"A Naga se move em velocidade estarrecedora em arcos sinuosos, quebrando blocos pelo caminho. Acerte a cauda ou a cabeca ate desarma-la por completo!"
			]
			icon: {
				id: "twilightforest:naga_trophy"
			}
			id: "1003000000000060"
			shape: "diamond"
			size: 1.3d
			subtitle: "[Dificuldade: Media] O predador serpentino do patio ancestral"
			tasks: [
				{
					entity: "twilightforest:naga"
					id: "1003000000000061"
					type: "kill"
					value: 1L
				}
				{
					count: 8L
					id: "1003000000000062"
					item: {
						count: 1
						id: "twilightforest:naga_scale"
					}
					type: "item"
				}
			]
			rewards: [
				{
					id: "1003000000000063"
					item: {
						count: 1
						id: "twilightforest:naga_trophy"
					}
					type: "item"
				}
				{
					id: "1003000000000064"
					type: "xp_levels"
					xp_levels: 10
				}
			]
			title: "A Serpente do Patio: A Naga"
			x: -6.0d
			y: 0.0d
		}
		{
			dependencies: ["1003000000000060"]
			description: [
				"No topo de uma torre colossal ergue-se o Lich do Crepusculo, protegido por escudos magicos invulneraveis."
				"Rebata os projeteis azuis com sua espada para romper seus escudos, elimine seus clones e encare sua forma fisica quando ele empunhar sua espada dourada!"
			]
			icon: {
				id: "twilightforest:lich_trophy"
			}
			id: "1003000000000070"
			shape: "diamond"
			size: 1.3d
			subtitle: "[Dificuldade: Media] O feiticeiro soberano da torre espiral"
			tasks: [
				{
					entity: "twilightforest:lich"
					id: "1003000000000071"
					type: "kill"
					value: 1L
				}
			]
			rewards: [
				{
					id: "1003000000000072"
					item: {
						count: 1
						id: "twilightforest:lich_trophy"
					}
					type: "item"
				}
				{
					id: "1003000000000073"
					type: "xp_levels"
					xp_levels: 15
				}
			]
			title: "O Soberano da Torre: Twilight Lich"
			x: -3.5d
			y: 0.0d
		}
		{
			dependencies: ["1003000000000070"]
			description: [
				"No segundo nivel dos labirintos no pantano reside o Minocogumelo (Minoshroom)."
				"Ele investe violentamente com seu machado de diamante. Abata-o para recolher a saborosa sopa Stroganoff de Meef, que quebra a maldicao de fome do pantano!"
			]
			icon: {
				id: "twilightforest:minoshroom_trophy"
			}
			id: "1003000000000080"
			shape: "pentagon"
			size: 1.25d
			subtitle: "[Dificuldade: Media] O lorde touro dos corredores subterraneos"
			tasks: [
				{
					entity: "twilightforest:minoshroom"
					id: "1003000000000081"
					type: "kill"
					value: 1L
				}
				{
					id: "1003000000000082"
					item: {
						count: 1
						id: "twilightforest:meef_stroganoff"
					}
					type: "item"
				}
			]
			rewards: [
				{
					id: "1003000000000083"
					item: {
						count: 1
						id: "twilightforest:mazebreaker_pickaxe"
					}
					type: "item"
				}
				{
					id: "1003000000000084"
					type: "xp_levels"
					xp_levels: 12
				}
			]
			title: "O Terror do Labirinto: Minoshroom"
			x: -1.0d
			y: 0.0d
		}
		{
			dependencies: ["1003000000000080"]
			description: [
				"Nas entranhas de uma montanha calcinada no pantano flamejante ruge a Hidra."
				"Cada cabeca decepada faz nascer outras duas, vomitando fogo e bombas incendiarias!"
				"Mire na boca aberta quando ela for cuspir chamas para causar dano critico triplicado e colher o Sangue Ígneo (Fiery Blood)!"
			]
			icon: {
				id: "twilightforest:hydra_trophy"
			}
			id: "1003000000000090"
			shape: "pentagon"
			size: 1.3d
			subtitle: "[Dificuldade: Dificil] O monstro multicabecas do pantano ardente"
			tasks: [
				{
					entity: "twilightforest:hydra"
					id: "1003000000000091"
					type: "kill"
					value: 1L
				}
				{
					count: 4L
					id: "1003000000000092"
					item: {
						count: 1
						id: "twilightforest:fiery_blood"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 8
					id: "1003000000000093"
					item: {
						count: 1
						id: "twilightforest:fiery_ingot"
					}
					type: "item"
				}
				{
					id: "1003000000000094"
					type: "xp_levels"
					xp_levels: 20
				}
			]
			title: "O Fogo Eterno da Hidra"
			x: 1.5d
			y: 0.0d
		}
		{
			dependencies: ["1003000000000070"]
			description: [
				"Na impenetravel Floresta Negra, sob o labirinto de goblins, fantasmas de cavaleiros espectrais defendem sua tumba sagrada."
				"Seis espectros voam simultaneamente arremessando armas fantasmagoricas e machados. Fique atento aos seus escudos e abata todos eles!"
			]
			icon: {
				id: "twilightforest:knight_phantom_trophy"
			}
			id: "1003000000000100"
			shape: "pentagon"
			size: 1.25d
			subtitle: "[Dificuldade: Dificil] Os cavaleiros espectrais da tumba esquecida"
			tasks: [
				{
					entity: "twilightforest:knight_phantom"
					id: "1003000000000101"
					type: "kill"
					value: 1L
				}
				{
					count: 8L
					id: "1003000000000102"
					item: {
						count: 1
						id: "twilightforest:knightmetal_ingot"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 8
					id: "1003000000000103"
					item: {
						count: 1
						id: "twilightforest:knightmetal_ingot"
					}
					type: "item"
				}
				{
					id: "1003000000000104"
					type: "xp_levels"
					xp_levels: 18
				}
			]
			title: "O Conclave dos Cavaleiros Espectrais"
			x: 1.5d
			y: -2.5d
		}
		{
			dependencies: ["1003000000000100"]
			description: [
				"No pinaculo da Torre Sombria flutua o Ur-Ghast, uma colossal aberracao mecânica-espectral com tentaculos de carminita."
				"Ele chora lagrimas de fogo e devora ghasts menores para se curar. Ative as Armadilhas de Ghast na plataforma para pulveriza-lo com raios de redstone!"
			]
			icon: {
				id: "twilightforest:ur_ghast_trophy"
			}
			id: "1003000000000110"
			shape: "pentagon"
			size: 1.3d
			subtitle: "[Dificuldade: Dificil] O colosso carmesim no topo da Torre Sombria"
			tasks: [
				{
					entity: "twilightforest:ur_ghast"
					id: "1003000000000111"
					type: "kill"
					value: 1L
				}
			]
			rewards: [
				{
					id: "1003000000000112"
					item: {
						count: 1
						id: "twilightforest:ur_ghast_trophy"
					}
					type: "item"
				}
				{
					id: "1003000000000113"
					type: "xp_levels"
					xp_levels: 20
				}
			]
			title: "O Terror Carmesim: Ur-Ghast"
			x: 4.0d
			y: -2.5d
		}
		{
			dependencies: ["1003000000000070"]
			description: [
				"Nas cavernas glaciais sob a neve eterna vive o Alfa Yeti."
				"Ele arremessa blocos macicos de gelo e pisa no chao causando estalagmites pontiagudas do teto. Sobreviva a tempestade glacial para colher as Peles Articas!"
			]
			icon: {
				id: "twilightforest:arctic_fur"
			}
			id: "1003000000000120"
			shape: "pentagon"
			size: 1.25d
			subtitle: "[Dificuldade: Dificil] A forca bruta das cavernas congeladas"
			tasks: [
				{
					entity: "twilightforest:alpha_yeti"
					id: "1003000000000121"
					type: "kill"
					value: 1L
				}
				{
					count: 6L
					id: "1003000000000122"
					item: {
						count: 1
						id: "twilightforest:arctic_fur"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 8
					id: "1003000000000123"
					item: {
						count: 1
						id: "twilightforest:arctic_fur"
					}
					type: "item"
				}
				{
					id: "1003000000000124"
					type: "xp_levels"
					xp_levels: 18
				}
			]
			title: "A Furia Glacial: Alpha Yeti"
			x: 1.5d
			y: 2.5d
		}
		{
			dependencies: ["1003000000000120"]
			description: [
				"No topo do Palacio de Aurora brilha a soberana absoluta do gelo: a Rainha da Neve."
				"Flutuando sobre um escudo impenetravel de gelo, ela invoca tempestades e fadas de neve cortantes. Quebre seu treno de gelo para desarma-la e conquistar o cobicado Arco de Gelo!"
			]
			icon: {
				id: "twilightforest:snow_queen_trophy"
			}
			id: "1003000000000130"
			shape: "diamond"
			size: 1.5d
			subtitle: "[Dificuldade: Extrema] A soberana do Palacio de Aurora"
			tasks: [
				{
					entity: "twilightforest:snow_queen"
					id: "1003000000000131"
					type: "kill"
					value: 1L
				}
			]
			rewards: [
				{
					id: "1003000000000132"
					item: {
						count: 1
						id: "twilightforest:snow_queen_trophy"
					}
					type: "item"
				}
				{
					id: "1003000000000133"
					type: "xp_levels"
					xp_levels: 30
				}
			]
			title: "A Soberana da Aurora: Snow Queen"
			x: 4.0d
			y: 2.5d
		}
		{
			dependencies: [
				"1003000000000090"
				"1003000000000110"
				"1003000000000130"
			]
			description: [
				"Com os poderes da Hidra, do Ur-Ghast e da Rainha da Neve absorvidos, o Planalto das Terras Altas se abre."
				"Suba ate os castelos de nuvens, enfrente os Gigantes Mineiros e guerreiros colossais e acenda a Lampada das Cinzas para queimar os espinhos eternos do Castelo Final!"
			]
			icon: {
				id: "twilightforest:lamp_of_cinders"
			}
			id: "1003000000000140"
			shape: "diamond"
			size: 1.5d
			subtitle: "[Dificuldade: Extrema] A queima dos espinhos e a conquista do Castelo Final"
			tasks: [
				{
					id: "1003000000000141"
					item: {
						count: 1
						id: "twilightforest:lamp_of_cinders"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 4
					id: "1003000000000142"
					item: {
						count: 1
						id: "minecraft:netherite_ingot"
					}
					type: "item"
				}
				{
					id: "1003000000000143"
					type: "xp_levels"
					xp_levels: 35
				}
			]
			title: "A Lampada das Cinzas e o Castelo Final"
			x: 6.5d
			y: 0.0d
		}
	]
}
"""

# =====================================================================
# CAPÍTULO 4: THE BUMBLEZONE (15 QUESTS)
# =====================================================================
BUMBLEZONE_SNBT = """{
	default_hide_dependency_lines: false
	default_quest_shape: "circle"
	filename: "capitulo_4_bumblezone"
	group: "1A2B3C4D5E6F7001"
	icon: {
		id: "the_bumblezone:royal_jelly_bottle"
	}
	id: "1004000000000001"
	order_index: 4
	title: "4. Zumbidos e Abismos (The Bumblezone)"
	quests: [
		{
			description: [
				"Para ingressar no reino milenar das abelhas, arremesse uma Perola do Ender diretamente contra qualquer colmeia ou ninho de abelha comum no Overworld."
				"Voce sera encolhido e transportado para um universo colossal feito inteiramente de favos dourados, rios de mel e zumbidos estrondosos!"
			]
			icon: {
				id: "minecraft:ender_pearl"
			}
			id: "1004000000000010"
			shape: "hexagon"
			size: 1.5d
			subtitle: "O teleporte para o interior do favo dimensional"
			tasks: [
				{
					id: "1004000000000011"
					title: "Adentre o Bumblezone"
					type: "checkmark"
				}
			]
			rewards: [
				{
					count: 4
					id: "1004000000000012"
					item: {
						count: 1
						id: "minecraft:honey_bottle"
					}
					type: "item"
				}
				{
					id: "1004000000000013"
					type: "xp_levels"
					xp_levels: 5
				}
			]
			title: "A Fenda dos Favos: O Bumblezone"
			x: -9.0d
			y: 0.0d
		}
		{
			dependencies: ["1004000000000010"]
			description: [
				"Nas paredes das cavernas de mel crescem cristais dourados reluzentes."
				"Com esses fragmentos, voce pode forjar ferramentas refractarias e o formidavel Escudo de Mel Cristalizado, que regenera sua propria durabilidade quando banhado em mel!"
			]
			icon: {
				id: "the_bumblezone:honey_crystal_shards"
			}
			id: "1004000000000020"
			shape: "circle"
			size: 1.1d
			subtitle: "[Dificuldade: Media] Minerios cristalinos e armaduras refractarias"
			tasks: [
				{
					count: 16L
					id: "1004000000000021"
					item: {
						count: 1
						id: "the_bumblezone:honey_crystal_shards"
					}
					type: "item"
				}
				{
					id: "1004000000000022"
					item: {
						count: 1
						id: "the_bumblezone:honey_crystal_shield"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 4
					id: "1004000000000023"
					item: {
						count: 1
						id: "the_bumblezone:glistering_honey_crystal"
					}
					type: "item"
				}
				{
					id: "1004000000000024"
					type: "xp_levels"
					xp_levels: 6
				}
			]
			title: "Mel Cristalizado e Escudo Dourado"
			x: -6.5d
			y: 0.0d
		}
		{
			dependencies: ["1004000000000020"]
			description: [
				"A Bussola de Mel sintoniza a vibracao de feromonios no ar."
				"Clique com o botao direito para faze-la apontar para Santuarios Sempiternos, Salas do Trono da Rainha ou Labirintos de Celulas subterraneos sem perambular no escuro!"
			]
			icon: {
				id: "the_bumblezone:honey_compass"
			}
			id: "1004000000000030"
			shape: "circle"
			size: 1.1d
			subtitle: "Navegacao por feromonios entre as colmeias"
			tasks: [
				{
					id: "1004000000000031"
					item: {
						count: 1
						id: "the_bumblezone:honey_compass"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 8
					id: "1004000000000032"
					item: {
						count: 1
						id: "minecraft:honeycomb"
					}
					type: "item"
				}
				{
					id: "1004000000000033"
					type: "xp_levels"
					xp_levels: 6
				}
			]
			title: "A Bussola de Mel"
			x: -6.5d
			y: -2.5d
		}
		{
			dependencies: ["1004000000000020"]
			description: [
				"Ao arremessar Bolas de Polen (Pollen Puffs) em flores e cultivos, elas polinizam e aceleram colheitas instantaneamente."
				"Use seu estilingue ou arremesse com a mao para domesticar ou acalmar abelhas agitadas."
			]
			icon: {
				id: "the_bumblezone:pollen_puff"
			}
			id: "1004000000000040"
			shape: "circle"
			size: 1.1d
			subtitle: "[Dificuldade: Media] A poeira floral que fertiliza biomas inteiros"
			tasks: [
				{
					count: 16L
					id: "1004000000000041"
					item: {
						count: 1
						id: "the_bumblezone:pollen_puff"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 16
					id: "1004000000000042"
					item: {
						count: 1
						id: "the_bumblezone:pollen_puff"
					}
					type: "item"
				}
				{
					id: "1004000000000043"
					type: "xp_levels"
					xp_levels: 6
				}
			]
			title: "Projéteis de Polen"
			x: -6.5d
			y: 2.5d
		}
		{
			dependencies: ["1004000000000020"]
			description: [
				"A Geleia Real e o elixir maximo das abelhas nobres."
				"Beber este néctar divino concede restauracao instantanea de todos os coracoes e previne venenos por longos minutos."
			]
			icon: {
				id: "the_bumblezone:royal_jelly_bottle"
			}
			id: "1004000000000050"
			shape: "diamond"
			size: 1.3d
			subtitle: "[Dificuldade: Dificil] O elixir sagrado da colmeia imperial"
			tasks: [
				{
					count: 3L
					id: "1004000000000051"
					item: {
						count: 1
						id: "the_bumblezone:royal_jelly_bottle"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 2
					id: "1004000000000052"
					item: {
						count: 1
						id: "the_bumblezone:royal_jelly_bottle"
					}
					type: "item"
				}
				{
					id: "1004000000000053"
					type: "xp_levels"
					xp_levels: 10
				}
			]
			title: "O Manjar Imperial: Geleia Real"
			x: -4.0d
			y: 0.0d
		}
		{
			dependencies: ["1004000000000050"]
			description: [
				"Forjada com o ferrão endurecido de abelhas gigantes, esta lanca causa sangramento e perfuracao aguda."
				"Excelente para investidas velozes enquanto voce desliza sobre blocos pegajosos de mel!"
			]
			icon: {
				id: "the_bumblezone:stinger_spear"
			}
			id: "1004000000000060"
			shape: "pentagon"
			size: 1.25d
			subtitle: "[Dificuldade: Dificil] Perfuracao pontiaguda com ferroes gigantes"
			tasks: [
				{
					id: "1004000000000061"
					item: {
						count: 1
						id: "the_bumblezone:stinger_spear"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 4
					id: "1004000000000062"
					item: {
						count: 1
						id: "minecraft:emerald"
					}
					type: "item"
				}
				{
					id: "1004000000000063"
					type: "xp_levels"
					xp_levels: 12
				}
			]
			title: "A Lança de Ferrão"
			x: -4.0d
			y: 2.5d
		}
		{
			dependencies: ["1004000000000050"]
			description: [
				"Uma peca de artilharia apicola que dispara abelhas amigaveis a alta velocidade contra os inimigos!"
				"As abelhas atacam os alvos e retornam para o canhao apos a batalha."
			]
			icon: {
				id: "the_bumblezone:bee_cannon"
			}
			id: "1004000000000070"
			shape: "pentagon"
			size: 1.25d
			subtitle: "[Dificuldade: Dificil] Artilharia viva com projeteis voadores"
			tasks: [
				{
					id: "1004000000000071"
					item: {
						count: 1
						id: "the_bumblezone:bee_cannon"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 16
					id: "1004000000000072"
					item: {
						count: 1
						id: "minecraft:honey_bottle"
					}
					type: "item"
				}
				{
					id: "1004000000000073"
					type: "xp_levels"
					xp_levels: 15
				}
			]
			title: "O Canhão de Abelhas"
			x: -1.5d
			y: 2.5d
		}
		{
			dependencies: ["1004000000000050"]
			description: [
				"Localize a grandiosa Sala do Trono das Abelhas e curve-se diante da Rainha das Abelhas (Bee Queen)."
				"Ela e neutra e comercializa artefatos arcanos em troca de baldes e frascos de Geleia Real. Complete seus pedidos para ganhar a graca e o respeito de todo o enxame!"
			]
			icon: {
				id: "minecraft:honeycomb_block"
			}
			id: "1004000000000080"
			shape: "diamond"
			size: 1.5d
			subtitle: "[Dificuldade: Dificil] Audiencia real com a soberana do enxame"
			tasks: [
				{
					id: "1004000000000081"
					title: "Encontre a Rainha das Abelhas"
					type: "checkmark"
				}
			]
			rewards: [
				{
					count: 3
					id: "1004000000000082"
					item: {
						count: 1
						id: "the_bumblezone:royal_jelly_bottle"
					}
					type: "item"
				}
				{
					id: "1004000000000083"
					type: "xp_levels"
					xp_levels: 20
				}
			]
			title: "A Sala do Trono da Rainha"
			x: -1.5d
			y: 0.0d
		}
		{
			dependencies: ["1004000000000080"]
			description: [
				"A Flor Cristalina e uma reliquia viva que absorve experiencia e néctar místico para florescer em niveis cosmicos."
				"Alimente-a com niveis de XP ate que ela atinja a maturidade maxima, liberando as Essencias das Abelhas e atributos transcendentes para suas armaduras!"
			]
			icon: {
				id: "the_bumblezone:crystalline_flower"
			}
			id: "1004000000000090"
			shape: "diamond"
			size: 1.5d
			subtitle: "[Dificuldade: Extrema] O milagre botânico do cosmos apicola"
			tasks: [
				{
					id: "1004000000000091"
					item: {
						count: 1
						id: "the_bumblezone:crystalline_flower"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 2
					id: "1004000000000092"
					item: {
						count: 1
						id: "minecraft:netherite_block"
					}
					type: "item"
				}
				{
					id: "1004000000000093"
					type: "xp_levels"
					xp_levels: 30
				}
			]
			title: "A Flor Cristalina Cosmica"
			x: 1.5d
			y: 0.0d
		}
	]
}
"""

# =====================================================================
# CAPÍTULO 5: O ARSENAL LENDÁRIO (16 QUESTS)
# =====================================================================
ARSENAL_SNBT = """{
	default_hide_dependency_lines: false
	default_quest_shape: "circle"
	filename: "capitulo_5_arsenal"
	group: "1A2B3C4D5E6F7001"
	icon: {
		id: "simplyswords:brimstone_claymore"
	}
	id: "1005000000000001"
	order_index: 5
	title: "5. O Arsenal Lendario"
	quests: [
		{
			description: [
				"Para enfrentar as entidades supremas que ameacam o Mundo Eterno, laminas convencionais nao sao suficientes."
				"Forje armas pesadas especializadas de diamante — Katana para golpes em sequencia rápida, Claymore para varreduras em arco ou Glaive para perfuracao com alcance ampliado!"
			]
			icon: {
				id: "simplyswords:diamond_claymore"
			}
			id: "1005000000000010"
			shape: "hexagon"
			size: 1.4d
			subtitle: "Armamentos de diamante com posturas de combate avançadas"
			tasks: [
				{
					id: "1005000000000011"
					item: {
						count: 1
						id: "simplyswords:diamond_claymore"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 4
					id: "1005000000000012"
					item: {
						count: 1
						id: "minecraft:diamond"
					}
					type: "item"
				}
				{
					id: "1005000000000013"
					type: "xp_levels"
					xp_levels: 10
				}
			]
			title: "A Forja da Lâmina Pesada"
			x: -11.0d
			y: 0.0d
		}
		{
			dependencies: ["1005000000000010"]
			description: [
				"Revestir sua arma de combate com Netherite eleva sua massa e estabilidade, impedindo que golpes fortes sejam interrompidos por recuo."
				"Com a Claymore de Netherite, cada golpe desestabiliza a armadura de chefes e colossos."
			]
			icon: {
				id: "simplyswords:netherite_claymore"
			}
			id: "1005000000000020"
			shape: "diamond"
			size: 1.3d
			subtitle: "[Dificuldade: Media] O impacto maciço do aco negro do Nether"
			tasks: [
				{
					id: "1005000000000021"
					item: {
						count: 1
						id: "simplyswords:netherite_claymore"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 1
					id: "1005000000000022"
					item: {
						count: 1
						id: "minecraft:netherite_ingot"
					}
					type: "item"
				}
				{
					id: "1005000000000023"
					type: "xp_levels"
					xp_levels: 15
				}
			]
			title: "O Peso do Netherite: Claymore Suprema"
			x: -8.5d
			y: 0.0d
		}
		{
			dependencies: ["1005000000000010"]
			description: [
				"O mod Armor of the Ages traz vestimentas de guerra dos maiores imperios da historia."
				"Forje uma armadura cerimonial de Centuriao Romano ou Armadura Samurai O-Yoroi para ganhar defesa equilibrada e estetica marcial incomparavel."
			]
			icon: {
				id: "armoroftheages:centurion_armor_chest"
			}
			id: "1005000000000030"
			shape: "circle"
			size: 1.2d
			subtitle: "[Dificuldade: Media] As armaduras que ergueram os grandes imperios"
			tasks: [
				{
					id: "1005000000000031"
					item: {
						count: 1
						id: "armoroftheages:centurion_armor_chest"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 8
					id: "1005000000000032"
					item: {
						count: 1
						id: "minecraft:iron_ingot"
					}
					type: "item"
				}
				{
					id: "1005000000000033"
					type: "xp_levels"
					xp_levels: 8
				}
			]
			title: "Armadura dos Seculos: O Centuriao"
			x: -8.5d
			y: -2.5d
		}
		{
			dependencies: ["1005000000000020"]
			description: [
				"O Altar Runico (Runic Forge) canaliza a energia de Tabuas Runicas para despertar habilidades sobrenaturais em armas ordinarias."
				"Construa a forja para fundir runas de fogo, gelo, vacuo e cura diretamente no aco!"
			]
			icon: {
				id: "simplyswords:runic_forge"
			}
			id: "1005000000000040"
			shape: "diamond"
			size: 1.3d
			subtitle: "[Dificuldade: Dificil] O altar místico de infusao de runas"
			tasks: [
				{
					id: "1005000000000041"
					item: {
						count: 1
						id: "simplyswords:runic_forge"
					}
					type: "item"
				}
				{
					id: "1005000000000042"
					item: {
						count: 1
						id: "simplyswords:runic_tablet"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 8
					id: "1005000000000043"
					item: {
						count: 1
						id: "minecraft:diamond"
					}
					type: "item"
				}
				{
					id: "1005000000000044"
					type: "xp_levels"
					xp_levels: 15
				}
			]
			title: "A Forja Rúnica Mítica"
			x: -6.0d
			y: 0.0d
		}
		{
			dependencies: ["1005000000000040"]
			description: [
				"Forjada nas profundezas vulcanicas do Nether, a Brimstone Claymore irradia ondas continuas de magma incandescente."
				"Ao atingir inimigos, ergue colunas de chamas que incineram o terreno e causam queimaduras penetrantes."
			]
			icon: {
				id: "simplyswords:brimstone_claymore"
			}
			id: "1005000000000050"
			shape: "pentagon"
			size: 1.3d
			subtitle: "[Dificuldade: Dificil] O espadao forjado em rocha de enxofre ardente"
			tasks: [
				{
					id: "1005000000000051"
					item: {
						count: 1
						id: "simplyswords:brimstone_claymore"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 2
					id: "1005000000000052"
					item: {
						count: 1
						id: "minecraft:netherite_ingot"
					}
					type: "item"
				}
				{
					id: "1005000000000053"
					type: "xp_levels"
					xp_levels: 20
				}
			]
			title: "A Furia Vulcanica: Brimstone Claymore"
			x: -3.5d
			y: -2.5d
		}
		{
			dependencies: ["1005000000000040"]
			description: [
				"Imbuida com geodos de ametista pura e energia arcana, esta lamina projeta laminas espectrais flutuantes que buscam alvos automaticamente ao redor do atacante."
			]
			icon: {
				id: "simplyswords:arcanethyst"
			}
			id: "1005000000000060"
			shape: "pentagon"
			size: 1.3d
			subtitle: "[Dificuldade: Dificil] Ressonância cristalina de ametista e magia pura"
			tasks: [
				{
					id: "1005000000000061"
					item: {
						count: 1
						id: "simplyswords:arcanethyst"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 4
					id: "1005000000000062"
					item: {
						count: 1
						id: "minecraft:amethyst_shard"
					}
					type: "item"
				}
				{
					id: "1005000000000063"
					type: "xp_levels"
					xp_levels: 20
				}
			]
			title: "A Canção Arcana: Arcanethyst"
			x: -3.5d
			y: 2.5d
		}
		{
			dependencies: ["1005000000000040"]
			description: [
				"A temida lamina sanguinea se alimenta do dano causado aos inimigos, convertendo ferimentos em roubo de vida imediato para o seu portador."
			]
			icon: {
				id: "simplyswords:bloodwake"
			}
			id: "1005000000000070"
			shape: "pentagon"
			size: 1.3d
			subtitle: "[Dificuldade: Dificil] O furor vampírico da maré carmesim"
			tasks: [
				{
					id: "1005000000000071"
					item: {
						count: 1
						id: "simplyswords:bloodwake"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 1
					id: "1005000000000072"
					item: {
						count: 1
						id: "minecraft:enchanted_golden_apple"
					}
					type: "item"
				}
				{
					id: "1005000000000073"
					type: "xp_levels"
					xp_levels: 20
				}
			]
			title: "O Despertar da Maré Vermelha: Bloodwake"
			x: -3.5d
			y: 0.0d
		}
		{
			dependencies: [
				"1005000000000050"
				"1005000000000070"
			]
			description: [
				"Ao alimentar a espada dormente das almas com o sangue de inimigos caídos, a Lichblade atinge seu estagio desperto definitivo."
				"Ela invoca guerreiros espectrais que lutam sob seu comando e drena a essencia vital de qualquer monstro que ouse cruzar seu caminho!"
			]
			icon: {
				id: "simplyswords:awakened_lichblade"
			}
			id: "1005000000000080"
			shape: "diamond"
			size: 1.6d
			subtitle: "[Dificuldade: Extrema] A lamina das almas ressuscitada em sua gloria máxima"
			tasks: [
				{
					id: "1005000000000081"
					item: {
						count: 1
						id: "simplyswords:awakened_lichblade"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 4
					id: "1005000000000082"
					item: {
						count: 1
						id: "minecraft:netherite_block"
					}
					type: "item"
				}
				{
					id: "1005000000000083"
					type: "xp_levels"
					xp_levels: 40
				}
			]
			title: "A Lâmina dos Mortos: Awakened Lichblade"
			x: -1.0d
			y: 0.0d
		}
	]
}
"""

# =====================================================================
# CAPÍTULO 6: O FIM DOS TITÃS - CATACLYSM (18 QUESTS)
# =====================================================================
CATACLYSM_SNBT = """{
	default_hide_dependency_lines: false
	default_quest_shape: "circle"
	filename: "capitulo_6_cataclysm"
	group: "1A2B3C4D5E6F7001"
	icon: {
		id: "cataclysm:monstrous_horn"
	}
	id: "1006000000000001"
	order_index: 6
	title: "6. O Fim dos Titas (Cataclysm)"
	quests: [
		{
			description: [
				"O mod L_Ender's Cataclysm desperta deuses ancestrais e horrores colossais que habitam as ruinas esquecidas do mundo."
				"Nas profundezas oceanicas da Cidade Submersa (Sunken City), guerreiros Deeplings e bruxos das profundezas protegem o altar do abismo."
				"Sobreviva aos terrores aquaticos e colete Carne Abencoada de Caranguejo de Ametista!"
			]
			icon: {
				id: "cataclysm:blessed_amethyst_crab_meat"
			}
			id: "1006000000000010"
			shape: "hexagon"
			size: 1.4d
			subtitle: "[Dificuldade: Media] As primeiras incursões na Cidade Submersa"
			tasks: [
				{
					count: 2L
					id: "1006000000000011"
					item: {
						count: 1
						id: "cataclysm:blessed_amethyst_crab_meat"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 8
					id: "1006000000000012"
					item: {
						count: 1
						id: "minecraft:prismarine_crystals"
					}
					type: "item"
				}
				{
					id: "1006000000000013"
					type: "xp_levels"
					xp_levels: 10
				}
			]
			title: "O Chamado do Abismo Submerso"
			x: -11.0d
			y: 0.0d
		}
		{
			dependencies: ["1006000000000010"]
			description: [
				"Nas profundezas do Nether, ergue-se a Forja das Almas (Soul Forge), onde repousa a Monstruosidade de Netherite."
				"Armado com um martelo descomunal, este golem de magma e netherite esmaga o solo causando ondas de choque cataclismicas e vomitando lava viva."
				"Quebre seus chifres para conquistar o Chifre Monstruoso e forjar o elmo invulneravel!"
			]
			icon: {
				id: "cataclysm:monstrous_horn"
			}
			id: "1006000000000020"
			shape: "pentagon"
			size: 1.4d
			subtitle: "[Dificuldade: Dificil] O titan de magma e aco negro da Forja das Almas"
			tasks: [
				{
					entity: "cataclysm:netherite_monstrosity"
					id: "1006000000000021"
					type: "kill"
					value: 1L
				}
				{
					id: "1006000000000022"
					item: {
						count: 1
						id: "cataclysm:monstrous_horn"
					}
					type: "item"
				}
			]
			rewards: [
				{
					id: "1006000000000023"
					item: {
						count: 1
						id: "cataclysm:monstrous_helm"
					}
					type: "item"
				}
				{
					id: "1006000000000024"
					type: "xp_levels"
					xp_levels: 25
				}
			]
			title: "A Monstruosidade de Netherite"
			x: -8.5d
			y: 0.0d
		}
		{
			dependencies: ["1006000000000010"]
			description: [
				"Na grandiosa Piramide Amaldicoada no deserto profundo dorme o Remanescente Ancestral (Ancient Remnant)."
				"Desperto pelas areias movedicas, ele cria tempestades de poeira e investidas devastadoras. Abata-o para recolher o Lendario Colar do Deserto!"
			]
			icon: {
				id: "cataclysm:necklace_of_the_desert"
			}
			id: "1006000000000030"
			shape: "pentagon"
			size: 1.3d
			subtitle: "[Dificuldade: Dificil] O lorde serpentino das areias da Piramide Maldita"
			tasks: [
				{
					entity: "cataclysm:ancient_remnant"
					id: "1006000000000031"
					type: "kill"
					value: 1L
				}
				{
					id: "1006000000000032"
					item: {
						count: 1
						id: "cataclysm:necklace_of_the_desert"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 4
					id: "1006000000000033"
					item: {
						count: 1
						id: "minecraft:diamond_block"
					}
					type: "item"
				}
				{
					id: "1006000000000034"
					type: "xp_levels"
					xp_levels: 20
				}
			]
			title: "O Farao das Areias: Ancient Remnant"
			x: -8.5d
			y: 2.5d
		}
		{
			dependencies: ["1006000000000020"]
			description: [
				"No centro da Arena em Chamas (Burning Arena) no Nether espera Ignis, o cavaleiro supremo do fogo."
				"Empunhando a Incineradora (The Incinerator), ele corta a realidade com laminas de labaredas e arremessa escudos de magma. Derrote-o para reivindicar a espada mais destrutiva do jogo!"
			]
			icon: {
				id: "cataclysm:the_incinerator"
			}
			id: "1006000000000040"
			shape: "diamond"
			size: 1.6d
			subtitle: "[Dificuldade: Extrema] O soberano em chamas da Arena Infernal"
			tasks: [
				{
					entity: "cataclysm:ignis"
					id: "1006000000000041"
					type: "kill"
					value: 1L
				}
				{
					id: "1006000000000042"
					item: {
						count: 1
						id: "cataclysm:the_incinerator"
					}
					type: "item"
				}
			]
			rewards: [
				{
					id: "1006000000000043"
					item: {
						count: 1
						id: "cataclysm:bulwark_of_the_flame"
					}
					type: "item"
				}
				{
					id: "1006000000000044"
					type: "xp_levels"
					xp_levels: 35
				}
			]
			title: "O Carrasco das Cinzas: Ignis"
			x: -6.0d
			y: -2.5d
		}
		{
			dependencies: ["1006000000000020"]
			description: [
				"Nas entranhas da Fabrica Ancestral descansa o Arauto (The Harbinger) — uma temivel arma cibernetica-wither do apocalipse."
				"Ele dispara feixes continuos de laser letal e chuva teleguiada de misseis wither. Sobreviva a tempestade mecanica para extrair o Olho Mecanico!"
			]
			icon: {
				id: "cataclysm:void_core"
			}
			id: "1006000000000050"
			shape: "diamond"
			size: 1.6d
			subtitle: "[Dificuldade: Extrema] O titã cibernetico de artilharia wither da Fabrica Ancestral"
			tasks: [
				{
					entity: "cataclysm:the_harbinger"
					id: "1006000000000051"
					type: "kill"
					value: 1L
				}
			]
			rewards: [
				{
					count: 2
					id: "1006000000000052"
					item: {
						count: 1
						id: "minecraft:netherite_block"
					}
					type: "item"
				}
				{
					id: "1006000000000053"
					type: "xp_levels"
					xp_levels: 35
				}
			]
			title: "A Máquina do Fim: The Harbinger"
			x: -6.0d
			y: 2.5d
		}
		{
			dependencies: ["1006000000000010"]
			description: [
				"No fosso mais profundo da Cidade Submersa, realize o Sacrificio Abissal no Altar do Abismo."
				"O Leviata emerge com suas garras titanicas e boca de fendas dimensionais, invocando buracos negros e turbilhoes maremotos."
				"Sobreviva a este deus marinho para forjar as Manoplas do Maelstrom!"
			]
			icon: {
				id: "cataclysm:abyssal_sacrifice"
			}
			id: "1006000000000060"
			shape: "diamond"
			size: 1.6d
			subtitle: "[Dificuldade: Extrema] O deus ancestral das profundezas e dos buracos negros"
			tasks: [
				{
					entity: "cataclysm:the_leviathan"
					id: "1006000000000061"
					type: "kill"
					value: 1L
				}
			]
			rewards: [
				{
					id: "1006000000000062"
					item: {
						count: 1
						id: "cataclysm:gauntlet_of_maelstrom"
					}
					type: "item"
				}
				{
					id: "1006000000000063"
					type: "xp_levels"
					xp_levels: 40
				}
			]
			title: "O Soberano dos Oceanos: The Leviathan"
			x: -6.0d
			y: 0.0d
		}
		{
			dependencies: [
				"1006000000000040"
				"1006000000000050"
				"1006000000000060"
			]
			description: [
				"Voce superou os terrores do Overworld, dominou o vapor do Create, desbravou o Crepusculo e o Bumblezone, forjou as armas runicas lendarias e destruiu todos os titas cataclismicos."
				"Seu legado no Mundo Eterno esta gravado para sempre nas estrelas. Nada mais pode ameacar a sua supremacia!"
			]
			icon: {
				id: "cataclysm:gauntlet_of_guard"
			}
			id: "1006000000000070"
			shape: "hexagon"
			size: 2.0d
			subtitle: "A consumação suprema da jornada do seu Mundo Eterno"
			tasks: [
				{
					id: "1006000000000071"
					title: "O Conquistador Imortal do BlessForge"
					type: "checkmark"
				}
			]
			rewards: [
				{
					count: 1
					id: "1006000000000072"
					item: {
						count: 1
						id: "minecraft:dragon_egg"
					}
					type: "item"
				}
				{
					count: 4
					id: "1006000000000073"
					item: {
						count: 1
						id: "minecraft:netherite_block"
					}
					type: "item"
				}
				{
					id: "1006000000000074"
					type: "xp_levels"
					xp_levels: 100
				}
			]
			title: "O Panteao da Eternidade"
			x: -3.5d
			y: 0.0d
		}
	]
}
"""

chapters = [
    ("capitulo_3_twilight.snbt", TWILIGHT_SNBT),
    ("capitulo_4_bumblezone.snbt", BUMBLEZONE_SNBT),
    ("capitulo_5_arsenal.snbt", ARSENAL_SNBT),
    ("capitulo_6_cataclysm.snbt", CATACLYSM_SNBT),
]

dir_workspace = "/home/n31415/Games/Minecraft/Ultimate Mods/config/ftbquests/quests/chapters"
dir_game = "/home/n31415/Minecraft/config/ftbquests/quests/chapters"

for filename, content in chapters:
    # 1. Check no unescaped ampersand
    assert "&" not in content, f"ERRO: Ampersand encontrado em {filename}"

    # 2. Check coordinates distance
    coords = []
    for m in re.finditer(r"x:\s*([-\d\.]+)d\s*\n\s*y:\s*([-\d\.]+)d", content):
        coords.append((float(m.group(1)), float(m.group(2))))

    min_d = 999.0
    for i in range(len(coords)):
        for j in range(i+1, len(coords)):
            d = math.hypot(coords[i][0] - coords[j][0], coords[i][1] - coords[j][1])
            if d < min_d:
                min_d = d

    print(f"[{filename}] {len(coords)} quests validadas. Distância mínima: {min_d:.2f}")
    assert min_d >= 2.50, f"ERRO: Distância muito curta ({min_d:.2f}) em {filename}"

    # 3. Write to both dirs
    p1 = os.path.join(dir_workspace, filename)
    p2 = os.path.join(dir_game, filename)

    with open(p1, "w", encoding="utf-8") as f:
        f.write(content)
    with open(p2, "w", encoding="utf-8") as f:
        f.write(content)

print("\n🎉 TODOS OS CAPÍTULOS FORAM SALVOS COM SUCESSO EM AMBOS OS DIRETÓRIOS!")
