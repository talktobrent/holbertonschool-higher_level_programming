#!/usr/bin/python3
class Square:
    """  a square

    Attributes:
        __size (int): Size of square
        area (self): area of sqaure
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size * self.__size
