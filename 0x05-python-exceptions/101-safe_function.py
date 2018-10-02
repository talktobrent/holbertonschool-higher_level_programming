#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as x:
        print("Exception: {}".format(x), file=stderr)
        return None
