#!/usr/bin/python3
"""
say_my_name - prints a hello message
first_name: string
last_name: string
"""
def say_my_name(first_name, last_name=""):
    """
    Method to say hello
    """
    if not (isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    if not (isinstance(last_name, str)):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
