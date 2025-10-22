import math

def circle(radius):
    area = math.pi*radius**2
    circumference = math.pi*2*radius

    # returning a tuple (items separated by commas)
    return area, circumference

print("Enter radius: ")

radius = float(input())

answer = circle(radius)
print(f"{answer=}")

container_of_stuff = (answer, "Corin", 100.99999, ["Things", "in", "a", "list"])
print(f"{container_of_stuff=}")
print(f"Length of container_of_stuff = {len(container_of_stuff)}")

answer = "A different answer"
print(f"{container_of_stuff=}")

print("Corin" in container_of_stuff)
print("Things" in container_of_stuff)

item_list = [100, "bottles of root beer."]
container_with_list = (answer, "Corin", 100.99999, item_list)
print(f"{container_with_list=}")

item_list[0] -= 1
print(f"{container_with_list}")

a=1
b=2
calc_val = [a+b]
print(f"{calc_val=}")
a = 99
print(f"{calc_val=}")





