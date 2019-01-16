#!/usr/bin/python3
""" find_peak module """


def find_peak(list_of_integers):
    """ finds peak integer of list """

    x = list_of_integers

    high = None

    for index, number in enumerate(x):
        if index == 0 or x[index - 1] < number:
            left = True
        else:
            left = False
        if index == len(x) - 1 or x[index + 1] < number:
            right = True
        else:
            right = False
        if right and left:
            return number
        if high is None or number > high:
            high = number

    return high
