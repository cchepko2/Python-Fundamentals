'''
A program to make random numbers and select random
items from a list
'''

# first we need to import the library
import random


random_number = random.randint(1, 10)
print(f"{random_number=}")

random_number = random.random()
print(f"{random_number=}")

words = ["Apple", "Bannana", "Mango","Brussel Sprouts"]
random_word = random.choice(words)
print(f"{random_word=}")