#!/usr/bin/python3
for a in range(122, 96, -1):
    if a % 2 == 0:
        temp = a
    else:
        temp = a - 32
    print("{}".format(chr(temp)), end="")
