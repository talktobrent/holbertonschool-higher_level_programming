#!/usr/bin/python3
def roman_to_int(roman_string):
    number = 0
    if roman_string:
        rdic = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M': 1000}
        number = 0
        index = 0
        while index < len(roman_string):
            nextchar = None
            if roman_string[index] in rdic:
                n = rdic[roman_string[index]]
            if index < len(roman_string) - 1:
                nextchar = roman_string[index + 1]
                if rdic[nextchar] > n:
                    number += rdic[nextchar] - n
                    index += 1
                else:
                    number += n
            else:
                number += n
            index += 1
    return (number)
