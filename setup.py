#!/usr/bin/python3
#-*-coding:utf-8-*-
####  THIS TOOL MAKE BY SAIKOT
####  ENJOY MY TOOLS
#### Create Date 5 Sep 2025
#### Win By Arg 3🤟


import os
import time

GREEN = "\033[92m"
RESET = "\033[0m"
os.system("clear")
logo=("""
+-+-+-+-+-+-+-+-+-+-+-+-+
|T|e|r|m|u|x|-|S|e|t|u|p|
+-+-+-+-+-+-+-+-+-+-+-+-+  """)
print(GREEN + """
    ███████╗███████╗████████╗██╗   ██╗██████╗ 
    ██╔════╝██╔════╝╚══██╔══╝██║   ██║██╔══██╗
    ███████╗█████╗     ██║   ██║   ██║██████╔╝
    ╚════██║██╔══╝     ██║   ██║   ██║██╔═══╝ 
    ███████║███████╗   ██║   ╚██████╔╝██║     
    ╚══════╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝     
                                           """)
time.sleep(2)
print(GREEN + "\n[•] Starting Termux Setup...\n" + RESET)
time.sleep(1)

# -------------------------------
# Update & Upgrade
# -------------------------------
print(GREEN + "[•] Updating & Upgrading packages..." + RESET)
os.system("pkg update -y && pkg upgrade -y")
time.sleep(2)

# -------------------------------
# Languages
# -------------------------------
languages = ["python", "git", "php", "perl", "ruby", "clang", "golang", "lua53"]
print(GREEN + f"[•] Installing Languages: {', '.join(languages)}" + RESET)
for pkg in languages:
    os.system(f"pkg install -y {pkg}")
time.sleep(1)

# -------------------------------
# Utilities & Networking
# -------------------------------
utilities = [
    "curl", "wget", "unzip", "zip", "tar", "nano", "vim",
    "figlet", "toilet", "cowsay", "cmatrix", "bash",
    "openssh", "net-tools", "openssl", "nmap", "proot", "mpv",
    "tmux", "screen", "neofetch", "ffmpeg", "bmon"
]
print(GREEN + f"[•] Installing Utilities: {', '.join(utilities)}" + RESET)
for pkg in utilities:
    os.system(f"pkg install -y {pkg}")
time.sleep(1)

# -------------------------------
# Python Libraries
# -------------------------------
python_packages = [
    "requests", "mechanize", "bs4", "Pillow",
    "colorama", "termcolor", "pyfiglet",
    "youtube-dl", "wget", "autopep8", "pylint"
]
print(GREEN + f"[•] Installing Python libraries: {', '.join(python_packages)}" + RESET)
os.system("pip install --upgrade pip")
for pkg in python_packages:
    os.system(f"pip install {pkg}")
time.sleep(1)

# -------------------------------
# Completion
# -------------------------------
print(GREEN + """
    ██████╗  ██████╗ ███╗   ██╗███████╗
    ██╔══██╗██╔═══██╗████╗  ██║██╔════╝
    ██║  ██║██║   ██║██╔██╗ ██║█████╗  
    ██║  ██║██║   ██║██║╚██╗██║██╔══╝  
    ██████╔╝╚██████╔╝██║ ╚████║███████╗
    ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚══════╝  """)
    
print(GREEN + "\n✅ Termux setup completed successfully!" + RESET)
time.sleep(5)
