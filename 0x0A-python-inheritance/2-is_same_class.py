#!/usr/bin/python3
def is_same_class(obj, a_class):
    """ checks if object is a class

    Args:
        obj: object given
        a_class: class given

    Returns: True or False

    """
    return type(obj) == a_class
