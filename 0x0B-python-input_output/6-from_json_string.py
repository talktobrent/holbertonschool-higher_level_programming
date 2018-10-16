#!/usr/bin/python3
import json


def from_json_string(my_str):
    """ JSON string to python object

    Args:
       my_str (JSON str)

    Returns:
        object
    """
    return json.loads(my_str)
