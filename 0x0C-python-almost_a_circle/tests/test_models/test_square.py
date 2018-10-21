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
        a.size = 9
        self.assertEqual(a.size, 9)
        self.assertEqual(a._Rectangle__width, 9)
        self.assertEqual(a._Rectangle__height, 9)
        a.update(size=1)
        self.assertEqual(a._Rectangle__width, 1)
        self.assertEqual(a._Rectangle__height, 1)

        a = Square(1, 1, 1, 1)
        with self.assertRaises(AttributeError):
            print(a.width)
            print(a.height)
            a.height = 5
            a.width = 5
            a.update(width=5)
            a.update(height=5)
            a.update(size=5, width=5)
            a.update(size=4, height=5)
            a.update(dog=4)
            a.update(width=None)
            a.update(heigth=None)
