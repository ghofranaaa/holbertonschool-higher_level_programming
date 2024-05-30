#!/usr/bin/python3
"""
Module for XML serialization and deserialization.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary to an XML file.
    
    Parameters:
    dictionary (dict): The dictionary to serialize.
    filename (str): The name of the output XML file.
    
    Returns:
    None
    """
    root = ET.Element('data')
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)

def deserialize_from_xml(filename):
    """
    Deserialize XML data from a file and reconstruct it into a Python dictionary.

    Parameters:
        filename (str): The name of the XML file containing the serialized data.

    Returns:
        dict: A Python dictionary reconstructed from the deserialized XML data.
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text
    return dictionary