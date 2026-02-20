'''
Corin Chepko
2/18/26
Program: Calculate area and perimeter of a triangle, given the base and height
Kattis link - https://open.kattis.com/problems/triarea
Algorithm:
    input the height and base separated by a space
    convert to floats
    calculate area and perimeter
    print area
'''

import math

height, base = input().split()
height = float(height)
base = float(base)
area = base*height/2
perimeter = base+height+math.hypot(base, height)
print(area)