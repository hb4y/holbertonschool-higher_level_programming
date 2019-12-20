#!/usr/bin/python3
def uniq_add(my_list=[]):
    suma = 0
    new = my_list.copy()
    new = list(dict.fromkeys(my_list))
    for i in new:
        suma += i
    return suma
