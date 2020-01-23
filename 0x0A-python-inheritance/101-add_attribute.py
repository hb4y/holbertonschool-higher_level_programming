#!/usr/bin/python3
"""
add attribute if can
"""


def add_attribute(obj, aname, value):
    """set attrib"""
    if obj.__class__.__module__ == 'builtins':
        raise TypeError("can't add new attribute")
    setattr(obj, aname, value)
