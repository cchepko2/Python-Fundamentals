'''
Corin Chepko
10/1/30
Program: Kattis Problem - https://open.kattis.com/problems/oddecho
Algorithm Steps:
    input number of words to read, N, from 1 to N, convert to int
    for each input:
        if index is odd (index%2 == 1):
            print(currrent word)
'''

import sys

def print_word(index: int) -> bool:
    if(i%2 == 1):
        return True
    else:
        return False

print("Enter number of words: ", file=sys.stderr)
num_words = int(input())

for i in range(1, num_words+1):
    word = input()
    if (print_word(i)):
        print(word)