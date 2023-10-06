#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    "Iterate through the list in reverse order and print each integer"
    for num in reversed(my_list):
        print("{:d}".format(num))
