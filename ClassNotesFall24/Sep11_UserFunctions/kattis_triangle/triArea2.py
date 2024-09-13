'''
Author: Corin Chepko
Date: 9-11-2024
Program: Kattis problem - https://open.kattis.com/problems/triarea
Algorithm Steps:
    input two numbers, height and base, and convert to floats
    compute area
    print area
'''

def squareArea(length, width):
    area = length*width
    perimeter = 2*(length+width)

    mini_a = 1
    mini_b = 1
    mini_area, mini_perimeter = squareArea(mini_a, mini_b)

    print("MiniStuff Square Area = {} and Perimeter = {}".format(mini_area, mini_perimeter))

    return area, perimeter

h,b = input().split()
h = int(h)
b = int(b)

area, perimeter = squareArea(h, b)

print(area)