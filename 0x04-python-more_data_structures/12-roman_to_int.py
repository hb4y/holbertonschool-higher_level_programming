#!/usr/bin/python3
def roman_to_int(roman_string):
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0

    for i in roman_string:
        if not (i in d.keys()):
            return res
    if len(roman_string) == 1:
            return d[roman_string]

    res = d[roman_string[0]]
    for i in range(1, len(roman_string)):
        if d[roman_string[i - 1]] < d[roman_string[i]]:
            res -= d[roman_string[i]]
        else:
            res += d[roman_string[i]]
    return res if res > 0 else res * -1
