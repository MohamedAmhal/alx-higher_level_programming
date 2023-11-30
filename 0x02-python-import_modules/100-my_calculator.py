#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    import calculator_1 as clt

    if len(sys.argv) - 1 == 3:
        a = sys.argv[2]
        x = int(sys.argv[1])
        y = int(sys.argv[3])

        if a == '+':
            print("{} + {} = {}".format(x, y, clt.add(x, y)))
            exit(1)
        elif a == '-':
            print("{} + {} = {}".format(x, y, clt.sub(x, y)))
            exit(1)
        elif a == '*':
            print("{} + {} = {}".format(x, y, clt.mul(x, y)))
            exit(1)
        elif a == '/':
            if y != 0:
                print("{} + {} = {}".format(x, y, clt.div(x, y)))
                exit(1)
            else:
                print("you are not devided by 0!!")
                exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(0)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
