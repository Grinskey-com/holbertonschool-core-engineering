#!/usr/bin/env python3

def pow(a, b):

    if b == 0:
        return 1

    result = 1 
    iterations = b if b > 0 else -b

    for _ in range(iterations):
        result *= a

    if b < 0:
        return 1 /result 

    return result
