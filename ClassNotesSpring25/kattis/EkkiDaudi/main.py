'''
Corin Chepko
2/7/25
Kattis Problem - https://open.kattis.com/problems/ekkidaudi
Algorithm Steps:
    input first line
    input second line

'''

import sys

# Use file=sys.stderr so print is ignored by Kattis
#print("Enter first line: ", file=sys.stderr)

line1a, line1b = input().split('|')
line2a, line2b = input().split('|')

print(line1a+line2a + ' ' + line1b+line2b)