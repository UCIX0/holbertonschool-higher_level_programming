#!/usr/bin/python3
for i in range(0, 10):
    for o in range(0, 10):
        if i == 8 and o == 9:
            print("{:d}{:d}".format(i, o))
        elif i < o:
            print("{:d}{:d}".format(i, o), end=", ")
