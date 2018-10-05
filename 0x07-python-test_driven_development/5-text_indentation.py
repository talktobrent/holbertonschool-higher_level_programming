#!/usr/bin/python3
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

    count = 0
    while count < len(text):
        print("{:s}".format(text[count]), end="")
        if text[count] in ['.', '?', ':']:
            print("\n")
            for x in text[count + 1:]:
                if x.isspace() is False:
                    break
                else:
                    count += 1
        count += 1
