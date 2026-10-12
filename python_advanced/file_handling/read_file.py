#!/usr/bin/env python3


"""read_file: """
"""provides a utility function to read and pront the contents"""
def read_file(filename=""):
    with open(filename, encoding="utf-8") as my_File:
        print(my_File.read(),end="")
