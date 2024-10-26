#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    from calculator_1 import add, sub, mul, div
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    operators = {"+": add, "-": sub, "*": mul, "/": div}
    if argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    result = operators[argv[2]](a, b)
    print("{} {} {} = {}".format(a, argv[2], b, result))
