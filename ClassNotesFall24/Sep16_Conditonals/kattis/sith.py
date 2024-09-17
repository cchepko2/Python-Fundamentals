'''
Author: Corin Chepko
Date: 9/16/24
Program: kattis problem - https://open.kattis.com/problems/sith
Algorithm Steps:
    input name
    input and convert integer a
    input and convert integer b
    input and convert a_minus_b
    if( a-b is positive):
        print VEIT EKKI
    else:
        if( a_minus_b is negative):
            print JEDI
        if( a_minus_b is positive):
            print SITH
'''

def main():
    name = input()
    a = int(input())
    b = int(input())
    a_minus_b = int(input())

    print(a,b,a_minus_b)

    answer = ""

    if( a-b >= 0):
        answer = "VEIT EKKI"
    else:
        if( a_minus_b < 0):
            answer = "JEDI"
        else:
            answer = "SITH"
    
    print(answer)



main()