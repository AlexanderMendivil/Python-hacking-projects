#!/usr/bin/env python3

from ast import Pass
from urllib.request import urlopen
import hashlib
from termcolor import colored

sha1hash = input("[*] Enter sha1 hash value: ")
passlist = str(urlopen("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000.txt").read(), "utf-8")

for password in passlist.split('\n'):
    hashGuess = hashlib.sha1(bytes(password, "utf-8")).hexdigest()
    if(hashGuess == sha1hash):
        print(colored(f"[+] Password is: {str(password)}","green"))
        quit()
    else:
        print(colored(f"[-]Password guess {str(password)} does not match trying next...","red"))

print("Password not in password list.")