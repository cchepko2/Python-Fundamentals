print(range(10))
numbers = list(range(10))
print(f"{numbers=}")


name = "Stacy"
condition = ('S' in name)
print(condition)
condition = ('s' in name)
print(condition)

print(len(name))

# iterate through a string with indices
for i in range(len(name)):
    print(name[i], end=' ')
print()
print(i)

# iterate by value in a container
for character in name:
    print(character, end=' ')
print()
print(character)

number = "10"

while True:
    user_input = input("Enter a floating-point number: ")
    try:
        float_value = float(user_input)
        print(f"Valid float entered: {float_value}")
        break  # Exit the loop if conversion is successful
    except ValueError:
        print("Invalid input. Please enter a valid floating-point number.")


