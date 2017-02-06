#! /usr/bin/python


def biggest(a_dict):
    """
    Return the key of the longest list contained in a dictionary
    :param aDict: Dictionary of lists
    :return: Key of the longest list
    """
    bg_key = None
    bg_length = -1
    for key in a_dict:
        if len(a_dict[key]) > bg_length:
            bg_key = key
            bg_length = len(a_dict[key])
    return bg_key


animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')


print(biggest(animals))
