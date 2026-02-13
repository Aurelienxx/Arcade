#!/bin/bash

sudo apt upgrade

# Fonction pour vérifier et installer un paquet
check_and_install() {
  command -v "$1" &> /dev/null
  if [ $? -ne 0 ]; then
    echo "$1 n'est pas installé. Installation..."
    sudo apt-get update
    sudo apt-get install -y "$2"
  else
    echo "$1 est déjà installé."
  fi
}

# Vérifier et installer Python
check_and_install "python3" "python3"

# Vérifier et installer Java
check_and_install "java" "default-jdk"

# Vérifier et installer pip (gestionnaire de paquets pour Python)
check_and_install "pip3" "python3-pip"

# Vérifier et installer Lua
check_and_install "lua" "lua5.3"

# Créer un environnement virtuel pour Python si ce n'est pas déjà fait
if [ ! -d "$HOME/python_env" ]; then
  echo "Création d'un environnement virtuel Python dans $HOME/python_env..."
  python3 -m venv $HOME/python_env
fi

# Activer l'environnement virtuel
source $HOME/python_env/bin/activate

# Vérifier et installer Pygame (via pip dans l'environnement virtuel)
if ! python3 -c "import pygame" &> /dev/null; then
  echo "Pygame n'est pas installé dans l'environnement virtuel. Installation..."
  pip install pygame
else
  echo "Pygame est déjà installé dans l'environnement virtuel."
fi

# Vérifier et installer librosa (via pip dans l'environnement virtuel)
if ! python3 -c "import librosa" &> /dev/null; then
  echo "Librosa n'est pas installé dans l'environnement virtuel. Installation..."
  pip install librosa
else
  echo "Librosa est déjà installé dans l'environnement virtuel."
fi

echo "Vérification et installation terminées."
