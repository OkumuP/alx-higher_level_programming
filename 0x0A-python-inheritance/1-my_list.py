#!/usr/bin/python3
"""Define an inherited class."""


class MyList(list):
    """Works with sorted printing for the  list class."""

    def print_sorted(self):
        """Print a list in ascending order."""
        print(sorted(self))
