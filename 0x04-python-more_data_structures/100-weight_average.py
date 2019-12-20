#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list) != 0:
        mul = 1
        suma = 0
        dividendo = 0
        for i in my_list:
            for j in i:
                mul *= j
            dividendo += i[1]
            suma += mul
            mul = 1
        return suma / dividendo
    return 0
