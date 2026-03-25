'''
Corin Chepko
3/25/26
Katiis Problem: piglatin - https://open.kattis.com/problems/piglatin
'''


import sys

def main():

    #for message in sys.stdin:
        #print("Enter a message: ", file=sys.stderr)
        #message = input()       
    while(True):
        try:
            message = input()
        except EOFError:
            break
        
        translated = ""

        for word in message.split():
            new_word = solution(word)
            translated += new_word + ' '

        print(translated)

def solution(word):
    vowels = 'aeiouy'
    
    if word[0] in vowels:
        return word + 'yay'
    else:
        index = 0
        for c in word:
            if c in vowels:
                new_word = word[index:] + word[0:index] + 'ay'
                return new_word
                break
            index+=1

def test():
    assert solution('pig') == 'igpay'
    assert solution('Corin') == 'orinCay'

    print('All tests passed!', file=sys.stderr)


if __name__ == '__main__':
    test()
    main()
