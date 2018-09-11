def uppercase(str):
    for index in str:
        if 96 < ord(index) < 123:
            temp = chr(ord(index) - 32)
        else:
            temp = index
        print(temp, end="")
    print("")
