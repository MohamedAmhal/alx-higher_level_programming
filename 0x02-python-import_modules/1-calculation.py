#!/usr/bin/python3
if __name__ == '__main__':
    import calculator_1 as clt
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, clt.add(a, b)))
    print("{} - {} = {}".format(a, b, clt.sub(a, b)))
    print("{} * {} = {}".format(a, b, clt.mul(a, b)))
    print("{} / {} = {}".format(a, b, clt.div(a, b)))
