#!/usr/bin/python3
"""
square class
inherits from rectangle
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Square __init__"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str overloading"""
        aux1 = "[Square] (" + str(self.id)
        aux2 = ") " + str(self.x) + "/" + str(self.y)
        aux3 = " - " + str(self.width)
        return aux1 + aux2 + aux3

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """update attrib"""
        attrib = ["id", "size", "x", "y"]
        if args and len(args):
            for index, value in enumerate(args):
                setattr(self, attrib[index], value)
        else:
            for key, value in kwargs.items():
                if key in attrib:
                    setattr(self, key, value)

    def to_dictionary(self):
        """to dic"""
        aux = {}
        aux["id"] = self.id
        aux["size"] = self.width
        aux["x"] = self.x
        aux["y"] = self.y
        return aux
