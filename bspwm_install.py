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
bspwm_install = "sudo apt-get install bspwm sxhkd build-essential git vim libxcb-util0-dev libxcb-ewmh-dev libxcb-randr0-dev libxcb-icccm4-dev libxcb-keysyms1-dev libxcb-xinerama0-dev libasound2-dev libxcb-xtest0-dev libxcb-shape0-dev thunar cmake cmake-data pkg-config python3-sphinx libcairo2-dev libxcb1-dev libxcb-util0-dev libxcb-randr0-dev libxcb-composite0-dev python3-xcbgen xcb-proto libxcb-image0-dev libxcb-ewmh-dev libxcb-icccm4-dev libxcb-xkb-dev libxcb-xrm-dev libxcb-cursor-dev libasound2-dev libpulse-dev libjsoncpp-dev libmpdclient-dev libcurl4-openssl-dev libnl-genl-3-dev polybar rofi calc network-manager picom kali-screensaver hollywood-activate xss-lock meson libxext-dev libxcb1-dev libxcb-damage0-dev libxcb-xfixes0-dev libxcb-shape0-dev libxcb-render-util0-dev libxcb-render0-dev libxcb-randr0-dev libxcb-composite0-dev libxcb-image0-dev libxcb-present-dev libxcb-xinerama0-dev libpixman-1-dev libdbus-1-dev libconfig-dev libgl1-mesa-dev libpcre2-dev libevdev-dev uthash-dev libev-dev libx11-xcb-dev libxcb-glx0-dev feh wget pulseaudio pulseaudio alsa-utils pamixer brightnessctl i3lock-color"

print(Fore.BLUE + " - Instalando paquetes necesarios!")
try:
    bspwm = subprocess.run(bspwm_install, shell=True, text=True, capture_output=True)
    print(Fore.BLUE + " - Paquetes necesarios instalados Correctamente!")
except subprocess.CalledProcessError as e:
    print(Fore.RED + " - Error al instalar los paquetes que se requieren!")
    print(e.stdout)
    print(e.stderr)

#------------------------------------------------------------
# Creando Carpetas Bspwm y Sxhkd 
# ----------------------------------------------------------
print(Fore.BLUE + " - Creando carpetas necesarias")

try:
    subprocess.run("mkdir -p ~/.config/bspwm/ && mkdir -p ~/.config/sxhkd/", shell=True, text=True, capture_output=True)
    subprocess.run("cp -r ./bspwm/bspwmrc ~/.config/bspwm && cp -r ./sxhkd/sxhkdrc ~/.config/sxhkd", shell=True, text=True, capture_output=True)
    subprocess.run("chmod +x ~/.config/bspwm/bspwmrc", shell=True, text=True, capture_output=True)
    print(Fore.BLUE + " - Carpetas bspwm y sxhkd creadas correctamente!")
except subprocess.CalledProcessError as e:
    print(Fore.RED + " - Error al crear las carpetas para configuracion bspwm y sxhkd")
    print(e.stdout)
    print(e.stderr)

#---------------------------------------------------------
# Creando Carpetas para Polybar
# --------------------------------------------------------

print(Fore.BLUE + " - Creando carpetas y configuracion para Polybar")
try:
    subprocess.run("mkdir -p ~/.config/polybar", shell=True, text=True, capture_output=True)
    subprocess.run("mkdir -p ~/.local/share/fonts", shell=True, text=True, capture_output=True)
    subprocess.run("cp -r ./polybar/* ~/.config/polybar", shell=True, text=True, capture_output=True)
    subprocess.run("cp -r ./fonts/* ~/.local/share/fonts", shell=True, text=True, capture_output=True)
    print(Fore.BLUE + " - Polybar configurada correctamente!")
except subprocess.CalledProcessError as e:
    print(Fore.RED + " - Error al configurar polybar!")
    print(e.stdout)
    print(e.stderr)


#----------------------------------------------------------
# ROFI ---------------------------------------------------
# --------------------------.------------------------------

