#!/usr/bin/python3

def uppercase(str):
    upper = ""
    for i in str:
        if ord(i) > 96 and ord(i) < 124:
            upper = upper + "{:c}".format(ord(i) - 32)
            continue
        upper = upper + i

    print(upper)
