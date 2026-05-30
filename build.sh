#!/usr/bin/env bash
set -o errexit

# Instalar dependencias
pip install -r requirements.txt

# Aplicar migraciones de la base de datos
reflex db migrate