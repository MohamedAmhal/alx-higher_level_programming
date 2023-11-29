#!/usr/bin/python3
def remove_char_at(str, n):
    a = list(str)
    if n <= len(a) and n >= 0:
     a.remove(a[n])
     return "".join(a)
    else:
        return str
