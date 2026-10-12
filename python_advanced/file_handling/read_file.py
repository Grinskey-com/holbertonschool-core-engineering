#!/usr/bin/env python3


def read_file(filename=""):
    with open(filename, encoding="utf-8") as my_File:
        print(my_File.read(),end="")
