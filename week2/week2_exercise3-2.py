#! /usr/bin/python
print('Think of a number between {} and {}!'.format(low, high))

high = 100
low = 0
guessing = True

while guessing:
    # bisection search:  guess the midpoint between our current high and low guesses
    guess = (high + low) // 2
    print('Is your secret number {}?'.format(guess))
    pointer = input('Enter \'h\' to indicate the guess is to high. '
                    'Enter \'l\' if the guess is to low. '
                    'Enter \'c\' to indicate I guessed correctly.').lower()

    if pointer == 'h':
        high = guess
    elif pointer == 'l':
        low = guess
    elif pointer == 'c':
        guessing = False
    else:
        print('Sorry, I did not understand your input.')

print('Game over.  Your secret number was {}'.format(guess))
