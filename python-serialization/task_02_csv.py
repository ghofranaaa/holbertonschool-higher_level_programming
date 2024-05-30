#!/usr/bin/python3
"""
This module converts CSV data to JSON format.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert CSV data to JSON format and write it to data.json.

    Parameters:
    csv_filename : str
        The filename of the input CSV file.

    Returns:
    bool
        True if the conversion was successful, False otherwise.
    """
    try:
        with open(csv_filename, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]
        
        with open('data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
            
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
