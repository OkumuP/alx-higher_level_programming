#!/usr/bin/python3
"""A function which adds attributes to objects."""


def add_attribute(obj, att, value):
    """Add a new attribute to an object.

    Args:
        obj (any): The object to add attribute.
        att (str): The attribute name to add.
        value (any): The value of attribute.
    Raises:
        TypeError: If attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
