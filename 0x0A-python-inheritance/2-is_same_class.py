#!/usr/bin/python3
"""A function the performs class-checking."""


def is_same_class(obj, a_class):
    """Check if object is exactly an instance of a particular class.

    Args:
        obj (any): The object to be checked.
        a_class (type): The class to match the type of object to check.
    Returns:
        True - if the object is the exact instance.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
