#!/usr/bin/env python3

import crypt


def main():
    
    passFile = open("pass.txt", "r")
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(":")[0]
            cryptWord = line.split(":")[1].strip("\n")
            print(cryptWord)


if __name__ == "__main__":
    main()