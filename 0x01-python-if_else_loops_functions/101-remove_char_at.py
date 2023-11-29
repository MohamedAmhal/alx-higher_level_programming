#!/usr/bin/python3
def remove_char_at(str, n):
    a = list(str)
    if n <= len(a) and n > -len(a):
     a.remove(a[n])
     return "".join(a)
    else:
        return str
