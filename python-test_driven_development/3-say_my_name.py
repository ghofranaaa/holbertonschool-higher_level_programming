#!/usr/bin/python3
"""
This module provides a function `say_my_name` that prints a name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first_name> <last_name>".

    Args:
        first_name (string): The first name to be printed.
        last_name (string): The last name to be printed.

    Raises:
        TypeError: If `first_name` or `last_name` is not a string.
    """
    if not isinstance(first_name, string):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, string):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")

    if __name__ == "__main__":
        import doctest
        doctest.testfile("tests/3-say_my_name.txt")
