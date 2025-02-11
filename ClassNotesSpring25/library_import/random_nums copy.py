'''
A program to make random numbers and select random
items from a list
'''

# first we need to import the library
# for this import, we will shorten random to r
import random as r
from random import randint

# imported randint directly, so don't need "r.
random_number = randint(1, 10)
print(f"{random_number=}")

random_number = r.random()
print(f"{random_number=}")

words = ["Apple", "Bannana", "Mango","Brussel Sprouts"]
random_word = r.choice(words)
print(f"{random_word=}")