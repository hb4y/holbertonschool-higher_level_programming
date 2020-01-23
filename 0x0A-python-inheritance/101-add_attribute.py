#!/usr/bin/python3
"""
add attribute if can
"""


def add_attribute(obj, aname, value):
    """if not inmutable set attrib"""
    if isinstance(obj, (bool, int, float, tuple, str, frozenset)):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, aname, value)
