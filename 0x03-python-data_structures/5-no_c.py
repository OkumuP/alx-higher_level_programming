#!/usr/bin/python3
# 5-no_c.py


def no_c(my_string):
    
    copy = [y for y in my_string if y != 'c' and y != 'C']
    return ("".join(copy))
