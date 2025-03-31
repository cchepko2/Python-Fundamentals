import copy

names = ["Corin", "Jon", "Rose", "Alice", "Bob"]
names_alias = names

# Two ways to make a shallow copy
names_shallow_copy = names[:]
names_shallow_copy = names.copy()

names.sort()
print(names)
print(names_alias)
print(names_shallow_copy)

print(names is names_alias)
print(names is names_shallow_copy)

list_ages_and_names = [20, 25, 22, 44, 35, 50, names]

#make a shallow copy of list_ages_and_names
list_a_and_n_2 = list_ages_and_names.copy()
list_a_and_n_3_deep_copy = copy.deepcopy(list_ages_and_names)
names_alias[3] = "Kelly"
list_ages_and_names[0] = 999999999
print(list_ages_and_names)
print(list_a_and_n_2)
print(list_a_and_n_3_deep_copy)