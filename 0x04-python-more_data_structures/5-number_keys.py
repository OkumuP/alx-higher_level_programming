#!/usr/bin/python3
def number_keys(a_dictionary):
    num_keys = 0
    key_list = list(a_dictionary.keys())

    for _ in key_list:
        num_keys += 1

    return num_keys
