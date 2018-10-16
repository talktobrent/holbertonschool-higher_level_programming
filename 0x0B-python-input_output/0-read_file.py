#!/usr/bin/python3
def read_file(filename=""):
    """ opens and reads a file """
    with open(filename, "r") as fyle:
        print(fyle.read(), end="")
