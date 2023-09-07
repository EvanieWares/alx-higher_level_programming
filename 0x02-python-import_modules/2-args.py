#!/usr/bin/python3
import sys

def main():
    argv = sys.argv[1:]
    argc = len(argv)
    print(argc, end=" ")
    if argc == 0:
        print("arguments.")
    else:
        print("argument" + ("s:" if argc > 1 else ":"))
        for i, arg in enumerate(argv, start=1):
            print("{}: {}".format(i, arg))

if __name__ == "__main__":
    main()
