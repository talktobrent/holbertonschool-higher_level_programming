#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    newset = set(set_1)
    newset.symmetric_difference_update(set_2)
    return newset
