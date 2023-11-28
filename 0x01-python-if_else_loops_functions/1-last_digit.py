#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
a = number
if a < 0:
    a = -1 * a
    a = a % 10
    if a > 5:
        print(f"Last digit of {number} is {-1 *a} and is greater than 5")
    elif a == 0:
        print(f"Last digit of {number} is {a} and is 0")
    elif a < 6 and a != 0:
        print(f"Last digit of {number} is {-1 *a} and is less than 6 and not 0")
else:
    a = a % 10
    if a > 5:
        print(f"Last digit of {number} is {a} and is greater than 5")
    elif a == 0:
        print(f"Last digit of {number} is {a} and is 0")
    elif a < 6 and a != 0:
        print(f"Last digit of {number} is {a} and is less than 6 and not 0")
