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
                raise Exception
            return json.dumps(list_dictionaries)
        else:
            return json.dumps([])

    @classmethod
    def save_to_file(cls, list_objs):
        """ JSON string to file
        """
        jlist = []
        if list_objs and len(list_objs) > 0:
            if not all(type(x) is cls for x in list_objs):
                raise Exception
            jlist = [x.to_dictionary() for x in list_objs]
        with open("{:s}.json".format(cls.__name__), "w") as afile:
            json.dump(jlist, afile)

    @staticmethod
    def from_json_string(json_string):
        """ JSON string to list
        """
        if json_string:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        """ build instance from dictionary
        """
        if cls.__name__ is "Square":
            new = cls(1)
        else:
            new = cls(1, 1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """ creates class instances from JSON file
        """
        with open("{:s}.json".format(cls.__name__), "r") as f:
            jlist = json.load(f)
        return [cls.create(**x) for x in jlist]
