#!/usr/bin/python3
import sys
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("numbers", nargs="+", type=int)
    args = parser.parse_args()
    numbers = args.numbers

    total = 0
    for number in numbers:
        total += number

    print(total)


if __name__ == "__main__":
    main()
