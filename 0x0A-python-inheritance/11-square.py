#!/usr/bin/python3
"""
class Square
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        msg = "[Square] " + str(self.__size) + "/" + str(self.__size)
        return msg
