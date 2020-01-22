#!/usr/bin/python3
"""
the object is an instance of a class that inherited
(directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """return True or False"""
    return issubclass(type(obj), a_class) and (not type(obj) is a_class)
