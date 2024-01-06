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
        if type(self.__size) != int:
            raise ValueError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return (self.__size) ** 2
