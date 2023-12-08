#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0
    a = 0
    b = 0
    for i in my_list:
        a = a + i[0] * i[1]
        b = b + i[1]

    return a/b
