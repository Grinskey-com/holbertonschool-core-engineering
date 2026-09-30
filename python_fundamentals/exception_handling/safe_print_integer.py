#!/usr/bin/env python3

def print_safe_integer(value):
    try:
        isinstance(value, int)
        print("{:d}".format(value))
        return(True)
    except ValueError:
        print()
        return(False)
    
    