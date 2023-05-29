#!/usr/bin/python3
for i in range(25, 0, -2):
    i = i
    o = 1 + i
    ic = i + 97
    oc = o + 63
    icc = chr(ic)
    occ = chr(oc)
    print(f"{icc}{occ}", end="")
