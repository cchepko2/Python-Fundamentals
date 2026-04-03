'''
Corin Chepko
kattis problem - https://open.kattis.com/problems/morsecodepalindromes
Algorithm:
    input string
    convert string to morse
    check if morse code string equals itself reversed
'''

import string

MORSE_CODE_DICT = {
    'A': '.-',     'B': '-...',   'C': '-.-.',   'D': '-..',    'E': '.',      'F': '..-.',
    'G': '--.',    'H': '....',   'I': '..',     'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',    'P': '.--.',   'Q': '--.-',   'R': '.-.',
    'S': '...',    'T': '-',      'U': '..-',    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',   '1': '.----',  '2': '..---',  '3': '...--',  '4': '....-',
    '5': '.....',  '6': '-....',  '7': '--...',  '8': '---..',  '9': '----.',  '0': '-----'}

def main():
    phrase = input()
    
    if phrase == '':
        answer = 0
    else:
        morse_code = translate(phrase)
        if morse_code == morse_code[::-1] and morse_code != '':
            answer = 1
        else:
            answer = 0
    
    print(answer)

def translate(phrase: str) -> str:
    morse_code = ""
    for letter in phrase.upper():
        if letter.isalnum() and letter in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[letter]
    return morse_code



if __name__ == '__main__':
    main()