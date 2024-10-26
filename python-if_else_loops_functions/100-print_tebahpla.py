#!/usr/bin/python3
for i in range(25, 0, -2):
    ic = chr(i + 97)
    oc = chr(i + 64)
    print("{}{}".format(ic, oc), end="")
