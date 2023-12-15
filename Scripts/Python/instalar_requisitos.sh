#!/bin/bash

mkdir scripts
cd scripts
source venv/bin/activate

cd ..
pip install --upgrade pip
pip install --upgrade pip
sudo pacman -S base-devel

while IFS= read -r line; do
    package=$(echo "$line" | tr -d '\r\n')
    echo "Instalando $package..."
    pip install "$package"
done < requisitos.txt

deactivate
echo "Instalación completada, eliminando residuos..."
rm -rf scripts
