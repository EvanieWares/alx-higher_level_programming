#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    result = 0
    if len(argv) != 1:
        for i in range(1, len(argv)):
            result = result + int(argv[i])
        print("{}".format(result))
