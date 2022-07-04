#!/usr/bin/python3

""" sorting the list in ascending order """

class list:
    def __init__(self):
        pass


class MyList(list):
    def __init__(self, integers):
        super().__init__()
        
    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
