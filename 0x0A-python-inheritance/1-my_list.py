#!/usr/bin/python3

"""
sorting the list in ascending order
"""


class MyList(list):
    """subclass of the list"""
    def __init__(self):
        """initializes the object"""
        super().__init__()
        
    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))