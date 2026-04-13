'''
Read words from a file into a list
'''

import os
import random

filename = 'dict-words.txt'
script_dir = os.path.dirname(__file__)

full_filename = script_dir + "\\" + filename

with open(filename) as fin:
    word_list = fin.readlines()
    #print(word_list)
    print(f"There are {len(word_list)} words.")

word_of_the_day = random.choice(word_list).strip()
print(f'{word_of_the_day=}')