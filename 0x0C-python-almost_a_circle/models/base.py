#!/usr/bin/python3
""" Base module
"""


class Base:
    """ Base class of shapes

    Attributes:
        __nb_objects (int): class total instance count
        id

    Raises:

    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
