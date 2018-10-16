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
