#!/usr/bin/python3
"""
rectangle
"""


class Rectangle:
    """
    implementation of the rectangle shape
    """
    #def __init__(self, width=0, height=0):#

    @property
    def width(self):
        self.width = width

    @property setter
    def width(self, value):
        self.value = value
        if width != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be  >= 0")
        return self.value


    
    @property
    def height(self):
        self.height = height

     @property setter
    def height(self, value):
        self.value = value
        if height != int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be  >= 0")
        return self.value
