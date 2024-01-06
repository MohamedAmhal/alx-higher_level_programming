#!/usr/bin/python3
"""
this is a function class
"""


class Square:
    """
    this is the class square that contient theprivate attribute size
"""

    def __init__(self, __size=0, __position=(0, 0)):
        self.__size = __size
        self.__position = __position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        a = type(value) != tuple
        b = (value[0] > 0 and value[1] > 0)
        c = (type(value[0]) == int and type(value[1]) == int)
        if a or not (b) or not (c):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        if type(self.__size) != int:
            raise ValueError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
        else:
            return (self.__size) ** 2

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(1, self.__size + 1):
                if self.__position[0] > 0:
                    print(" " * self.__position[0], "#" * self.__size)
                else:
                    print("#" * self.__size)
