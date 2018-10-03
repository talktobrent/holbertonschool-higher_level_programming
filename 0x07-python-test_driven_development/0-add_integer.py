#!/usr/bin/python3
def add_integer(a, b=98):
    """ Adds 2 integers

    Args:
        a (int)
        b (int)

    Returns:
        Sum of integer on success
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be integer")
    return int(a) + int(b)
