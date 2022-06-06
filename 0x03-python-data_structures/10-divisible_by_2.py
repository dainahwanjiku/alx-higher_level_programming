#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    if not my_list:
        return
    new_list = [n % 2 == 0 "TRUE" for n in my_list else "FALSE"]
    return new_list
