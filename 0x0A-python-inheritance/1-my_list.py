#!/usr/bin/python3
"""
prints the list, but sorted
"""


class MyList(list):
    """inherits from list"""
    def print_sorted(self):
        """print int sorted list"""
        print(sorted(self))
