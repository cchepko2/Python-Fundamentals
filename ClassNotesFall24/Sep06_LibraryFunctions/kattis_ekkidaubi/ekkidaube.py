'''
Authour: Corin Chepko
Date: 9/6/24
Program: kattis problem - https://open.kattis.com/problems/ekkidaudi
Algorithm:
    input first line
    use .split('|') on line to split into two strings, word1a, word1b
    input second line
    use .split('|') method on line2 tp split into another two strings, word2a, word2b
    print(word1a+word1b + word2a+word2b)
'''

import sys

print("Enter two words separated by a '|': ", file=sys.stderr)
word1a, word1b = input().split('|')
#print(word1a, word1b)

print("Enter two more words separated by a '|': ", file=sys.stderr)
word2a, word2b = input().split('|')
#print(word2a, word2b)
print(word1a+word2a, word1b+word2b)