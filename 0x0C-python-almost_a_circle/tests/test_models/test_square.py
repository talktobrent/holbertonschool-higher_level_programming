#!/usr/bin/python3
""" unittest for base module
"""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """ Tests Square class
    """

    def test_init(self):
        """ tests new square
        """
        a = Square(1, 2, 3, 4)
        self.assertEqual(a.size, 1)
        self.assertEqual(a.x, 2)
        self.assertEqual(a.y, 3)
        self.assertEqual(a.id, 4)

        a = Square(7)
        self.assertEqual(a.size, 7)

        a.size = 9
        self.assertEqual(a.size, 9)
        self.assertEqual(a._Rectangle__width, 9)
        self.assertEqual(a._Rectangle__height, 9)
        a.update(size=1)
        self.assertEqual(a._Rectangle__width, 1)
        self.assertEqual(a._Rectangle__height, 1)

        with self.assertRaises(AttributeError):
            print(a.width)
            print(a.height)
            a.height = 5
            a.width = 5

        with self.assertRaises(TypeError):
            a = Square(1, "2", 1, 1)

    def test_update(self):
        """ update test
        """
        args = ()
        kwargs = {}
        a = Square(1, 2, 3, 4)
        a.update(*args, **kwargs)
        self.assertEqual(a.size, 1)
        self.assertEqual(a.x, 2)
        self.assertEqual(a.y, 3)
        self.assertEqual(a.id, 4)
        a.update(0)
        self.assertEqual(a.id, 0)

        a = Square(1, 1, 1, 1)
        with self.assertRaises(AttributeError):
            a.update(width=5)
            a.update(height=5)
            a.update(size=5, width=5)
            a.update(size=4, height=5)
            a.update(dog=4)
            a.update(width=None)
            a.update(height=None)

        a = Square(1, 1, 1, 1)
        with self.assertRaises(ValueError):
            a.update(size=0)

    def test_dict(self):
        """ dict test
        """
        s1 = Square(10, 2, 1, 1)
        d = s1.to_dictionary()
        self.assertEqual(d, {'id': 1, 'x': 2, 'size': 10, 'y': 1})
