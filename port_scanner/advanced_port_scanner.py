#!/usr/bin/env python3

from socket import *
import optparse
from threading import *

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
        portScan(tgtHost, tgtPorts)

def portScan(host, port):
    print(1)

if __name__ == "__main__":
    try:
        main()
    except:
        print("No error handling")
