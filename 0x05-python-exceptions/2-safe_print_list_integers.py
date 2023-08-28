#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    Print the first x elements of a list that are integers.

    :param my_list: The list to print elements from.
    :type my_list: list
    :param x: The number of elements of my_list to print.
    :type x: int

    :return: The number of elements printed.
    :rtype: int
    """
    ret = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return ret
