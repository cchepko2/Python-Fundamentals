'''
Programmer: Corin Chepko
Date: 10-17-25
Program: Kattis problem - Pig Latin - https://open.kattis.com/problems/piglatin
Algorithm Steps:
    read lines while lines to read:
        split line into words
        for each word:
            convert to piglatin:
                if word begins with consonent:
                    subtract the part before the first vowel, 
                    and add it to the end with an 'ay' attached
                if word begins with vowel:
                    add 'yay' to end of word

'''

import sys

def main():
    print("Enter a phrase to convert: ", file=sys.stderr)

    while(True):
        try:
            line = input()
        except EOFError:
            break

        if(line == ''):
            break

        words = line.split()

        ans = ''
        for word in words:
            converted = pig_translate(word)
            ans = ans + converted + " "

        print(ans)

def pig_translate(word: str) -> str:
    vowels = 'aeiouy'
    ans = ''
    for vowel in vowels:
        if word[0] in vowels:
          ans = word + 'yay'
          return ans
    
    index = 0
    while(word[index] not in vowels):
        index += 1
    ans = word[index::] + word[0:index] + 'ay'
    return ans

def test():
    assert pig_translate('i') == 'iyay'
    print("All tests passed!", file=sys.stderr)

if __name__ == '__main__':
    test()
    main()