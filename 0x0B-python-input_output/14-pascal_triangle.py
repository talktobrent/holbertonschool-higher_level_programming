#!/usr/bin/python3
def pascal_triangle(n):
    """ creates pascal triangle

    Args:
        n (int): size of triangle

    Returns:
        matrix of pascal triangle
    """
    if type(n) is not int or n <= 0:
        return None

    last = []
    new = []
    matrix = []
    for x in range(1, n + 1):
        for y in range(x):
            if 0 < y < x - 1:
                new.append(last[y] + last[y - 1])
            else:
                new.append(1)
        matrix.append(new)
        last = new
        new = []
    return matrix
