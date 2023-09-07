#!/usr/bin/python3
import sys


def main():
    argv = sys.argv[1:]
    argc = len(argv)
    total = 0

    if argc > 0:
        for i in range(argc):
            total += int(argv[i])

    print(total)


if __name__ == "__main__":
    main()
