#!/usr/bin/python3
"""
this is the documantation
of this function
"""


class BaseGeometry:
    """
    this is an empty class
    """

    def area(self):
        """
        Raises
        ------
        Exception
            DESCRIPTION.

        Returns
        -------
        None.

        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Parameters
        ----------
        name : TYPE
            DESCRIPTION.
        value : TYPE
            DESCRIPTION.

        Returns
        -------
        None.
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    this is the fils of the class
    basegeometry
    """

    def __init__(self, width, height):
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
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
