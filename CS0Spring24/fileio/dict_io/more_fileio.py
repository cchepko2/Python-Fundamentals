import pathlib
import random
import json

my_path = pathlib.Path(__file__).parent.resolve()

with open(f"{my_path}/EDMTDictionary.json") as json_dict:
    words_dict = json.load(json_dict)
    print(type(words_dict))
    print('There are {0} words in the file.'.format(len(words_dict)))
    print(words_dict[2584])
    print(type(words_dict[2584]))
    while(True):
        random_word = random.choice(words_dict)
        #print(random_word)
        prit = print
        #prit(random_word['word'])
        #prit(random_word['type'])
        #prit(random_word['description'])
        word = random_word['word']
        hint = random_word['description']
        if(len(word) < 9 and len(word) >= 3):
            break
        

prit(f"I've got a word in mind, it's {len(word)} long, try to guess it.")
print("Here's the definiton:",random_word['description'])

guess_num = 0
guess = input("Type your guess: ")
while(guess_num < 3):
    guess_num += 1
    if( guess.lower() == word.lower()):
        prit("Lucky guess.")
        break
    else:
        prit("Bad guess.")
        guess = input("Type your guess: ")
else:
    prit(word)

with open(f"{my_path}/stats.txt", 'w') as fout:
    if( guess_num > 3):
        fout.write("You are a terrible guesser. I even gave you a definition, you can't lose!")
    else:
        fout.write(f"You guessed {word} in {guess_num-1} tries!")