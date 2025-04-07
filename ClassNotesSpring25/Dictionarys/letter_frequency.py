'''
Corin Chepko
4/7/25
Counting frequency of letters in a string.
Algorithm Steps:
    input a string
    create an empty disctionary
    for each character in the string:
        convert to lower case
        if key=charater doesn't exist:
            add a new key with a value of 1
            ex: letters_dict['key'] = 1
        if key=character does exist:
            increment key-value by 1
            ex: letters_dict['key'] += 1
        print dictionary key and values in alphabetical order            
'''

import string

def count_letters(phrase: str) -> dict:
    '''
    Takes a string input, return a dictionary with key-value
    pairs of letter:frequency
    '''

    phrase = list(phrase.lower())
    phrase.sort()

    letters_dict = {}

    for letter in phrase:

        # only want to count letters, not punctuation or spaces
        if letter in string.ascii_lowercase:

            if letter not in letters_dict:
                letters_dict[letter] = 1
            else:
                letters_dict[letter] += 1
    
    return letters_dict

def main():
    phrase = input("Input a string: ")
    letters_dict = count_letters(phrase)
    
    for key,value in letters_dict.items():
        print(f"{key} {value}")


if __name__ == '__main__':
    main()