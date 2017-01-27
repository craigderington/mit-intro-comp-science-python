#! /usr/bin/python


def recurPower(base, exp):
    """
    :param base: int or float
    :param exp: int >= 0
    :return: int or float, base^exp
    """
    result = 1
    if exp <= 0:
        return 1

    return base * recurPower(base, exp - 1)


a = recurPower(9, 3)
print(a)

