# 📦 Catálogo Geral & Organização de Mods — Minecraft 1.21.1 (NeoForge)

> [!TIP] 🎮 Interface Visual Interativa (Mod Menu Web) Pronta!
> Criamos uma interface visual completa estilo in-game **Mod Menu** para você explorar seus mods com ícones oficiais extraídos, pesquisa em tempo real (`Ctrl+K`), dependências clicáveis e alternância entre Ativos, Desativados, Resource Packs e Wishlist.
> 🔗 **Para abrir:** Execute `./abrir_mod_menu.sh` ou abra [mod_menu.html](../mod_menu.html) no navegador!

## 📊 Resumo da Pasta Organizada

| Localização / Status | Quantidade | Descrição |
| :--- | :---: | :--- |
| 🟢 **ATIVOS** (`mods/`) | **98** | Mods prontos para copiar/usar no Minecraft |
| 🔴 **DESATIVADOS** (`desativados/`) | **12** | Mods isolados para teste ou backup |
| 🎨 **RESOURCE PACKS** (`resourcepacks/`) | **8** | Pacotes visuais e de áudio em formato `.zip` |
| **Total Geral** | **110** | **Arquivos JAR únicos catalogados** |

---

## 📑 Índice por Categorias

- [⚔️ Combate, Armas & Equipamentos (3 mods)](#combate,-armas--equipamentos)
- [⚙️ Tecnologia & Automação (2 mods)](#tecnologia--automação)
- [⚡ Otimização & Performance (10 mods)](#otimização--performance)
- [🎒 Armazenamento & Inventário (8 mods)](#armazenamento--inventário)
- [🎨 Gráficos, Áudio & Imersão (9 mods)](#gráficos,-áudio--imersão)
- [💡 Qualidade de Vida (QoL) & Utilidades (31 mods)](#qualidade-de-vida-qol--utilidades)
- [📚 Bibliotecas, Frameworks & APIs (26 mods)](#bibliotecas,-frameworks--apis)
- [🖥️ Interface (UI/HUD) & Controles (11 mods)](#interface-ui/hud--controles)
- [🗺️ Aventura, Dimensões & Estruturas (10 mods)](#aventura,-dimensões--estruturas)
- [🎨 Resource Packs & Pacotes Visuais](#resource-packs--pacotes-visuais)
- [📌 Mods e Datapacks em Análise / Lista de Desejos](#mods-e-datapacks-em-análise--lista-de-desejos)

---

## ⚔️ Combate, Armas & Equipamentos

| Status | Mod / Nome | Arquivo JAR | Lado | Tipo | Dependências | Usado Por (Dependentes) | Descrição & Links |
| :---: | :--- | :--- | :---: | :---: | :--- | :--- | :--- |
| 🟢 Ativo | **armoroftheages-neoforge-1.21.1-1.5.11.jar** | `armoroftheages-neoforge-1.21.1-1.5.11.jar` | Client | Mod | yet_another_config_lib_v3 | --- | --- |
| 🟢 Ativo | **[NukaTeam's Gun Lib](https://discord.com/invite/njb6EKaDVJ)** | `ntgl-1.21.1-3.2.0.jar` | Both | Mod | geckolib | Create: Gunsmithing | Core for weapon mods |
| 🟢 Ativo | **Simply Swords** | `simplyswords-neoforge-1.70.2-1.21.1.jar` | Client | Mod | architectury, fzzy_config, simplytooltips | --- | --- |

---

## ⚙️ Tecnologia & Automação

| Status | Mod / Nome | Arquivo JAR | Lado | Tipo | Dependências | Usado Por (Dependentes) | Descrição & Links |
| :---: | :--- | :--- | :---: | :---: | :--- | :--- | :--- |
| 🟢 Ativo | **[Create](https://www.curseforge.com/minecraft/mc-mods/create)** | `create-1.21.1-6.0.10.jar` | Client | Mod | flywheel, ponder, sodium, lithium, journeymap, xaeroworldmap, radium, palladium | Create: Gunsmithing | Technology that empowers the player. |
| 🟢 Ativo | **Create: Gunsmithing** | `create-gunsmithing-1.21.1-1.4.9.jar` | Both | Mod | ntgl, create | --- | "Adds steampunk weapons to the Create mod" |

---

## ⚡ Otimização & Performance

| Status | Mod / Nome | Arquivo JAR | Lado | Tipo | Dependências | Usado Por (Dependentes) | Descrição & Links |
| :---: | :--- | :--- | :---: | :---: | :--- | :--- | :--- |
| 🟢 Ativo | **BadOptimizations** | `BadOptimizations-2.4.1-1.21.1.jar` | Client | Mod | --- | --- | --- |
| 🟢 Ativo | **[Dynamic FPS](https://dapprgames.com/mods)** | `dynamic-fps-3.11.4+minecraft-1.21.0-neoforge.jar` | Client | Mod | --- | --- | Reduce resource usage while Minecraft is in the background or idle. |
| 🟢 Ativo | **[EntityCulling](https://modrinth.com/mod/entityculling)** | `entityculling-neoforge-1.11.3-mc1.21.1.jar` | Both | Mod | --- | --- | --- |
| 🟢 Ativo | **Ferrite Core** | `ferritecore-7.0.3-neoforge.jar` | Both | Mod | --- | --- | --- |
| 🟢 Ativo | **[ImmediatelyFast](https://github.com/RaphiMC/ImmediatelyFast)** | `ImmediatelyFast-NeoForge-1.6.14+1.21.1.jar` | Client | Mod | --- | --- | Speed up and optimize immediate mode rendering in Minecraft |
| 🟢 Ativo | **modernfix-neoforge-5.27.24+mc1.21.1.jar** | `modernfix-neoforge-5.27.24+mc1.21.1.jar` | Client | Mod | jei | --- | --- |
| 🟢 Ativo | **moreculling-neoforge-1.21.1-1.0.10.jar** | `moreculling-neoforge-1.21.1-1.0.10.jar` | Both | Mod | cloth_config, sodium | --- | --- |
| 🟢 Ativo | **Sodium** | `sodium-neoforge-0.8.13+mc1.21.1.jar` | Client | Mod | embeddium | Create, moreculling-neoforge-1.21.1-1.0.10.jar, Sodium Extra, Voxy | --- |
| 🟢 Ativo | **Sodium Extra** | `sodium-extra-neoforge-0.9.4+mc1.21.1.jar` | Client | Mod | sodium, greenlight | --- | --- |
| 🟢 Ativo | **spark** | `spark-1.10.124-neoforge.jar` | Both | Mod | --- | --- | spark is a performance profiling plugin/mod for Minecraft clients, servers and proxies. |

---

## 🎒 Armazenamento & Inventário

| Status | Mod / Nome | Arquivo JAR | Lado | Tipo | Dependências | Usado Por (Dependentes) | Descrição & Links |
| :---: | :--- | :--- | :---: | :---: | :--- | :--- | :--- |
| 🟢 Ativo | **[Bartering Station](https://github.com/Fuzss/barteringstation)** | `BarteringStation-v21.1.0-1.21.1-NeoForge.jar` | Both | Mod | puzzleslib | --- | Still running around bartering manually? Let's put those lazy piglins to work instead! |
| 🔴 Desativado | **[Chest Tracker](https://github.com/JackFred2/ChestTracker)** | `chesttracker-2.6.8+1.21.1-neoforge.jar` | Client | Mod | yet_another_config_lib_v3 | --- | Client-side item storage and searching for Minecraft. This is an unofficial NeoForge 1.21.1 port of Chest Tracker. |
| 🟢 Ativo | **[Easy Anvils](https://github.com/Fuzss/easyanvils)** | `EasyAnvils-v21.1.0-1.21.1-NeoForge.jar` | Both | Mod | puzzleslib | --- | Be ready for overhauled anvils! Items stay, better name tags, many tweaks! |
| 🟢 Ativo | **[Inventory Tweak](https://modrinth.com/mod/inventorytweak)** | `inventorytweak-neoforge-1.21-3.3.jar` | Client | Mod | anvianslib, cloth_config | --- | Fast and easy inventory sorter |
| 🟢 Ativo | **[Mouse Tweaks](https://minecraft.curseforge.com/projects/mouse-tweaks)** | `MouseTweaks-neoforge-mc1.21-2.26.1.jar` | Both | Mod | --- | --- | A mod that enhances the inventory management by adding various additional functions to the usual mouse buttons. |
| 🟢 Ativo | **[Sophisticated Backpacks](https://www.curseforge.com/minecraft/mc-mods/sophisticated-backpacks)** | `sophisticatedbackpacks-1.21.1-3.26.7.2182.jar` | Both | Mod | sophisticatedcore | --- | Fancy and functional backpacks. |
| 🟢 Ativo | **[Sophisticated Core](https://www.curseforge.com/minecraft/mc-mods/sophisticated-core)** | `sophisticatedcore-1.21.1-1.5.5.2363.jar` | Both | Mod | neoforge" #mandatory | Sophisticated Backpacks | A library / shared functionality mod for Sophisticated Storage and Backpacks |
| 🟢 Ativo | **toms_storage-1.21-2.4.2.jar** | `toms_storage-1.21-2.4.2.jar` | Both | Mod | sophisticatedstorage | --- | --- |

---

## 🎨 Gráficos, Áudio & Imersão

| Status | Mod / Nome | Arquivo JAR | Lado | Tipo | Dependências | Usado Por (Dependentes) | Descrição & Links |
| :---: | :--- | :--- | :---: | :---: | :--- | :--- | :--- |
| 🟢 Ativo | **[AmbientSounds](https://modrinth.com/mod/ambientsounds)** | `AmbientSounds_NEOFORGE_v6.3.11_mc1.21.1.jar` | Both | Mod | creativecore | --- | Expands minecraft's ambient sounds. |
| 🟢 Ativo | **Cinematic Respawn** | `cinematic_respawn-1.21.1-neoforge-1.4.1.jar` | Client | Mod | --- | --- | Cinematic respawn experience for Minecraft. |
| 🟢 Ativo | **cinematiczoom-1.0.0-1.21.1.jar** | `cinematiczoom-1.0.0-1.21.1.jar` | Both | Mod | --- | --- | --- |
| 🟢 Ativo | **[Continuity](https://modrinth.com/mod/continuity)** | `continuity-3.0.0+1.21.neoforge.jar` | Both | Mod | connector, fabric_api | --- | Continuity is a Fabric mod that allows resource packs that use the OptiFine connected textures format, OptiFine emissive textures format (only for blocks and it... |
| 🟢 Ativo | **[LambDynamicLights](https://lambdaurora.dev/projects/lambdynamiclights)** | `lambdynamiclights-4.8.11+1.21.1.jar` | Client | Mod | lambdynlights_runtime | --- | The most feature-complete dynamic lighting mod. |
| 🟢 Ativo | **[Music Player](https://u-team.info/mods/musicplayer)** | `music_player-neoforge-1.21.1-2.7.3.373.jar` | Both | Mod | uteamcore | --- | Join our discord server here: https://discord.hycrafthd.net\n\nPlay every youtube video, livestream and more with this player! We use lava player to ensure this... |
| 🟢 Ativo | **PresenceFootsteps-1.21.1-1.12.0-beta.1-1.21NeoForge.jar** | `PresenceFootsteps-1.21.1-1.12.0-beta.1-1.21NeoForge.jar` | Both | Mod | --- | --- | --- |
| 🟢 Ativo | **[Sound Physics Remastered](https://www.curseforge.com/minecraft/mc-mods/sound-physics-remastered)** | `sound-physics-remastered-neoforge-1.21.1-1.4.10.jar` | Both | Mod | cloth_config, voicechat | --- | Provides realistic sound attenuation, reverberation, and absorption through blocks. |
| 🟢 Ativo | **[Visual Workbench](https://github.com/Fuzss/visualworkbench)** | `VisualWorkbench-v21.1.2-1.21.1-NeoForge.jar` | Both | Mod | puzzleslib | --- | Items stay inside crafting tables and are also rendered on top. It's really fancy! |

---

## 💡 Qualidade de Vida (QoL) & Utilidades

| Status | Mod / Nome | Arquivo JAR | Lado | Tipo | Dependências | Usado Por (Dependentes) | Descrição & Links |
| :---: | :--- | :--- | :---: | :---: | :--- | :--- | :--- |
| 🔴 Desativado | **[Auto Eat](https://modrinth.com/project/automaticallyeat/)** | `autoeat-1.6.8.jar` | Client | Mod | simpleguiapi, multiloaderapi | --- | When your fullness drops below the specified value, you will automatically consume food items in your inventory. |
| 🟢 Ativo | **carryon-neoforge-1.21.1-2.2.6.13.jar** | `carryon-neoforge-1.21.1-2.2.6.13.jar` | Both | Mod | --- | --- | --- |
| 🔴 Desativado | **[Chunky](https://github.com/pop4959/Chunky)** | `Chunky-NeoForge-1.4.23.jar` | Both | Mod | --- | --- | Pre-generates chunks, quickly, efficiently, and safely |
| 🟢 Ativo | **connector-2.0.0-beta.17+1.21.1-full.jar** | `connector-2.0.0-beta.17+1.21.1-full.jar` | Both | Mod | --- | --- | --- |
| 🟢 Ativo | **[CreativeCore](https://modrinth.com/mod/creativecore)** | `CreativeCore_NEOFORGE_v2.13.51_mc1.21.1.jar` | Both | Mod | --- | AmbientSounds | A simple but powerful coremod. |
| 🟢 Ativo | **DistantHorizons-3.3.3-1.21.1-fabric-neoforge.jar** | `DistantHorizons-3.3.3-1.21.1-fabric-neoforge.jar` | Both | Mod | ssrd | --- | --- |
| 🟢 Ativo | **[Easy Magic](https://github.com/Fuzss/easymagic)** | `EasyMagic-v21.1.4-1.21.1-NeoForge.jar` | Both | Mod | puzzleslib | --- | Enchanting tables as they always should have been! Items stay after closing, and easy re-rolls. |
| 🟢 Ativo | **EMI** | `emi-1.1.24+1.21.1+neoforge.jar` | Both | Mod | --- | --- | --- |
| 🔴 Desativado | **EMI** | `emi-1.1.24+1.21.1+neoforge.jar` | Both | Mod | --- | EMI Loot | --- |
| 🟢 Ativo | **[EMI Loot](https://github.com/fzzyhmstrs/EMI_loot)** | `emi_loot-0.7.9+1.21+neoforge.jar` | Client | Mod | emi, fzzy_config | --- | Plugin for EMI that shows chest loot, block drops, mob drops, and gameplay loot like fishing. |
| 🔴 Desativado | **[EMI Loot](https://github.com/fzzyhmstrs/EMI_loot)** | `emi_loot-0.7.9+1.21+neoforge.jar` | Client | Mod | emi, fzzy_config | --- | Plugin for EMI that shows chest loot, block drops, mob drops, and gameplay loot like fishing. |
| 🟢 Ativo | **[Freecam](https://www.curseforge.com/minecraft/mc-mods/free-cam)** | `freecam-neoforge-1.3.0+mc1.21.jar` | Client | Mod | --- | --- | --- |
| 🟢 Ativo | **FTB Ranks** | `ftb-ranks-neoforge-2101.1.5.jar` | Client | Mod | architectury, ftblibrary | --- | --- |
| 🟢 Ativo | **FTB Ultimine** | `ftb-ultimine-neoforge-2101.1.15.jar` | Both | Mod | architectury, ftblibrary, ftbezcrystals | --- | --- |
| 🟢 Ativo | **[Gravestone Mod](https://www.curseforge.com/minecraft/mc-mods/gravestone-mod)** | `gravestone-neoforge-1.21.1-1.0.40.jar` | Both | Mod | jade | --- | Places a gravestone with your inventory items inside when you die |
| 🟢 Ativo | **hennyfullbright-neoforge-1.21.1-1.0.jar** | `hennyfullbright-neoforge-1.21.1-1.0.jar` | Client | Mod | --- | --- | --- |
| 🟢 Ativo | **[HT's TreeChop](https://github.com/hammertater/treechop)** | `TreeChop-1.21.1-neoforge-0.19.3.jar` | Both | Mod | --- | --- | Makes trees more choppable. |
| 🔴 Desativado | **improved-inventory-tabs-neoforge-1.21.1-1.5.0.jar** | `improved-inventory-tabs-neoforge-1.21.1-1.5.0.jar` | Client | Mod | cloth_config | --- | --- |
| 🔴 Desativado | **Jack's Fullbright** | `jackfullbright-neoforge-26.3.jar` | Client | Mod | --- | --- | A configurable fullbright toggle with client-side night vision. |
| 🟢 Ativo | **jei-1.21.1-neoforge-19.57.0.450.jar** | `jei-1.21.1-neoforge-19.57.0.450.jar` | Client | Mod | mezz_config" #mandatory, mezz_config_gui, neoforge" #mandatory, minecraft" #mandatory | --- | --- |
| 🟢 Ativo | **JustEnoughResources-NeoForge-1.21.1-1.6.0.66.jar** | `JustEnoughResources-NeoForge-1.21.1-1.6.0.66.jar` | Both | Mod | jei | --- | --- |
| 🟢 Ativo | **[Lootr](https://minecraft.curseforge.com/projects/lootr)** | `lootr-neoforge-1.21.1-1.11.38.127.jar` | Both | Mod | --- | --- | Generates unique loot for each player that opens a loot container. |
| 🟢 Ativo | **[Nature's Compass](https://github.com/MattCzyr/NaturesCompass)** | `NaturesCompass-1.21.1-3.4.0-neoforge.jar` | Both | Mod | --- | --- | --- |
| 🔴 Desativado | **[Pathogen : monster plague](https://www.curseforge.com/minecraft/mc-mods/pathogen)** | `pathogen-1.4.7-neoforge-1.21.1.jar` | Both | Mod | geckolib, GeckoLib | --- | --- |
| 🔴 Desativado | **[Resource Pack Options](https://git.frohnmeyer-wds.de/JfMods/Respackopts)** | `respackopts-4.11.3+forge.jar` | Both | Mod | libjf_base, libjf_data_manipulation_v0, libjf_config_core_v2, muscript | --- | --- |
| 🟢 Ativo | **[Skin Changer](https://www.curseforge.com/minecraft/mc-mods/skinchanger)** | `skin_changer-neoforge-1.21-0.9.2.jar` | Both | Mod | architectury | --- | This mod allows you to change your Minecraft server skin on the fly even if it is in offline mode. |
| 🟢 Ativo | **Symbols 'n' Stuff** | `symbols_n_stuff-0.1.2+1.21+neoforge.jar` | Both | Mod | kotlinforforge | --- | --- |
| 🟢 Ativo | **[Trade Cycling](https://www.curseforge.com/minecraft/mc-mods/trade-cycling)** | `trade-cycling-neoforge-1.21.1-1.0.22.jar` | Both | Mod | --- | --- | The trade cycling functionality from Easy Villagers. |
| 🟢 Ativo | **Upgrader** | `upgrader-neoforge-1.2.1+1.21.1.jar` | Both | Mod | --- | --- | Gambling-style item upgrader: risk an item for a shot at a better one. |
| 🔴 Desativado | **Voxy** | `voxy-0.6.0.jar` | Client | Mod | sodium, fabric_api | --- | Far distance rendering mod utilising LoDs |
| 🟢 Ativo | **[Waystones](https://mods.twelveiterations.com/minecraft/waystones)** | `waystones-neoforge-1.21.1-21.1.46.jar` | Both | Mod | balm | --- | Teleport back to activated waystones. For Survival, Adventure or Servers. |

---

## 📚 Bibliotecas, Frameworks & APIs

| Status | Mod / Nome | Arquivo JAR | Lado | Tipo | Dependências | Usado Por (Dependentes) | Descrição & Links |
| :---: | :--- | :--- | :---: | :---: | :--- | :--- | :--- |
| 🟢 Ativo | **[Anvian's Lib](https://modrinth.com/mod/anvians-lib)** | `anvianslib-neoforge-1.21-1.4.2.jar` | Both | Lib | --- | Inventory Tweak | A small utility library for Anvian's mods. |
| 🟢 Ativo | **Architectury** | `architectury-13.0.11-neoforge.jar` | Both | Lib | --- | Simply Tooltips, FTB Library, FTB Ranks, FTB Ultimine, Simply Swords, Skin Changer | --- |
| 🟢 Ativo | **[Balm](https://mods.twelveiterations.com/)** | `balm-neoforge-1.21.1-21.0.66.jar` | Both | Lib | --- | Waystones | Abstraction Layer (but not really) for Blay's multiplatform mods |
| 🟢 Ativo | **[Blueprint](https://www.teamabnormals.com/mods/blueprint)** | `blueprint-1.21.1-8.2.0.jar` | Both | Lib | --- | Caverns & Chasms | --- |
| 🟢 Ativo | **Cloth Config v15 API** | `cloth-config-15.0.140-neoforge.jar` | Both | Lib | --- | BetterF3, InvMove, Inventory Tweak, moreculling-neoforge-1.21.1-1.0.10.jar, Sound Physics Remastered, improved-inventory-tabs-neoforge-1.21.1-1.5.0.jar | --- |
| 🟢 Ativo | **cristellib-neoforge-1.21.1-3.1.7.jar** | `cristellib-neoforge-1.21.1-3.1.7.jar` | Both | Lib | t_and_t, expanded_ecosphere | --- | --- |
| 🟢 Ativo | **[Curios API](https://github.com/TheIllusiveC4/Curios)** | `curios-neoforge-9.5.1+1.21.1.jar` | Both | Lib | --- | L_Ender's Cataclysm 1.21.1-3.33.jar | A flexible and expandable accessory/equipment API for users and developers. |
| 🟢 Ativo | **[Forge Config API Port](https://github.com/Fuzss/forgeconfigapiport)** | `ForgeConfigAPIPort-v21.1.6-1.21.1-NeoForge.jar` | Both | Lib | --- | --- | Provides NeoForge's & Forge's config systems to other modding ecosystems. Designed for a multi-loader architecture. |
| 🟢 Ativo | **[Forgified Fabric API](https://github.com/Sinytra/ForgifiedFabricAPI)** | `forgified-fabric-api-0.116.15+2.3.5+1.21.1.jar` | Both | Lib | --- | Continuity, Voxy | Core API module providing key hooks and intercompatibility features. |
| 🟢 Ativo | **FTB Library** | `ftb-library-neoforge-2101.1.37.jar` | Both | Lib | architectury | FTB Ranks, FTB Ultimine | --- |
| 🟢 Ativo | **Fzzy Config** | `fzzy_config-0.7.7+1.21+neoforge.jar` | Both | Lib | kotlinforforge | Simply Tooltips, EMI Loot, Simply Swords | --- |
| 🟢 Ativo | **[GeckoLib 4](http://geckolib.com/)** | `geckolib-neoforge-1.21.1-4.9.3.jar` | Both | Lib | geckoanimfix | Mielon's The Sift, NukaTeam's Gun Lib, Pathogen : monster plague | --- |
| 🟢 Ativo | **kotlinforforge-5.12.0-all.jar** | `kotlinforforge-5.12.0-all.jar` | Both | Lib | --- | --- | --- |
| 🟢 Ativo | **[KotlinLangForge](https://modrinth.com/mod/kotlin-lang-forge)** | `KotlinLangForge-2.14.1-k2.4.20-3.0+neoforge.jar` | Both | Lib | --- | --- | --- |
| 🟢 Ativo | **[KotlinLangForge](https://modrinth.com/mod/kotlin-lang-forge)** | `KotlinLangForge-2.15.0-k2.4.21-3.0+neoforge.jar` | Both | Lib | --- | --- | --- |
| 🔴 Desativado | **[LibJF](https://git.frohnmeyer-wds.de/JfMods/LibJF)** | `libjf-3.17.4+forge.jar` | Both | Lib | --- | --- | --- |
| 🟢 Ativo | **lionfishapi-3.1.jar** | `lionfishapi-3.1.jar` | Both | Lib | --- | --- | --- |
| 🟢 Ativo | **Lithostitched** | `lithostitched-1.8.1-neoforge-21.1.jar` | Both | Lib | apollib | --- | A library mod with new configurability and compatibility enhancements for worldgen |
| 🟢 Ativo | **[MaFgLib](https://github.com/CagayakeGirls/malilib-neoforge)** | `mafglib-0.4.3+mc1.21.1.jar` | Both | Lib | --- | Forgematica | --- |
| 🟢 Ativo | **[Player Animator](https://github.com/KosmX/minecraftPlayerAnimator)** | `player-animation-lib-forge-2.0.4+1.21.1.jar` | Both | Lib | --- | --- | A lightweight library to easily animate the player |
| 🟢 Ativo | **[Puzzles Lib](https://www.curseforge.com/minecraft/mc-mods/puzzles-lib)** | `puzzleslib-v21.1.62-mc1.21.1+neoforge.jar` | Both | Lib | --- | Bartering Station, Distinguished Potions, Easy Anvils, Easy Magic, Visual Workbench | Why it's called Puzzles, you ask? That's the puzzle! |
| 🟢 Ativo | **Resourceful Lib** | `resourcefullib-neoforge-1.21-3.0.12.jar` | Both | Lib | --- | --- | Team Resourceful Library |
| 🔴 Desativado | **Simple GUI API** | `simpleguiapi-1.5.10.jar` | Both | Lib | multiloaderapi | Auto Eat | Reusable config GUI API for NeoForge mods. |
| 🟢 Ativo | **[U Team Core](https://u-team.info/mods/uteamcore)** | `u_team_core-neoforge-1.21.1-5.6.2.384.jar` | Both | Lib | --- | Music Player | Join our discord server here: https://discord.hycrafthd.net\n\nThis library contains many useful modding stuff! |
| 🟢 Ativo | **YetAnotherConfigLib** | `yet_another_config_lib_v3-3.8.2+1.21.1-neoforge.jar` | Both | Lib | --- | armoroftheages-neoforge-1.21.1-1.5.11.jar, Chest Tracker | YetAnotherConfigLib (yacl) is just that. A builder-based configuration library for Minecraft.\n |
| 🟢 Ativo | **[YUNG's API](https://www.curseforge.com/minecraft/mc-mods/yungs-api-neoforge)** | `YungsApi-1.21.1-NeoForge-5.1.9.jar` | Both | Lib | --- | Traveler's Titles | API Library for YUNG's minecraft mods. |

---

## 🖥️ Interface (UI/HUD) & Controles

| Status | Mod / Nome | Arquivo JAR | Lado | Tipo | Dependências | Usado Por (Dependentes) | Descrição & Links |
| :---: | :--- | :--- | :---: | :---: | :--- | :--- | :--- |
| 🟢 Ativo | **[AppleSkin](https://github.com/squeek502/AppleSkin)** | `appleskin-neoforge-mc1.21-3.0.9.jar` | Client | Mod | --- | --- | Adds various food-related HUD improvements |
| 🟢 Ativo | **[BetterF3](https://modrinth.com/mod/betterf3)** | `BetterF3-11.0.3-NeoForge-1.21.1.jar` | Both | Mod | cloth_config | --- | --- |
| 🟢 Ativo | **[Distinguished Potions](https://github.com/Fuzss/distinguishedpotions)** | `DistinguishedPotions-v21.1.1-1.21.1-NeoForge.jar` | Both | Mod | puzzleslib | --- | Trouble telling your potions apart? Time to give you a helping hand with that. |
| 🟢 Ativo | **[Forgematica](https://github.com/CagayakeGirls/litematica-neoforge)** | `forgematica-0.4.2+mc1.21.1.jar` | Both | Mod | mafglib | --- | --- |
| 🟢 Ativo | **InvMove** | `InvMove-0.9.3+1.21.1-NeoForge.jar` | Client | Mod | cloth_config, invmove_compat | --- | Lets you move while in inventories. |
| 🟢 Ativo | **[Jade](https://www.curseforge.com/minecraft/mc-mods/jade)** | `Jade-1.21.1-NeoForge-15.10.6.jar` | Both | Mod | --- | Jade Addons, Gravestone Mod | Minecraft mod shows what you are looking at. (Hwyla fork) |
| 🟢 Ativo | **[Jade Addons](https://www.curseforge.com/minecraft/mc-mods/jade-addons)** | `JadeAddons-1.21.1-NeoForge-6.1.2.jar` | Both | Mod | jade | --- | Jade additional mod supports |
| 🟢 Ativo | **Mod Menu (NeoForge Edition) 1.21.1-1.0.2.jar** | `Mod Menu (NeoForge Edition) 1.21.1-1.0.2.jar` | Client | Mod | connector | --- | --- |
| 🟢 Ativo | **Scribble** | `Scribble-1.5.1+mc1.21-neoforge.jar` | Both | Mod | --- | --- | Expertly edit your books with rich formatting options, page utilities and more! |
| 🟢 Ativo | **Simply Tooltips** | `SimplyTooltips-neoforge-0.1.5.jar` | Both | Mod | architectury, fzzy_config | Simply Swords | --- |
| 🟢 Ativo | **[Traveler's Titles](https://www.curseforge.com/minecraft/mc-mods/travelers-titles-neoforge)** | `TravelersTitles-1.21.1-NeoForge-5.1.3.jar` | Both | Mod | yungsapi | --- | Epic, RPG-like titles when entering biomes & dimensions |

---

## 🗺️ Aventura, Dimensões & Estruturas

| Status | Mod / Nome | Arquivo JAR | Lado | Tipo | Dependências | Usado Por (Dependentes) | Descrição & Links |
| :---: | :--- | :--- | :---: | :---: | :--- | :--- | :--- |
| 🟢 Ativo | **[Caverns & Chasms](https://www.teamabnormals.com/mods/caverns-and-chasms)** | `caverns_and_chasms-1.21.1-3.0.1.jar` | Both | Mod | blueprint | --- | --- |
| 🟢 Ativo | **[Explorify](https://modrinth.com/datapack/explorify)** | `Explorify-v1.6.6.jar` | Both | Mod | --- | --- | A simplistic, vanilla-friendly collection of new structures. |
| 🟢 Ativo | **L_Ender's Cataclysm 1.21.1-3.33.jar** | `L_Ender's Cataclysm 1.21.1-3.33.jar` | Both | Mod | curios, lionfishapi | --- | --- |
| 🟢 Ativo | **[Mielon's The Sift](https://x.com/MielonDev)** | `mielon's-the-sift-1.1.0-mc1.21.1-neo.jar` | Both | Mod | geckolib | --- | Explore The Sift: a strange dimension of siftslate, Ichor, ancient life, and resonant souls. |
| 🟢 Ativo | **Tectonic** | `tectonic-3.0.28-neoforge-21.1.jar` | Both | Mod | apollib | --- | Terrain shaping brought to new heights, grander and more varied than ever before! |
| 🟢 Ativo | **Terralith_1.21.1_v2.6.2_Neoforge.jar** | `Terralith_1.21.1_v2.6.2_Neoforge.jar` | Both | Mod | --- | --- | --- |
| 🟢 Ativo | **[The Bumblezone](https://www.curseforge.com/projects/362479)** | `the_bumblezone-7.17.3+1.21.1-neoforge.jar` | Both | Mod | --- | --- | A wonderful bee dimension mod with lots of new exploration and adventuring to do! Check out the advancements for how to play the mod! |
| 🟢 Ativo | **[The Twilight Forest](https://www.curseforge.com/minecraft/mc-mods/the-twilight-forest)** | `twilightforest-1.21.1-4.8.3345-universal.jar` | Both | Mod | --- | --- | --- |
| 🟢 Ativo | **[Towns and Towers](https://modrinth.com/mod/towns-and-towers)** | `t_and_t-fabric-neoforge-1.13.11.jar` | Both | Mod | cristellib | cristellib-neoforge-1.21.1-3.1.7.jar | Spice up your world with new villages, pillager outposts, and even new ships! |
| 🟢 Ativo | **When Dungeons Arise** | `DungeonsArise-1.21.1-2.1.68-release.jar` | Both | Mod | --- | --- | Elegant - and likely dangerous - structures and roguelike dungeons to lose yourself in... |

---

## 🎨 Resource Packs & Pacotes Visuais

| Pacote / Nome | Arquivo ZIP | Descrição & Links |
| :--- | :--- | :--- |
| **[3D Default 1.20+ v1.16.0](https://www.curseforge.com/minecraft/texture-packs/3d-default-1.20+-v1.16.0)** | `3D Default 1.20+ v1.16.0.zip` | 3D Default by GeForceLegend |
| **[Cherry Grove Panorama](https://www.curseforge.com/minecraft/texture-packs/cherry-grove-panorama)** | `Cherry Grove Panorama.zip` | Panorama Of A Cherry Grove Biome and Mountains |
| **[Connected-Paths 1.21-1.21.3 v3.1.1](https://www.curseforge.com/minecraft/texture-packs/connected-paths-1.21-1.21.3-v3.1.1)** | `Connected-Paths 1.21-1.21.3 v3.1.1.zip` | §7by §2Jacosvaldo |
| **[EvenBetterEnchants_v2_r1](https://www.curseforge.com/minecraft/texture-packs/evenbetterenchants_v2_r1)** | `EvenBetterEnchants_v2_r1.zip` | §dby §6Mythitorium
§7v2 §8- §71.21+ |
| **[Jackson's Cave Sounds](https://www.curseforge.com/minecraft/texture-packs/jackson's-cave-sounds)** | `Jackson's Cave Sounds.zip` | §a■ Update 1.0§r
■ By FurGalaxy |
| **[LowOnFire 1.21.3](https://www.curseforge.com/minecraft/texture-packs/lowonfire-1.21.3)** | `LowOnFire 1.21.3.zip` | §4❏ Lower Fire Texture §r
❏ By §6Haikis |
| **[NightUI v1.4.1](https://www.curseforge.com/minecraft/texture-packs/nightui-v1.4.1)** | `NightUI v1.4.1.zip` | §5A Dark Themed Resource Pack
§9👤§o NotToBlame |
| **[Spectator_Xray_v1.2.1](https://www.curseforge.com/minecraft/texture-packs/spectator_xray_v1.2.1)** | `Spectator_Xray_v1.2.1.zip` | §bMade By AlphaLeoli
§7Xray in spectator mode |

---

## 📌 Mods e Datapacks em Análise / Lista de Desejos

| Nome / Recurso | Tipo | Link / Referência | Descrição / Objetivo |
| :--- | :---: | :--- | :--- |
| **Fancy World Animation** | `Mod/Ideia` | Fancy World Animation | Ideia ou mod citado nas anotações. |
| **Inventorio** | `Mod/Ideia` | Inventorio | Ideia ou mod citado nas anotações. |
| **Pumpkillagers Quest** | `Mod` | [Pumpkillagers Quest](https://www.curseforge.com/minecraft/mc-mods/pumpkillagers-quest) | Mod anotado para avaliação. |
| **Fluxwolf** | `Mod` | [Fluxwolf](https://www.curseforge.com/minecraft/mc-mods/fluxwolf) | Mod anotado para avaliação. |
| **The Bumblezone Forge** | `Mod` | [The Bumblezone Forge](https://www.curseforge.com/minecraft/mc-mods/the-bumblezone-forge) | Mod anotado para avaliação. |
| **Wall Climb** | `Mod` | [Wall Climb](https://www.curseforge.com/minecraft/mc-mods/wall-climb) | Mod anotado para avaliação. |
| **Customskinloader** | `Mod` | [Customskinloader](https://www.curseforge.com/minecraft/mc-mods/customskinloader) | Mod anotado para avaliação. |
| **Biomes O’ Plenty** | `Mod/Ideia` | Biomes O’ Plenty | Ideia ou mod citado nas anotações. |
| **Tinkers’ Construct** | `Mod/Ideia` | Tinkers’ Construct | Ideia ou mod citado nas anotações. |
| **Geyser & Floodgate ou ViaVersion** | `Mod/Ideia` | Geyser & Floodgate ou ViaVersion | Ideia ou mod citado nas anotações. |
| **Vista** | `Mod/Ideia` | Vista | Ideia ou mod citado nas anotações. |
| **Vanilla Tweaks** | `Mod/Ideia` | Vanilla Tweaks | Ideia ou mod citado nas anotações. |
| **Just Enough Resources Jer** | `Mod` | [Just Enough Resources Jer](https://www.curseforge.com/minecraft/mc-mods/just-enough-resources-jer) | Mod anotado para avaliação. |
| **Traveler Titles** | `Mod/Ideia` | Traveler Titles | Ideia ou mod citado nas anotações. |
| **minimapa com crias** | `Mod/Ideia` | minimapa com crias | Ideia ou mod citado nas anotações. |
| **SkyFactory 4** | `Mod/Ideia` | SkyFactory 4 | Ideia ou mod citado nas anotações. |
| **Old Ruin Structures** | `Mod` | [Old Ruin Structures](https://www.curseforge.com/minecraft/mc-mods/old-ruin-structures/) | Mod anotado para avaliação. |
| **Abandoned Structures** | `Mod` | [Abandoned Structures](https://www.curseforge.com/minecraft/mc-mods/abandoned-structures/) | Mod anotado para avaliação. |

