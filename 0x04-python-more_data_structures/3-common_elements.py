#!/usr/bin/python3
def common_elements(set_1, set_2):
    newset = set(set_1)
    newset.intersection_update(set_2)
    return newset
