#! /bin/bash
sudo apt install nodejs npm -y
python3 ~/QuetzalOS/olmec-shell/terminal_server.py &
cd ~/QuetzalOS/olmec-shell
npx electron .
