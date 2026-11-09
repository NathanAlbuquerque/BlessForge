#!/usr/bin/env bash
cd "$(dirname "$0")"
python3 tools/atualizar_catalogo.py
read -p "Pressione [Enter] para fechar..."
