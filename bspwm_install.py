import os
import sys
import colorama
from colorama import Fore, Style
import getpass
import subprocess

#---------------------------------------------------------------
# INFORMACION CREADOR
#----------------------------------------------------------------
print(Fore.RED + 

"""
  __  __         ___ _ _                     _ 
 |  \/  |_ _ ___/ __| | | _ __ _  _ _ _ __ _/ |
 | |\/| | '_|___\__ \_  _| '  \ || | '_/ _` | |
 |_|  |_|_|     |___/ |_||_|_|_\_,_|_| \__,_|_|
"""
)
print(Fore.BLUE + " - AutoBspwm de Mr-S4mura1 - 2024")
print(Fore.BLUE + " - Github: https://github.com/Mr-S4mura1")


#----------------------------------------------------------------
# COMPROBACION DE USUARIO ROOT
# ----------------------------------------------------------------

def check_root():
    if os.geteuid() == 0:
        print("")
        print(Fore.RED + " - Eres usuario root.")
    else:
        print("")
        print(Fore.RED + " - Requires ser usuario Root!")
        sys.exit()
check_root()
            
# ----------------------------------------------------------------
# Actualizacion de paquetes
#-----------------------------------------------------------------

print(Fore.BLUE + " - Actualizando paquetes Linux!")
command_update = "sudo apt-get update -y"
command_upgrade = "sudo apt-get upgrade -y"

try:
    update = subprocess.run(command_update, shell=True, text=True, capture_output=True)
    upgrade = subprocess.run(command_upgrade, shell=True, text=True, capture_output=True)
    print(Fore.BLUE + " - Paquetes Actualizados correctamente!")
except subprocess.CalledProcessError as e:
    print(Fore.RED + " - Error al instalar paquetes!")
    print(e.stdout)
    print(e.stderr)

#---------------------------------------------------------------
# Instalacion paquetes bspwm sxhkd
#---------------------------------------------------------------
bspwm_install = "sudo apt-get install bspwm sxhkd build-essential git vim libxcb-util0-dev libxcb-ewmh-dev libxcb-randr0-dev libxcb-icccm4-dev libxcb-keysyms1-dev libxcb-xinerama0-dev libasound2-dev libxcb-xtest0-dev libxcb-shape0-dev thunar cmake cmake-data pkg-config python3-sphinx libcairo2-dev libxcb1-dev libxcb-util0-dev libxcb-randr0-dev libxcb-composite0-dev python3-xcbgen xcb-proto libxcb-image0-dev libxcb-ewmh-dev libxcb-icccm4-dev libxcb-xkb-dev libxcb-xrm-dev libxcb-cursor-dev libasound2-dev libpulse-dev libjsoncpp-dev libmpdclient-dev libcurl4-openssl-dev libnl-genl-3-dev polybar rofi calc network-manager picom kali-screensaver hollywood-activate xss-lock meson libxext-dev libxcb1-dev libxcb-damage0-dev libxcb-xfixes0-dev libxcb-shape0-dev libxcb-render-util0-dev libxcb-render0-dev libxcb-randr0-dev libxcb-composite0-dev libxcb-image0-dev libxcb-present-dev libxcb-xinerama0-dev libpixman-1-dev libdbus-1-dev libconfig-dev libgl1-mesa-dev libpcre2-dev libevdev-dev uthash-dev libev-dev libx11-xcb-dev libxcb-glx0-dev feh wget pulseaudio pulseaudio alsa-utils pamixer brightnessctl"

print(Fore.BLUE + " - Instalando paquetes necesarios!")
try:
    bspwm = subprocess.run(bspwm_install, shell=True, text=True, capture_output=True)
    print(Fore.BLUE + " - Paquetes necesarios instalados Correctamente!")
except subprocess.CalledProcessError as e:
    print(Fore.RED + " - Error al instalar los paquetes que se requieren!")
    print(e.stdout)
    print(e.stderr)

#------------------------------------------------------------
# Clonacion de Repositorios 
# ----------------------------------------------------------
print(Fore.BLUE + " - Clonando repositorios necesarios")
