# -*- coding: utf-8 -*-

import time
import os
import subprocess


try:
    check_pip3 = subprocess.check_output('dpkg -s python3-pip', shell=True)
    if str('install ok installed') in str(check_pip3):
        pass
except subprocess.CalledProcessError:
    print('[+] pip3 not installed')
    subprocess.check_output('sudo apt update',shell=True)
    subprocess.check_output('sudo apt install python3-pip -y', shell=True)
    print('[!] pip3 installed succesfully')


try:

    import requests
except Exception:
    print('[+] python3 requests is not installed')
    os.system('pip3 install requests')
    os.system('pip3 install requests[socks]')
    print('[!] python3 requests is installed ')
try:

    check_tor = subprocess.check_output('which tor', shell=True)
except subprocess.CalledProcessError:

    print('[+] tor is not installed !')
    subprocess.check_output('sudo apt update',shell=True)
    subprocess.check_output('sudo apt install tor -y',shell=True)
    print('[!] tor is installed succesfully ')

os.system("clear")
def ma_ip():
    url='https://www.myexternalip.com/raw'
    get_ip= requests.get(url,proxies=dict(http='socks5://127.0.0.1:9001',https='socks5://127.0.0.1:9001'))
    return get_ip.text

def change():
    os.system("service tor reload")
    print ('[+] IP has been Changed to : '+str(ma_ip()))

print('''\033[1;32;40m \n

|''||''|                 '|.   '|'           .                               '||      
   ||      ...   ... ..   |'|   |    ....  .||.  ... ... ...   ...   ... ..   ||  ..  
   ||    .|  '|.  ||' ''  | '|. |  .|...||  ||    ||  ||  |  .|  '|.  ||' ''  || .'   
   ||    ||   ||  ||      |   |||  ||       ||     ||| |||   ||   ||  ||      ||'|.   
  .||.    '|..|' .||.    .|.   '|   '|...'  '|.'    |   |     '|..|' .||.    .||. ||.
                
 V 2.1    
from MadMaxxx
''')
print("\033[1;40;31m I believe there is another world waiting for us. A better world. And I'll be waiting for you there/\n")

os.system("service tor start")



time.sleep(3)
print("\033[1;32;40m change your  SOCKES to 127.0.0.1:9001 \n")
os.system("service tor start")
x = input("[+] Time to change Ip in Sec [type=60] >> ")
lin = input("[+] How many time do you wish to change your ip [type=1000]for infinte ip change type [0] >>")
if int(lin) ==int(0):

	while True:
		try:
			time.sleep(int(x))
			change()
		except KeyboardInterrupt:

		 	print('\n tor is closed ')
		 	quit()

else:
	for i in range(int(lin)):
		    time.sleep(int(x))
		    change()
