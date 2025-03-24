'''
Create lists
'''

import string

def add_all(numbers):
    '''
    Takes a list of numbers and returns the sum
    '''
    sum=0
    for num in numbers:
        sum += num
    
    return sum

alist = [] # Creates an empty list
blist = list() # Also creates an empty list

print(f"{alist=}")
print(f"{blist=}")

print(string.ascii_letters)
acsi_list = list(string.ascii_letters)
print(f"{acsi_list=}")

# lists with elements of different types
list3 = ["hello", 2.0, 10, [10, ('hi', 'world'), 3.5], (1, 'uno')]
print(list3[0]) # Print the first item of the list
print(list3[0][2]) # Print the 3rd character of the first item of the list

print(list3[3]) # Print the fourth item of the list
print(list3[3][1][0]) # Print the first item of 2nd item in the tuple of the 4 item in the list

list_numbers = list(range(1,20)) # Create a list of numbers from 1 to 19
print(f"{list_numbers=}")
print(f"{add_all(list_numbers)=}")

#We could have used the sum() function...
print(f"{sum(list_numbers)=}")

# A list is mutable...values can be modified
list_numbers[1] = 99999.9999
print(f"{list_numbers=}")



