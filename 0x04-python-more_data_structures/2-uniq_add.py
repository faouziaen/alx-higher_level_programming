#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_set = set()
    total = 0

    for number in my_list:
        if number not in unique_set:
            unique_set.add(number)
            total += number

    return total
