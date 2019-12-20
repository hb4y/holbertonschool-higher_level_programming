#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary and len(a_dictionary) > 0:
        for key, val in list(a_dictionary.items()):
            if val == value:
                del a_dictionary[key]
    return a_dictionary
