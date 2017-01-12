# /usr/bin/python

print([x**3 for x in range(15)])
x = int(input('Please enter an integer: '))
ans = 0

while ans**3 < x:
    ans += 1

if ans**3 != x:
    print('{} is not a perfect cube'.format(x))
else:
    print('The cubed root of {} is {}'.format(x, ans))


