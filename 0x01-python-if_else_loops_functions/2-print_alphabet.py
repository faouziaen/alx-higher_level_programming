#!/usr/bin/python3
# 2-print_alphabet.py

alphabet = ""
for letter in range(97, 123):
        alphabet += chr(letter)
print("{}".format(alphabet), end="")