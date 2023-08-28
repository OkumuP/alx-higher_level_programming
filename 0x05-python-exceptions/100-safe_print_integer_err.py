#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    """Prints an integer with "{:d}".format() and handles exceptions.

    Args:
        value (int): The integer to print.

    Returns:
        bool: True if the integer was successfully printed, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as e:
        error_message = "Exception: {}".format(e)
        print(error_message, file=sys.stderr)
        return False
