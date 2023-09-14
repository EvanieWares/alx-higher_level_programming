#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        best_key = None
        for key, value in a_dictionary.items():
            if best_key is None or value > a_dictionary[best_key]:
                best_key = key
        return best_key
