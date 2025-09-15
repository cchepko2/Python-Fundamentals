def rectangle_calc(length, width):
    perimeter = 2*length + 2*width
    area = length*width
    return area, perimeter

# Collect two pieces of input and split 
l_and_w = input("Enter the length and width separated by a space: ").split()
print(f"{l_and_w=}")

# Separate input value into two variables (assuming the user inputs two things)
length, width = l_and_w
length = float(length)
width = float(width)

# Do it all at once, map the "float" function onto each element returned from the .split() statement
length, width = map(float, input("Enter the length and width separated by a space: ").split())

print(f"{length=}", f"{width=}")

area, perimeter = rectangle_calc(length, width)

print(f"Rectangle area and perimeter: {area}, {perimeter}")

