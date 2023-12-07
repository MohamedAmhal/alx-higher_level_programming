#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a = dict({})
    for i in a_dictionary.keys():
        a[i] = a_dictionary[i] * 2
    return a
