pattern = 'bob'
count = 0
flag = True
start = 0
while flag:
    a = s.find(pattern, start)
    if a == -1:
        flag = False
    else:
        count += 1
        start = a + 1

print('Number of times bob occurs is: ' + str(count))