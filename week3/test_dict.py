def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.
    returns: int, how many values are in the dictionary.
    '''
    counter = 0
    for e in aDict:
        counter += len(aDict[e])

    return counter


# Test Code
animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

howMany(animals)