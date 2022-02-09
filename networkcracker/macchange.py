#!/usr/bin/env python3

import subprocess
from termcolor import colored

def change_mac_address(inteface, mac):
    subprocess.call(["ifconfig " + inteface + " down"])
    subprocess.call(["ifconfig " + inteface + "hw " + "ether " + mac])
    subprocess.call(["ifconfig " + inteface + " up"])

def main():
    interface = input("[+] Enter to change MAC address: ")
    new_mac_address = input("[*] Enter MAC address to change to: ")
    
    before_change = subprocess.check_output(f"ifconfig {interface}")
    change_mac_address(interface, new_mac_address)
    after_change = subprocess.check_output(f"ifconfig {interface}")

    if before_change == after_change:
        print(colored(f"[-] Failed to change MAC address to: {new_mac_address}", "red"))
    else:
        print(colored(f"[+] MAC address changed to: {new_mac_address} on interface: {interface}","green"))


if __name__ == "__main__":
    main()
        