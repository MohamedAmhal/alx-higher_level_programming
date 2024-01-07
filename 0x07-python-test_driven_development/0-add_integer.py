#!/usr/bin/python3
"""the function add """


def add_integer(a, b=98):
    """Return the integer addition of a and b.

    see tests 

    Raises:
        TypeError: if a or b are not intergers 
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
