names = "Corin", "Sam", "Alice", "Jane", "Jhon"

print(names)

for name in names:  # traversing through items in a tuple
    print(name)

# 2 tuple methods:
# count
print(names.count("Corin"))

# index
print(names.index("Alice"))

print(names[1:])