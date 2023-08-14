#!/usr/bin/python3
# 8-multiple_returns.py


def multiple_returns(sentence):
    """Return string length and the first character of the string."""
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
