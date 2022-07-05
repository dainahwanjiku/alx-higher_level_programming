#!/usr/bin/python3
"""
a function that writes an object to a text file,
using a json representation
"""


def save_to_json_file(my_obj, filename):
    """save to json"""
    with open(filename, mode="w", encoding="utf-8") as fd:
        fd.write(json.dumps(my_obj))


