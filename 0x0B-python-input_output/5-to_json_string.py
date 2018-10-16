#!/usr/bin/python3
import json


def to_json_string(my_obj):
    """ JSON representation of object

    Args:
        my_obj (object)

    Returns:
        JSON string
    """
    return json.dumps(my_obj)
