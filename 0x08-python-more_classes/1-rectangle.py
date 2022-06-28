#!/usr/bin/python3
"""
defined rectangle
"""


class Rectangle:
    """
    rectangle object with getter and setter
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @property setter
    def width(self, value):
        self.__value = value
        if width != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be  >= 0")
        self.__width = value


    
    @property
    def height(self):
        return self.__height

     @property setter
     def height(self, value):
         if height != int:
             raise TypeError("height must be an integer")
         elif height < 0:
             raise ValueError("height must be  >= 0")
        self.__height = value
