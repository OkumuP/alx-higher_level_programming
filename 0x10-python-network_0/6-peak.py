#!/usr/bin/python3
"""Defines lists of integers."""


def find_peak(list_of_integers):
    """Defination opf p[eak """
    if not list_of_integers:
        return ""

    lo, h = 0, len(list_of_integers) - 1

    while lo < h:
        mid = (lo + h) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            h = mid
        else:
            lo = mid + 1

    return list_of_integers[lo]
