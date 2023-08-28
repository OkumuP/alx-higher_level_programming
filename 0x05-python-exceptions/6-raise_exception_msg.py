#!/usr/bin/python3

def raise_exception_msg(message=""):
    """Raise a NameError exception with an optional message.

    Args:
        message (str, optional): A custom error message.
            Defaults to an empty string.

    Raises:
        NameError: Always raises a NameError exception
            with the provided message.
    """
    raise NameError(message)
