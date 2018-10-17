#!/usr/bin/python3
""" Student module
"""


class Student:
    """ A student

    Atrributes:
        first_name (str)
        last_name (str)
        age (int)
    """

    def __init__(self, first_name, last_name, age):
        """ initializes a Student

        Args:
            first_name (str)
            last_name (str)
            age (int)
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ JSON representation """
        return self.__dict__
