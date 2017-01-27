#! /usr/bin/python


def isIn(char, aStr):
    """
    Return boolean if a character is in a string of text
    :param char:
    :param aStr:
    :return: boolean True or False
    """

    if aStr == '':
        return False

    if len(aStr) == 1:
        return aStr == char

    mindex = len(aStr) // 2
    mchar = aStr[mindex]
    if char == mchar:
        return True

    elif char < mchar:
        return isIn(char, aStr[:mindex])

    else:
        return isIn(char, aStr[mindex + 1:])


a = isIn('c', 'cookies')
print(a)
