'''
Some examples of list comprehension
'''

# create a list of x**2 for x in range(1,10)
x_squared = []
for x in range(1,10):
    x_squared.append(x**2)

print(x_squared)

x_squared2 = [x**2 for x in range(1,10)]
print(x_squared2)

# create a list of x**2 for x in range(1,10) if x is even
x_squared = []
for x in range(1,10):
    if x%2 == 0:
        x_squared.append(x**2)

print(x_squared)

x_squared2 = [x**2 for x in range(1,10) if x%2 == 0]
print(x_squared2)

tuple_list = [('THE', 'the', 3),
 ('QUICK', 'quick', 5),
 ('BROWN', 'brown', 5),
 ('FOX', 'fox', 3),
 ('JUMPS', 'jumps', 5),
 ('OVER', 'over', 4),
 ('THE', 'the', 3),
 ('LAZY', 'lazy', 4),
 ('DOG', 'dog', 3)]

tuple_list.sort()
print(tuple_list)
