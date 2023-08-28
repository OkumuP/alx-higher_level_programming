#!/usr/bin/python3

def safe_print_integer(value):
    """
    Print an integer using "{:d}".format().

    :param value: The integer to print.
    :type value: int

    :return: True if the integer was successfully printed, False otherwise.
    :rtype: bool
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
