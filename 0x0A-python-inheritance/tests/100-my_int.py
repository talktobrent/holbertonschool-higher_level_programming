#!/usr/bin/python3
""" MyInt module """


class MyInt(int):
    """ MyInt """

    def __eq__(self, other):
        """ reverses equality test

        Args:
            other (int)

        Returns:
            True if not equal, False if equal
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """ reverses non-equal test

        Args:
            other (int)

        Returns:
            True if equal, False if not equal
        """
        return super().__eq__(other)
