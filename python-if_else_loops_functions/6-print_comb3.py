#!/usr/bin/python3
for i in range(0, 10):
    for o in range(0, 10):
        if i == 8 and o == 9:
            print("89")
        elif i < o:
            print(f"{i}{o}", end=", ")
