'''
Python Class 2/21/25
Kattis Problem: https://open.kattis.com/problems/sith
Algorithm Steps:
    4 lines of input
    first line is Jedi or Sith name and can be discarded
    second line is an integer a
        input and convert to int
    third line is an integer b
        input and convert to int
    forth line is to be checked against c
    determine if (a-b) == c or (a-b)== -c
    print("JEDI") is both are negative
    print("SITH") is signs don't match
    print("VEIT EKKI")
'''

import sys

def main():
    print("Enter 4 lines, name, integer a, integer b, and a-b", file=sys.stderr)
    input() # input name, don't care, so I don't assign it to anything
    a = int(input())
    b = int(input())
    c = int(input())
    a_minus_b = a-b

    answer = "VEIT EKKI"
    if(a_minus_b < 0):
        if(a_minus_b == c): # both negative, must be a JEDI
            answer = "JEDI"
        else: # one must be positive, so a SITH is involved
            answer = "SITH"
    
    print(answer)




if __name__ == "__main__":
    main()