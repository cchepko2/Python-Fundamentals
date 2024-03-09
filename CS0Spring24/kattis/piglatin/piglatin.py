import string

'''
Corin Chepko
3/6/24
Kattis problem: Piglatin https://open.kattis.com/problems/piglatin
Algorithm Steps:
    While reading lines in until end of file:
        separate the line in words
        for each word:
            convert to piglatin by:
                if word begins with consonant:
                    move all letters before vowel to end of word and add 'ay'
                else:
                    add 'yay' to end of word
            print piglatin line by joining words using join method
'''

def piglatin(word: str):
    '''
    Converts a word into piglatin and returns that string
    '''
    vowels = ['a','e','i','o','u']
    if(word[0] in vowels):
        word = word + 'yay'
    else:       #it begins with a consonant
        index = 0
        for c in word:
            if c in vowels: #found first vowel
                beg = word[0:index]
                word = word[index::] + beg + 'ay'
                break
            index+=1
    return word

while(True):
    try:
        phrase = input()
    except EOFError:
        break
    words = input().split()
    for word in words:
        translation = piglatin(word)
        print(translation, end=' ')
    print()

