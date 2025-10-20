import math

def circle(radius):
    area = math.pi*radius**2
    circumference = math.pi*2*radius
    return area, circumference

print("Enter radius: ")

radius = float(input())

answer = circle(radius)
print(f"{answer=}")

container_of_stuff = (answer, "Corin", 100.99999, ["Things", "in", "a", "list"])
print(f"{container_of_stuff=}")

print("Corin" in container_of_stuff)

