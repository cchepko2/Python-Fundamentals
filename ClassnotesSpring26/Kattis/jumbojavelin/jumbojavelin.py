'''
Corin Chepko
3/8/26
Program: Kattis problem - https://open.kattis.com/problems/jumbojavelin
Algorithm:
    input N, convert to int
    sum = 0
    for N:
        input number, convert to int
        add number to sum
    compute sum-(n-1)
'''

import sys


def main():
    print("Enter number of pieces: ", file=sys.stderr)
    number_pieces = int(input())

    summation = 0
    for i in range(number_pieces):
        number = int(input())
        summation += number
    
    total = summation - (number_pieces-1)
    print(total)
    
    '''numbers = []
    for i in range(number_pieces):
        numbers.append(int(input()))

    summation = solution(numbers)'''

    

def solution(numbers, num_pieces):
    return sum(numbers) - (num_pieces-1)


if __name__ == '__main__':
    main()