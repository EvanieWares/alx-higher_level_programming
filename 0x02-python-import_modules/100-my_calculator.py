#!/usr/bin/python3


def main():
    import sys
    from calculator_1 import add, sub, mul, div

    argv = sys.argv[1:]
    argc = len(argv)

    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[0])
    b = int(argv[2])
    operator = argv[1]

    operations = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
    }

    if operator in operations:
        operation = operations[operator]
        result = operation(a, b)
        print("{:d} {:s} {:d} = {:d}".format(a, operator, b, result))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)


if __name__ == "__main__":
    main()
