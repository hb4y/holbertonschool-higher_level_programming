#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        for i in matrix:
            for index, elem in enumerate(i):
                if (index + 1) != len(i):
                    print("{:d} ".format(elem), end='')
                else:
                    print("{:d}".format(elem))
