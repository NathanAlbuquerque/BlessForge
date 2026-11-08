# ⚔️ BlessForge — Curated NeoForge 1.21.1 Modpack & Manager Suite

[![Minecraft](https://img.shields.io/badge/Minecraft-1.21.1-brightgreen.svg?logo=minecraft)](https://minecraft.net/)
[![Loader](https://img.shields.io/badge/ModLoader-NeoForge-orange.svg)](https://neoforged.net/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python)](https://python.org/)
[![License](https://img.shields.io/badge/License-MIT-purple.svg)](LICENSE)

Sistema integrado de **gerenciamento, catalogação visual e exportação automatizada de modpacks** para Minecraft 1.21.1 NeoForge.

O projeto resolve o problema clássico de gerenciar dezenas de mods e suas dependências técnicas, permitindo:
1. Navegar por todos os mods em uma interface visual in-game (*Mod Menu*).
2. Atualizar e sincronizar automaticamente metadados e logos ao adicionar novos arquivos `.jar`.
3. Selecionar qualquer combinação de mods com **resolução recursiva de dependências** para exportar em formato `.zip` (para amigos) ou pasta pronta (para jogar).

---

## 🚀 Funcionalidades Principais

- 🎮 **Visual Mod Menu Offline (`mod_menu.html`):**
  - Interface rica com logos oficiais extraídos direto dos arquivos `.jar`.
  - Pesquisa instantânea em tempo real (`Ctrl+K`), filtros por categoria e status.
  - Inspetor completo de detalhes: links oficiais do CurseForge, escopo (*Client/Server*), tamanho em disco e árvore de dependências interativa.

- 📦 **Construtor & Exportador de Modpacks (`exportador.py` / `exportar.sh`):**
  - Selecione qualquer conjunto de mods (ou use *Presets Rápidos*).
  - O sistema calcula automaticamente todas as bibliotecas e APIs obrigatórias.
  - Gera pacotes comprimidos `.zip` com subpasta `mods/`, `resourcepacks/`, `manifest.json` e instruções passo a passo em `LEIA-ME_INSTALACAO.txt`.

- ⚡ **Presets Rápidos Incluídos:**
  - 🌐 **Client-Side Only (Para Servidores):** Seleciona exclusivamente mods de tela, HUD, som e performance que você pode usar ao entrar no servidor de amigos ou servidores públicos sem causar erro de incompatibilidade.
  - 🚀 **Todos os Ativos:** O pacote completo com toda a biblioteca ativa.
  - ⚡ **Vanilla+ & Otimização:** Otimização máxima (Sodium, ModernFix, FerriteCore) + QoL essencial.
  - ⚙️ **Create & Tecnologia:** Create, armas de fogo (`Create: Gunsmithing`), engenharias e dependências gráficas.
  - ⚔️ **Aventura & RPG:** Chefes épicos (*L_Ender's Cataclysm*), *The Twilight Forest*, *Simply Swords* e masmorras.
  - 🎒 **Armazenamento Avançado:** *Sophisticated Backpacks*, *Tom's Simple Storage*, etc.

- 🔄 **Sincronização com 1 Clique (`atualizar_catalogo.py` / `servidor_mod_menu.py`):**
  - Extração automatizada de metadados (`neoforge.mods.toml`, `mods.toml`, `fabric.mod.json`).
  - Botão de sincronização ao vivo direto na interface web.

---

## 🛠️ Como Usar

### 1. Abrir o Mod Menu Visual (Recomendado)
Execute o script inicializador para abrir o servidor local com sincronização em tempo real:
```bash
./abrir_mod_menu.sh
```
> O menu será aberto automaticamente no seu navegador padrão em `http://localhost:8080`.

### 2. Exportar um Modpack Personalizado
Você pode exportar diretamente pelo **Mod Menu visual** (marcando as caixinhas `[✔]` e clicando em **Exportar**) ou pelo terminal:
```bash
./exportar.sh
```
Os pacotes gerados serão salvos na pasta `exportados/`.

### 3. Atualizar ao Baixar Novos Mods
Sempre que colar novos arquivos `.jar` na pasta, clique em **"🔄 Sincronizar Novos Mods"** no topo da interface visual, ou execute no terminal:
```bash
./atualizar.sh
```

---

## 📂 Estrutura de Pastas

```text
.
├── .                           # Mods ativos (.jar) prontos para uso
├── desativados/                # Mods desativados/em teste temporário
├── resourcepacks/              # Pacotes de texturas e sons (.zip)
├── exportados/                 # Pacotes .zip e pastas geradas pelo exportador
├── assets/icons/               # Logos e ícones oficiais extraídos dos mods
├── mod_menu.html               # Aplicação visual offline do Mod Menu
├── MODS_CATALOG.md             # Catálogo estruturado em Markdown com tabelas completas
├── ideias_e_links.txt          # Lista de desejos de mods/datapacks anotados
├── servidor_mod_menu.py        # Servidor local para a interface web
├── atualizar_catalogo.py       # Motor de extração e sincronização de metadados
├── exportador.py               # Motor de resolução de dependências e empacotador
├── abrir_mod_menu.sh           # Inicializador do Mod Menu no navegador
├── atualizar.sh                # Script de sincronização rápida
└── exportar.sh                 # Assistente de exportação no terminal
```

---

## 📋 Requisitos do Sistema

- **Python 3.8+** (utiliza apenas bibliotecas padrão do Python: `http.server`, `zipfile`, `json`, `urllib`).
- Qualquer navegador moderno (Google Chrome, Firefox, Brave, Edge).
