#!/usr/bin/python3

def search_replace(my_list, search, replace):
    # Create a new list by iterating through the original list
    new_list = [replace if element == search else element for element in my_list]
    return new_list
