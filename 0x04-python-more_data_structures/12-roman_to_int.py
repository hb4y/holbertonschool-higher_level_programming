#!/usr/bin/python3
def roman_to_int(roman_string):
    if (isinstance(roman_string, str)) and (roman_string):
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0

        for i in range(len(roman_string)):
            if (i > 0) and (d[roman_string[i - 1]] < d[roman_string[i]]):
                res += d[roman_string[i]] - 2 * d[roman_string[i - 1]]
            else:
                res += d[roman_string[i]]
        return int(res)
    else:
        return 0
