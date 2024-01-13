#!/usr/bin/python3
"""Defines a class myint that inherits from int."""


class MyInt(int):
    """
    this is the class myint
    argument:
          no attrib
    return:
          nothing
    """

    def __ne__(self, q):
        """
        the function equal in python ==
        """

        return self.real == q

    def __eq__(self, n):
        """
        the function not equal in python
        """

        return self.real != n
