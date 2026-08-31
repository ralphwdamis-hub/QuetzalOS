# 🐍 QuetzalOS
Première distribution Linux à thème aztèque, basée sur Parrot OS Security

## Versions
- **v1.0 Beta** — Version initiale
- **v1.1 Beta** — Version enrichie (branche v1.1)

## Nouveautés v1.1
- 📖 Dictionnaire nahuatl 170+ mots + Grammaire
- 🌞 Roue solaire améliorée
- 📝 Itzamná — Traitement de texte
- 📊 Tlaloc — Tableur
- 🎨 Xochiquetzal — Présentations
- 🔢 Cipactli — Calculatrice scientifique
- 🖼️ Coatlicue — Visionneuse images
- 📄 Quetzalcóatl Reader — PDF
- 🎵 Xochipilli Player — Média player
- 🛡️ Teotihuacan Antivirus
- 🥁 Huehuetl Studio — Musique aztèque
- 🔐 Cipactli Cipher — Chiffrement AES-256 .nah
- 💬 Pochteca Network — Messagerie
- 🗑️ Mictlan — Corbeille
- 🔌 Calli USB — Gestionnaire fichiers
- 🔍 Recherche rapide des applications

## Installation

### Étape 1 — Installer l'interface graphique
sudo apt install xorg mate-desktop-environment lightdm -y

### Étape 2 — Démarrer l'interface graphique
sudo systemctl start lightdm

### Étape 3 — Connexion
Username : user
Password : live

### Étape 4 — Cloner le dépôt (après avoir ouvert le terminal MATE)
git clone https://github.com/ralphwdamis-hub/QuetzalOS.git

### Étape 5 — Installer les dépendances
cd QuetzalOS/olmec-shell
npm install --timeout=60000

### Étape 6 — Lancer QuetzalOS
cd ~/QuetzalOS
git pull origin master
~/QuetzalOS/start.sh

## Contact
ralphwdamis@gmail.com

## Licence
GPL v3
