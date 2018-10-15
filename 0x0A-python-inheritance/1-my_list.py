#!/usr/bin/python3
""" MyList module
"""


class MyList(list):
    """ custom list class inherits from list class
    """

    def print_sorted(self):
        """ prints list in ascending order
        """

        print(sorted(self))
