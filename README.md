# 🐍 QuetzalOS

> Première distribution Linux à thème aztèque, basée sur Parrot OS Security — Version 1.0 Beta

## Description
QuetzalOS est une distribution Linux orientée sécurité informatique,
habillée d'un thème aztèque complet. Inspirée de Red Star OS.

## Installation

### Étape 1 — Installer l'interface graphique
```bash
sudo apt install xorg mate-desktop-environment lightdm -y

###Étape 2 — Démarrer l'interface graphique
sudo systemctl start lightdm

###Étape 3 — Connexion
Username : user
Password : live

###Étape 4 — Cloner le dépôt
git clone https://github.com/ralphwdamis-hub/QuetzalOS.git

###Étape 5 — Lancer QuetzalOS
cd QuetzalOS/olmec-shell
sudo apt install nodejs npm -y
npx electron .

###Basé sur
Parrot OS Security 6.x
Bureau MATE
Olmec Shell (terminal sécurité)
Calendrier Tonalpohualli + Haab' maya
Milpa Market (boutique aztèque)

###Licence
GPL v3
