"""
Demo of math library functions
"""

import math

degrees = 30

print(math.pi)
radians = degrees*math.pi/180
print(radians)

radians = math.radians(degrees)
print(radians)

result = math.sin(radians)

print(result)

print(math.log2(4))  # log2(4) = 2