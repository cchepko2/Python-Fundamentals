'''
Using the split() method of strings
'''
# split the string, using space as separater, 
# into multiple variables
numbers = "1 2 3 4 5"
num1, num2, num3, num4, num5 = numbers.split()
print(num1+num2+num3, num4, num5)

# split the string, using space as separater, 
# into multiple variables
numbers = "1,2,3,4,5"
num1, num2, num3, num4, num5 = numbers.split(sep=',')
print(num1+num2+num3, num4, num5)

# split the string, using space as separater, 
# into multiple variables
numbers = "1 2 3 4 5"
num1, num2, num3, num4, num5 = numbers.split()
print(num1+num2+num3, num4, num5)


numbers = "1 2 3 4 5"
numbers_split = numbers.split()
print(numbers_split)
num1, num2, num3, num4, num5 = numbers_split
# to use these numbers, we need to convert them
num1 = float(num1)
num2 = float(num2)
num3 = float(num3)
num4 = float(num4)
num5 = float(num5)
print(num1+num2+num3, num4, num5)

# a better way to convert all at once
# use the "map" function
numbers = "1 2 3 4 5"
numbers_split = numbers.split()
print(numbers_split)
numbers_split = list(map(float, numbers_split))
print(numbers_split)

# I know there are 5 elements in this list,
# I unpack them into individual variables
num1, num2, num3, num4, num5 = numbers_split
print(num1+num2+num3, num4, num5)

# All at once
num1, num2, num3, num4, num5 = list(map(float,input("Please enter five numbers separated by a space").split()))
print(num1+num2+num3, num4, num5)