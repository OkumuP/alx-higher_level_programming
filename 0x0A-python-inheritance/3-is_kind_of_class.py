#!/usr/bin/python3


def is_kind_of_class(obj, a_class):
    """Check whether an object is an insatnce of a class.

    Args:
        obj (any): The object to be checked.
        a_class (type): The class to match the type of object to.
    Returns:
        True - if the object is an instance or inherited instance.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
