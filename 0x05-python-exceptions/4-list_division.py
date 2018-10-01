#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newlist = []
    for index in range(list_length):
        x = 0;
        try:
            x = my_list_1[index] / my_list_2[index]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            newlist.append(x)
    return newlist
