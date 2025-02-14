'''
Program: Kattis Problem - 
    https://open.kattis.com/problems/addtwonumbers
A Program that inputs two numbers, adds them,
and prints the result.
'''

# defining a function that take two parameters, or arguments
# as input
# returns the output

import sys
import add_two

def main():
    print_output = print("Enter two numbers separated by a space: ", file=sys.stderr)
    print(f"{print_output=}")
    # Python 3
    line = input()
    a, b = line.split()
    a = int(a)
    b = int(b)

    #assert( add_two(1,1) == 2 )

    a_plus_b = add_two.add_two(a ,b)
    print(a_plus_b)

    print(f"{a=}, {b=}")

if(__name__ == "__main__"):
    main()