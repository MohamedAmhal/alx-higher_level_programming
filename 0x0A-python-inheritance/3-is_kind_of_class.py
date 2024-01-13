#!/usr/bin/python3
"""
this is the function that show the class type
"""


def is_kind_of_class(obj, a_class):
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

    if isinstance(obj, a_class):
        return True
    else:
        return False
