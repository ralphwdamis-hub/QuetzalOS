#! /bin/bash
sudo apt install nodejs npm -y
python3 ~/QuetzalOS/milpa-market/terminal_server.py &
cd ~/QuetzalOS/olmec-shell
npx electron .
