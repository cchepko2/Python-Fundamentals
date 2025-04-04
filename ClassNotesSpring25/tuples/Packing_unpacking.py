'''Tuple packing and unpacking. Same as lists'''

import math

def circle_area_perimeter(radius: float) -> float:
    return 2*math.pi*radius, 2*math.pi*radius**2

def main():
    radius = float(input("Enter a radius: "))
    return_val = circle_area_perimeter(radius)
    print(f"{return_val=}")
    return_val = list(return_val)
    return_val[0] = "something else"
    print(f"{return_val=}")
    return_val = tuple(return_val)
    print(f"{return_val=}")
    perimeter, area = return_val
    print(f"The perimeter of the circle is {perimeter}, and the area is {area}.")

if __name__ == "__main__":
    main()
