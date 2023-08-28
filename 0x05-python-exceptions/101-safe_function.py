#!/usr/bin/python3

import sys

def safe_function(fct, *args):
    """Execute a function safely.

    Args:
        fct: The function to execute.
        *args: Arguments for the function.

    Returns:
        The result of the function call, or None if an error occurs.
    """
    try:
        result = fct(*args)
        return result
    except Exception as e:
        error_message = "Exception: {}".format(e)
        print(error_message, file=sys.stderr)
        return None
