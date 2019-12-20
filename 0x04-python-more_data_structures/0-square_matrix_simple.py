#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = [i[:] for i in matrix]
    for i in new:

        for j in range(len(i)):
            i[j] = i[j] * i[j]
    return new
