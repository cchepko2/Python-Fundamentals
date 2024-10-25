'''
Author: Corin Chepko
Date: 10/23/24
Program info - Kattis problem - https://open.kattis.com/problems/morsecodepalindromes
Alogorithm Steps:
    input a phrase
    convert characters to morse code, ignoring spaces
    check if morse_string == morse_string[::-1]
    if(True):
        print(1)
    else:
        print(0)
'''

import sys
import string

# Dictionary representing the morse code chart
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
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def translate(phrase):
    phrase = phrase.upper()
    translated = ""
    if phrase != "":
        for character in phrase:
            #if character in MORSE_CODE_DICT: #requires dictionary 
                                        # not to have non-alphanumeric characters
            if character in (string.ascii_uppercase+string.digits):
                translated += MORSE_CODE_DICT[character.upper()]
        
        return translated    
    else:
        return translated

def test():
    assert translate("SOS") == "...---..."
    assert translate("Hello") == "......-...-..---"

    print("All tests passed!", file=sys.stderr)


def main():
    phrase = input()

    translated = translate(phrase)
    if( translated != ""):
        if( translated == translated[::-1] and translated != ""):
            print(1)
        else:
            print(0)
    else:
        print(0)

if __name__ == '__main__':
    test()
    main()