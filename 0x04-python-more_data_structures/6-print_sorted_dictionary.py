#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a_dictionary = dict(a_dictionary)
    a = []
    for i in a_dictionary.keys():
        a.append(i)
    a.sort()
    for i in a:
        print("{}: {}".format(i, a_dictionary[i]))
