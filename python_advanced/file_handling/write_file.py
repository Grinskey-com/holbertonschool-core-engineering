#!/usr/bin/env python3
"""
Writes to a file and prints the number of chars 

"""


def write_file(filename="", text=""):
    with open(filename, mode="w", encoding="utf-8") as f:
        nb_characters = f.write("This chool is so cool\n")
        print(nb_characters)
