#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) and len(tuple_b) > 1:
        newtup = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
        return newtup
    else:
        if len(tuple_a) == 1:
            la = [tuple_a[0], 0]
        elif len(tuple_a) == 0:
            la = [0, 0]
        else:
            la = list(tuple_a)
        if len(tuple_b) == 1:
            lb = [tuple_b[0], 0]
        elif len(tuple_b) == 0:
            lb = [0, 0]
        else:
            lb = list(tuple_b)
        newtup = (la[0] + lb[0], la[1] + lb[1])
    return newtup
