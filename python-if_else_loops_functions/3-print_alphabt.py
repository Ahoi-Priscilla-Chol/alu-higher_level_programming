#!/usr/bin/python3
for i in range(26):
    if chr(ord('a') + i) not in ('q', 'e'):
        print("{}".format(chr(ord('a') + i)), end="")
