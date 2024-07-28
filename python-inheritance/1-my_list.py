#!/usr/bin/python3

"""
This module introduces a custom list class, MyList, which extends
Python's built-in list capabilities.
"""


class MyList(list):
    """
    Inherits from Python's built-in list class
    and adds functionality to sort and print its items in ascending order.
    """


    def print_sorted(self):
        """
        Sorts the list in ascending order and prints it.
        Ensures compatibility with integer types.
        """
        print(sorted(self))


if __name__ == "__main__":
    doctest.testfile("tests/1-my_list.txt")
