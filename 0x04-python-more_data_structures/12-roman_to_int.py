#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    sum = 0
    dernierelem = 0
    b = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in roman_string[::-1]:
        v = b[i]
        if v < dernierelem:
            sum = sum - v
        else:
            sum = sum + v
        dernierelem = v
    return sum
