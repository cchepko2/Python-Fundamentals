random_word = "skiing"

stage1 = '''
|=====|
|     O
|     |
|
|
==============
'''

print("Random word is ")
for c in random_word:
    print(c, end = ' ')

guess = input("\n\nGuess a letter\n")
if(not len(guess) == 1 or not guess.isalpha()):
    print("Bad human")
    quit()


print()
if guess in random_word:
    print("You guessed a letter!")
else:
    print(stage1)

for c in random_word:
    if(guess == c):     # if guess matches character, print it
        print(c, end=' ')
    else:
        print('_', end=' ')

print()