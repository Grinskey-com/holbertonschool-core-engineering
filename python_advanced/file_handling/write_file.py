#!/usr/bin/env python3
"""
write_file
a fucntion that writes a string to a text file
and returns the number of chars written 
"""


def write_file(filename="", text=""):
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
        
