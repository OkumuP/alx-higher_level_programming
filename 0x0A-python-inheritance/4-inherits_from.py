#!/usr/bin/python3
"""Inherited class-checking function."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.

    Args:
        obj (any): The object to be checked.
        a_class (type): The class to match the type with.
    Returns:
        True- if the object is an inherited instance.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
