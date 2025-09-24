'''
Corin Chepko
9/24/25
Program: Kattis problem: https://open.kattis.com/problems/sith
Algorithm:
    collect name, we dont need this, 
        but we do need to collect it for the input stream
    collect first number and convert to int
    collect second number and convert to int
    collect third number and convert to int

    check if first-second is negative:
        if(third == pos)
            ans = "SITH"
        elif(third == neg)
            ans = "JEDI"
    else:
        ans = "VIET EKKI"
'''
import sys

def main():
    
    first, second, third = read_data()

    if(first-second < 0):
        if(third < 0):
            ans = "JEDI"
        else:
            ans = "SITH"
    else:
        ans = "VEIT EKKI"

    print(ans)

def read_data():
    print("Name: ", file=sys.stderr)
    input()  # Collect the name, we don't need to keep it
    first = int(input())
    second = int(input())
    third = int(input())
    return first, second, third

if __name__ == '__main__':
    main()