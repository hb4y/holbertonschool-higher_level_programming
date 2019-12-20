#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    d = dict(a_dictionary)
    if key in d.keys():
        del d[key]
    return d
