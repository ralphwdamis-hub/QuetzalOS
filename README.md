# 🐍 QuetzalOS
Première distribution Linux à thème aztèque, basée sur Parrot OS Security — Version 1.0 Beta

## Installation

### Étape 1 — Installer l'interface graphique
sudo apt install xorg mate-desktop-environment lightdm -y

### Étape 2 — Démarrer l'interface graphique
sudo systemctl start lightdm

### Étape 3 — Connexion
Username : user
Password : live

### Étape 4 — Cloner le dépôt
git clone https://github.com/ralphwdamis-hub/QuetzalOS.git

### Étape 5 — Installer les dépendances
cd QuetzalOS/olmec-shell
npm install --timeout=60000

### Étape 6 — Lancer QuetzalOS
cd ~/QuetzalOS
git pull origin master
~/QuetzalOS/start.sh

###Basé sur
Parrot OS Security 6.x
Bureau MATE
Olmec Shell (terminal sécurité)
Calendrier Tonalpohualli + Haab' maya
Milpa Market (boutique aztèque)

###Licence
GPL v3
