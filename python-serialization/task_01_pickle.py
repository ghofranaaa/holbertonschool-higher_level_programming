#!/usr/bin/python3
"""
This module for custom object class with serialization and deserialization
"""
import pickle


class CustomObject:
    """
    A custom python class.
    """
    def __init__(self, name, age, is_student):
        """
        Initialize the CustomObject instance with name, age, and is_student.

        Parameters:
        ----------
        name : str
            The name of the person
        age : int
            The age of the person
        is_student : bool
            Whether the person is a student or not
        """
        self.name = name
        self.age = age
        self.is_student = is_student


    def display(self):
        """
        Displays the attributes of the custom object.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the CustomObject instance to a file.

        Parameters:
        filename : str
            The name of the file to serialize the object to.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception as e:
            print(f"Serialization error: {e}")
    
    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize a CustomObject instance from a file.

        Parameters:
        filename : str
            The name of the file to deserialize the object from

        Returns:
        CustomObject
            The deserialized CustomObject instance
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception as e:
            print(f"Deserialization error: {e}")
            return None
