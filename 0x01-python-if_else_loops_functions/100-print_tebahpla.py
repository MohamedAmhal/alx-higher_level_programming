#!/usr/bin/python3
for i in range(0,26):
    print("{}".format(chr(122 - (i % 2) * 32 - i)), end="")
