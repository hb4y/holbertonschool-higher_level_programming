#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not (len(matrix) == 1 and len(matrix[0]) == 0):
        for i in matrix:
            for index, elem in enumerate(i):
                if (index + 1) != len(i):
                    print("{:d} ".format(elem), end='')
                else:
                    print("{:d}".format(elem))
    else:
        print("")
