#! /usr/bin/python

"""
def foo(x, y=5):
    def bar(x):
        return x + 1
    return bar(y * 2)
"""


def foo(x):
    def bar(z, x = 0):
        return z + x

    return bar(3)

result = foo(5)
print(result)
