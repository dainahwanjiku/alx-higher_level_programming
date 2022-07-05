#!/usr/bin/python3
"""function that creates an object from a json file"""
import json


def load_from_json_file(filename):
    """load from json"""
    with open(filename, encoding="utf-8") as fd:
        return json.load(fd)
