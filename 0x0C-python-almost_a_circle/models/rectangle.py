#!/usr/bin/python3
"""
rectangle class
inherits from Base
"""


from models.base import Base


class Rectangle(Base):
    """rectagle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init for rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """width setter"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, height):
        """height setter"""
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter"""
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter"""
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """return area"""
        return self.height * self.width

    def display(self):
        """display rectangle"""
        for j in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """custom __str__"""
        aux1 = "[Rectangle] (" + str(self.id) + ")"
        aux2 = " " + str(self.__x) + "/" + str(self.__y) + " -"
        aux3 = " " + str(self.__width) + "/" + str(self.__height)
        return aux1 + aux2 + aux3

    def update(self, *args):
        """update attrib"""
        if len(args):
            attrib = ["id", "width", "height", "x", "y"]
            for index, value in enumerate(args):
                setattr(self, attrib[index], value)
