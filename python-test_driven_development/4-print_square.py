#!/usr/bin/python3
"""
This module contains a function that\
 prints a square with the charactere #.
"""


def print_square(size):
    """
    Prints a square with the character #.

    Args:
        size : (int) : the length of the square.

    Raises:
        TypeError: If the size if not int and if it is float and less than 0.
        ValueError: If the size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)


if __name__ == "__main__":
    import doctest

    doctest.testfile("tests/4-print_square.txt")
