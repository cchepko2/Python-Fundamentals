'''
Corin Chepko
4.7.25
Kattis Problem: https://open.kattis.com/problems/morsecodepalindromes
Algorithm Steps:
    input phrase
    convert letters in phrase to list of morse strings
    join morse strings: ''.join(morse_string)
    test if string is a palindrome 
        (check if string sliced backwards == string)
    print(1 for True, 0 for False)
'''

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----'}

import sys
import string

def translate(phrase: str) -> str:
    translated = ''

    for letter in phrase:
        if letter in MORSE_CODE_DICT:
            #translated.append(MORSE_CODE_DICT[letter])
            translated += MORSE_CODE_DICT[letter]


    return ''.join(translated)

def main():
    print("Enter a phrase: ", file=sys.stderr)
    phrase = input().upper()

    translated = translate(phrase)
    print(translated, file=sys.stderr)
    print(translated[::-1], file=sys.stderr)

    reversed = translated[::-1]
    if (translated == reversed) and (translated != ''):
        print(1)
    else:
        print(0)

if __name__ == '__main__':
    main()