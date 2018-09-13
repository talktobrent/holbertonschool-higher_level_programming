#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    print("{:d} argument".format(len(argv) - 1), end="")
    if len(argv) == 1:
        print("s.")
        exit()
    elif len(argv) - 1 > 1:
        print("s:")
    else:
        print(":")
    for count in range(1, len(argv)):
        print("{:d}: {:s}".format(count, argv[count]))
