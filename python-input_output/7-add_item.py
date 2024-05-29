#!/usr/bin/python3
"""
This script adds all command-line arguments to a Python list \
and saves them to a file.

The list is saved as a JSON representation in a file named 'add_item.json'.
If the file doesn't exist, it is created.

Usage:
    ./7-add_item.py arg1 arg2 ...

Arguments:
    arg1, arg2, ... : Arguments to be added to the list and saved to the file.
"""
import sys
import os


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = 'add_item.json'
if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

items.extend(sys.argv[1:])
save_to_json_file(items, filename)
