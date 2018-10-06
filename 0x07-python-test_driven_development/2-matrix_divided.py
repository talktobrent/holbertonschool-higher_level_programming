#!/usr/bin/python3
""" Matrix divided module
"""


def matrix_divided(matrix, div):
    """ Divides all elements of a matrix

    Inserts result of division on each element (rounded to two decimal places),
    into a new matrix

    Args:
        matrix []: matrix given
        div: number to divide by

    Returns:
        A new matrix with results of division

    Raises:
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: div must be a number
        TypeError: Each row of the matrix must have the same size
        ZeroDivisionError: division by zero

    """
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    for index, x in enumerate(matrix):
        if type(x) is not list or len(x) == 0:
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")
        if index > 0:
            newlen = len(x)
            if newlen != lastlen:
                raise TypeError("Each row of the matrix must have the same "
                                "size")
        lastlen = len(x)
        for y in x:
            if type(y) not in (float, int):
                raise TypeError("matrix must be a matrix (list of lists) of "
                                "integers/floats")

    if type(div) not in (float, int):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round((y / div), 2) for y in x] for x in matrix]
