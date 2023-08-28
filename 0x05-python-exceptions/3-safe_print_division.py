#!/usr/bin/python3

def safe_print_division(a, b):
    """Returns the division of a by b.

    :param a: The numerator.
    :type a: int or float
    :param b: The denominator.
    :type b: int or float

    :return: The result of the division, or None if division is not possible.
    :rtype: float or None
    """
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return div
