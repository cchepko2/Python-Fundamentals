'''
Program: Kattis Problem - 
    https://open.kattis.com/problems/addtwonumbers
A Program that inputs two numbers, adds them,
and prints the result.
'''

# defining a function that take two parameters, or arguments
# as input
# returns the output

def add_two(num1, num2):
    sum = num1+num2
    return sum

# Python 3
line = input()
a, b = line.split()
a = int(a)
b = int(b)

assert( add_two(1,1) == 2 )

a_plus_b = add_two(a ,b)
print(a_plus_b)