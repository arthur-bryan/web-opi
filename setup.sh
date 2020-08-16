#!/bin/bash

if ((EUID != 0))
then
	echo "[ ! ] Please, run this script with sudo or as root!"
else
	apt install python3-pip -y
    chmod +x uninstall.sh
    python3 -m pip install -r requirements.txt
	echo -e "\n[ + ] Setup done! Start the server with 'python3 start-web-opi' command from this folder.\n"
    sleep 1
fi
