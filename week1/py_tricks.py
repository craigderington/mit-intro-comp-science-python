#! /usr/bin/python
from collections import Counter

x = Counter({'a': 1, 'b': 2})
y = Counter({'b': 3, 'c': 4})

z = x + y
print(z)
