#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        keys = list(a_dictionary.keys())
        best = a_dictionary[keys.pop()]
        for key in keys:
            if a_dictionary[key] > best:
                best = a_dictionary[key]
        return best
