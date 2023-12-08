#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    a = []
    for i in a_dictionary.keys():
        if a_dictionary[i] == value:
            a.append(i)

    for i in a:
        del a_dictionary[i]
    return a_dictionary
