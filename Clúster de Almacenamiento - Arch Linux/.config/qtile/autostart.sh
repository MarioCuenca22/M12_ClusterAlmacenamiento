#!/bin/sh

# Gestor de Volumen (Systray)
cbatticon -u 5 &

# Gestor de Redes (Systray)
nm-applet &

#Gestor de Dispositivos
udiskie &
