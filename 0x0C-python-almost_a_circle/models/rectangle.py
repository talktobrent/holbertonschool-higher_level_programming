#!/usr/bin/python3
from models.base import Base

""" Rectangle module """


class Rectangle(Base):
    """ Rectangle: a shape that inherits from Base

    Attributes:
        __width (int):
        __height (int):
        __x (x):
        __y (y):


    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initializer """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        """ sets width """

        self.__width = width


    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        """ sets height """

        self.__height = height


    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        """ sets x """

        self.__x = x


    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        """ sets y """

        self.__y = y
