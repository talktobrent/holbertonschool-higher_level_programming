#!/usr/bin/python3
""" Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ tests max_integer function
    """

    def test_max_integer(self):
	""" max_integer argument tests
	"""

        result = max_integer([1, 2, 3])
        self.assertEqual(result, 3)

        result = max_integer([1, 3, 2])
        self.assertEqual(result, 3)

        result = max_integer([3, 2, 1])
        self.assertEqual(result, 3)

        result = max_integer([-3, 2, 1])
        self.assertEqual(result, 2)

        result = max_integer([3.2, 2.3, 1.1])
        self.assertEqual(result, 3.2)

        result = max_integer([3])
        self.assertEqual(result, 3)

        result = max_integer([0, 0, 0])
        self.assertEqual(result, 0)

        result = max_integer([])
        self.assertIsNone(result)

        with self.assertRaises(TypeError):
            max_integer(3, 2)
            max_integer(["3", "2"])
            max_integer([[3, 2], [3, 2]])
