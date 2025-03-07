'''
Programmer: Corin Chepko
Date: 3/5/25
Program: Kattis Problem - Fizzbuzz - https://open.kattis.com/problems/fizzbuzz
Algorithm Steps:
    input 3 integers separted by spaces, x, y, N
    count from number = 1 and up to and including N
    if(number % x == 0)  # if divisible by x
        print("Fizz")
    elif(number % y == 0)  # if divisible by y
        print("Buzz")
    elif(both)
        print("FizzBuzz")
    else
        print the number
'''

import sys

def main():
    print("Enter 3 numbers separated by a space, x, y, and N: ", file=sys.stderr)
    x ,y, N = input().split()
    x = int(x)
    y = int(y)
    N = int(N)

    print(f"{x=}, {y=}, {N=}", file=sys.stderr)

    # Lets count to N
    '''i = 1
    while(i<=N):
        print(i)
        i+=1
    '''
    # Lets count to N using a for loop
    for i in range(1,N+1):
        return_string = fizzbuzz(x, y, i)
        print(return_string)

def test():
    assert(fizzbuzz(2, 3, 6) == "FizzBuzz")
    assert(fizzbuzz(2, 3, 2) == "Fizz")
    assert(fizzbuzz(2, 3, 3) == "Buzz")
    assert(fizzbuzz(2, 3, 5) == "5")
    print("All tests passed!", file=sys.stderr)


def fizzbuzz(x:int, y:int, i:int) -> str:
    '''
    Input x, y, and i (current_number),
    output current_number, "Fizz" if divisible by x,
    "Buzz" if divible by y, "FizzBuzz" if divisible by x and y.
    '''
    if((i%x == 0) and (i%y == 0)):  # if divisible by x
        #print("FizzBuzz")
        return "FizzBuzz"
    elif(i % y == 0):  # if divisible by y
        #print("Buzz")
        return "Buzz"
    elif(i % x == 0):
        #print("Fizz")
        return "Fizz"
    else:
        #print(i)
        return str(i)

if __name__ == "__main__":
    test()
    main()

