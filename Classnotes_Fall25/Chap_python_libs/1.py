'''
Some python libraries
'''

import math
import sys
import random
import time
import string

print(math.degrees(math.pi/4))
print(math.sin(math.radians(30)))

# To print to error console output (which is ignored by Kattis):
print("Hello Error World!", file=sys.stderr)

# Use a seed for the same random sets
#random.seed('Corin')
print(random.random()*10)
print(random.randint(1, 10))

words = ["Apple", "Orange", "Pineapple"]
print(random.choice(words))

print(time.localtime())
time_fields = time.localtime()

print(f"{string.ascii_letters=}")
print(string.punctuation)
print(string.hexdigits)
letter = 'A'
print(letter in string.digits)
