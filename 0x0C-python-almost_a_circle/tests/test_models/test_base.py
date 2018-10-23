#!/usr/bin/python3
""" unittest for base module
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """ Tests Base class id creation
    """
    def test_idcheck(self):
        """ checks id creation
        """
        b1 = Base()
        self.assertEqual(b1.id, Base._Base__nb_objects)

        b2 = Base()
        self.assertGreater(b2.id, b1.id)

        b4 = Base(12)
        self.assertEqual(b4.id, 12)

        b6 = Base(12)
        self.assertEqual(b6.id, 12)

        b5 = Base()
        self.assertEqual(b5.id, Base._Base__nb_objects)

        x = Base._Base__nb_objects + 1

        bno = Base(0)
        self.assertNotEqual(bno.id, x)

        b6 = Base()
        self.assertEqual(b6.id, x)

        b7 = Base(None)
        self.assertEqual(b7.id, x + 1)

    def test_jsonstring(self):
        """ test json to string function
        """
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertIsInstance(json_dictionary, str)
        self.assertEqual(json_dictionary[:3], "[{\"")

        json_dictionary = Base.to_json_string([dictionary, {}])
        json_dictionary = Base.to_json_string([{}])
        self.assertEqual(json_dictionary, "[{}]")

        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 7, 2, 8)
            dictionary = r1.to_dictionary()
            json_dictionary = Base.to_json_string([dictionary, r1])

    def test_json_to_file(self):
        """ test json to file
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as f:
            string = f.read()
            self.assertEqual(string[:3], "[{\"")

    def test_from_json_string(self):
        """ tests string to dict
        """
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
            ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertCountEqual(list_output, list_input)

    def test_create(self):
        """ tests create method
        """
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))

    def test_create_incorrect_class(self):
        """ tests with dict of wrong class
        """
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        with self.assertRaises(AttributeError):
            Square.create(**r1_dictionary)

    def test_load_from_file(self):
        """ test load from file
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertCountEqual([str(x) for x in list_rectangles_input],
                              [str(x) for x in list_rectangles_output])
