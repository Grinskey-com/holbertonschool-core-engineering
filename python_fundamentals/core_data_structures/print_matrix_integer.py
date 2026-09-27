#!/usr/bin/env python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        formatted_elements = ["{:d}".format(num) for num in row]
        print(" ".join(formatted_elements))