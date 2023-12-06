#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    a = []
    for i in my_list:
        if i not in a:
            sum = sum + i
            a.append(i)

    return sum
