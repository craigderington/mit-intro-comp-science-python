#! /usr/bin/python

def how_many(a_dict):
    """
    Count the number of items in a dictionary
    :param a_dict: a dictionary of lists
    :return: the sum of the number of values in the dict
    """
    count = 0
    for value in a_dict:
        count += len(a_dict[value])

    return count


animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')


print(how_many(animals))