print(Fore.BLUE + " - Clonando repositorio rofi")
try:
    subprocess.run("git clone --depth=1 https://github.com/adi1090x/rofi.git && cd rofi", shell=True, text=True, capture_output=True)
    subprocess.run("chmod +x setup.sh", shell=True, text=True, capture_output=True)
    subprocess.run("bash setup.sh", shell=True, text=True, capture_output=True)
    print(Fore.BLUE + " - Rofi clonado correctamente!")
    print(Fore.BLUE + " - Creando carpetas para rofi")
    subprocess.run("rm -rf ~/.config/rofi/*", shell=True, text=True, capture_output=True)
    subprocess.run("cp -r ./rofi/* ~/.config/rofi", shell=True, text=True, capture_output=True)
    print(Fore.BLUE + " - Carpetas rofi configuradas correctamente!")
except subprocess.CalledProcessError as e:
    print(Fore.RED + " - Error al configurar el rofi!")
    print(e.stdout)
    print(e.stderr)

#----------------------------------------------------------
# Kitty ---------------------------------------------------
# --------------------------.------------------------------

print(Fore.BLUE + " - Configurando Kitty como Terminal")
try:
    subprocess.run("mkdir -p ~/.config/kitty", shell=True, text=True, capture_output=True)
    subprocess.run("cp -r ./kitty/* ~/.config/kitty", shell=True, text=True, capture_output=True)
    print(Fore.BLUE + " - Configuracion creada correctamete para Kitty!")
except subprocess.CalledProcessError as e:
    print(Fore.RED + " - Error al configurar la kitty")
    print(e.stdout)
    print(e.stderr)

#----------------------------------------------------------
# Picom ---------------------------------------------------
# --------------------------.------------------------------

print(Fore.BLUE + " - Configurando picom")
try:
    subprocess.run("mkdir -p ~/.config/picom", shell=True, text=True, capture_output=True)
    subprocess.run("cp -r ./picom/* ~/.config/picom", shell=True, text=True, capture_output=True)
    print(Fore.BLUE + " - Configuracion creada correctamete para la Picom!")
except subprocess.CalledProcessError as e:
    print(Fore.RED + " - Error al configurar la Picom")
    print(e.stdout)
    print(e.stderr)



# I3lock  ---------------------------------------------------
# --------------------------.------------------------------

print(Fore.BLUE + " - Configurando I3lock")
try:
    subprocess.run("mkdir -p ~/.config/i3lock", shell=True, text=True, capture_output=True)
    subprocess.run("cp -r ./i3lock/* ~/.config/i3lock", shell=True, text=True, capture_output=True)
    print(Fore.BLUE + " - Configuracion creada correctamete I3lock!")
except subprocess.CalledProcessError as e:
    print(Fore.RED + " - Error al configurar I3lock")
    print(e.stdout)
    print(e.stderr)


# Nvchad  ---------------------------------------------------
# --------------------------.------------------------------


print(Fore.BLUE + " - Configurando Nvhad")
try:
    subprocess.run("git clone https://github.com/NvChad/starter ~/.config/nvim && nvim", shell=True, text=True, capture_output=True)
    subprocess.run("rm -rf ~/.config/nvim/*", shell=True, text=True, capture_output=True)
    subprocess.run("cp -r ./nvim/* ~/.config/nvim", shell=True, text=True, capture_output=True)
    print(Fore.BLUE + " - Nvchad esta configurado!")
except subprocess.CalledProcessError as e:
    print(Fore.RED + " - Error al configurar Nvchad")
    print(e.stdout)
    print(e.stderr)

#------------------------------------------------------------
# Configurando capeta Pictures------------------------------

print(Fore.BLUE + " - Configurando carpeta Pictures")
try:
    subprocess.run("cp -r ./Pictures/* $HOME/Pictures", shell=True, text=True, capture_output=True)
    print(Fore.BLUE + " - Imagenes instaladas correctamente!")
except subprocess.CalledProcessError as e:
    print(Fore.RED + " - Error al configurar Pictures")
    print(e.stdout)
    print(e.stderr)

reboot = input(Fore.GREEN + " - Se ha configurado Correctamente el Entorno ¿Desea reiniciar?")
if reboot == "yes" or reboot == "y":
    print(Fore.BLUE + " - Gracias por instalar mi entorno!")
    subprocess.run("reboot", shell=True, text=True, capture_output=True)

else: 
    print(Fore.BLUE + " - Gracias por instalar mi entorno")
    sys.exit()
