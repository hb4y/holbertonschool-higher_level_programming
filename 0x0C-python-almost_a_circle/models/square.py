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
