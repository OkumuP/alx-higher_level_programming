#!/usr/bin/python3
"""Module to find the maximum int in a list.
"""


def max_integer(lst=[]):
    """Find and return the maximum integer in a list of integers.

    Args:
        lst (list): The list of integers to search for the maximum value.

    Returns:
        int or None: The maximum integer if the list is not empty, else None.
    """
    if len(lst) == 0:
        return None
    result = lst[0]
    i = 1
    while i < len(lst):
        if lst[i] > result:
            result = lst[i]
        i += 1
    return result
