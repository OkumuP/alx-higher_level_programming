#!/usr/bin/python3
"""Defines a class which inherits from int."""


class MyInt(int):
    """Invert int operators"""

    def __eq__(self, value):
        """This Overrides == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """This Overrides != operator with == behavior."""
        return self.real == value
