#!/usr/bin/python3
def write_file(filename="", text=""):
    """ writes string to text file

    Args:
        filename (str): file to write to
        text (str): string to write

    Returns:
        number of chars written
    """
    with open(filename, "w", encoding="UTF8") as fyle:
        return fyle.write(text)
