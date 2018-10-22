#!/usr/bin/python3
import json


""" Base module
"""


class Base:
    """ Base class of shapes

    Attributes:
        __nb_objects (int): class total instance count
        id

    Raises:

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initializer
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ JSON string
        """
        if list_dictionaries:
            if not all(type(x) is dict for x in list_dictionaries):
                raise TypeError("list must contain only dictionaries")
            return json.dumps(list_dictionaries)
        return json.dumps([])

    @classmethod
    def save_to_file(cls, list_objs):
        """ JSON string to file
        """
        jlist = []
        if list_objs and len(list_objs) > 0:
            if not all(type(x) is cls for x in list_objs):
                raise TypeError("all objects in list must be {:s}".format(
                                cls.__name__))
            jlist = [x.to_dictionary() for x in list_objs]
        with open("{:s}.json".format(cls.__name__), "w") as afile:
            afile.write(cls.to_json_string(jlist))

    @staticmethod
    def from_json_string(json_string):
        """ JSON string to list
        """
        if json_string:
            if type(json_string) is str:
                return json.loads(json_string)
            else:
                raise TypeError("from_json_string requires string")
        return []

    @classmethod
    def create(cls, **dictionary):
        """ build instance from dictionary
        """
        if cls.__name__ is "Square":
            args = tuple(dictionary.pop(x, None) for x in ["size", "x", "y", "id"])
        else:
            args = tuple(dictionary.pop(x, None) for x in ["width", "height", "x", "y", "id"])
        if not dictionary:
            test = object.__new__(cls)
            test.__init__(*args)
        if dictionary:
            raise AttributeError("no method: {:s} in {:s}".format(
                next(iter(dictionary)), cls.__name__))
        test.update(**dictionary)
        return test

    @classmethod
    def load_from_file(cls):
        """ creates class instances from JSON file
        """
        with open("{:s}.json".format(cls.__name__), "r") as f:
            jlist = cls.from_json_string(f.read())
            return [cls.create(**x) for x in jlist]
