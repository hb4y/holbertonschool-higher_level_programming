#!/usr/bin/python3
class Square:
    """Square class"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.position = position

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not (isinstance(value, int)):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if self.__size == 0:
            print("")
            return
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        largo = len(value) != 2
        not_tuple = not (isinstance(value, tuple))
        not_num = any(not isinstance(n, int) for n in value)
        less = any(n < 0 for n in value)

        if largo or not_tuple or not_num or less:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
