#!/usr/bin/python3
"""
the class to json function
"""


def class_to_json(obj):
    """
    returns the dictionary description with simple data structure
    """
    return obj.__dict__
