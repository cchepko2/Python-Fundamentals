number = 1025

stuff = (17, "Corin", number)
l_stuff = [17, "Corin", number]

print(stuff)
print(l_stuff)

number = 15

print(stuff)
print(l_stuff)

print(range(10))
print(tuple(range(10)))
print(list(range(10)))

numbers = input("Enter numbers separated by a space: ")
numbers = map(int, numbers.split())
print(numbers)
# map is a promisary function, it returns a map object
# need to use a list or tuple constructor to get the values

numbers = list(numbers)
print(numbers)

old_nums = numbers
numbers.sort()
print(numbers)
print(old_nums)

empty = []
empty = list() # does same thing as previous statement, creates empty list
print(type(empty))