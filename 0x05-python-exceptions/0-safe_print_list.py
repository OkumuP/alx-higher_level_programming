#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    Print x elements from a list safely.

    :param my_list: The list to print elements from.
    :type my_list: list
    :param x: The number of elements from my_list to print.
    :type x: int

    :return: The number of elements actually printed.
    :rtype: int
    """
    elements_printed = 0

    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            elements_printed += 1
        except IndexError:
            break
        print("")  # Print a newline after printing the elements
        return elements_printed
