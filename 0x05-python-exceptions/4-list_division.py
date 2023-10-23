#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            d = my_list_1[i] if i < len(my_list_1) else 0
            div = my_list_2[i] if i < len(my_list_2) else 0

            if isinstance(d, (int, float)) and isinstance(div, (int, float)):
                if div == 0:
                    result.append(0)
                    print("division by 0")
                else:
                    result.append(d / div)
            else:
                result.append(0)
                print("wrong type")
        except IndexError:
            print("out of range")
            result.append(0)
        finally:
            pass
    return result
