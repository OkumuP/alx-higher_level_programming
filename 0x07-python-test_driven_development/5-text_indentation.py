#!/usr/bin/python3
# text_indentation.py
"""Defines a custom text-indentation function."""

def text_indentation(text):
    """Prints two new lines after each '.', '?', and ':'.

    Args:
        text (string): This is the text to be printed.
    Raises:
        TypeError: Text not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
