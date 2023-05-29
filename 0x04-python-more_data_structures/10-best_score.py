#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return (None)
    else:
        key = 0
        item = 0
        for i in a_dictionary:
            if item < a_dictionary[i]:
                item = a_dictionary[i]
                key = i
        return (key)
