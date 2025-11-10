import os
import random
script_dir = os.path.dirname(__file__)

with open(script_dir + '\\dict-words.txt') as fin:
    words = fin.readlines()
    random_word = random.choice(words).strip()

    print(f"The dictionary has {len(words)} words.")
    print(f"Random word is: {random_word}")