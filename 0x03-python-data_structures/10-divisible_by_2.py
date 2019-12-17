#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    aux = []
    for i in my_list:
        if i % 2 == 0:
            aux.append(True)
        else:
            aux.append(False)
    return aux
