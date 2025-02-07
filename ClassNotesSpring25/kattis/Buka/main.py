'''
Corin Chepko
2/7/25
Program: Kattis Prblem - https://open.kattis.com/problems/buka
Algorithm Steps:
    collect 3 lines of input:
        input first line into variable a
        input operator_character
        input third line into variable b

    print eval(a+operator_character+b)
'''

import sys

a = input()
operator = input()
b = input()

# Using the "file=sys.stderr", which requires an import sys, means the output
# goes to "error output" which is ignored by kattis
print(f"{a+operator+b=}", file=sys.stderr)

print(eval(a+operator+b))