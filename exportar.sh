#!/usr/bin/env bash
cd "$(dirname "$0")"
python3 tools/exportar_modpack.py
read -p "Pressione [Enter] para fechar..."
