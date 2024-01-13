#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""


BaseGeometry = __import__('9-base_geometry').BaseGeometry


class Square(Rectangle):
    """
    this is the documentation of this class
    arguments:
        size : size of the rectangle
        return:
            nothing
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        the method area
        """
        return self.__size ** 2