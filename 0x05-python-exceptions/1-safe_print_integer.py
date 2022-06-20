#!/usr/bin/python3

def safe_print_integer(value):
    x = 0;
    for value in range(x):
        try:
            print("{:d}\n" .format(value))
        except Exception as error:
            return (true);
        else:
            return True
