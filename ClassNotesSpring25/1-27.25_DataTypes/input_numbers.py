'''
Program: Inputs some numbers to do mathmatical operations
'''

print("I'm going to ask for two numbers, then print the sum!")

# Collects input and tries to convert it into an integer all at once
number1 = int(input("Enter number 1: ")) 

number2 = input("Enter number 2: ")
number2 = int(number2) # convert number2 from a str to and int

print("Your numbers are:", number1, 'and', number2)

print("The sum is", number1+number2)