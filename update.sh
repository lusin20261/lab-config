#!/bin/bash

set -e

REPO=/home/alumno/.config/lab-config

cd "$REPO"

git pull origin main

sudo python3 generate_rules.py

sudo systemctl restart dnsmasq

echo "Configuración actualizada."
