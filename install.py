import os
choice = input('[+] to install press (Y) to uninstall press (N) >> ')
run = os.system
if str(choice) =='Y' or str(choice)=='y':

    run('chmod 777 tor.py')
    run('mkdir /usr/share/onion')
    run('cp tor.py /usr/share/onion/tor.py')

    cmnd=(' #! /bin/sh \n exec python3 /usr/share/onion/tor.py "$@"')
    with open('/usr/bin/onion','w')as file:
        file.write(cmnd)
    run('chmod +x /usr/bin/onion & chmod +x /usr/share/onion/tor.py')
    print('''\n\nWoo-hoo Tor Ip Changer is successfully installed \nfrom now just type \x1b[6;30;42monion\x1b[0m in terminal ''')
if str(choice)=='N' or str(choice)=='n':
    run('rm -r /usr/share/onion ')
    run('rm /usr/bin/onion ')
    print('[!] now Tor Ip changer  has been removed successfully')
