#! /usr/bin/python

x = 0
balance = 4773
annualInterestRate = 0.2
mir = annualInterestRate/12.0


def totalInterests(x):
    total_interests = 0
    new_balance = balance
    for month in range(12):
        interests = (new_balance - x) * mir
        new_balance = (new_balance - x) * (1 + mir)
        total_interests += interests
    return total_interests


while 12 * x < totalInterests(x) + balance:
    x += 10

print("Lowest Payment: %s" % x)
