#!/usr/bin/python3
def inherits_from(obj, a_class):
    """ tests if sub class

    Args:

    obj: object given
    a_class: class given

    Returns:

        True or False
    """
    if type(obj) == a_class:
        return False

    return issubclass(type(obj), a_class)
