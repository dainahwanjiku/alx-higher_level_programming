#!/usr/bin/python3
"""
this is a class square

it implements value and type checks for its attributes
"""


class Square:
    """
    implementation
    """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
