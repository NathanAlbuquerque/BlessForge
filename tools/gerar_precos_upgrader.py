#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de Valores Balanceados para o Mod Upgrader.
Calcula e injeta preços lógicos e justos para centenas de itens de mods e do vanilla,
eliminando a queda para o valor mínimo "3" em itens raros ou sem receita tradicional.
"""

import os, zipfile

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODS_DIR = os.path.join(ROOT_DIR, "mods")
CONFIG_SRC = os.path.join(ROOT_DIR, "config", "upgrader-common.toml")
CONFIG_MC = "/home/n31415/Minecraft/config/upgrader-common.toml"

overrides = {}

# ==============================================================================
# 1. VANILLA FIXES & BALANCES
# ==============================================================================
overrides['minecraft:sea_pickle'] = 30.0

# Baldes (Balde vazio = 3 ferros = 120. Cheio sempre >= vazio!)
overrides['minecraft:bucket'] = 120.0
overrides['minecraft:water_bucket'] = 130.0
overrides['minecraft:milk_bucket'] = 140.0
overrides['minecraft:powder_snow_bucket'] = 150.0
overrides['minecraft:lava_bucket'] = 180.0
overrides['minecraft:cod_bucket'] = 160.0
overrides['minecraft:salmon_bucket'] = 160.0
overrides['minecraft:tadpole_bucket'] = 180.0
overrides['minecraft:tropical_fish_bucket'] = 200.0
overrides['minecraft:pufferfish_bucket'] = 220.0
overrides['minecraft:axolotl_bucket'] = 350.0

# Itens raros / 1.21 Trial Chambers
overrides['minecraft:heavy_core'] = 5000.0
overrides['minecraft:mace'] = 6000.0
overrides['minecraft:breeze_rod'] = 80.0
overrides['minecraft:wind_charge'] = 20.0
overrides['minecraft:sniffer_egg'] = 1200.0
overrides['minecraft:dragon_breath'] = 150.0
overrides['minecraft:scute'] = 60.0
overrides['minecraft:turtle_helmet'] = 350.0
overrides['minecraft:armadillo_scute'] = 40.0
overrides['minecraft:wolf_armor'] = 260.0
overrides['minecraft:wet_sponge'] = 300.0
overrides['minecraft:sea_lantern'] = 100.0
overrides['minecraft:recovery_compass'] = 2500.0
overrides['minecraft:ominous_bottle'] = 500.0

# Discos de Música Vanilla
for d in ['13', 'cat', 'blocks', 'chirp', 'far', 'mall', 'mellohi', 'stal', 'strad', 'ward', '11', 'wait', 'otherside', 'relic', '5', 'pigstep', 'creator', 'creator_music_box', 'precipice']:
    overrides[f'minecraft:music_disc_{d}'] = 800.0
overrides['minecraft:music_disc_pigstep'] = 1500.0
overrides['minecraft:music_disc_otherside'] = 1200.0

# Moldes de Ferraria de Armadura (Smithing Trims)
for trim in ['sentry', 'vex', 'wild', 'coast', 'dune', 'wayfinder', 'raiser', 'shaper', 'host', 'ward', 'silence', 'tide', 'snout', 'rib', 'eye', 'spire', 'flow', 'bolt']:
    val = 2500.0 if trim == 'silence' else 800.0
    overrides[f'minecraft:{trim}_armor_trim_smithing_template'] = val

# ==============================================================================
# 2. SOPHISTICATED BACKPACKS (Mochilas e Upgrades)
# ==============================================================================
# Mochilas base
overrides['sophisticatedbackpacks:backpack'] = 150.0          # Couro + Baú + Linha
overrides['sophisticatedbackpacks:copper_backpack'] = 300.0   # + Cobre
overrides['sophisticatedbackpacks:iron_backpack'] = 650.0     # + 4 Ferros
overrides['sophisticatedbackpacks:gold_backpack'] = 1500.0    # + 8 Ouros
overrides['sophisticatedbackpacks:diamond_backpack'] = 4800.0 # + 8 Diamantes
overrides['sophisticatedbackpacks:netherite_backpack'] = 12000.0 # + Barra Netherite

# Base de Upgrades
overrides['sophisticatedbackpacks:upgrade_base'] = 100.0

# Upgrades Básicos
basic_upgrades = [
    'pickup_upgrade', 'filter_upgrade', 'magnet_upgrade', 'feeding_upgrade',
    'compacting_upgrade', 'void_upgrade', 'restock_upgrade', 'deposit_upgrade',
    'refill_upgrade', 'smelting_upgrade', 'smoking_upgrade', 'blasting_upgrade',
    'crafting_upgrade', 'stonecutter_upgrade', 'jukebox_upgrade', 'tool_swapper_upgrade',
    'tank_upgrade', 'battery_upgrade', 'pump_upgrade', 'xp_pump_upgrade', 'alchemy_upgrade'
]
for up in basic_upgrades:
    overrides[f'sophisticatedbackpacks:{up}'] = 250.0

# Upgrades Avançados (+Diamantes/Redstone)
adv_upgrades = [
    'advanced_pickup_upgrade', 'advanced_filter_upgrade', 'advanced_magnet_upgrade',
    'advanced_feeding_upgrade', 'advanced_compacting_upgrade', 'advanced_void_upgrade',
    'advanced_restock_upgrade', 'advanced_deposit_upgrade', 'advanced_refill_upgrade',
    'auto_smelting_upgrade', 'auto_smoking_upgrade', 'auto_blasting_upgrade',
    'advanced_jukebox_upgrade', 'advanced_tool_swapper_upgrade', 'advanced_pump_upgrade',
    'advanced_alchemy_upgrade', 'advanced_mob_catcher_upgrade', 'anvil_upgrade', 'smithing_upgrade'
]
for up in adv_upgrades:
    overrides[f'sophisticatedbackpacks:{up}'] = 950.0

# Upgrades de Capacidade (Stack Upgrades)
overrides['sophisticatedbackpacks:stack_upgrade_starter_tier'] = 200.0
overrides['sophisticatedbackpacks:stack_upgrade_tier_1'] = 400.0
overrides['sophisticatedbackpacks:stack_upgrade_tier_2'] = 1000.0
overrides['sophisticatedbackpacks:stack_upgrade_tier_3'] = 2400.0
overrides['sophisticatedbackpacks:stack_upgrade_tier_4'] = 5500.0
overrides['sophisticatedbackpacks:stack_upgrade_omega_tier'] = 12000.0
overrides['sophisticatedbackpacks:inception_upgrade'] = 3000.0
overrides['sophisticatedbackpacks:everlasting_upgrade'] = 6000.0

# ==============================================================================
# 3. SIMPLY SWORDS (Armas Normais e Míticas)
# ==============================================================================
# Tiers normais (Chakrams, Claymores, Cutlasses, Glaives, Greataxes, Halberds, Rapiers, Scythes, Spears, Twinblades, etc.)
weapon_types = [
    'longsword', 'twinblade', 'rapier', 'katana', 'sai', 'spear', 'glaive',
    'warglaive', 'cutlass', 'claymore', 'greathammer', 'greataxe', 'chakram',
    'scythe', 'halberd'
]

for w in weapon_types:
    overrides[f'simplyswords:iron_{w}'] = 150.0
    overrides[f'simplyswords:gold_{w}'] = 220.0
    overrides[f'simplyswords:diamond_{w}'] = 1400.0
    overrides[f'simplyswords:netherite_{w}'] = 3800.0
    overrides[f'simplyswords:runic_{w}'] = 2800.0

overrides['simplyswords:runic_tablet'] = 1200.0
overrides['simplyswords:runic_forge'] = 2500.0
overrides['simplyswords:netherfused_gem'] = 1500.0
overrides['simplyswords:empowered_remnant'] = 1800.0

# Armas Míticas / Lendárias Únicas
unique_swords = {
    'bramblethorn': 3500.0, 'brimstone_claymore': 3800.0, 'frostfall': 3800.0,
    'harbinger': 4200.0, 'hiveheart': 3500.0, 'icewhisper': 3800.0,
    'magiscythe': 4000.0, 'magispear': 4000.0, 'mjolnir': 5000.0,
    'shadowsting': 3600.0, 'soulkeeper': 4200.0, 'soulpyre': 4200.0,
    'soulrender': 4200.0, 'soulstealer': 4500.0, 'stormbringer': 4000.0,
    'stormcaller': 4000.0, 'sunfire': 4200.0, 'solfire': 4200.0,
    'whisperwind': 3600.0, 'dormant_relic': 2000.0, 'stars_edge': 4800.0,
    'twisted_blade': 3800.0, 'ribcleaver': 3500.0, 'livis_axe': 3800.0,
    'watching_warglaive': 4000.0, 'toxic_longsword': 3500.0, 'emberblade': 3800.0,
    'emberlash': 3800.0, 'thunderbrand': 4000.0, 'bloodwake': 4200.0,
    'flamewind': 4000.0, 'dreadtide': 4200.0, 'dreadwhisper': 4200.0,
    'caelestis': 4500.0, 'arcanethyst': 3500.0, 'hearthflame': 4000.0,
    'ribboncleaver': 3600.0, 'tempest': 4200.0
}
for name, val in unique_swords.items():
    overrides[f'simplyswords:{name}'] = val

# Variantes de compatibilidade de materiais (Mythic Metals / Bronze / Steel / etc.)
for mat, mult in [('bronze', 200.0), ('copper', 100.0), ('steel', 400.0), ('mythril', 1800.0), ('adamantite', 2200.0), ('orichalcum', 2400.0), ('runite', 2000.0), ('celestium', 3500.0)]:
    for w in weapon_types:
        overrides[f'simplyswords:{mat}_{w}'] = mult

# ==============================================================================
# 4. TWILIGHT FOREST (Dimensão e Chefes)
# ==============================================================================
# Materiais base
overrides['twilightforest:ironwood_ingot'] = 120.0
overrides['twilightforest:steeleaf_ingot'] = 100.0
overrides['twilightforest:knightmetal_ingot'] = 250.0
overrides['twilightforest:fiery_ingot'] = 500.0
overrides['twilightforest:fiery_blood'] = 450.0
overrides['twilightforest:fiery_tears'] = 450.0
overrides['twilightforest:naga_scale'] = 150.0
overrides['twilightforest:carminite'] = 300.0
overrides['twilightforest:hydra_chop'] = 80.0
overrides['twilightforest:meef_raw'] = 30.0
overrides['twilightforest:meef_steak'] = 40.0
overrides['twilightforest:meef_stroganoff'] = 250.0

# Ferramentas e Armaduras de Ironwood / Steeleaf / Knightmetal / Fiery
for mat, val_helm, val_chest, val_legs, val_boots, val_tool in [
    ('ironwood', 600.0, 950.0, 800.0, 500.0, 350.0),
    ('steeleaf', 500.0, 800.0, 700.0, 450.0, 300.0),
    ('knightmetal', 1200.0, 2000.0, 1600.0, 1000.0, 750.0),
    ('fiery', 2500.0, 4000.0, 3200.0, 2000.0, 1500.0)
]:
    overrides[f'twilightforest:{mat}_helmet'] = val_helm
    overrides[f'twilightforest:{mat}_chestplate'] = val_chest
    overrides[f'twilightforest:{mat}_leggings'] = val_legs
    overrides[f'twilightforest:{mat}_boots'] = val_boots
    for tool in ['sword', 'pickaxe', 'axe', 'shovel', 'hoe']:
        overrides[f'twilightforest:{mat}_{tool}'] = val_tool

overrides['twilightforest:knightmetal_shield'] = 1200.0

# Relíquias e Armas de Bosses
overrides['twilightforest:glass_sword'] = 1500.0
overrides['twilightforest:diamond_minotaur_axe'] = 2200.0
overrides['twilightforest:gold_minotaur_axe'] = 800.0
overrides['twilightforest:mazebreaker'] = 2500.0
overrides['twilightforest:twilight_scepter'] = 2000.0
overrides['twilightforest:lifedrain_scepter'] = 2000.0
overrides['twilightforest:zombie_scepter'] = 2000.0
overrides['twilightforest:shield_scepter'] = 2000.0
overrides['twilightforest:fortification_scepter'] = 2000.0
overrides['twilightforest:seeker_bow'] = 2200.0
overrides['twilightforest:triple_bow'] = 2200.0
overrides['twilightforest:ice_bow'] = 2200.0
overrides['twilightforest:ender_bow'] = 2500.0
overrides['twilightforest:ice_sword'] = 1600.0
overrides['twilightforest:giant_sword'] = 3000.0
overrides['twilightforest:giant_pickaxe'] = 3000.0
overrides['twilightforest:cube_of_annihilation'] = 3500.0
overrides['twilightforest:crumble_horn'] = 1800.0
overrides['twilightforest:ore_magnet'] = 1800.0
overrides['twilightforest:charm_of_life_1'] = 600.0
overrides['twilightforest:charm_of_life_2'] = 1800.0
overrides['twilightforest:charm_of_keeping_1'] = 500.0
overrides['twilightforest:charm_of_keeping_2'] = 1500.0
overrides['twilightforest:charm_of_keeping_3'] = 3500.0

# Troféus de Chefes do Twilight Forest
for trophy in ['naga', 'lich', 'hydra', 'ur_ghast', 'knight_phantom', 'snow_queen', 'alpha_yeti', 'minoshroom', 'questing_ram']:
    overrides[f'twilightforest:{trophy}_trophy'] = 2500.0

# ==============================================================================
# 5. CREATE & CREATE GUNSMITHING
# ==============================================================================
# Componentes Mecânicos do Create
overrides['create:brass_ingot'] = 80.0
overrides['create:brass_sheet'] = 80.0
overrides['create:electron_tube'] = 150.0
overrides['create:precision_mechanism'] = 600.0
overrides['create:blaze_burner'] = 800.0
overrides['create:empty_blaze_burner'] = 250.0
overrides['create:steam_engine'] = 1200.0
overrides['create:extendo_grip'] = 1500.0
overrides['create:potato_cannon'] = 1800.0
overrides['create:wand_of_symmetry'] = 2200.0
overrides['create:goggles'] = 120.0
overrides['create:wrench'] = 120.0
overrides['create:crushing_wheel'] = 1200.0
overrides['create:mechanical_arm'] = 900.0
overrides['create:schematicannon'] = 2000.0

# Create Gunsmithing (Armas de Fogo, Peças e Munição)
overrides['cgs:lead_ingot'] = 50.0
overrides['cgs:steel_ingot'] = 90.0
overrides['cgs:niter'] = 30.0
overrides['cgs:sulfur'] = 30.0
overrides['cgs:flintlock'] = 800.0
overrides['cgs:blunderbuss_barrel'] = 500.0
overrides['cgs:shotgun'] = 1800.0
overrides['cgs:revolver'] = 2200.0
overrides['cgs:gatling'] = 4500.0
overrides['cgs:blazegun'] = 3800.0
overrides['cgs:ballistazooka'] = 4000.0
overrides['cgs:nailgun'] = 1400.0
overrides['cgs:launcher'] = 3000.0
overrides['cgs:launcher_auto'] = 4500.0
overrides['cgs:frag_grenade'] = 250.0
overrides['cgs:rocket'] = 300.0
overrides['cgs:rocket_small'] = 150.0
overrides['cgs:scope'] = 350.0

# ==============================================================================
# 6. THE SIFT (Dimensão e Equipamentos de Siftite)
# ==============================================================================
overrides['the_sift:siftite_ingot'] = 600.0
overrides['the_sift:siftite_nugget'] = 66.0
overrides['the_sift:charoite'] = 450.0
overrides['the_sift:ichor_shard'] = 180.0
overrides['the_sift:ichor_bottle'] = 250.0
overrides['the_sift:ichor_bucket'] = 400.0
overrides['the_sift:siftite_upgrade_smithing_template'] = 1000.0

# Equipamentos de Siftite (Nível Netherite+)
overrides['the_sift:siftite_helmet'] = 3200.0
overrides['the_sift:siftite_chestplate'] = 5000.0
overrides['the_sift:siftite_leggings'] = 4200.0
overrides['the_sift:siftite_boots'] = 2800.0
overrides['the_sift:siftite_sword'] = 2500.0
overrides['the_sift:siftite_pickaxe'] = 2500.0
overrides['the_sift:siftite_axe'] = 2500.0
overrides['the_sift:siftite_shovel'] = 1200.0
overrides['the_sift:siftite_hoe'] = 1800.0
overrides['the_sift:music_disc_rift'] = 800.0
overrides['the_sift:music_disc_wellspring'] = 800.0

# ==============================================================================
# 7. TOM'S SIMPLE STORAGE & WAYSTONES
# ==============================================================================
overrides['toms_storage:storage_terminal'] = 450.0
overrides['toms_storage:crafting_terminal'] = 950.0
overrides['toms_storage:wireless_terminal'] = 1800.0
overrides['toms_storage:adv_wireless_terminal'] = 3800.0
overrides['toms_storage:inventory_connector'] = 350.0
overrides['toms_storage:inventory_cable'] = 25.0
overrides['toms_storage:inventory_cable_connector'] = 120.0
overrides['toms_storage:filing_cabinet'] = 300.0

overrides['waystones:waystone'] = 600.0
overrides['waystones:sharestone'] = 750.0
overrides['waystones:warp_stone'] = 1500.0
overrides['waystones:warp_plate'] = 800.0
overrides['waystones:warp_scroll'] = 120.0
overrides['waystones:return_scroll'] = 100.0
overrides['waystones:bound_scroll'] = 150.0
overrides['waystones:attuned_shard'] = 250.0

# ==============================================================================
# 8. CATACLYSM (Bosses Supremos)
# ==============================================================================
cataclysm_boss = {
    'cataclysm:ignitium_ingot': 2400.0,
    'cataclysm:ignitium_block': 21600.0,
    'cataclysm:witherite_ingot': 3000.0,
    'cataclysm:witherite_block': 27000.0,
    'cataclysm:void_core': 5000.0,
    'cataclysm:monstrous_horn': 3500.0,
    'cataclysm:abyssal_sacrifice': 4000.0,
    'cataclysm:infernal_forge': 15000.0,
    'cataclysm:ignitium_upgrade_smithing_template': 1200.0,
    'cataclysm:flame_eye': 800.0,
    'cataclysm:abyss_eye': 800.0,
    'cataclysm:desert_eye': 800.0,
    'cataclysm:cursed_eye': 800.0,
    'cataclysm:mech_eye': 800.0,
    'cataclysm:monstrous_eye': 800.0,
    'cataclysm:storm_eye': 800.0,
    'cataclysm:void_eye': 1200.0,
    'cataclysm:the_incinerator': 8000.0,
    'cataclysm:gauntlet_of_guard': 7500.0,
    'cataclysm:gauntlet_of_bulwark': 7500.0,
    'cataclysm:gauntlet_of_maelstrom': 9000.0,
    'cataclysm:meat_shredder': 6000.0,
    'cataclysm:tidal_claws': 7000.0,
    'cataclysm:coral_spear': 2500.0,
    'cataclysm:ancient_spear': 3000.0,
    'cataclysm:azure_sea_shield': 3500.0,
    'cataclysm:ignitium_helmet': 7000.0,
    'cataclysm:ignitium_chestplate': 12000.0,
    'cataclysm:ignitium_elytra_chestplate': 16000.0,
    'cataclysm:ignitium_leggings': 9000.0,
    'cataclysm:ignitium_boots': 6000.0,
    'cataclysm:monstrous_helm': 7500.0,
    'cataclysm:cursium_helmet': 5000.0,
    'cataclysm:cursium_chestplate': 8000.0,
    'cataclysm:cursium_boots': 4500.0
}
overrides.update(cataclysm_boss)

# ==============================================================================
# 9. THE BUMBLEZONE & ARMOR OF THE AGES
# ==============================================================================
bumble_ages = {
    'the_bumblezone:royal_jelly_bottle': 600.0,
    'the_bumblezone:royal_jelly_block': 5400.0,
    'the_bumblezone:bee_cannon': 2500.0,
    'the_bumblezone:crystal_cannon': 3500.0,
    'the_bumblezone:stingless_bee_helmet_1': 1500.0,
    'the_bumblezone:bumble_bee_chestplate_1': 2500.0,
    'the_bumblezone:honey_bee_leggings_1': 2000.0,
    'the_bumblezone:carpenter_bee_boots_1': 1500.0,
    'the_bumblezone:honey_crystal_shards': 80.0,
    'the_bumblezone:pollen_puff': 15.0,
    'armoroftheages:holy_armor_head': 1200.0,
    'armoroftheages:holy_armor_chest': 2000.0,
    'armoroftheages:holy_armor_legs': 1600.0,
    'armoroftheages:holy_armor_feet': 1000.0,
    'armoroftheages:centurion_armor_head': 1200.0,
    'armoroftheages:centurion_armor_chest': 2000.0,
    'armoroftheages:centurion_armor_legs': 1600.0,
    'armoroftheages:centurion_armor_feet': 1000.0,
    'armoroftheages:pharaoh_armor_head': 1500.0,
    'armoroftheages:pharaoh_armor_chest': 2400.0,
    'armoroftheages:pharaoh_armor_legs': 1800.0,
    'armoroftheages:pharaoh_armor_feet': 1200.0,
    'armoroftheages:quetzalcoatl_armor_head': 1600.0,
    'armoroftheages:quetzalcoatl_armor_chest': 2600.0,
    'armoroftheages:quetzalcoatl_armor_legs': 2000.0,
    'armoroftheages:quetzalcoatl_armor_feet': 1400.0
}
overrides.update(bumble_ages)

# Formata o arquivo TOML
override_lines = [f'    \"{k}={int(v)}\"' for k, v in sorted(overrides.items())]
formatted_overrides = ',\n'.join(override_lines)

config_content = f'''# Multiplier applied to the raw value ratio. 1.0 = fair odds, 0.9 = 10% house edge.
# Default: 0.9
houseEdge = 0.9

# Lowest possible success chance (0.001 = 0.1%).
minChance = 0.001

# Highest possible success chance. Keeps 'downgrades' from being a free win.
maxChance = 0.9

# How long the wheel spins before the result is applied, in ticks (20 = 1 second).
spinDurationTicks = 70

# Hard-coded item values, format 'modid:item=value'. These win over the built-in table.
# Configurado pelo BlessForge com balanceamento para +{len(overrides)} itens!
valueOverrides = [
{formatted_overrides}
]

# Multiplies every item's price, valueOverrides included.
globalValueMultiplier = 1.0

# Per-item multipliers on top of globalValueMultiplier.
valueMultipliers = []

# Items that can never be used as an input or picked as a target.
blacklist = []

# Most target items one upgrade may ask for.
maxTargetCount = 64

# Attempts a player gets per window. 0 removes the limit.
attemptLimit = 0

# Length of that window in seconds. 0 removes the limit.
attemptWindowSeconds = 0
'''

os.makedirs(os.path.dirname(CONFIG_SRC), exist_ok=True)
with open(CONFIG_SRC, 'w', encoding='utf-8') as f:
    f.write(config_content)

os.makedirs(os.path.dirname(CONFIG_MC), exist_ok=True)
with open(CONFIG_MC, 'w', encoding='utf-8') as f:
    f.write(config_content)

print(f"🎉 Sucesso! {len(overrides)} itens calibrados e injetados em:")
print(f"   └─ {CONFIG_SRC}")
print(f"   └─ {CONFIG_MC}")
