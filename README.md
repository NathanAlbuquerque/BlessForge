# ⚔️ BlessForge — Modpack & Ecossistema Minecraft 1.21.1 (NeoForge)

[![Minecraft](https://img.shields.io/badge/Minecraft-1.21.1-brightgreen.svg)](https://www.minecraft.net/)
[![NeoForge](https://img.shields.io/badge/NeoForge-21.1.259-orange.svg)](https://neoforged.net/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

O **BlessForge** é uma curadoria de alta performance e aventura para Minecraft 1.21.1, combinando geração de terreno cinematográfica (**Tectonic + Terralith**), automação e engenharia (**Create**), chefes e dimensões épicas (**Cataclysm + Twilight Forest + Bumblezone**), combate dinâmico e otimizações extremas para máxima estabilidade de FPS.

---

## 🌟 Destaques do Projeto

* 🏔️ **Geração Épica:** Cordilheiras realistas, rios navegáveis e mais de 90 biomas sem blocos incompatíveis.
* ⚡ **Performance Otimizada:** Sodium, ModernFix, FerriteCore, EntityCulling, ImmediatelyFast e BadOptimizations.
* 🎮 **Mod Menu Web Interativo:** Aplicativo offline local para explorar, filtrar e exportar seleções personalizadas do modpack.
* 📦 **Resolvedor de Dependências Automático:** Exportador que garante que nenhum mod falte com dependências quebradas.

---

## 📁 Estrutura do Repositório

Consulte o documento completo de diretrizes em [ARQUITETURA.md](docs/ARQUITETURA.md).

```
BlessForge/
├── mods/                  # Mods ativos (.jar) prontos para jogar
├── desativados/           # Mods isolados para testes ou diagnóstico
├── resourcepacks/         # Pacotes de recursos (.zip)
├── exportados/            # Builds e pacotes gerados pelo exportador
├── tools/                 # Automações Python (scanner, exportador, servidor)
├── docs/                  # Documentação técnica e catálogo analítico
├── assets/                # Recursos visuais e ícones extraídos dos mods
├── abrir_mod_menu.sh      # Atalho para iniciar a interface web do Mod Menu
├── atualizar.sh           # Atalho para sincronizar metadados e atualizar catálogos
├── exportar.sh            # Atalho para exportar pacotes (.zip ou pastas)
└── mod_menu.html          # Web app offline estilo in-game
```

---

## 🛠️ Como Utilizar

### 1. Atualizar Catálogos e Metadados
Após adicionar ou remover qualquer mod em `mods/`:
```bash
./atualizar.sh
```

### 2. Abrir o Mod Menu Interativo no Navegador
```bash
./abrir_mod_menu.sh
```

### 3. Exportar Modpacks Personalizados
Para gerar um pacote ZIP (ex: apenas Client-Side para entrar em servidores públicos, ou versão Vanilla+):
```bash
./exportar.sh
```

---

## 📄 Catálogo Completo dos Mods
A lista detalhada de cada mod instalado, suas versões, dependências e descrições encontra-se em:
👉 **[Catálogo Geral de Mods (docs/MODS_CATALOG.md)](docs/MODS_CATALOG.md)**
