#!/usr/bin/python3
""" unittest for base module
"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ Tests Rectangle class
    """
    def test_init(self):
        """ tests initialization
        """
        a = Rectangle(1, 2, 3, 4, 8)
        self.assertEqual(a.width, 1)
        self.assertEqual(a.height, 2)
        self.assertEqual(a.x, 3)
        self.assertEqual(a.y, 4)
        self.assertEqual(a.id, 8)

        a = Rectangle(1, 2)
        self.assertEqual(a.width, 1)
        self.assertEqual(a.height, 2)
        self.assertEqual(a.x, 0)
        self.assertEqual(a.y, 0)

        a = Rectangle(1, 2, None, None, 8)
        self.assertEqual(a.width, 1)
        self.assertEqual(a.height, 2)
        self.assertEqual(a.x, 0)
        self.assertEqual(a.y, 0)
        self.assertEqual(a.id, 8)

        with self.assertRaises(TypeError):
            Rectangle(None, None, None, None, 8)
            Rectangle(1, "9")
            Rectangle(9.9, 1)
            Rectangle(None, 1)
            Rectangle(True, 1)

        with self.assertRaises(ValueError):
            Rectangle(0, 1)
            Rectangle(1, -1)
            Rectangle(1, 1, -1)

    def test_area(self):
        """ area test
        """
        a = Rectangle(1, 2)
        self.assertEqual(a.area(), 2)

    def test_str(self):
        """ string test
        """
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

    def test_update(self):
        """ update test
        """
        r1 = Rectangle(1, 1, 1, 1, 1)
        r1.update(12, 4, 6, 2, 2)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/2 - 4/6")

        r1 = Rectangle(1, 1, 1, 1, 1)
        r1.update(None, None, None, None, 3)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.y, 3)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.height, 1)
        self.assertEqual(r1.width, 1)

        r1 = Rectangle(1, 1, 1, 1, 1)
        r1.update(12)
        self.assertEqual(r1.id, 12)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 1)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 1)

        r1 = Rectangle(1, 1, 1, 1, 1)
        r1.update(id=None, x=None, y=None, width=None, height=2)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 1)
        self.assertEqual(r1.id, 1)

        r1 = Rectangle(1, 1, 1, 1, 1)
        r1.update(id=0, x=0, y=0, width=None, height=None)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 1)
        self.assertEqual(r1.id, 0)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r1 = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaises(AttributeError):
            r1.update(dog=7, height=5)
            r1.update(size=7, height=5)
            r1.update(dog=None, height=5)

        with self.assertRaises(ValueError):
            r1.update(height=0)
            r1.update(0, 0)

        with self.assertRaises(TypeError):
            r1.update(height="7")
            r1.update(0, "7")
