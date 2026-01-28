name = input("Enter your name: ")

print("Nice to meet you,", name)

#input does not need to show text:
data = input()

# input some numbers and do math operations
pi = 3.14159
radius = input("Enter the radius of your circle and I'll calculate the area: ")
print(f'{radius=}')
# Convert radius into a float
radius = float(radius)
area = pi*radius**2
print("Area =", area)
# Composition: combining into one line
print("Area =", float(radius)**2*pi)
