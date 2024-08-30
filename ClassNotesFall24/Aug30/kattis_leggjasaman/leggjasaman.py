'''
Author: Corin Chepko
Date: 8/30/24
Program: Kattis problem - leggjasaman - 
    https://open.kattis.com/problems/leggjasaman
Algorithm:
    input first number and convert to int
    input second number and convert to int
    print sum of numbers
'''

def solution(num1, num2):
    #print( num1 + num2) # print output
    return num1+num2

def test():
    num1 = 3
    num2 = 4
    assert(solution(num1,num2) == 7)

test()
arnar_cars = input() # collect input for first number
arnar_cars = int(arnar_cars)  # convert last input to an integer
hannes_cars = int(input()) # Same as above but all in one line
solution()