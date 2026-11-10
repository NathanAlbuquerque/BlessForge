#!/usr/bin/env python3
import os

SNBT_CONTENT = """{
	default_hide_dependency_lines: false
	default_quest_shape: "circle"
	filename: "capitulo_2_create"
	group: "1A2B3C4D5E6F7001"
	icon: {
		id: "create:cogwheel"
	}
	id: "1002000000000001"
	order_index: 2
	title: "2. Revolucao do Vapor e Balistica"
	quests: [
		{
			description: [
				"A pedra angular de toda a engenharia cinetica do Create."
				"Misture cascalho de ferro com andesito para criar as ligas que suportam o estresse de rotacao (Stress Units) das suas maquinas industriais."
				"Com esta liga, voce forja eixos, pequenas e grandes engrenagens para conduzir movimento por toda a sua oficina."
			]
			icon: {
				id: "create:andesite_alloy"
			}
			id: "1002000000000010"
			shape: "hexagon"
			size: 1.5d
			subtitle: "O nascimento do poder mecanico"
			tasks: [
				{
					count: 16L
					id: "1002000000000011"
					item: {
						count: 1
						id: "create:andesite_alloy"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 16
					id: "1002000000000012"
					item: {
						count: 1
						id: "create:shaft"
					}
					type: "item"
				}
				{
					count: 8
					id: "1002000000000013"
					item: {
						count: 1
						id: "create:cogwheel"
					}
					type: "item"
				}
				{
					count: 4
					id: "1002000000000014"
					item: {
						count: 1
						id: "create:large_cogwheel"
					}
					type: "item"
				}
			]
			title: "A Pedra Angular: Liga de Andesito"
			x: -11.0d
			y: 0.0d
		}
		{
			dependencies: ["1002000000000010"]
			description: [
				"A forca da agua corrente impulsiona suas primeiras palhetas giratorias."
				"A Roda Dagua gera a Capacidade de Estresse inicial sem consumir combustivel algum, perfeita para alimentar suas primeiras prensas e moinhos continuos."
				"Dica: Faca a agua fluir ao redor de toda a circunferencia da roda para atingir a velocidade angular maxima!"
			]
			icon: {
				id: "create:water_wheel"
			}
			id: "1002000000000020"
			shape: "circle"
			size: 1.1d
			subtitle: "A correnteza dos rios ao seu favor"
			tasks: [
				{
					id: "1002000000000021"
					item: {
						count: 1
						id: "create:water_wheel"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 8
					id: "1002000000000022"
					item: {
						count: 1
						id: "create:shaft"
					}
					type: "item"
				}
				{
					id: "1002000000000023"
					type: "xp_levels"
					xp_levels: 4
				}
			]
			title: "Energia Hidraulica Cinetica"
			x: -8.5d
			y: 0.0d
		}
		{
			dependencies: ["1002000000000020"]
			description: [
				"Posicione a Prensa Mecanica sobre uma bancada ou mesa e transmita forca rotacional ao seu topo."
				"Ela achata lingotes de ferro, cobre e latao em chapas de alta precisao estrutural, necessarias para montar carretilhas, dutos e armamentos."
			]
			icon: {
				id: "create:mechanical_press"
			}
			id: "1002000000000030"
			shape: "circle"
			size: 1.2d
			subtitle: "Amassando metais pesados em laminas"
			tasks: [
				{
					id: "1002000000000031"
					item: {
						count: 1
						id: "create:mechanical_press"
					}
					type: "item"
				}
				{
					count: 8L
					id: "1002000000000032"
					item: {
						count: 1
						id: "create:iron_sheet"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 8
					id: "1002000000000033"
					item: {
						count: 1
						id: "create:iron_sheet"
					}
					type: "item"
				}
				{
					id: "1002000000000034"
					type: "xp_levels"
					xp_levels: 5
				}
			]
			title: "Prensagem Industrial"
			x: -6.0d
			y: 0.0d
		}
		{
			dependencies: ["1002000000000020"]
			description: [
				"O corte e a moagem automatizados transformam troncos em tabuas perfeitas sem perdas e trituram trigo e minerais em pos finos."
				"A Serra Mecanica pode cortar arvores inteiras ou funcionar como bancada de corte continuo de blocos em esteiras rolantes."
			]
			icon: {
				id: "create:mechanical_saw"
			}
			id: "1002000000000040"
			shape: "circle"
			size: 1.1d
			subtitle: "Serraria e processamento mineral continuo"
			tasks: [
				{
					id: "1002000000000041"
					item: {
						count: 1
						id: "create:mechanical_saw"
					}
					type: "item"
				}
				{
					id: "1002000000000042"
					item: {
						count: 1
						id: "create:millstone"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 16
					id: "1002000000000043"
					item: {
						count: 1
						id: "minecraft:oak_log"
					}
					type: "item"
				}
				{
					id: "1002000000000044"
					type: "xp_levels"
					xp_levels: 5
				}
			]
			title: "Corte e Moagem de Precisao"
			x: -6.0d
			y: -2.5d
		}
		{
			dependencies: ["1002000000000030"]
			description: [
				"Ao soprar vento atraves de agua, lava ou fogo, o Ventilador Enclausurado processa itens em massa no chao ou sobre esteiras."
				"• Vento com Agua: Lava cascalho para extrair pepitas de ferro e sementes."
				"• Vento com Lava: Funde pilhas inteiras de minérios sem gastar carvao!"
				"• Vento com Fogo de Almas: Assombra itens, transformando materiais comuns em misticos."
			]
			icon: {
				id: "create:encased_fan"
			}
			id: "1002000000000050"
			shape: "circle"
			size: 1.1d
			subtitle: "Lavagem, fundicao e assombro em massa"
			tasks: [
				{
					id: "1002000000000051"
					item: {
						count: 1
						id: "create:encased_fan"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 16
					id: "1002000000000052"
					item: {
						count: 1
						id: "minecraft:iron_nugget"
					}
					type: "item"
				}
				{
					id: "1002000000000053"
					type: "xp_levels"
					xp_levels: 5
				}
			]
			title: "Ventilacao Cinetica e Lavagem"
			x: -3.5d
			y: 0.0d
		}
		{
			dependencies: ["1002000000000050"]
			description: [
				"O Misturador Mecanico opera sobre uma Bacia para combinar liquidos e solidos com agitacao termica e cinetica."
				"Ele e o responsavel por criar as ligas mais avancadas do Create, como o cobicado Latao (Brass) a partir de Cobre e Zinco aquecidos."
			]
			icon: {
				id: "create:mechanical_mixer"
			}
			id: "1002000000000060"
			shape: "circle"
			size: 1.1d
			subtitle: "A alquimia mecanica das ligas"
			tasks: [
				{
					id: "1002000000000061"
					item: {
						count: 1
						id: "create:mechanical_mixer"
					}
					type: "item"
				}
				{
					id: "1002000000000062"
					item: {
						count: 1
						id: "create:basin"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 8
					id: "1002000000000063"
					item: {
						count: 1
						id: "minecraft:copper_ingot"
					}
					type: "item"
				}
				{
					id: "1002000000000064"
					type: "xp_levels"
					xp_levels: 6
				}
			]
			title: "Mistura e Reacao Termica"
			x: -1.0d
			y: 0.0d
		}
		{
			dependencies: [
				"1002000000000060"
				"1002000000000130"
			]
			description: [
				"Aquecendo a bacia com um Queimador de Blaze e combinando Cobre com Zinco, voce alcanca a Era do Latao (Brass)!"
				"O latao abre as portas para a computacao mecanica, tubos eletronicos, filtros de logica e esteiras inteligentes."
			]
			icon: {
				id: "create:brass_ingot"
			}
			id: "1002000000000070"
			shape: "diamond"
			size: 1.3d
			subtitle: "A entrada triunfal na Era de Ouro da engenharia"
			tasks: [
				{
					count: 16L
					id: "1002000000000071"
					item: {
						count: 1
						id: "create:brass_ingot"
					}
					type: "item"
				}
				{
					count: 4L
					id: "1002000000000072"
					item: {
						count: 1
						id: "create:brass_casing"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 8
					id: "1002000000000073"
					item: {
						count: 1
						id: "create:brass_sheet"
					}
					type: "item"
				}
				{
					id: "1002000000000074"
					type: "xp_levels"
					xp_levels: 8
				}
			]
			title: "A Nobre Era do Latao"
			x: 1.5d
			y: 0.0d
		}
		{
			dependencies: ["1002000000000070"]
			description: [
				"O Mecanismo de Precisao e o componente mais nobre de maquinas de alta tecnologia."
				"Ele e fabricado atraves de montagem sequencial: coloque uma chapa dourada em uma esteira sob 3 Implantadores (Deployers) adicionando pequenas engrenagens, grandes engrenagens e pepitas de ferro com precisao de relogio!"
			]
			icon: {
				id: "create:precision_mechanism"
			}
			id: "1002000000000080"
			shape: "hexagon"
			size: 1.3d
			subtitle: "Engrenagens de relogio e automatizacao cirurgica"
			tasks: [
				{
					id: "1002000000000081"
					item: {
						count: 1
						id: "create:precision_mechanism"
					}
					type: "item"
				}
				{
					id: "1002000000000082"
					item: {
						count: 1
						id: "create:electron_tube"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 2
					id: "1002000000000083"
					item: {
						count: 1
						id: "create:precision_mechanism"
					}
					type: "item"
				}
				{
					id: "1002000000000084"
					type: "xp_levels"
					xp_levels: 10
				}
			]
			title: "Mecanismo de Alta Precisao"
			x: 4.0d
			y: 0.0d
		}
		{
			dependencies: ["1002000000000070"]
			description: [
				"Esqueca sistemas desorganizados de agua e funis lentos de madeira."
				"Com os Funis de Latao, voce pode programar filtros para extrair apenas itens especificos em quantidades exatas (ex: pilhas de 16 ou 64), integrando diretamente a baus e esteiras."
			]
			icon: {
				id: "create:brass_funnel"
			}
			id: "1002000000000090"
			shape: "circle"
			size: 1.1d
			subtitle: "Triagem e filtros com logica instantanea"
			tasks: [
				{
					count: 2L
					id: "1002000000000091"
					item: {
						count: 1
						id: "create:brass_funnel"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 16
					id: "1002000000000092"
					item: {
						count: 1
						id: "create:brass_sheet"
					}
					type: "item"
				}
				{
					id: "1002000000000093"
					type: "xp_levels"
					xp_levels: 6
				}
			]
			title: "Logistica Avancada de Latao"
			x: 6.5d
			y: 0.0d
		}
		{
			dependencies: ["1002000000000080"]
			description: [
				"As Rodas de Esmagamento sao o ápice da mineracao industrial."
				"Duas rodas colossais girando em sentidos opostos esmagam blocos de minerio bruto, cascalho e pedra com forca descomunal, multiplicando consideravelmente seu rendimento de metais raros!"
			]
			icon: {
				id: "create:crushing_wheel"
			}
			id: "1002000000000100"
			shape: "diamond"
			size: 1.3d
			subtitle: "Multiplicacao colossal de minerios brutos"
			tasks: [
				{
					count: 2L
					id: "1002000000000101"
					item: {
						count: 1
						id: "create:crushing_wheel"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 8
					id: "1002000000000102"
					item: {
						count: 1
						id: "minecraft:raw_iron_block"
					}
					type: "item"
				}
				{
					id: "1002000000000103"
					type: "xp_levels"
					xp_levels: 12
				}
			]
			title: "As Rodas de Esmagamento"
			x: 9.0d
			y: 0.0d
		}
		{
			dependencies: ["1002000000000080"]
			description: [
				"Conecte todos os seus postos do Mundo Eterno atraves de trens automotivos reais sobre trilhos de aco!"
				"Monte estacoes, programe itinerarios para vagoes de carga carregarem seus minerios e viaje pelas paisagens do Terralith contemplando seu progresso."
			]
			icon: {
				id: "create:track"
			}
			id: "1002000000000110"
			shape: "hexagon"
			size: 1.5d
			subtitle: "Conectando continentes nos trilhos do progresso"
			tasks: [
				{
					count: 64L
					id: "1002000000000111"
					item: {
						count: 1
						id: "create:track"
					}
					type: "item"
				}
				{
					id: "1002000000000112"
					item: {
						count: 1
						id: "create:track_station"
					}
					type: "item"
				}
				{
					id: "1002000000000113"
					item: {
						count: 1
						id: "create:controls"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 64
					id: "1002000000000114"
					item: {
						count: 1
						id: "create:track"
					}
					type: "item"
				}
				{
					id: "1002000000000115"
					type: "xp_levels"
					xp_levels: 15
				}
			]
			title: "A Revolucao Ferroviaria"
			x: 11.5d
			y: 0.0d
		}

		{
			dependencies: ["1002000000000030"]
			description: [
				"O transporte de fluidos e vital para refrigeracao, bombas e queima de combustivel."
				"Forje tubulacoes de cobre com chapas de cobre e monte bombas mecanicas para conduzir agua e lava a dezenas de blocos por segundo."
			]
			icon: {
				id: "create:fluid_pipe"
			}
			id: "1002000000000120"
			shape: "circle"
			size: 1.1d
			subtitle: "Dutos de cobre e bombeamento hidraulico"
			tasks: [
				{
					count: 16L
					id: "1002000000000121"
					item: {
						count: 1
						id: "create:fluid_pipe"
					}
					type: "item"
				}
				{
					id: "1002000000000122"
					item: {
						count: 1
						id: "create:mechanical_pump"
					}
					type: "item"
				}
				{
					count: 4L
					id: "1002000000000123"
					item: {
						count: 1
						id: "create:fluid_tank"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 16
					id: "1002000000000124"
					item: {
						count: 1
						id: "create:fluid_pipe"
					}
					type: "item"
				}
				{
					id: "1002000000000125"
					type: "xp_levels"
					xp_levels: 5
				}
			]
			title: "Hidraulica e Dutos de Cobre"
			x: -3.5d
			y: 2.5d
		}
		{
			dependencies: [
				"1002000000000120"
				"1002000000000220"
			]
			description: [
				"A chama viva do Nether agora trabalha para sua forja."
				"Ao aprisionar um Blaze em um Queimador Vazio, ele responde ao carvao, madeira e combustiveis quentes gerando o calor necessario para fundir latao e gerar vapor sob pressao."
			]
			icon: {
				id: "create:blaze_burner"
			}
			id: "1002000000000130"
			shape: "diamond"
			size: 1.25d
			subtitle: "A alma do fogo canalizada para a industria"
			tasks: [
				{
					id: "1002000000000131"
					item: {
						count: 1
						id: "create:blaze_burner"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 32
					id: "1002000000000132"
					item: {
						count: 1
						id: "minecraft:coal"
					}
					type: "item"
				}
				{
					id: "1002000000000133"
					type: "xp_levels"
					xp_levels: 7
				}
			]
			title: "O Queimador de Blaze"
			x: -1.0d
			y: 2.5d
		}
		{
			dependencies: [
				"1002000000000130"
				"1002000000000070"
			]
			description: [
				"Posicione um Motor a Vapor (Steam Engine) fixado a um tanque de fluido aquecido por Queimadores de Blaze."
				"Quando alimentado com agua continua e calor intenso, o tanque se transforma em uma Caldeira de Alta Pressao, gerando estresse cinetico incomparavel capaz de mover oficinas inteiras simultaneamente!"
			]
			icon: {
				id: "create:steam_engine"
			}
			id: "1002000000000140"
			shape: "hexagon"
			size: 1.3d
			subtitle: "A forca motriz maxima da termodinamica"
			tasks: [
				{
					id: "1002000000000141"
					item: {
						count: 1
						id: "create:steam_engine"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 8
					id: "1002000000000142"
					item: {
						count: 1
						id: "create:fluid_tank"
					}
					type: "item"
				}
				{
					id: "1002000000000143"
					type: "xp_levels"
					xp_levels: 10
				}
			]
			title: "A Maquina a Vapor"
			x: -1.0d
			y: 5.0d
		}

		{
			dependencies: ["1002000000000030"]
			description: [
				"Com o mod Create Gunsmithing, a metalurgia se volta para a quimica e balistica."
				"Extraia minerios de Chumbo (Lead) e Enxofre (Sulfur) das fendas do subsolo para iniciar a sintese de capsulas de projeteis e composicoes de polvora concentrada."
			]
			icon: {
				id: "cgs:lead_ingot"
			}
			id: "1002000000000150"
			shape: "circle"
			size: 1.1d
			subtitle: "Chumbo fundido e compostos de enxofre"
			tasks: [
				{
					count: 16L
					id: "1002000000000151"
					item: {
						count: 1
						id: "cgs:lead_ingot"
					}
					type: "item"
				}
				{
					count: 16L
					id: "1002000000000152"
					item: {
						count: 1
						id: "cgs:sulfur"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 32
					id: "1002000000000153"
					item: {
						count: 1
						id: "minecraft:gunpowder"
					}
					type: "item"
				}
				{
					id: "1002000000000154"
					type: "xp_levels"
					xp_levels: 6
				}
			]
			title: "Fundicao de Chumbo e Enxofre"
			x: 4.0d
			y: 2.5d
		}
		{
			dependencies: ["1002000000000150"]
			description: [
				"A primeira arma de fogo da sua oficina balistica."
				"O Mosquete Flintlock utiliza cartuchos de papel comprimido com esferas de chumbo para disparos potentes a longa distancia, superando flechas comuns em velocidade de impacto."
			]
			icon: {
				id: "cgs:flintlock"
			}
			id: "1002000000000160"
			shape: "square"
			size: 1.25d
			subtitle: "O pioneiro da balistica de polvora negra"
			tasks: [
				{
					id: "1002000000000161"
					item: {
						count: 1
						id: "cgs:flintlock"
					}
					type: "item"
				}
				{
					count: 16L
					id: "1002000000000162"
					item: {
						count: 1
						id: "cgs:paper_cartridge"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 32
					id: "1002000000000163"
					item: {
						count: 1
						id: "cgs:paper_cartridge"
					}
					type: "item"
				}
				{
					id: "1002000000000164"
					type: "xp_levels"
					xp_levels: 6
				}
			]
			title: "O Primeiro Disparo: Flintlock"
			x: 6.5d
			y: 2.5d
		}
		{
			dependencies: ["1002000000000160"]
			description: [
				"Ideal contra hordas cerradas de monstros ou quando um Creeper surge de surpresa em esquinas estreitas."
				"A Shotgun dispara múltiplos balotes de chumbo que se espalham em cone, dizimando alvos proximos com forca de recuo macica."
			]
			icon: {
				id: "cgs:shotgun"
			}
			id: "1002000000000170"
			shape: "square"
			size: 1.25d
			subtitle: "Dispersao pesada para curta distancia"
			tasks: [
				{
					id: "1002000000000171"
					item: {
						count: 1
						id: "cgs:shotgun"
					}
					type: "item"
				}
				{
					count: 16L
					id: "1002000000000172"
					item: {
						count: 1
						id: "cgs:round_shotgun"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 24
					id: "1002000000000173"
					item: {
						count: 1
						id: "cgs:round_shotgun"
					}
					type: "item"
				}
				{
					id: "1002000000000174"
					type: "xp_levels"
					xp_levels: 8
				}
			]
			title: "Poder de Dispersao: A Shotgun"
			x: 9.0d
			y: 2.5d
		}
		{
			dependencies: [
				"1002000000000160"
				"1002000000000070"
			]
			description: [
				"Usando lingotes de Aco laminado do Create Gunsmithing e pecas de latao, construa o Revolver de seis tiros."
				"Com recarga de tambor e cadencia veloz, o Revolver e a arma favorita para exploradores em cavernas hostis."
			]
			icon: {
				id: "cgs:revolver"
			}
			id: "1002000000000180"
			shape: "square"
			size: 1.25d
			subtitle: "Precisao giratoria em aco reforcado"
			tasks: [
				{
					id: "1002000000000181"
					item: {
						count: 1
						id: "cgs:revolver"
					}
					type: "item"
				}
				{
					count: 8L
					id: "1002000000000182"
					item: {
						count: 1
						id: "cgs:steel_ingot"
					}
					type: "item"
				}
				{
					count: 24L
					id: "1002000000000183"
					item: {
						count: 1
						id: "cgs:round_revolver"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 32
					id: "1002000000000184"
					item: {
						count: 1
						id: "cgs:round_revolver"
					}
					type: "item"
				}
				{
					id: "1002000000000185"
					type: "xp_levels"
					xp_levels: 10
				}
			]
			title: "Aco e Cadencia: O Revolver"
			x: 6.5d
			y: 5.0d
		}
		{
			dependencies: ["1002000000000150"]
			description: [
				"Quando a quantidade de inimigos for avassaladora, limpe o terreno com explosivos de estilhacos de ferro e polvora densa."
				"Arremesse e mantenha distancia para obliterar barricadas de monstros."
			]
			icon: {
				id: "cgs:frag_grenade"
			}
			id: "1002000000000190"
			shape: "circle"
			size: 1.1d
			subtitle: "Artilharia explosiva arremessavel"
			tasks: [
				{
					count: 4L
					id: "1002000000000191"
					item: {
						count: 1
						id: "cgs:frag_grenade"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 4
					id: "1002000000000192"
					item: {
						count: 1
						id: "cgs:frag_grenade"
					}
					type: "item"
				}
				{
					id: "1002000000000193"
					type: "xp_levels"
					xp_levels: 6
				}
			]
			title: "Granadas de Fragmentacao"
			x: 9.0d
			y: 5.0d
		}

		{
			dependencies: ["1002000000000030"]
			description: [
				"Para alcancar o poder do vapor e do fogo vivo, voce deve romper as fronteiras do mundo mortal e erguer um portal de Obsidiana."
				"Prepare suas armas e suprimentos: o Nether e uma dimensao de mares de lava fervente, calor asfixiante e hostilidade sem descanso."
			]
			icon: {
				id: "minecraft:obsidian"
			}
			id: "1002000000000210"
			shape: "circle"
			size: 1.1d
			subtitle: "[Dificuldade: Media] Abra a passagem para o inferno de magma"
			tasks: [
				{
					count: 14L
					id: "1002000000000211"
					item: {
						count: 1
						id: "minecraft:obsidian"
					}
					type: "item"
				}
				{
					count: 16L
					id: "1002000000000212"
					item: {
						count: 1
						id: "minecraft:netherrack"
					}
					type: "item"
				}
				{
					count: 8L
					id: "1002000000000213"
					item: {
						count: 1
						id: "minecraft:soul_sand"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 2
					id: "1002000000000214"
					item: {
						count: 1
						id: "minecraft:fire_charge"
					}
					type: "item"
				}
				{
					id: "1002000000000215"
					type: "xp_levels"
					xp_levels: 6
				}
			]
			title: "A Fenda Infernal: O Portal do Nether"
			x: -1.0d
			y: -3.0d
		}
		{
			dependencies: ["1002000000000210"]
			description: [
				"As Fortalezas do Nether guardam geradores de Blazes — espiritos colericos que flutuam em colunas de fogo desferindo rajadas triplas abrasadoras."
				"Use seu escudo para rebater as chamas ou dispare suas armas de fogo a distancia para recolher Varas de Blaze vitais para a industria!"
			]
			icon: {
				id: "minecraft:blaze_rod"
			}
			id: "1002000000000220"
			shape: "circle"
			size: 1.1d
			subtitle: "[Dificuldade: Media] Sobreviva a chuva de fogo nas pontes da Fortaleza"
			tasks: [
				{
					entity: "minecraft:blaze"
					id: "1002000000000221"
					type: "kill"
					value: 8L
				}
				{
					count: 6L
					id: "1002000000000222"
					item: {
						count: 1
						id: "minecraft:blaze_rod"
					}
					type: "item"
				}
			]
			rewards: [
				{
					id: "1002000000000223"
					item: {
						count: 1
						id: "create:empty_blaze_burner"
					}
					type: "item"
				}
				{
					id: "1002000000000224"
					type: "xp_levels"
					xp_levels: 8
				}
			]
			title: "Cacada Incandescente: Os Blazes"
			x: 1.5d
			y: -3.0d
		}
		{
			dependencies: [
				"1002000000000210"
				"1002000000000160"
			]
			description: [
				"Os uivos lamentosos dos Ghasts ecoam pelo teto do Nether, e suas bolas de fogo explosivas destroem pontes de cobblestone sob seus pes."
				"Com seu mosquete Flintlock ou rifle, mire no centro do colosso voador e abata-o em pleno voo para recolher a preciosa Lagrima de Ghast!"
			]
			icon: {
				id: "minecraft:ghast_tear"
			}
			id: "1002000000000230"
			shape: "circle"
			size: 1.1d
			subtitle: "[Dificuldade: Media] Duelo balistico aereo contra os fantasmas do Nether"
			tasks: [
				{
					entity: "minecraft:ghast"
					id: "1002000000000231"
					type: "kill"
					value: 3L
				}
				{
					count: 2L
					id: "1002000000000232"
					item: {
						count: 1
						id: "minecraft:ghast_tear"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 8
					id: "1002000000000233"
					item: {
						count: 1
						id: "minecraft:tnt"
					}
					type: "item"
				}
				{
					id: "1002000000000234"
					type: "xp_levels"
					xp_levels: 8
				}
			]
			title: "O Lamento dos Ceus: O Duelo com o Ghast"
			x: 4.0d
			y: -3.0d
		}
		{
			dependencies: [
				"1002000000000180"
				"1002000000000210"
			]
			description: [
				"Cuidado: um único tiro acidental em um Zumbi Piglin alertara a horda inteira em dezenas de blocos ao redor!"
				"Mostre seu dominio com o Revolver de Aco ou a Espingarda, mantendo uma distancia segura e eliminando alvos estrategicos sem ser cercado."
			]
			icon: {
				id: "minecraft:golden_sword"
			}
			id: "1002000000000240"
			shape: "circle"
			size: 1.1d
			subtitle: "[Dificuldade: Media] Teste sua pontaria e reflexos contra a horda dourada"
			tasks: [
				{
					entity: "minecraft:zombified_piglin"
					id: "1002000000000241"
					type: "kill"
					value: 20L
				}
				{
					count: 16L
					id: "1002000000000242"
					item: {
						count: 1
						id: "minecraft:gold_nugget"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 8
					id: "1002000000000243"
					item: {
						count: 1
						id: "minecraft:gold_ingot"
					}
					type: "item"
				}
				{
					id: "1002000000000244"
					type: "xp_levels"
					xp_levels: 8
				}
			]
			title: "Batismo de Fogo no Nether"
			x: 6.5d
			y: -3.0d
		}
		{
			dependencies: ["1002000000000210"]
			description: [
				"Nos deltas de basalto e lagos incandescentes vivem os Cubos de Magma."
				"Quando fragmentados, atacam em enxames saltitantes. Elimine-os para extrair Creme de Magma, fundamental para preparar pocoes de resistencia ao fogo e fluidos industriais."
			]
			icon: {
				id: "minecraft:magma_cream"
			}
			id: "1002000000000250"
			shape: "circle"
			size: 1.1d
			subtitle: "[Dificuldade: Media] Pule entre fendas de basalto e colha creme igneo"
			tasks: [
				{
					entity: "minecraft:magma_cube"
					id: "1002000000000251"
					type: "kill"
					value: 12L
				}
				{
					count: 8L
					id: "1002000000000252"
					item: {
						count: 1
						id: "minecraft:magma_cream"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 2
					id: "1002000000000253"
					item: {
						count: 1
						id: "minecraft:fire_resistance_potion"
					}
					type: "item"
				}
				{
					id: "1002000000000254"
					type: "xp_levels"
					xp_levels: 7
				}
			]
			title: "O Magma Voraz: Cubos Vulcanicos"
			x: -1.0d
			y: -5.5d
		}
		{
			dependencies: ["1002000000000210"]
			description: [
				"Vista ao menos uma peca de armadura de ouro para que os Piglins nao o ataquem a primeira vista."
				"Jogue barras de ouro no chao perto deles para receber perolas do ender, couro, pocoes e quartzo sem precisar lutar, poupando seu precioso tempo."
			]
			icon: {
				id: "minecraft:gold_ingot"
			}
			id: "1002000000000260"
			shape: "circle"
			size: 1.1d
			subtitle: "[Dificuldade: Media] Diplomacia aurea com os mercadores do Nether"
			tasks: [
				{
					count: 16L
					id: "1002000000000261"
					item: {
						count: 1
						id: "minecraft:gold_ingot"
					}
					type: "item"
				}
				{
					count: 8L
					id: "1002000000000262"
					item: {
						count: 1
						id: "minecraft:ender_pearl"
					}
					type: "item"
				}
				{
					count: 16L
					id: "1002000000000263"
					item: {
						count: 1
						id: "minecraft:quartz"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 1
					id: "1002000000000264"
					item: {
						count: 1
						id: "minecraft:golden_apple"
					}
					type: "item"
				}
				{
					id: "1002000000000265"
					type: "xp_levels"
					xp_levels: 7
				}
			]
			title: "Comercio Selvagem: Barter dos Piglins"
			x: 1.5d
			y: -5.5d
		}

		{
			dependencies: ["1002000000000220"]
			description: [
				"Os Esqueletos Wither empunham espadas de pedra cobertas pelo toque da necrose (Wither), que consome sua vida sem parar."
				"Cace esses guardioes sombrios nas encruzilhadas das Fortalezas ate reunir os 3 cranios sagrados necessarios para rituais proibidos."
			]
			icon: {
				id: "minecraft:wither_skeleton_skull"
			}
			id: "1002000000000270"
			shape: "pentagon"
			size: 1.25d
			subtitle: "[Dificuldade: Dificil] Colha os tres cranios sombrios da necrose"
			tasks: [
				{
					entity: "minecraft:wither_skeleton"
					id: "1002000000000271"
					type: "kill"
					value: 15L
				}
				{
					count: 3L
					id: "1002000000000272"
					item: {
						count: 1
						id: "minecraft:wither_skeleton_skull"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 4
					id: "1002000000000273"
					item: {
						count: 1
						id: "minecraft:diamond"
					}
					type: "item"
				}
				{
					id: "1002000000000274"
					type: "xp_levels"
					xp_levels: 15
				}
			]
			title: "A Decapitacao Sombria: Cranios de Wither"
			x: 4.0d
			y: -5.5d
		}
		{
			dependencies: [
				"1002000000000260"
				"1002000000000180"
			]
			description: [
				"Os Bastoes dos Piglins sao ciudadelas colossais de pedra negra. Diferente dos piglins comuns, os Piglin Brutes atacam sem piedade com machados dourados mortais, ignorando armaduras de ouro."
				"Invada a fortaleza, abata os Brutes e saqueie o cobiçado Molde de Ferraria de Netherite para blindar seu equipamento definitivo!"
			]
			icon: {
				id: "minecraft:netherite_upgrade_smithing_template"
			}
			id: "1002000000000280"
			shape: "pentagon"
			size: 1.25d
			subtitle: "[Dificuldade: Dificil] Invada a cidadela de pedra negra dos Piglins"
			tasks: [
				{
					entity: "minecraft:piglin_brute"
					id: "1002000000000281"
					type: "kill"
					value: 4L
				}
				{
					id: "1002000000000282"
					item: {
						count: 1
						id: "minecraft:netherite_upgrade_smithing_template"
					}
					type: "item"
				}
				{
					count: 2L
					id: "1002000000000283"
					item: {
						count: 1
						id: "minecraft:gold_block"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 2
					id: "1002000000000284"
					item: {
						count: 1
						id: "minecraft:ancient_debris"
					}
					type: "item"
				}
				{
					id: "1002000000000285"
					type: "xp_levels"
					xp_levels: 15
				}
			]
			title: "Invasao ao Bastiao: A Furia do Brute"
			x: 6.5d
			y: -5.5d
		}
		{
			dependencies: [
				"1002000000000180"
				"1002000000000080"
			]
			description: [
				"A uniao definitiva entre a mecanica rotacional do Create e a forca balistica do Gunsmithing."
				"A Metralhadora Gatling conta com canos rotativos de aço acoplados a um tambor de municao continua. Seu poder de fogo pulveriza hordas inteiras em segundos!"
			]
			icon: {
				id: "cgs:gatling"
			}
			id: "1002000000000290"
			shape: "pentagon"
			size: 1.3d
			subtitle: "[Dificuldade: Dificil] Canos rotativos e supremacia balistica"
			tasks: [
				{
					id: "1002000000000291"
					item: {
						count: 1
						id: "cgs:gatling"
					}
					type: "item"
				}
				{
					id: "1002000000000292"
					item: {
						count: 1
						id: "cgs:gatling_drum"
					}
					type: "item"
				}
				{
					count: 64L
					id: "1002000000000293"
					item: {
						count: 1
						id: "cgs:round_gatling"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 64
					id: "1002000000000294"
					item: {
						count: 1
						id: "cgs:round_gatling"
					}
					type: "item"
				}
				{
					id: "1002000000000295"
					type: "xp_levels"
					xp_levels: 18
				}
			]
			title: "Supremacia Balistica: A Gatling"
			x: 9.0d
			y: -3.0d
		}
		{
			dependencies: [
				"1002000000000140"
				"1002000000000220"
			]
			description: [
				"Ao alimentar os Queimadores de Blaze com Bolos de Blaze (Blaze Cakes) produzidos no misturador, eles entram em estado Superaquecido (Superheated - chama azul)."
				"Uma caldeira conectada a agua abundante e calor superaquecido atinge o Nivel 9 de termodinamica, fornecendo centenas de milhares de unidades de estresse para impulsionar qualquer complexo industrial imaginavel!"
			]
			icon: {
				id: "create:blaze_cake"
			}
			id: "1002000000000300"
			shape: "pentagon"
			size: 1.25d
			subtitle: "[Dificuldade: Dificil] Chamas azuis e pressao termodinamica maxima"
			tasks: [
				{
					count: 4L
					id: "1002000000000301"
					item: {
						count: 1
						id: "create:blaze_cake"
					}
					type: "item"
				}
				{
					count: 16L
					id: "1002000000000302"
					item: {
						count: 1
						id: "create:fluid_tank"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 4
					id: "1002000000000303"
					item: {
						count: 1
						id: "create:blaze_cake"
					}
					type: "item"
				}
				{
					id: "1002000000000304"
					type: "xp_levels"
					xp_levels: 15
				}
			]
			title: "Caldeira a Vapor Superaquecida"
			x: 1.5d
			y: -8.0d
		}

		{
			dependencies: [
				"1002000000000290"
				"1002000000000300"
			]
			description: [
				"O ápice da tecnologia balistica do modpack."
				"Alimentado por tanques de lava comprimida e pecas de alta resistencia termica, o Blazegun projeta feixes de plasma incandescente devastadores, vaporizando monstros e blindagens instantaneamente."
			]
			icon: {
				id: "cgs:blazegun"
			}
			id: "1002000000000310"
			shape: "diamond"
			size: 1.5d
			subtitle: "[Dificuldade: Extrema] O canhao de plasma solar movido a lava fervente"
			tasks: [
				{
					id: "1002000000000311"
					item: {
						count: 1
						id: "cgs:blazegun"
					}
					type: "item"
				}
				{
					id: "1002000000000312"
					item: {
						count: 1
						id: "cgs:tank_lava"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 2
					id: "1002000000000313"
					item: {
						count: 1
						id: "minecraft:netherite_ingot"
					}
					type: "item"
				}
				{
					id: "1002000000000314"
					type: "xp_levels"
					xp_levels: 30
				}
			]
			title: "O Canhao Solar: Blazegun"
			x: 9.0d
			y: -6.5d
		}
		{
			dependencies: [
				"1002000000000270"
				"1002000000000290"
			]
			description: [
				"O ritual supremo da destruicao no Nether."
				"Posicione 4 blocos de Areia das Almas e os 3 Cranios de Wither. O colosso de tres cabecas surge detonando rochas, atirando crânios azuis de alta perfuracao e invocando o terror maximo."
				"Utilize todo o seu arsenal da Gatling, armadura e posicionamento tatico para derrota-lo e conquistar a Estrela do Nether para ativar o Sinalizador (Beacon) supremo!"
			]
			icon: {
				id: "minecraft:nether_star"
			}
			id: "1002000000000320"
			shape: "diamond"
			size: 1.5d
			subtitle: "[Dificuldade: Extrema] O terror supremo de tres cabecas e a estrela mística"
			tasks: [
				{
					entity: "minecraft:wither"
					id: "1002000000000321"
					type: "kill"
					value: 1L
				}
				{
					id: "1002000000000322"
					item: {
						count: 1
						id: "minecraft:nether_star"
					}
					type: "item"
				}
				{
					id: "1002000000000323"
					item: {
						count: 1
						id: "minecraft:beacon"
					}
					type: "item"
				}
			]
			rewards: [
				{
					count: 4
					id: "1002000000000324"
					item: {
						count: 1
						id: "minecraft:netherite_ingot"
					}
					type: "item"
				}
				{
					id: "1002000000000325"
					type: "xp_levels"
					xp_levels: 40
				}
			]
			title: "O Colosso do Wither e a Estrela"
			x: 5.2d
			y: -8.0d
		}
	]
}
"""

target1 = "/home/n31415/Games/Minecraft/Ultimate Mods/config/ftbquests/quests/chapters/capitulo_2_create.snbt"
target2 = "/home/n31415/Minecraft/config/ftbquests/quests/chapters/capitulo_2_create.snbt"

with open(target1, "w", encoding="utf-8") as f:
    f.write(SNBT_CONTENT)
print("Salvo com sucesso em:", target1)

with open(target2, "w", encoding="utf-8") as f:
    f.write(SNBT_CONTENT)
print("Salvo com sucesso em:", target2)
