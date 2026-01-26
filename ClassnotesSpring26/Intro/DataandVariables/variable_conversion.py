'''
Practice creating and converting variables.
'''

int_number = 5
print( type(int_number) )
print(int_number)
print(f'{int_number=}')

# Convert int_number into a string and store into a variable
# call str_number
str_number = str(int_number)
print( type(str_number) )
print(str_number)
print(f'{str_number=}')
print('str_number=', str_number)

# Create a string variable containing a new_line character
new_str = "H\tel\nlo!"
print(new_str)

# the print function automatically adds a new_line character
# That can be changed using the end= argument
print("Without a newline.", end='!')
print("More stuff on the same line.")
print("This will be on a new line.")

print("This solution\r is bonkered!")

