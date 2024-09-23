'''
Author: Corin Chepko
Date: 9/23/24
Kattis Problem: FizzBuzz - https://open.kattis.com/problems/fizzbuzz
Algorithm:
    input x, y, n separated by spaces
    convert to ints
    for each number in range(n):
        if number%x == 0:
            print("Fizz")
        elif number%y == 0:
            print("Buzz")
        elif number%x == 0 and number%y == 0:
            print("FizzBuzz")
        else:
        print(number)       
'''

def solution(x, y, n):
    # incorrect order so far...
    for number in range(1, n+1):
        if(number%x == 0 and number%y == 0):
            print("FizzBuzz")
        elif(number%y == 0):
            print("Buzz")
        elif(number%x == 0):
            print("Fizz")
        else:
            print(number)

def main():
    x,y,n = input().split()
    x = int(x)
    y = int(y)
    n = int(n)

    solution(x,y,n)

    

if __name__ == "__main__":
    main()