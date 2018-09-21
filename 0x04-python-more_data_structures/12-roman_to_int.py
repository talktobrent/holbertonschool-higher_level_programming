#!/usr/bin/python3
def roman_to_int(roman_string):
    number = 0
    if roman_string:
        rdic = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M': 1000}
        number = 0
        for char in roman_string:
            for r, n in rdic.items():
                if char == r:
                    number += n
    return (number)
