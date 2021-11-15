#!/usr/bin/env/ python3

import socket

def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, port))
        banner = sock.recv(1024)
        return banner
    except:
        return

def main():

    ip = input("[*] Enter target IP: ")
    for port in range(1, 100):
        banner = retBanner(ip, port)
        if banner:
            print(f"[+] {ip} on port: {port}: {banner.strip('\n')}")


if __name__ == "__main__":
    try:
        main()
    except:
        pass