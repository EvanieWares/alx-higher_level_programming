#!/usr/bin/python3

def remove_char_at(str, n):
    copied = ""
    for i in range(len(str)):
        if i == n:
            continue
        copied = copied + str[i]

    return copied
