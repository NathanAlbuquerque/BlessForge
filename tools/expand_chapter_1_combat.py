#!/usr/bin/env python3
import os
import re

NEW_QUESTS_SNBT = """
		{
			description: [
				"O Mundo Eterno nao perdoa quem se descobre no escuro sem preparo."
				"Quando a noite cai sobre as colinas, esqueletos e arqueiros cercam as planicies com disparos a distancia."
				"Utilize seu escudo para rebater flechas, aproxime-se em zigue-zague e elimine a ameaca para recolher municoes preciosas."
			]
			icon: {
				id: "minecraft:bow"
			}
			id: "1001000000000710"
			shape: "circle"
			size: 1.1d
			subtitle: "[Dificuldade: Media] Sobreviva a chuva de flechas na noite aberta"
			dependencies: ["1001000000000320"]
			tasks: [
				{
					entity: "minecraft:skeleton"
					id: "1001000000000711"
					type: "kill"
					value: 15L
				}
				{
					id: "1001000000000712"
					item: {
						count: 1
						id: "minecraft:bow"
					}
					type: "item"
				}
				{
					count: 32L
					id: "1001000000000713"
					item: {
						count: 1
						id: "minecraft:arrow"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 16
					id: "1001000000000714"
					item: {
						count: 1
						id: "minecraft:spectral_arrow"
					}
					type: "item"
				}
				{
					id: "1001000000000715"
					type: "xp_levels"
					xp_levels: 5
				}
			]
			title: "Cacada Noturna: Hordas Esqueleticas"
			x: -1.5d
			y: -3.5d
		}
		{
			description: [
				"Um silvo sutil pelas suas costas pode desfazer horas de mineracao e construcao."
				"Para vencer Creepers sem sofrer danos colossais, golpeie e recue imediatamente, ou use seu escudo para absorver o impacto frontal."
				"Reuna a polvora necessaria para preparar explosivos controlados de mineracao e municao!"
			]
			icon: {
				id: "minecraft:gunpowder"
			}
			id: "1001000000000720"
			shape: "circle"
			size: 1.1d
			subtitle: "[Dificuldade: Media] Elimine o pesadelo de qualquer construtor sem detonar"
			dependencies: ["1001000000000710"]
			tasks: [
				{
					entity: "minecraft:creeper"
					id: "1001000000000721"
					type: "kill"
					value: 10L
				}
				{
					count: 16L
					id: "1001000000000722"
					item: {
						count: 1
						id: "minecraft:gunpowder"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 8
					id: "1001000000000723"
					item: {
						count: 1
						id: "minecraft:tnt"
					}
					type: "item"
				}
				{
					id: "1001000000000724"
					type: "xp_levels"
					xp_levels: 6
				}
			]
			title: "Risco Explosivo: Emboscada de Creepers"
			x: -0.5d
			y: -4.5d
		}
		{
			description: [
				"As minas abandonadas que cortam as fendas do Terralith guardam tesouros, mas tambem ninhos letais de Aranhas das Cavernas."
				"Seu veneno consome seus pontos de vida rapidamente ate deixa-lo a beira da morte."
				"Dica de ouro: Sempre carregue um balde de leite para cortar efeitos venenosos instantaneamente e tochas para neutralizar os geradores."
			]
			icon: {
				id: "minecraft:spider_eye"
			}
			id: "1001000000000730"
			shape: "circle"
			size: 1.1d
			subtitle: "[Dificuldade: Media] Invada tuneis infestados de aranhas peconhentas"
			dependencies: ["1001000000000710"]
			tasks: [
				{
					entity: "minecraft:cave_spider"
					id: "1001000000000731"
					type: "kill"
					value: 8L
				}
				{
					id: "1001000000000732"
					item: {
						count: 1
						id: "minecraft:milk_bucket"
					}
					type: "item"
				}
				{
					count: 16L
					id: "1001000000000733"
					item: {
						count: 1
						id: "minecraft:string"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 2
					id: "1001000000000734"
					item: {
						count: 1
						id: "minecraft:golden_apple"
					}
					type: "item"
				}
				{
					id: "1001000000000735"
					type: "xp_levels"
					xp_levels: 6
				}
			]
			title: "O Veneno nas Trevas: Minas Abandonadas"
			x: -1.5d
			y: -4.5d
		}
		{
			description: [
				"Nas profundezas dos pantanos ou em cabanas isoladas sobre as aguas residem as Bruxas."
				"Elas arremessam pocoes de dano imediato, fraqueza e lentidao enquanto se curam constantemente."
				"Abata-as rapidamente antes que consigam arremessar seu arsenal quimico e colete materiais para iniciar seus proprios estudos alquimicos!"
			]
			icon: {
				id: "minecraft:brewing_stand"
			}
			id: "1001000000000740"
			shape: "circle"
			size: 1.1d
			subtitle: "[Dificuldade: Media] Cuidado com frascos arremessados de lentidao e veneno"
			dependencies: ["1001000000000730"]
			tasks: [
				{
					entity: "minecraft:witch"
					id: "1001000000000741"
					type: "kill"
					value: 3L
				}
				{
					count: 8L
					id: "1001000000000742"
					item: {
						count: 1
						id: "minecraft:glass_bottle"
					}
					type: "item"
				}
				{
					count: 2L
					id: "1001000000000743"
					item: {
						count: 1
						id: "minecraft:fermented_spider_eye"
					}
					type: "item"
				}
			]
			rewards: [
				{
					id: "1001000000000744"
					item: {
						count: 1
						id: "minecraft:brewing_stand"
					}
					type: "item"
				}
				{
					count: 4
					id: "1001000000000745"
					item: {
						count: 1
						id: "minecraft:blaze_powder"
					}
					type: "item"
				}
				{
					id: "1001000000000746"
					type: "xp_levels"
					xp_levels: 6
				}
			]
			title: "Maldicao do Pantano: O Covil da Bruxa"
			x: -0.5d
			y: -5.5d
		}
		{
			description: [
				"O mod Caverns and Chasms adiciona o Minerio de Prata as camadas profundas de ardosia."
				"A prata possui propriedades sagradas purificadoras: armamentos feitos ou reforcados com prata causam dano devastador aumentado contra zumbis, esqueletos e fantasmas."
				"Extraia esse metal nobre para equilibrar as batalhas noturnas a seu favor."
			]
			icon: {
				id: "caverns_and_chasms:silver_ingot"
			}
			id: "1001000000000750"
			shape: "circle"
			size: 1.1d
			subtitle: "[Dificuldade: Media] O minerio subterraneo que queima criaturas mortas-vivas"
			dependencies: ["1001000000000310"]
			tasks: [
				{
					count: 16L
					id: "1001000000000751"
					item: {
						count: 1
						id: "caverns_and_chasms:silver_ingot"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 1
					id: "1001000000000752"
					item: {
						count: 1
						id: "minecraft:golden_apple"
					}
					type: "item"
				}
				{
					id: "1001000000000753"
					type: "xp_levels"
					xp_levels: 5
				}
			]
			title: "A Prata Purificadora"
			x: 0.5d
			y: -3.5d
		}
		{
			description: [
				"Uma espada comum de ferro e apenas o comeco da sua jornada de combate."
				"Com o Simply Swords, voce pode forjar armas pesadas com habilidades e posturas unicas, como Espadoes (Claymores), Lancas, Cutelos e Alabardas."
				"Forje uma Claymore de Ferro para esmagar multiplos inimigos em arcos amplos de varredura!"
			]
			icon: {
				id: "simplyswords:iron_claymore"
			}
			id: "1001000000000760"
			shape: "circle"
			size: 1.1d
			subtitle: "[Dificuldade: Media] Empunhe armamentos de impacto com o Simply Swords"
			dependencies: ["1001000000000750"]
			tasks: [
				{
					id: "1001000000000761"
					item: {
						count: 1
						id: "simplyswords:iron_claymore"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 8
					id: "1001000000000762"
					item: {
						count: 1
						id: "minecraft:iron_ingot"
					}
					type: "item"
				}
				{
					id: "1001000000000763"
					type: "xp_levels"
					xp_levels: 6
				}
			]
			title: "Laminas Especializadas: A Forja de Combate"
			x: 1.5d
			y: -3.5d
		}
		{
			description: [
				"Os oceanos e rios guardam frotas naufragadas e templos submersos infestados de Afogados (Drowned)."
				"Muitos deles empunham tridentes letais capazes de perfurar sua armadura a distancia."
				"Derrote esses carniceiros das aguas e recupere Conchas de Nautilo para futuros artefatos marinhos!"
			]
			icon: {
				id: "minecraft:nautilus_shell"
			}
			id: "1001000000000770"
			shape: "circle"
			size: 1.1d
			subtitle: "[Dificuldade: Media] Mergulhe em ruinas oceanicas e enfrente zumbis aquaticos"
			dependencies: ["1001000000000710"]
			tasks: [
				{
					entity: "minecraft:drowned"
					id: "1001000000000771"
					type: "kill"
					value: 12L
				}
				{
					id: "1001000000000772"
					item: {
						count: 1
						id: "minecraft:nautilus_shell"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 8
					id: "1001000000000773"
					item: {
						count: 1
						id: "minecraft:prismarine_shard"
					}
					type: "item"
				}
				{
					id: "1001000000000774"
					type: "xp_levels"
					xp_levels: 6
				}
			]
			title: "O Terror dos Mares: Afogados e as Profundezas"
			x: 0.5d
			y: -4.5d
		}
		{
			description: [
				"Patrulhas de Saqueadores armados com bestas pesadas marcham pelas planicies em busca de vilarejos para pilhar."
				"O capitao do grupo carrega um estandarte sombrio e, na versao 1.21, um Frasco Sinistro (Ominous Bottle)."
				"Elimine a patrulha e reivindique a besta militar e seus mantimentos!"
			]
			icon: {
				id: "minecraft:crossbow"
			}
			id: "1001000000000780"
			shape: "circle"
			size: 1.1d
			subtitle: "[Dificuldade: Media] Elimine batedores pillagers que rondam as vilas"
			dependencies: ["1001000000000760"]
			tasks: [
				{
					entity: "minecraft:pillager"
					id: "1001000000000781"
					type: "kill"
					value: 10L
				}
				{
					id: "1001000000000782"
					item: {
						count: 1
						id: "minecraft:crossbow"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 48
					id: "1001000000000783"
					item: {
						count: 1
						id: "minecraft:arrow"
					}
					type: "item"
				}
				{
					id: "1001000000000784"
					type: "xp_levels"
					xp_levels: 6
				}
			]
			title: "A Patrulha Hostil: Batedores Saqueadores"
			x: 1.5d
			y: -4.5d
		}
		{
			description: [
				"Com as estruturas do Explorify e masmorras classicas espalhadas pelas cavernas, geradores de monstros (spawners) produzem hordas infinitas de mortos-vivos."
				"Avance com coragem, coloque tochas nas quatro faces do gerador para neutraliza-lo e abra os baus protegidos com o sistema Lootr!"
			]
			icon: {
				id: "minecraft:spawner"
			}
			id: "1001000000000790"
			shape: "circle"
			size: 1.1d
			subtitle: "[Dificuldade: Media] Encontre e neutralize um ninho subterraneo de monstros"
			dependencies: ["1001000000000720"]
			tasks: [
				{
					entity: "minecraft:zombie"
					id: "1001000000000791"
					type: "kill"
					value: 20L
				}
				{
					count: 4L
					id: "1001000000000792"
					item: {
						count: 1
						id: "minecraft:chest"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 2
					id: "1001000000000793"
					item: {
						count: 1
						id: "minecraft:name_tag"
					}
					type: "item"
				}
				{
					id: "1001000000000794"
					item: {
						count: 1
						id: "minecraft:saddle"
					}
					type: "item"
				}
				{
					id: "1001000000000795"
					type: "xp_levels"
					xp_levels: 6
				}
			]
			title: "Desbravador de Masmorras: Explorify e Spawners"
			x: 0.5d
			y: -5.5d
		}
		{
			description: [
				"Monstros equipados com espadas encantadas, explosoes a queima-roupa e flechadas certeiras pulverizam qualquer aventureiro desprotegido."
				"Forje um conjunto completo de armadura de ferro e utilize a bigorna para reparar e preparar seus equipamentos para as provacoes pesadas que estao por vir."
			]
			icon: {
				id: "minecraft:iron_chestplate"
			}
			id: "1001000000000800"
			shape: "circle"
			size: 1.1d
			subtitle: "[Dificuldade: Media] Nao ouse se aventurar sem estar protegido da cabeca aos pes"
			dependencies: ["1001000000000320"]
			tasks: [
				{
					id: "1001000000000801"
					item: {
						count: 1
						id: "minecraft:iron_helmet"
					}
					type: "item"
				}
				{
					id: "1001000000000802"
					item: {
						count: 1
						id: "minecraft:iron_chestplate"
					}
					type: "item"
				}
				{
					id: "1001000000000803"
					item: {
						count: 1
						id: "minecraft:iron_leggings"
					}
					type: "item"
				}
				{
					id: "1001000000000804"
					item: {
						count: 1
						id: "minecraft:iron_boots"
					}
					type: "item"
				}
			]
			rewards: [
				{
					id: "1001000000000805"
					item: {
						count: 1
						id: "minecraft:anvil"
					}
					type: "item"
				}
				{
					id: "1001000000000806"
					type: "xp_levels"
					xp_levels: 7
				}
			]
			title: "A Carapaca do Guerreiro: Blindagem Completa"
			x: 2.5d
			y: -3.5d
		}

		{
			description: [
				"Erguendo-se sobre a paisagem, as Torres de Vigia e Postos Avancados de Saqueadores sao fortalezas altamente hostis."
				"Varias duzias de atiradores cercam a estrutura, enquanto baus no topo guardam projetos e tesouros militares."
				"Cerque a torre, abata o esquadrao completo e capture o temido Frasco Sinistro (Ominous Bottle)!"
			]
			icon: {
				id: "minecraft:ominous_bottle"
			}
			id: "1001000000000810"
			shape: "pentagon"
			size: 1.25d
			subtitle: "[Dificuldade: Dificil] Invada o reduto fortificado dos Pillagers"
			dependencies: [
				"1001000000000780"
				"1001000000000800"
			]
			tasks: [
				{
					entity: "minecraft:pillager"
					id: "1001000000000811"
					type: "kill"
					value: 20L
				}
				{
					id: "1001000000000812"
					item: {
						count: 1
						id: "minecraft:ominous_bottle"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 16
					id: "1001000000000813"
					item: {
						count: 1
						id: "minecraft:emerald"
					}
					type: "item"
				}
				{
					count: 16
					id: "1001000000000814"
					item: {
						count: 1
						id: "minecraft:firework_rocket"
					}
					type: "item"
				}
				{
					id: "1001000000000815"
					type: "xp_levels"
					xp_levels: 10
				}
			]
			title: "A Fortaleza Saqueadora: O Posto Avancado"
			x: 2.5d
			y: -4.5d
		}
		{
			description: [
				"Entrar em um vilarejo com o efeito do Mau Pressagio ativado pelo Frasco Sinistro inicia uma Invasao militar completa (Raid)."
				"Vindicadores correm com machados letais, Invocadores (Evokers) invocam presas magicas pelo chao e o colosso Devastador (Ravager) esmaga tudo pelo caminho."
				"Sobreviva a todas as ondas para conquistar a imortalidade do Totem e salvar os habitantes!"
			]
			icon: {
				id: "minecraft:totem_of_undying"
			}
			id: "1001000000000820"
			shape: "pentagon"
			size: 1.25d
			subtitle: "[Dificuldade: Dificil] Defenda o vilarejo contra ondas implacaveis de invasores"
			dependencies: ["1001000000000810"]
			tasks: [
				{
					entity: "minecraft:ravager"
					id: "1001000000000821"
					type: "kill"
					value: 1L
				}
				{
					entity: "minecraft:evoker"
					id: "1001000000000822"
					type: "kill"
					value: 1L
				}
				{
					id: "1001000000000823"
					item: {
						count: 1
						id: "minecraft:totem_of_undying"
					}
					type: "item"
				}
			]
			rewards: [
				{
					id: "1001000000000824"
					item: {
						count: 1
						id: "minecraft:enchanted_golden_apple"
					}
					type: "item"
				}
				{
					id: "1001000000000825"
					item: {
						count: 1
						id: "minecraft:bell"
					}
					type: "item"
				}
				{
					id: "1001000000000826"
					type: "xp_levels"
					xp_levels: 15
				}
			]
			title: "O Cerco a Vila: O Massacre do Devastador"
			x: 3.5d
			y: -4.5d
		}
		{
			description: [
				"O Simply Swords esconde Tabuas Runicas (Runic Tablets) nos baus das estruturas mais hostis do Overworld e alem."
				"Esta reliquia antiga e o componente fundamental para fundir armas lendarias com habilidades devastadoras no altar runico."
				"Desbrave grandes masmorras, navios piratas ou fortalezas para reivindicar este artefato raro!"
			]
			icon: {
				id: "simplyswords:runic_tablet"
			}
			id: "1001000000000830"
			shape: "pentagon"
			size: 1.25d
			subtitle: "[Dificuldade: Dificil] Conquiste a reliquia runica nos baus mais perigosos"
			dependencies: [
				"1001000000000760"
				"1001000000000340"
			]
			tasks: [
				{
					id: "1001000000000831"
					item: {
						count: 1
						id: "simplyswords:runic_tablet"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 4
					id: "1001000000000832"
					item: {
						count: 1
						id: "minecraft:diamond"
					}
					type: "item"
				}
				{
					id: "1001000000000833"
					type: "xp_levels"
					xp_levels: 12
				}
			]
			title: "O Santuario das Laminas: A Tabua Runica"
			x: 3.5d
			y: -3.5d
		}
		{
			description: [
				"Enterradas no subterraneo profundo de cobre e tufo repousam as monumentais Camaras de Provacao (Trial Chambers) do Minecraft 1.21."
				"Os Trial Spawners ajustam a quantidade de monstros dinamicamente, gerando hordas de Bogged (esqueletos venenosos), zumbis velozes e armadilhas de lodo."
				"Derrote a onda ate que o gerador cuspa a cobicada Chave do Julgamento (Trial Key)!"
			]
			icon: {
				id: "minecraft:trial_key"
			}
			id: "1001000000000840"
			shape: "pentagon"
			size: 1.25d
			subtitle: "[Dificuldade: Dificil] Sobreviva aos geradores inteligentes de combate"
			dependencies: [
				"1001000000000800"
				"1001000000000340"
			]
			tasks: [
				{
					id: "1001000000000841"
					item: {
						count: 1
						id: "minecraft:trial_key"
					}
					type: "item"
				}
				{
					entity: "minecraft:bogged"
					id: "1001000000000842"
					type: "kill"
					value: 10L
				}
			]
			rewards: [
				{
					count: 8
					id: "1001000000000843"
					item: {
						count: 1
						id: "minecraft:chiseled_copper"
					}
					type: "item"
				}
				{
					id: "1001000000000844"
					type: "xp_levels"
					xp_levels: 12
				}
			]
			title: "Incursao as Camaras de Provacao"
			x: 4.5d
			y: -3.5d
		}
		{
			description: [
				"O Breeze e a entidade guardia das Camaras de Provacao. Ele se movimenta saltando dezenas de blocos no ar em trajetorias imprevisiveis."
				"Seus projeteis de vento detonam botoes, abrem portas e arremessam voce contra paredes e espinhos."
				"Use reflexos rapidos com seu escudo ou rebata seus projeteis para derrota-lo e recolher as Varas de Brisa (Breeze Rods)!"
			]
			icon: {
				id: "minecraft:breeze_rod"
			}
			id: "1001000000000850"
			shape: "pentagon"
			size: 1.25d
			subtitle: "[Dificuldade: Dificil] Desvie das rajadas aereas e rebata as bombas de vento"
			dependencies: ["1001000000000840"]
			tasks: [
				{
					entity: "minecraft:breeze"
					id: "1001000000000851"
					type: "kill"
					value: 3L
				}
				{
					count: 4L
					id: "1001000000000852"
					item: {
						count: 1
						id: "minecraft:breeze_rod"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 16
					id: "1001000000000853"
					item: {
						count: 1
						id: "minecraft:wind_charge"
					}
					type: "item"
				}
				{
					id: "1001000000000854"
					type: "xp_levels"
					xp_levels: 15
				}
			]
			title: "O Duelista dos Ventos: O Breeze das Alturas"
			x: 4.5d
			y: -4.5d
		}

		{
			description: [
				"Ao ingerir um Frasco Sinistro antes de pisar em uma Camara de Provacao, a prova se converte no terror do 'Ominous Trial'."
				"Geradores passam a invocar monstros trajando armaduras completas de diamante e ferro encantadas, enquanto pocoes de dano e fogo caem continuamente do teto."
				"Sobreviva a esse inferno tatico, conquiste a Chave Sinistra, abra o Cofre Ominous para extrair o lendario Nucleo Pesado (Heavy Core) e forje a lendaria Maca (Mace) — a arma suprema com dano de impacto infinito em queda livre!"
			]
			icon: {
				id: "minecraft:mace"
			}
			id: "1001000000000860"
			shape: "diamond"
			size: 1.5d
			subtitle: "[Dificuldade: Extrema] Conquiste o Nucleo Pesado sob a furia do evento Ominous"
			dependencies: [
				"1001000000000850"
				"1001000000000820"
			]
			tasks: [
				{
					id: "1001000000000861"
					item: {
						count: 1
						id: "minecraft:ominous_trial_key"
					}
					type: "item"
				}
				{
					id: "1001000000000862"
					item: {
						count: 1
						id: "minecraft:heavy_core"
					}
					type: "item"
				}
				{
					id: "1001000000000863"
					item: {
						count: 1
						id: "minecraft:mace"
					}
					type: "item"
				}
			]
			rewards: [
				{
					id: "1001000000000864"
					item: {
						count: 1
						id: "minecraft:heart_of_the_sea"
					}
					type: "item"
				}
				{
					count: 2
					id: "1001000000000865"
					item: {
						count: 1
						id: "minecraft:diamond_block"
					}
					type: "item"
				}
				{
					id: "1001000000000866"
					type: "xp_levels"
					xp_levels: 30
				}
			]
			title: "O Julgamento Sinistro: O Nucleo e a Maca"
			x: 5.5d
			y: -5.0d
		}
		{
			description: [
				"Nas profundezas mais abissais do mundo (abaixo de Y=-50) dorme o bioma Deep Dark e as ruinas colossais da Cidade Ancestral."
				"No dominio do Sculk, a visao e inutil e o som e o seu maior inimigo. Qualquer passo sem agachar ou bau aberto sem la fara os Gritadores (Sculk Shriekers) uivarem para a escuridao."
				"No quarto grito, o Warden emerge do solo com vida colossal e um ataque sonoro devastador que atravessa paredes e escudos."
				"Mantenha a calma, ande agachado sobre blocos de la, saqueie a cidade proibida e recupere os Fragmentos de Eco para forjar a Bussola de Recuperacao!"
			]
			icon: {
				id: "minecraft:recovery_compass"
			}
			id: "1001000000000870"
			shape: "diamond"
			size: 1.5d
			subtitle: "[Dificuldade: Extrema] Ande nas pontas dos pes no reino do Warden ou pereca"
			dependencies: [
				"1001000000000340"
				"1001000000000800"
			]
			tasks: [
				{
					count: 8L
					id: "1001000000000871"
					item: {
						count: 1
						id: "minecraft:echo_shard"
					}
					type: "item"
				}
				{
					id: "1001000000000872"
					item: {
						count: 1
						id: "minecraft:recovery_compass"
					}
					type: "item"
				}
				{
					id: "1001000000000873"
					item: {
						count: 1
						id: "minecraft:sculk_catalyst"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 2
					id: "1001000000000874"
					item: {
						count: 1
						id: "minecraft:enchanted_golden_apple"
					}
					type: "item"
				}
				{
					count: 2
					id: "1001000000000875"
					item: {
						count: 1
						id: "minecraft:netherite_scrap"
					}
					type: "item"
				}
				{
					id: "1001000000000876"
					type: "xp_levels"
					xp_levels: 35
				}
			]
			title: "O Silencio dos Abismos: A Cidade Ancestral"
			x: 3.5d
			y: -6.0d
		}
"""

def update_file(path):
    print("Atualizando:", path)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Find the last closing bracket of quests: [ ... ]
    # Quests array ends before final '}'
    last_bracket_idx = content.rfind("]")
    if last_bracket_idx == -1:
        print("Erro: ']' não encontrado em", path)
        return False

    new_content = content[:last_bracket_idx] + NEW_QUESTS_SNBT + "\t" + content[last_bracket_idx:]

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Sucesso ao atualizar", path)
    return True

target1 = "/home/n31415/Games/Minecraft/Ultimate Mods/config/ftbquests/quests/chapters/capitulo_1_pioneiro.snbt"
target2 = "/home/n31415/Minecraft/config/ftbquests/quests/chapters/capitulo_1_pioneiro.snbt"

update_file(target1)
update_file(target2)
