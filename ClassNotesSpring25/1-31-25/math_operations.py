'''
Practice with basic math operations in Python
'''

num1 = 4
num2 = 4
num3 = 6
num4 = 7

# printing use the 'sep=' argument
# by default, print separates arguments using a space
print(num1,num2,num3,num4)

# if I want to use a different character to separate value,
# I can define it using sep='<character>'
print(num1,num2,num3,num4, sep=',')

# if I want two print statments to be separted by something
# other than a newline character, '\n', I can use end='<character>'
print(num1,num2,num3,num4, end='_')
print(num1,num2,num3,num4)

# reverts back to newline default after print
print(num1,num2,num3,num4)


# Math Operations

# squaring a number
print(f"{num1**2=}")

# cubing a number
print(f"{num1**3=}")

# sqrt of a number
print(f"{num1**(1/2)=}")
# This is NOT a square root
print(f"{num1^2=}")

# print the binary representation of num1
print(bin(num1))
print(bin(2))
print(bin(6))
# octal
print(oct(num1))
#hexadecimal base 16
print(hex(num1))
#hexadecimal base 16
print(hex(15))