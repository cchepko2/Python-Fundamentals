'''
Corin Chepko
2/1/36
Kattis Problem - Buka - https://open.kattis.com/problems/buka
Algorithm Steps:
    input an integer
    input a symbol
    convert to integer

'''

import sys

# Adding strings
print("Enter the first number: ", file=sys.stderr)
first_int = input()
print("Enter the math operator: ", file=sys.stderr)
symbol = input()
print("Enter the second number: ", file=sys.stderr)
second_int = input()

full_experession = first_int + symbol + second_int
print(eval(full_experession))
