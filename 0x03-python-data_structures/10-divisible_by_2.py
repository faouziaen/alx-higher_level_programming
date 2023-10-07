#!/usr/bin/python3

def divisible_by_2(input_list=[]):
    """Find all multiples of 2 in a list."""
    result = []
    for num in input_list:
        if num % 2 == 0:
            result.append(True)
        else:
            result.append(False)

    return result
