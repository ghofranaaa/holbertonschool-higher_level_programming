#!/usr/bin/python3

"""
This module introduces a custom list class, MyList, which extends Python's built-in list capabilities.
MyList includes a method to sort and print its contents in ascending order, assuming integer types.
It also demonstrates the use of doctests for testing purposes.
"""


import doctest

class MyList(list):
    """
    Inherits from Python's built-in list class and adds functionality to sort and print its items in ascending order.
    All elements within the list are assumed to be integers.
    """

    def print_sorted(self):
        """
        Sorts the list in ascending order and prints it.
        Ensures compatibility with integer types.
        """
        print(sorted(self))

if __name__ == "__main__":
    doctest.testfile("tests/1-my_list.txt")
