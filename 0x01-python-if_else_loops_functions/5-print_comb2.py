#!/usr/bin/python3
for a in range(0, 100):
    if a < 99:
        print("{0:02}, ".format(a), end="")
    else:
        print("{0:02}".format(a))
