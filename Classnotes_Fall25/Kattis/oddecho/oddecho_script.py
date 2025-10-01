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

print("Enter number of words: ", file=sys.stderr)
num_words = int(input())

'''
Here are 3 solutions:
'''

for i in range(1, num_words+1):
    word = input()
    if(i%2 == 1):
        print(word)

for i in range(num_words):
    word = input()
    if((i+1)%2 == 1):
        print(word)

i = 1
while(i <= num_words):
    word = input()
    if(i%2 == 1):
        print(word)
    i += 1
