#!/usr/bin/python3

"""this is a class square"""


class Square:
    """implementation"""
    def__init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
