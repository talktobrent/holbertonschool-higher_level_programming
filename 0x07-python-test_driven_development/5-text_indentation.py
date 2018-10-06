#!/usr/bin/python3
""" Text indentation module
"""


def text_indentation(text):
    """ indents a text string

    Prints a newline when '.', ':', or '?' is found. Does not print the
    space(s) or tabs after the designated characters are found. The next
    printable text continues on a newline.

    Args:
        text (str): character string given

    Raises:
        TypeError: text must be a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    back = 0
    for index, x in enumerate(text):
        if x in ['.', ':', '?']:
            print("{:s}\n".format(text[back:index + 1].lstrip()))
            back = index + 1
            continue
        if index == len(text) - 1:
            print("{:s}".format(text[back:].lstrip()), end="")
