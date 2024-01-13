#!/usr/bin/python3
"""
this is the documantation
of this function
"""


def inherits_from(obj, a_class):
    """
    Parameters
    ----------
    obj : TYPE
        DESCRIPTION.
    a_class : TYPE
        DESCRIPTION.

    Returns
    -------
    None.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
