#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    u = 0
    for i in a_dictionary.keys():
        if i == key:
            a_dictionary[key] = value
            u = 1
    if u == 0:
        a_dictionary[key] = value
    return a_dictionary
