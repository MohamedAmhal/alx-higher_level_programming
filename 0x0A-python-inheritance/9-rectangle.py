!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


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

        def area(self):
            """
            the function area
            """

            return self.__width * self.__height

        def __str__(self):
            return f"[Rectangle] {self.__width}/{self.__height}"
