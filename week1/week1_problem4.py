#! /usr/bin/python

s = list('swodnqweodqwoendwq')


def analyze_list(l):
    counts = {}

    for item in l:
        if item in counts:
            counts[item] += counts[item]
        else:
            counts[item] = 1

    return counts

q = analyze_list(s)
print(q)



