#!/usr/bin/env Python3

import socket 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "192.168.56.1"
port = 445

def Scanner(port):
    if sock.connect_ex(( host, port )):
        print(f"Port {port} is closed")
    else:
        print(f"Port {port} is opened")


if __name__ == "__main__":
    try:
        Scanner(port)
    except:
        print("No error handling")

