#!/usr/bin/python3
def number_of_lines(filename=""):
    """ lines in text file
    """
    line = 0
    with open(filename, "r") as fyle:
        for aline in fyle:
            line += 1
    return line
