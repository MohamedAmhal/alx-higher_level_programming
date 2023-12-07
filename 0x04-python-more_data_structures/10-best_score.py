#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    a = []
    for i in a_dictionary.values():
        a.append(i)

    maxi = max(a)
    for i in a_dictionary.keys():
        if a_dictionary[i] == maxi:
            return i

    return None
