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
import sys

def main():
    height, base = input().split()
    height = float(height)
    base = float(base)

    area = tri_area(height, base)

    print(area)


def tri_area(h, b):
    area = b*h/2
    #perimeter = b+h+math.hypot(b, h)
    return area#, perimeter

def test():
    assert(tri_area(1,1) == 0.5)
    # With the file=sys.stdin, the ouput goes to an error console and is ignored by kattis
    print("All tests passed!", file=sys.stderr)

test() # If my test passes, nothing happens
main()