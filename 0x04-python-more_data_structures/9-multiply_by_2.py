#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary.copy()
    keys_list = list(new_dictionary.keys())

    for key in keys_list:
        new_dictionary[key] *= 2

    return new_dictionary
