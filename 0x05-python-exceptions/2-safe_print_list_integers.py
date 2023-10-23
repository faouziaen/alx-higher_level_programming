#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    n = 0
    while n < x:
        try:
            if n < len(my_list):
                print("{:d}".format(my_list[n]), end='')
                count += 1
            else:
                raise IndexError("list index out of range")
        except (ValueError, TypeError):
            pass
        n += 1
    print()
    return count
