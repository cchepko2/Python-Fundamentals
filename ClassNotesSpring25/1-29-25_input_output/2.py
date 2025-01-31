'''
Variable Type and converting
'''

a = 3  # an int
b = 5.0 # a float
c = '6' # a string that can be coverted to int or float
d = '7.7' # a string can only be converted to float

print(type(a))
print(type(b))
print(type(a-b))

print(a/2)

print(int(c)/2)

# convert d to float for an operation, but d remains a string
print(float(d)/2)
print(type(d))

# convert d into a float
d = float(d)
print(type(d))
print(d/2)

str_b = str(b)
print(b)
print(str_b)