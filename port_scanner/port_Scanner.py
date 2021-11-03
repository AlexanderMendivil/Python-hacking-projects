#!/usr/bin/env Python3

import socket 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(1)
# 192.168.56.1
host = input("[*] Enter the host to scan: ")
# port = int(input("[*] Enter de port to scan: "))

def Scanner(port):
    if sock.connect_ex(( host, port )):
        print(f"Port {port} is closed")
    else:
        print(f"Port {port} is open")


if __name__ == "__main__":
    try:
        for port in range(1,200):
            Scanner(port)
    except:
        print("No error handling")

