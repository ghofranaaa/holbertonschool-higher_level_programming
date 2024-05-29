#!/usr/bin/python3
"""
Module defines the Student class.
"""


class Student:
    """
    A class to represent a student.

    Attributes:
    ----------
    first_name : str
    last_name : str
    age : int
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialize the student instance with first name, last name, and age.

        Parameters:
        ----------
        first_name : str
            The first name of the student.
        last_name : str
            The last name of the student.
        age : int
            The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.

        Returns:
        -------
        dict
            A dictionary representation of the student's attributes.
        """
        return self.__dict__
 