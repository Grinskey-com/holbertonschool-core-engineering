#!/usr/bin/env python3
output = ""

for letter_code in range(ord('a'), ord('z') +1):
    letter = chr(letter_code)
    if letter not in "qe":
            output += letter

print(output)              