#!/usr/bin/python3
class Square:
    """  a square

    Attributes:
        __size (int): Size of square
        area (self): area of sqaure
    """
    def __init__(self, size=0):
        self.size = size

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        for x in range(self.__size):
            for y in range(self.__size):
                print("#", end="")
            print()

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
