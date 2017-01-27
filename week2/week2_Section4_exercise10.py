#! /usr/bin/python


def gcdRecur(a, b):
    if b == 0:
        return a

    return gcdRecur(b, a % b)


a = gcdRecur(9, 27)
print(a)
