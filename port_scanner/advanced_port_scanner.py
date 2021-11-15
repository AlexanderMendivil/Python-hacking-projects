#!/usr/bin/env python3

from socket import *
import optparse
from threading import *

def connection_scan(tgtHost, tgtPort):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((tgtHost, tgtPort))
        print(f"[+] tcp open: {tgtPort}")
    except:
        print(f"[-] tcp closed: {tgtPort}")
    finally:
        sock.close()

def port_scan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print(f"Unknow host: {tgtHost}")
    
    try:
        tgtName = gethostbyaddr(tgtIP)
        print(f"[+] Scan results for: {tgtName[0]}")
    except:
        print(f"[+] Scan results for: {tgtIP}")
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        t = Thread(target=connection_scan, args=(tgtHost, int(tgtPort)))
        t.start()


def main():
    parser = optparse.OptionParser('Usage of program: '+ '-H <target host> -p <target ports>')
    parser.add_option('-H', dest= 'tgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest= 'tgtPorts', type='string', help='specify target ports separated by comma')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPorts).split(',')

    if tgtHost == None or tgtPorts[0] == None:
        print(parser.usage)
        exit(0)
    else:
        port_scan(tgtHost, tgtPorts)

if __name__ == "__main__":
    try:
        main()
    except:
        print("No error handling")
