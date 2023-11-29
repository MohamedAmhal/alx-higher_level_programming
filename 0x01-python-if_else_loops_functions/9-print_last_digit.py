#!/usr/bin/python3
def print_last_digit(number):
    a = number
    if a < 0:
        a = -1 * a
    a = a % 10
    print("{}".format(a), end="")
    return a
