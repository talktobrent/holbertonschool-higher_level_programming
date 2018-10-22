#!/usr/bin/python3
""" Rectangle module """

from models.base import Base


class Rectangle(Base):
    """ Rectangle: a shape that inherits from Base

    Attributes:
        __width (int):
        __height (int):
        __x (x):
        __y (y):
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initializer
        """
        Rectangle.width.fset(self, width)
        Rectangle.height.fset(self, height)
        if not x:
            self.x = 0
        else:
            self.x = x
        if not y:
            self.y = 0
        else:
            self.y = y
        super().__init__(id)

    def validate(self, name, value):
        """ value validator
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if name in ("width", "height", "size") and value < 1:
            raise ValueError("{:s} must be > 0".format(name))
        if name in ("x", "y") and value < 0:
            raise ValueError("{:s} must be >= 0".format(name))

    def area(self):
        """ gets area
        """
        return Rectangle.width.fget(self) * Rectangle.height.fget(self)

    def display(self):
        """ prints an instance
        """
        print('\n' * self.y, end="")
        print("{1}{0}\n".format('#' * Rectangle.width.fget(self), " " *
              self.x) * Rectangle.height.fget(self), end="")

    def __str__(self):
        """ string representation
        """
        return "[{}] ({}) {}/{} - {}/{}".format(
                type(self).__name__, self.id, self.x, self.y,
                Rectangle.width.fget(self), Rectangle.height.fget(self))

    def update(self, *args, **kwargs):
        """ updates attributes of instance

        Args:
            args (list): values in order of operation
            kwargs (dict): dictionary with keys corresponding to attributes
        """
        func = ["id", "width", "height", "x", "y"]
        if args and len(args) > 0:
            if args[0] is not None:
                self.id = args[0]
            for f, arg in zip(func[1:], args[1:]):
                if arg is not None:
                    exec("Rectangle.{:s}.fset(self, arg)".format(f))
        if kwargs and len(kwargs) > 0:
            for key in kwargs:
                if key in func:
                    if kwargs[key] is not None:
                        exec("self.{:s} = {}".format(key, kwargs[key]))
                else:
                    raise AttributeError("no method: {:s} in {:s}".format(
                        key, type(self).__name__))

    def to_dictionary(self):
        """ dictionary output
        """
        return {att.rsplit('_', 1)[-1]: value for att, value in
                self.__dict__.items()}

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        """ sets width
        """
        self.validate("width", width)
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        """ sets height
        """
        self.validate("height", height)
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        """ sets x
        """
        self.validate("x", x)
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        """ sets y
        """
        self.validate("y", y)
        self.__y = y
