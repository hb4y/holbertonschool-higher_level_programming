#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    d = dict(a_dictionary.copy())
    for i in d:
        d[i] *= 2
    return d
