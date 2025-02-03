'''
Combining statements
'''

number = input("Please enter a number: ")
number = float(number)

print(number)

# Frequently combine statements within statements
number2 = float(input(f"Please enter a number above {number}: "))
print(number2)