#!/bin/bash

if ((EUID != 0))
then
	echo "[ ! ] Please, run this script with sudo or as root!."
else
	python3 -m pip uninstall -r requirements.txt -y
	rm -r ../web-opi
	echo "[ + ] Files was removed successfully!"
	sleep 1
fi
