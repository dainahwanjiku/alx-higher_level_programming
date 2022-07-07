#!/usr/bin/python3
"""
This module implements a Square object
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """represent a square"""

    def __init__(self, size):
        """initialize a new square.
    
        Args:
            size (int): size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
