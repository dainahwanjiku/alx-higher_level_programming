#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    print(my_string.translate({ord('Cc'):None}))
    return (new_string)

