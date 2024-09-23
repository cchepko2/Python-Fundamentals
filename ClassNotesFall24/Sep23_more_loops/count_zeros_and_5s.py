# solution 1
# converst positive integer into string and parse one character at a time
n = 12345505
n = str(n)
count0 = 0
count5 = 0
for c in n:
    if c == '0':
        count0 += 1
    elif c == '5':
        count5 += 1
print('There are {} zero(s) and {} five(s) digits in {}.'.format(count0, count5, n))