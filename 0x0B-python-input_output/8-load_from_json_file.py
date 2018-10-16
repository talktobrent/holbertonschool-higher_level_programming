#!/usr/bin/python3
import json


def load_from_json_file(filename):
    """ gets python object from JSON file

    Args:
        filename (str)

    Returns:
        object
    """
    with open(filename, "r") as fyle:
        return json.load(fyle)
