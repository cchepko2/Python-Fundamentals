import copy

inner_list = [99, 99, 99]
list1 = [1, 2, 3, 4, 5, inner_list]

list1_copy = list1

list1_deepcopy = copy.deepcopy(list1)

print(list1)
print(list1_copy)
print(list1_deepcopy)

inner_list[0] = "Hello"

print(list1)
print(list1_copy)
print(list1_deepcopy)

inner_list[-1] = "World"
print(list1)
print(list1_copy)
print(list1_deepcopy)