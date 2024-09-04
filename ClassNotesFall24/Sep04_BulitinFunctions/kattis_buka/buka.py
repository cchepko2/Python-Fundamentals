'''
Author: Corin Chepko
Date: 9/4/24
Program: kattis problem Buka - https://open.kattis.com/problems/buka
Algorithm:
    input first number
    input character
    input second number
    combine strings and use eval() to evaluate
'''

num1 = input()
operator = input()
num2 = input()
line = num1 + operator + num2
#print(line)
print( eval(line) )