#!/usr/bin/python3
"""
This module provides a function to read the contents of a file.
"""


def read_file(filename=""):
    """
    Reads and prints the content of a file.

    Args:
        filename (str): The file to read from.
    """
    with open(filename. encoding="UTF8") as f:
        print(f"{f.read()}", end="")
