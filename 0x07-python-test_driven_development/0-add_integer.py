#!/usr/bin/python3
""" Add integer module
"""


def add_integer(a, b=98):
    """ Adds 2 integers

    Args:
        a (int)
        b (int)

    Returns:
        Sum of a and b

    Raises:
        TypeError: a must be integer
        TypeError: b must be integer
    """
    if type(a) not in [int, float] or a is None:
        raise TypeError("a must be integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be integer")

    return int(a) + int(b)
