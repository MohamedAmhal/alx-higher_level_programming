#!/usr/bin/python3
def search_replace(my_list, search, replace):
    a = []
    for i in my_list:
        if i == search:
            a.append(replace)
        else:
            a.append(i)

    return a
