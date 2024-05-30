#!/usr/bin/python3
"""
Module to serialize and deserialize a Python dictionary
to and from a JSON file.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    This function serialize a python dictionary to a json file.
    Parameters:
    data: a python dictionary.
    filename: the name of the file to save the serialized data to.
    """
    
    with open(filename, 'w') as f:
        return json.dump(data, f)

def load_and_deserialize(filename):
    """
    This function deserialize the data from a json file.
    Parameters:
    filename: the name of the file to load the data from.
    Returns:
    dict: The deserialized Python dictionary.
    """
    
    with open(filename, 'r') as f:
        return json.load(f)
