#!/usr/bin/python3
"""Define a class MyList that inherits from the built-in list class"""


class MyList(list):
    """ Define a method print_sorted for the MyList class"""
    def print_sorted(self):
        """ Create a copy of the list using list slicing (self[:])"""
        sorted_list = self[:]

        sorted_list.sort()

        print(sorted_list)
