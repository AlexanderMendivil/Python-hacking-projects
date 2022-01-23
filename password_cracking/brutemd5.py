#!/usr/bin/env python3

from urllib.request import urlopen
import hashlib
from termcolor import colored

def tryOpen(wordlist):
    global pass_file
    try:
        pass_file = open(wordlist, "r")
    except:
        print("[-] There is no file in that path.")
        quit()

def main():
    pass_hash = input("[*] Enter md5 hash value: ")
    wordlist = input("[*] Enter path to password list: ")
    tryOpen(wordlist)
    
    for word in pass_file:
        print(colored("[-] Trying "+word.strip("\n"), "red"))
        encode_word = word.encode("utf-8")
        md5Digest = hashlib.md5(encode_word.strip()).hexdigest()
    
        if(md5Digest == pass_hash):
            print(colored("[+] Password found "+word,"green"))
            exit(0)
    
    print(colored("[+] Password not in the list","red"))

if __name__ == "__main__":
    main()