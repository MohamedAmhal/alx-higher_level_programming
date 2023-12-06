#!/usr/bin/python3
def number_keys(a_dictionary):
    a_dictionary = dict(a_dictionary)
    sum = 0
    for i in a_dictionary.keys():
            sum = sum + 1
    return sum
