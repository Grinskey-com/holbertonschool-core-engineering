#!/usr/bin/env python3

def print_safe_integer(value):
    try:
        print("{:d}".format(value))
        return(True)
    except (ValueError, TypeError):
        return(False)
    
    