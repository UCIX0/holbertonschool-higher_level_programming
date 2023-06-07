#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        f = my_list[0]
        for indes in range(len(my_list)):
            if my_list[indes] > f:
                f = my_list[indes]
        return f
