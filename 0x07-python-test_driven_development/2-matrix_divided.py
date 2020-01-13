#!/usr/bin/python3
"""
matrix_divided - divide a matrix for a number
matrix: matrix to divide
div: integer to divide the matrix
"""
def matrix_divided(matrix, div):
    """
    Divide matrix method
    """
    error_list = "matrix must be a matrix (list of lists) of integers/floats"
    error_size = "Each row of the matrix must have the same size"
    if not (isinstance(matrix, list)):
        raise TypeError(error_list)
    list_len = len(matrix[0])
    for inner_list in matrix:
        if len(inner_list) != list_len:
            raise TypeError(error_size)
        for number in inner_list:
            if not (isinstance(number, int) or isinstance(number, float)):
                raise TypeError(error_list)
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    new_list = []
    for inner_list in matrix:
        for number in inner_list:
            res = number / div
            new_list.append(round(res, 2))
        new_matrix.append(new_list)
        new_list = []
    return new_matrix
