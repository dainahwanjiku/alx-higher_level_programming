#!/usr/bin/python3
"""
sorting the list in ascending order
"""


class MyList(list):
    """implements sorted printing for the built-in list class."""
        
    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
