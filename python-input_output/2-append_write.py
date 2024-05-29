#!/usr/bin/python3
"""
This module provides a function to append a string to a text file (UTF8) \
and return the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string to a text file (UTF8) and returns \
    the number of characters added.

    Args:
        filename (str): The name of the file to append to.
        Defaults to an empty string.
        text (str): The text to append to the file.
        Defaults to an empty string.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, 'a', encoding="UTF8") as f:
        return f.write(text)
