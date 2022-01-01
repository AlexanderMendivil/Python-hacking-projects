#!/usr/bin/env python3

import pexpect

PROMPT = ["#", ">>>", ">", "\$"]

def send_command(child, command):
    child.sendLine(command)
    child.expect(PROMPT)
    print(child.before)

def connect(user, host, password):
    ssh_newKey = "Are you sure you want to continue connecting?"
    connStr = f"ssh {user}@{host}"
    child = pexpect.spawn(connStr)
    ret = child.expect([pexpect.TIMEOUT, ssh_newKey, "[P|p]assword: "])
    if ret == 0:
        print("[-] Error connnecting")
    else:
        child.sendline("yes")
        ret = child.expect([pexpect.TIMEOUT,"[P|p]assword: "])
        if ret == 0:
            print("[-] Error connnecting")
            return

    child.sendline(password)
    child.expect(PROMPT)
    return child

def main():
    host = input("Enter the host target: ")
    user = input("Enter SSH username: ")
    password = input("Enter SSH password: ")
    child = connect(user, host, password)
    send_command(child, "cat /etc/shadow | grep root;ps")



if __name__ == "__main__":
    main()