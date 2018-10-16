#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """ reads lines in file

    Args:
        nb_lines (int): amount of lines to read
    """
    with open(filename, "r", encoding="UTF8") as fyle:
        if nb_lines > 0:
            for line in range(nb_lines):
                print(fyle.readline(), end="")
        else:
            print(fyle.read(), end="")
