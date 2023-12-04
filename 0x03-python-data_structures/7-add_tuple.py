#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 2 and len(tuple_b) >= 2:
        a = tuple_a[0] + tuple_b[0]
        b = tuple_a[1] + tuple_b[1]
        return (a, b)
    elif len(tuple_a) >= 2 and len(tuple_b) == 1:
        a = tuple_a[0] + tuple_b[0]
        b = tuple_a[1] + 0
        return (a, b)
    elif len(tuple_a) == 1 and len(tuple_b) >= 2:
         a = tuple_a[0] + tuple_b[0]
         b = tuple_b[1] + 0
         return (a, b)
    elif (len(tuple_a) == 0 and len(tuple_b) >= 2) or (len(tuple_b) == 0 and len(tuple_a) >= 2):
         if len(tuple_a) >= 2:
            return (tuple_a[0], tuple_a[1])
        elif len(tuple_b) >= 2:
            return (tuple_b[0],tuple_b[1])
