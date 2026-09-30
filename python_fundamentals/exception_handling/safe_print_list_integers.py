#!/usr/bin/env python3

def safe_print_list_integers(my_list=[], x=0):
    
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(x))
            count += 1
        except (ValueError, TypeError):
            break
    return (count)
        