#!/usr/bin/python3
""" unittest for base module
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ Tests Base class id creation
    """
    def test_idcheck(self):
        """ checks id creation
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b4 = Base(12)
        self.assertEqual(b4.id, 12)

        b6 = Base(12)
        self.assertEqual(b6.id, 12)

        b5 = Base()
        self.assertEqual(b5.id, 3)

        del(b5)
        b5 = Base()
        self.assertEqual(b5.id, 4)

        b7 = Base(None)
        self.assertEqual(b7.id, 5)
