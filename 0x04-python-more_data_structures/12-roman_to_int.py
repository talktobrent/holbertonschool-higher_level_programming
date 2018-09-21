#!/usr/bin/python3
def roman_to_int(roman_string):
    number = 0
    if roman_string:
        rdic = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M': 1000}
        number = 0
        for index, char in enumerate(roman_string):
            for r, n in rdic.items():
                if char == r:
                    if char == 'I' and index != len(roman_string) - 1:
                        if roman_string[index + 1] in ('X', 'V'):
                            number -= 2
                        else:
                            pass
                    number += n
    return (number)
