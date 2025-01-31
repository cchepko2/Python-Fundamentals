'''
Creating formatted strings
'''

num1 = 5
num2 = 7

message = "num1 + num2 ="

# A formatted string is preceded by an 'f', varibles and expressions
# can be enclosed in {} braces
print(f"num1 + num2 = {num1+num2}")

print(f"{num1} + {num2} = {num1+num2}")
# The following statement is a shortcut for the above statement
print(f"{num1+num2=}")


name = input("Please enter your name: ")

# These two print statements have the same output
print(f"Hello {name}!") # A formatted print
print("Hello " + name + "!") # joining 3 strings by adding them