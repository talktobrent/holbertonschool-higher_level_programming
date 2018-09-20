#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    parent = []
    for loop in matrix:
        child = list(map(lambda x: x * x, loop))
        parent.append(child)
    return parent
