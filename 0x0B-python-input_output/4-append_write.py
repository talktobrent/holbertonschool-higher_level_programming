#!/usr/bin/python3
def append_write(filename="", text=""):
    """ appends string to text file

    Args:
        filename (str): file to write to
        text (str): string to write

    Returns:
        number of chars written
    """
    with open(filename, "a", encoding="UTF8") as fyle:
        return fyle.write(text)
