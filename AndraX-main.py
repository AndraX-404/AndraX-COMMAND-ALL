import os
os.system("pip uninstall requests -y")
os.system("pip install requests")
from os import system as clr
import random
import string 
from concurrent.futures import ThreadPoolExecutor as tred
import requests
from bs4 import BeautifulSoup as bxx
import re
import sys
import uuid
import json
import platform,math,smtplib
import platform
import smtplib
import math
import httpx
import os,base64,zlib,pip,urllib
from os import path
import requests,random,uuid,string,hashlib,json
from os import path
from urllib.request import urlopen
import os,base64,zlib,pip,urllib,urllib3

print('\n\033[1;37m install modules...')

try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        print('\n Installing missing modules ...')
        os.system('pip install requests futures==2 > /dev/null')
        os.system('python DX.py')
#-------------color----------------#
bblack="\033[1;30m"         # Black
M="\033[1;31m"            # Red
H="\033[1;32m"         # Green
byellow="\033[1;33m"        # Yellow
bblue="\033[1;34m"          # Blue
P="\033[1;35m"        # Purple
C="\033[1;36m"          # Cyan
B="\033[1;37m"         # White
my_color = [B,H]
warna = random.choice(my_color)

logo=(f'''
\033[38;5;46m      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢤⡖⠋⠀⣀⠠⢤⣤⡤⠄⠀⠀⠀⠀⠀⠀⠀⠀
\033[38;5;46m      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡟⡏⢀⣠⡾⠋⣕⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀
\033[38;5;46m      ⠀⠀⠀⠀⠀⠀⠀⠀⢠⣻⣙⠧⠛⠒⠛⠃⠍⡙⢍⠫⡙⡙⡒⠞⡫⠤⠲⠒⡨⠃
\033[38;5;46m      ⠀⠀⠀⠀⠀⠀⠀⠀⡧⠋⢀⢮⡭⠐⠀⠀⠀⠈⢀⣀⣃⣃⣀⣠⢡⡴⠒⠉⠀⠀
\033[38;5;46m      ⠀⠀⠀⢀⢺⣴⡤⢼⡡⠔⠡⢕⠁⠀⡠⠒⡀⠦⠉⠰⢮⢦⡀⠈⡒⣼⣲⣄⠀⠀
\033[38;5;46m       ⠀⠀⡾⡟⠉⠂⠁⢀⣤⣀⣠⢒⠔⠀⡔⠱⢦⠀⡢⠱⡚⠛⢦⡙⡄⠀⠈⠃⠀
\033[38;5;46m      ⠀⠀⠘⢄⣀⣄⣠⣴⣿⣿⣿⠞⠁⠀⢰⣡⣀⠐⠽⣧⠄⠘⡄⠀⠘⢿⢦⡄⠀⠀
\033[38;5;46m      ⠀⠀⢀⣀⣙⢿⡿⢿⣽⡟⠁⠀⢀⠠⠛⠫⡛⡤⠎⣥⡗⠀⠘⡄⠈⠆⢫⡝⠄⠀
\033[38;5;46m      ⠀⢔⠕⠉⠙⠵⢽⡿⠋⠀⣀⡤⠅⠒⢶⣢⠝⡀⠈⢺⠇⠀⠀⠰⠀⠀⠈⡇⠀⠀
\033[38;5;46m      ⡌⣯⣀⠀⠀⠀⠈⠢⠼⠮⠛⠀⠀⠀⠈⠋⠣⡈⠱⠘⢸⠀⠀⠀⠇⠀⠀⢹⠀⠀
\033[38;5;46m      ⠇⣢⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣗⡄⠀⢀⠀⢺⠀⢸⠀⠀⠘⠀⠀
\033[38;5;46m      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠉⠻⣻⠈⢂⠀⠆⠀⢺⠇ ⢺⠇⠀⠀⠀⠀⠀⠀⠀
\033[38;5;46m _____  _   _  ___    ___    _____  _    _ 
\033[38;5;46m(  _  )( ) ( )(  _`\ |  _`\ (  _  )( )  ( )
\x1b[38;5;47m| (_) || `\| || | ) || (_) )| (_) |`\`\/'/'
\x1b[38;5;47m|  _  || , ` || | | )| ,  / |  _  |  >  <  
\x1b[38;5;48m| | | || |`\ || |_) || |\ \ | | | | /'/\`\ 
\x1b[38;5;49m(_) (_)(_) (_)(____/'(_) (_)(_) (_)(_)  (_)

\033[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[1;97m[\x1b[38;5;196m•\033[1;97m]\x1b[38;5;123m OWNER      \033[38;5;46m ➢     \x1b[38;5;123m ABDULLAH AL MAMUN
\033[1;97m[\x1b[38;5;196m•\033[1;97m]\x1b[38;5;123m GITHUB     \033[38;5;46m ➢     \x1b[38;5;123m AndraX-404
\033[1;97m[\x1b[38;5;196m•\033[1;97m]\x1b[38;5;123m TYPE       \033[38;5;46m ➢     \x1b[38;5;123m RANDOM + FILE CLONE
\033[1;97m[\x1b[38;5;196m•\033[1;97m]\x1b[38;5;123m VERSION    \033[38;5;46m ➢      \033[1;91m\033[1;41m\033[1;97m 0.1 \033[;0m\033[1;91m\033[1;92m
\033[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━''')
def linex():
    print(f'{warna}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{H}')
def clear():
    clr('clear')
    print(logo)
def TARA_LOVE():
    clear()
    print(f'{B}[\x1b[38;5;196m01{B}] \x1b[38;5;47mRANDOM-CLONING\033[0;92m ')
    print(f'{B}[\x1b[38;5;196m02{B}] \x1b[38;5;47mFILE-CLONE\033[0;92m ')
    print(f'{B}[\x1b[38;5;196m03{B}] \x1b[38;5;47mMARDIS DEC\033[0;92m ')
    print(f'{B}[\x1b[38;5;196m04{B}] \x1b[38;5;47mCONTACT WHATSAPP')
    print(f'{B}[\x1b[38;5;196m00{B}] \x1b[38;5;196mEXIT PROGRAMING')
    linex()
    option=input(f'{B}[\x1b[38;5;196m??{B}] CHOOSE OPTION>> ')
    if option in ['01','1']:
        BD_CLONING()
    if option in ['02','2']:
    	os.system('W8 FOR COMING SOON');time.sleep(1)
    if option in ['03','3']:
    	os.system('apt install python2 git\ngit clone\nhttps://github.com/AndraX-404/andrax\ncd andrax\npython2 -m pip install xdis==5.0.11\npython2 -m pip install uncompyle6==3.7.4\npython2 setup.py install');time.sleep(1)
    if option in ['04','4']:
    	os.system('xdg-open https://wa.me/+8801725308028');time.sleep(1)
    else:
        exit(' Thanks for using dear :)')
TARA_LOVE()
