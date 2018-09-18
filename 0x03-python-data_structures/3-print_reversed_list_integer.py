#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    copylist = my_list[:]
    for x in reversed(copylist):
        print("{:d}".format(x))
