#!/usr/bin/python3

def safe_print_integer(value):
    for x in range(value):
        try:
            print("{:d}\n" .format(value))
        except Exception as error:
            return False
        else:
            return True
