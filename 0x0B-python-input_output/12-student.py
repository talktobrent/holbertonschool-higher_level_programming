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

    def to_json(self, attrs=None):
        """ JSON representation

        Args:
            attrs (list): list of strings

        Returns:
            Dictionary
        """
        if type(attrs) == list:
            for x in attrs:
                if type(x) is not str:
                    return self.__dict__
            return {key: self.__dict__[key] for key in attrs
                    if key in self.__dict__}
        return self.__dict__
