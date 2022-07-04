#!/usr/bin/python3

"""
function returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
otherwise False
"""


def is_kind_of_class(obj, a_class):
    """implementation

    Args:
        obj (Any): check object
        a_class (type): type to check against
    """
    return isinstance(obj, a_class)
