#!/usr/bin/python3
""" Base Geometry module
"""


class BaseGeometry:
    """ Geometric shape
    """
    def area(self):
        """ area of shape

        Raises:
            Exception: "area() is not implemented"
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates integer value

        Args:
            name (str): name given
            value (int): value given

        Raises:
            TypeError: "<name> must be an integer"
            ValueError: "<name> must be greater than 0"
        """
        if not isinstance(value, int) or value != value:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
