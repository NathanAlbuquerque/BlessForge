# 📐 Arquitetura & Diretrizes de Estrutura do BlessForge

Este documento define a organização profissional de pastas, convenções de código, regras de versionamento Git e procedimentos operacionais para o ecossistema **BlessForge**.

---

## 🏗️ Estrutura de Diretórios

```
BlessForge/
├── mods/                  # Mods ativos (.jar) prontos para jogar
├── desativados/           # Mods isolados para testes ou diagnóstico de conflitos
├── resourcepacks/         # Pacotes de recursos (.zip) visuais e de som
├── exportados/            # Builds exportadas (modpacks gerados em .zip ou pastas)
├── tools/                 # Scripts Python utilitários e automações de build
│   ├── atualizar_catalogo.py  # Scanner de metadados, dependências e gerador de docs
│   ├── exportador.py          # Resolvedor transitivo de dependências
│   ├── exportar_modpack.py    # Assistente CLI de exportação por presets
│   └── servidor_mod_menu.py   # Servidor HTTP local do Mod Menu Web
├── docs/                  # Documentação técnica e catálogos do projeto
│   ├── ARQUITETURA.md         # Este documento de regras e padrões
│   ├── MODS_CATALOG.md        # Catálogo analítico completo gerado automaticamente
│   └── ideias_e_links.txt     # Wishlist e anotações de mods para avaliação
├── assets/                # Recursos estáticos (ícones extraídos, logos)
│   └── icons/                 # Ícones dos mods em PNG
├── abrir_mod_menu.sh      # Atalho rápido para iniciar a interface web interativa
├── atualizar.sh           # Atalho rápido para re-escanear e atualizar o catálogo
├── exportar.sh            # Atalho rápido para o assistente de exportação
├── mod_menu.html          # Web app offline responsivo (estilo in-game Mod Menu)
├── README.md              # Visão geral do repositório no GitHub
└── .gitignore             # Filtro de binários pesados e artefatos de build
```

---

## 📋 Regras de Organização

### 1. Separação Estrita de Responsabilidades
* **Nenhum arquivo `.jar` deve ficar solto na raiz.** Todos os mods ativos residem em `mods/` e os inativos em `desativados/`.
* **Nenhum script Python deve ficar solto na raiz.** Automações residem em `tools/`.
* Na raiz do projeto, ficam apenas:
  * Os scripts executáveis de conveniência (`.sh`)
  * O aplicativo web offline (`mod_menu.html`)
  * Os arquivos de documentação principal (`README.md`, `.gitignore`)

### 2. Versionamento Git
* **Arquivos binários pesados (`.jar`, `.zip` de resource packs) NÃO são commitados no Git.** Eles são ignorados pelo `.gitignore` para manter o repositório leve, rápido para clonar e dentro dos limites do GitHub.
* O Git rastreia:
  * Todo o código-fonte de scripts (`tools/`)
  * A documentação técnica (`docs/`)
  * As definições de metadados, catálogos e interface web (`mod_menu.html`)
  * Scripts bash (`*.sh`)

### 3. Automação e Sincronização
* Sempre que um mod for adicionado, atualizado ou removido de `mods/`:
  1. Execute `./atualizar.sh` (ou `python3 tools/atualizar_catalogo.py`).
  2. O script detecta automaticamente o novo mod, lê o `META-INF/neoforge.mods.toml`, extrai o ícone oficial para `assets/icons/` e atualiza tanto o `docs/MODS_CATALOG.md` quanto o `mod_menu.html`.
  3. Faça o commit das alterações de documentação geradas.

---

## 🚀 Como Usar os Utilitários

| Comando / Script | Função |
| :--- | :--- |
| `./abrir_mod_menu.sh` | Inicia o servidor local e abre o **Mod Menu Web** com busca rápida (`Ctrl+K`), filtros e exportação. |
| `./atualizar.sh` | Escaneia todas as pastas, extrai ícones e recompila os catálogos Markdown e HTML. |
| `./exportar.sh` | Abre o assistente interativo no terminal para gerar modpacks (Client-side, Vanilla+, etc.) com resolução de dependências. |
