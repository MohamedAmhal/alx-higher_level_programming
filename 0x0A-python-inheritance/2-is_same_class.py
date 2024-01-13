#!/usr/bin/python3
"""
this program is to help you understand
the instance of the object
"""


def is_same_class(obj, a_class):
    """
    Parameters
    ----------
    obj : TYPE
        this obejct is created by the admine
    a_class : TYPE
        is also created by the user

    Returns
    -------
    bool
        True : if the obejt is a instance of the class
        Flase if not.

    """
    if type(obj) == a_class:
        return True
    else:
        return False
