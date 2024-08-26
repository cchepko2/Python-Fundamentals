# Corin Chepko
# 8/25/24

# Algorithm: 
# I'm inputting two numbers
# I will print the sum

first_num = input("Enter in a number: ")
print(type(first_num)) # After collecting first_num as a string, conver to int

first_num = int(first_num)
print(type(first_num))

second_num = int( input("Enter in a second number: ") )# Collect and convert second_num into an int in one line
print("Second_num type is ", type(second_num))

print(first_num+second_num)
