#!/usr/bin/python3
def no_c(my_string):
    string2 = ""
    for i in my_string:
        if i != "c" and i != "C":
            string2 += i
    return string2
