list_of_numbers = [1, 2, 3, 4]
print(f"{list_of_numbers=}")

list_of_numbers.clear()
print(f"{list_of_numbers=}")

list_of_numbers.append(1)
print(f"{list_of_numbers=}")

list_of_numbers.extend([1, 2, 4, 99])
print(f"{list_of_numbers=}")

list_of_numbers.pop(1)
print(f"{list_of_numbers=}")

print("Number of 1's =", list_of_numbers.count(1))

list_of_numbers.reverse()
print(f"{list_of_numbers=}")

reversed_list = list_of_numbers[::-1]
print(reversed_list)

list_of_numbers.insert(2, 1001)
print(f"{list_of_numbers=}")
list_of_numbers.sort()
print(f"{list_of_numbers=}")

list_of_numbers.sort(reverse=True)
print(f"{list_of_numbers=}")

#list_of_str_numbers = input("Enter some numbers separated by a space: ").split()
list_of_str_numbers = ['20', '1001', '6', '8', '30']

list_of_str_numbers.sort()
print(f"{list_of_str_numbers=}")

# if I want to sort numerically, I need to convert the list
# to a list of numbers
num_list = []
for item in list_of_str_numbers:
    num_list.append(int(item))
print(f"{num_list=}")

# alternative way to convert to ints, using map function
num_list = map(int, list_of_str_numbers)
print(f"{num_list=}")
# need to apply list function to a map object to get actual values
num_list = list(num_list)
print(f"{num_list=}")

num_list.sort()
print(f"{num_list=}")

