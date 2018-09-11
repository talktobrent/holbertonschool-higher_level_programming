def uppercase(str):
    for index in str:
        if 96 < ord(index) < 123:
            print(chr(ord(index) - 32), end="")
        else:
            print(index, end="")
    print("")
