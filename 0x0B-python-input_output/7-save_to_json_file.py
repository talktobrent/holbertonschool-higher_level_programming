#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    """ python object to JSON file

    Args:
        my_obj (object)
        filename (str)
    """
    with open(filename, "w") as fyle:
        json.dump(my_obj, fyle)
