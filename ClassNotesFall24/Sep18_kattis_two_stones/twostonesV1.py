'''
Author: Corin Chepko
Date: 9/19/24
Program Info: kattis problem - https://open.kattis.com/problems/twostones
Algorithm Steps:
    input a number
    convert to int
    if( even ):
        print("Bob")
    else:
        print("Alice")
'''

#import art

def main():
    #print(art.card1)
    #print(art.__name__)

    stones = int(input())

    if(stones%2 == 0):
        answer = "Bob"
    else:
        answer = "Alice"

    print(answer)


if __name__ == "__main__":
    main()