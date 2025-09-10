'''
Programmer: Corin Chepko
Date: 9/5/25
Program: Kattis Problem - https://open.kattis.com/problems/ekkidaudi
Algorithm Steps:
    input line1
    input line2

'''

import sys

print("Enter first line: ", file=sys.stderr)

line1 = input()
line2 = input()

line1a, line1b = line1.split('|')
line2a, line2b = line2.split('|')

print(line1a+line2a, line1b+line2b)