#!/usr/bin/python

import curses
import os

string = ""

def main(win):
    win.nodelay(True)
    key=""
    win.clear()
    win.addstr("Detected key:")
    while 1:
        try:
           key = win.getkey()
           win.clear()
           win.addstr("Detected key:")
           win.addstr(str(key))
           if key == os.linesep:
              break
           string+=key
        except Exception as e:
           # No input
           pass

curses.wrapper(main)

print(string)
