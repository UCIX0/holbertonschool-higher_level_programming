#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list2 = my_list[:]
    for i in range(len(list2)):
        if list2[i] == search:
            list2[i] = replace
    return (list2)
