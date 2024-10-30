import json
import os
import random
import pathlib

my_path = pathlib.Path(__file__).parent.resolve()

file_name = 'words.dict'
file_name = f'{my_path}/{file_name}'

if os.path.exists(file_name):
    with open(file_name) as json_dict:
        words_dict = json.load(json_dict)
        print(type(words_dict))
        print('There are {0} words in the file.'.format(len(words_dict)))
        print(words_dict[2584])
        print(type(words_dict[2584]))
        
        choice = random.choice(words_dict)
        print('{}\n{}\n{}'.format(choice['word'], \
            choice['type'], choice['description']))
else:
    print(f"Cannot open the file {file_name}.")