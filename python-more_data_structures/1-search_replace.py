#!/usr/bin/python3
def search_replace2(my_list, search, replace):
    return [replace if x == search else x for x in my_list ]
