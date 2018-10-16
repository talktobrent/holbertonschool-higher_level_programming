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
        if type(value) not in (int, float):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ ractangle class, inherits from BaseGeomtry

    Attributes:
        __width (int): width
        __height (int): height
    """

    def __init__(self, width, height):
        """ initializes Rectangle

        Args:
            width (int): width given
            height (int): height given
        """

        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)

    def __str__(self):
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

    def area(self):
        return self.__width * self.__height
