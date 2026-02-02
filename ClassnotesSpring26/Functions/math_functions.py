import math
import random
import time
import string

print(math.pi)
print(math.e)

print(1000000000000000000000000000000000/math.inf)

print(math.cos(math.radians(30)))
print(math.sin(math.radians(30)))

# If we want the same set of random number, use the same seed
random.seed(0)
# returns a number from 0 to 1
print(random.random())
# return a number from input a to b
a = 0
b = 10
print(random.randint(a, b))

loc_time = time.localtime()
print(loc_time)
print(loc_time.tm_isdst)

print(string.ascii_letters)