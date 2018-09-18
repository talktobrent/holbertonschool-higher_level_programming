#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for parent in matrix:
        for child in parent:
            print("{:d}".format(child), end="")
            if child in parent[:-1]:
                print(" ", end="")
        print()
