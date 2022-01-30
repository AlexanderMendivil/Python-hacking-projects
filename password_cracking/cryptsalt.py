#!/usr/bin/env python3

import crypt
from termcolor import colored

def crackPass(cryptWord):
    salt = cryptWord[0:2]
    dictionary = open("dictonary.txt", "r")

    for word in dictionary.readlines():
        word = word.strip("\n")
        cryptPass = crypt.crypt(word, salt)
        if(cryptWord == cryptPass):
            print(colored(f"[+] Found password: {word}", "green"))
            return
        else:
            print(colored("[-] Password not found.", "red"))
def main():
    
    passFile = open("pass.txt", "r")
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(":")[0]
            cryptWord = line.split(":")[1].strip(" ").strip("\n")
            print(colored(f"[*] Cracking password for user: {user}", "yellow"))
            crackPass(cryptWord)


if __name__ == "__main__":
    main()