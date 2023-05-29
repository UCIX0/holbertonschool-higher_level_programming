#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is not None:
        list2 = my_list.copy()
    for indes in range(len(my_list)):
        if my_list[indes] % 2 == 0:
            list2[indes] = True
        else:
            list2[indes] = False
    return list2
