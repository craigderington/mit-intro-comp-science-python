#! /usr/bin/python


def gcdIter(a, b):
    """
    Find the greatest common divisor
    :param a:
    :param b:
    :return: int (greatest common divisor of a and b)
    """
    test_value = min(a, b)
    while a % test_value != 0 or b % test_value != 0:
        test_value -= 1

    return test_value


a = gcdIter(9, 12)
print(a)
