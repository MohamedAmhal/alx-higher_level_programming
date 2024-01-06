#!/usr/bin/python3
"""
this is a function class
"""


class Square:
    """
    this is the class square that contient theprivate attribute size
"""

    def __init__(self, __size=0):
        self.__size = __size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise ValueError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        if type(self.__size) != int:
            raise ValueError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
        else:
            return (self.__size) ** 2
