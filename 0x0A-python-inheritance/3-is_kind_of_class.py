#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """ test if class or subclass

    Args:
        obj: object given
        a_class: class given

    Returns:
        True or False
    """

    return isinstance(obj, a_class)
