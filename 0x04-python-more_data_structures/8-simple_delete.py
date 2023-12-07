#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    u = 0
    for i in a_dictionary.keys():
        if i == key:
            u = 1
    if u == 1:
        del a_dictionary[key]
    return a_dictionary
