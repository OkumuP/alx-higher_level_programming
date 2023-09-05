#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    Prevent the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    # Use __slots__ to restrict attribute names to 'first_name'
    __slots__ = ["first_name"]
