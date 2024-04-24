'''
Corin Chepko
4/24/24
Kattis problem: https://open.kattis.com/problems/morsecodepalindromes
Algorithm:
    input string
    for each char and digit:
        convert to morse equivalent
    check if translated == translated(backwards)
    if( palindrome)
        print(1)
    else
        print(0)
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
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

import string, sys

def solution(line):
    if line=='':
        return 0
    morse_code = []
    for char in line.upper():
        if char in string.ascii_letters or char in string.digits:
            morse_code.append(MORSE_CODE_DICT[char])
    
    morse_line = ''.join(morse_code)
    #print(morse_line)
    if(morse_line == ''):
        return 0
    if(morse_line == morse_line[::-1]):
        return 1
    else:
        return 0


def test():
    line = "sos"
    assert solution(line) == 1
    assert solution("123") == 0
    assert solution("racecar") == 0
    print("All tests passed!", file=sys.stderr)

def main():
    line = input()
    ans = solution(line)
    print(ans)

if __name__ == "__main__":
    test()
    main()