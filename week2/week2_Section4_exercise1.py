#! /ur/bin/python

x = 12


def g(x):
    x += 1

    def h(y):
        return x + y
    return h(6)

print(g(x))
