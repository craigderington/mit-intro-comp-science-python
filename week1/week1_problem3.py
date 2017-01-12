#! /usr/bin/python

substr = ""
long = ""
for i in range(len(s)):
    if len(long) > 0:
        if long[-1] <= s[i]:
            long += s[i]
        else:
            long = s[i]
    else:
        long = s[i]
    if len(long) > len(substr):
        substr = long
print('Longest substring is alphabetical order is: ' + str(substr))


