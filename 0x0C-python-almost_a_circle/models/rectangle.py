#!/usr/bin/python3
"""
Rectangle that inherits from Base
"""


Base = __import__('base').Base

class Rectangle(Base):
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

        def __init__(self, width, height, x=0, y=0, id=None):
            """
            THE CONSTRUCTOR
            """

            self.__width = width
            self.__height = height
            self.__x = x
            self.__y = y
            super().__init__(id)

        @property
        def width(self):
            """
            the width of the rectangle
            """

            return self.__width

        @witdh.setter
        def width(self, value):
            """
            the method setter
            """

            if type(value) != int:
                raise TypeError("width must be an integer")
            elif value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value


        @property
        def height(self):
            """
            the height of the rectange
            """

            return self.__height

        @height.setter
        def height(self, value):
            """
            the method setter
            """

            if type(value) != int:
                raise TypeError("height must be an integer")
            elif value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value

        @property
        def x(self):
            """
            Set/get the x coordinate of the Rectangle.
            """
            return self.__x

        @x.setter
        def x(self, value):
            """
            the method setter of x
            """
            if type(value) != int:
                raise TypeError("x must be an integer")
            elif value < 0:
                raise ValueError("x must be > 0")
            self.__x = value

        @property
        def y(self):
            """
            Set/get the y coordinate of the Rectangle.
            """

            return self.__y

        @y.setter
        def y(self, value):
            """
            the method setter
            """

            if type(value) != int:
                raise TypeError("y must be an integer")
            elif value < 0:
                raise ValueError("y must be > 0")
            self.__y = value

        def area(self):
            """
            this is the instance methode
            that return the area of the 
            rectangle
            """

            return self.__width * self.height

        def display(self):
            """
            this instance methode
            is print the rectangle
            with ####
            the x and y 
            don't handdle!!
            """

            if self.width == 0 or self.height == 0:
                print("")
                return

            [print("") for y in range(self.y)]
            for h in range(self.height):
                [print(" ", end="") for x in range(self.x)]
                [print("#", end="") for w in range(self.width)]
                print("")

        def __str__(self):
            """
            the instance methode str
            """

            str = f"[{Rectangle}] ({id}) {x}/{y} -"
            str += f"{width}/{height}"
            return str

        def update(self, *args, **kwargs):
            """
            that assigns an argument to each attribute:
            1st argument should be the id attribute
            2nd argument should be the width attribute
            3rd argument should be the height attribute
            4th argument should be the x attribute
            5th argument should be the y attribute
            """

            if args and len(args) != 0:
                a = 0
                for i in args:
                    if a == 0:
                        if i is None:
                            self.__init__(self.__width, self.__height, self.__x, self.__y)
                        else:
                            self.__id = i
                    elif a == 1:
                        self.__width = i
                    elif a == 2:
                        self.__height = i
                    elif a == 3:
                        self.__x = i
                    elif a == 4:
                        self.__y = i
                    a += 1

            elif kwargs and len(kwargs) != 0:
                for i, j in kwargs.items():
                    if i == "id":
                        if j is None:
                            self.__init__(self.__width, self.__height, self.__x, self.__y)
                        else:
                            self.__id = j

                    elif i == "width":
                        self.__width = j
                    elif i == "height":
                        self.__height = j
                    elif i == "x":
                        self.__x = j
                    elif i == "y":
                        self.__y = j


        def to_dictionary(self):
            """
            this instance methode print the dictionary
            items : the attributs of the calss
            """

            return {
            "id": self.__id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y
        }
