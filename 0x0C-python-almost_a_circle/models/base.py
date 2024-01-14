#!/usr/bin/python3
"""
this module is created to 
start the class base
"""


class Base:
    """
        Parameters
        ----------
        width : TYPE
            DESCRIPTION.
        height : TYPE
            DESCRIPTION.

        Returns
        -------
        None.
        """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        THE CONSTRUCTOR
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
