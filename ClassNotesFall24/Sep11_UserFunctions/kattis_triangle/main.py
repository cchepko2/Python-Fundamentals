'''
Author: Corin Chepko
Date: 9-11-2024
Program: Kattis problem - https://open.kattis.com/problems/triarea
Algorithm Steps:
    input two numbers, height and base, and convert to floats
    compute area
    print area
'''

import sys

def triArea(height, base):
    return height*base/2

def testing():
    height = 0
    base = 0
    assert(triArea(height, base) == 0)
    assert(triArea(1, 1) == 0.5)
    assert(triArea(2,2) == 2)

    print("All tests passed!", file=sys.stderr)

testing()

h,b = input().split()
h = int(h)
b = int(b)

area = triArea(h, b)

print(area)