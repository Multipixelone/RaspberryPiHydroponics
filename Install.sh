#!/bin/bash
# Made by Multipixelone
if [ "$EUID" -ne 0 ]
  then echo "Sorry, I need root access . Please run as root or with sudo ;)"
  exit
fi

read -r -p "Proceed with Install? [y/n]"
echo
if [[ ! $REPLY =~ ^[Nn]$ ]]
then
    apt-get update
    apt-get --yes upgrade
    sudo apt-get install --yes rpi.gpio
    reboot
else
    echo Install Cancelled... Exiting
    exit 0
fi
