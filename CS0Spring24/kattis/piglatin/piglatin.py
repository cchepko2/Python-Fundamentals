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