import json
import os
import random
import string
from urllib import request

def retrieve_page(url, file_name):
    """ Download the contents of a web page.
    """
    response = request.urlretrieve(url, file_name)

file_name = 'EDMTDictionary.json'
if os.path.isfile(file_name) != True:
    retrieve_page('https://github.com/eddydn/DictionaryDatabase/raw/master/EDMTDictionary.json', file_name)
else:
    print("Already have the dictionary")

with open("EDMTDictionary.json") as json_dict:
    words_dict = json.load(json_dict)
    #print(type(words_dict))
    #print('There are {0} words in the file.'.format(len(words_dict)))
    #print(words_dict[2584])
    #print(type(words_dict[2584]))
    
    #choice = random.choice(words_dict)
    #print(choice["word"])
    choice = "ard'wolf"
    punct_list = list(string.punctuation)
    print(punct_list)

    while( any(sub in choice for sub in punct_list) == True): #Found punctuation
        choice = random.choice(words_dict)['word']
    
    print(choice)

    #print('{}\n{}\n{}'.format(choice['word'], \
    #    choice['type'], choice['description']))