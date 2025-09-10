import math
import time

# print is a fruitless function and returns 'None'
return_val = print("Hello World!")

print(f"{return_val=}")

# math.sin is a fruitful function and returns the value of sin(data)
return_val = math.sin(30*math.pi/180)
print(f"{return_val=}")
time.sleep(2)
print(f"{return_val=}")

side_b = 5

# AVOID this unless you know what you are doing!
side_a = input

side_c = side_a + side_b
#side_a = input("Enter stuff:")



