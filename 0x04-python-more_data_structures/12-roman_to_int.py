#!/usr/bin/python3

def to_subtract(list_num):
    to_subtract_value = 0
    max_value = max(list_num)

    for n in list_num:
        if max_value > n:
            to_subtract_value += n

    return max_value - to_subtract_value


def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0

    if not roman_string:
        return 0

    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numeral_keys = list(roman_numerals.keys())

    num = 0
    last_roman_value = 0
    numeral_values = [0]

    for ch in roman_string:
        for r_num in numeral_keys:
            if r_num == ch:
                if roman_numerals.get(ch) <= last_roman_value:
                    num += to_subtract(numeral_values)
                    numeral_values = [roman_numerals.get(ch)]
                else:
                    numeral_values.append(roman_numerals.get(ch))

                last_roman_value = roman_numerals.get(ch)

    num += to_subtract(numeral_values)

    return num
