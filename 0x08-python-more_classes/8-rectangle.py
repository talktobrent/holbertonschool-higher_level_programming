#!/usr/bin/python3
""" Rectangle class module

"""


class Rectangle:
    """ A rectangle

    Attributes:
        number_of_instances (int): total instances
        print_symbol (any): symbol to represent size of rectangle
        bigger_or_equal (rect_1, rect_2): compares 2 rectangles
        __width (int)
        __height (int)
        __str (str): rectangle shown in string form (#)
        __repr (str): declaration form of rectangle
        __del (str): deletion messsage
        area() (int)
        perimeter() (int)
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ initializes rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ compares area of two rectangles

            Args:
                rect_1 (Rectangle)
                rect_2 (Rectangle)

            Returns:
                rect_1 if both equal, otherwise the rectangle with
                the greater area

            Raises:
                TypeError: "rect_1 must be an instance of Rectangle"
                TypeError: "rect_2 must be an instance of Rectangle"
        """
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __str__(self):
        """ prints square in string form
        """
        string = ""
        for x in range(self.height):
            string += "{}".format(self.print_symbol) * self.width
            if x != self.height - 1:
                string += '\n'
        return string

    def __repr__(self):
        """ represents a rectangle declaration in string form
        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """ prints deletion message and decrements class instance number
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """ sets height of rectangle

        Args:
            value (int): height

        Raises:
            TypeError: "height must be an integer"
            ValueError: "height must be >= 0"
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """ sets width of rectangle

        Args:
            value (int): width

        Raises:
            TypeError: "width must be an integer"
            ValueError: "width must be >= 0"
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """ area of rectangle
        """
        return int(self.width * self.height)

    def perimeter(self):
        """ perimeter of rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2
