import os
import random
script_dir = os.path.dirname(__file__)

with open(script_dir + '\\words.txt') as fin:
    words = fin.readlines()
    print(words)
    new_words = list(map(str.strip, words))
    print(new_words)
    random_word = random.choice(words).strip()

print(random_word)