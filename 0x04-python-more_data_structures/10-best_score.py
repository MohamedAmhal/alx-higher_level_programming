#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    a = []
    for i in a_dictionary.values():
        a.append(i)
    maxi = max(a)
    for j in a_dictionary.keys():
        if a_dictionary[j] == maxi:
            return j
