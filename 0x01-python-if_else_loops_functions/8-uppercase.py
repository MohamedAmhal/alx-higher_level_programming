#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            a = chr(ord(i) - 32)
        else:
            a = i
        print("{}".format(a), end="")
    print("")
