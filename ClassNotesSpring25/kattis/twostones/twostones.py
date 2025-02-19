'''
Corin Chepko
2/19/25
Program info: Kattis problem - https://open.kattis.com/problems/twostones
Algorithm Steps:
    input number
    convert to int
    determine if number is even or oddd
    print 'Bob' for even, 'Alice' for odd
'''

import sys

def solution(num):
    if(num%2 == 0):  # if num is even
        even_odd = 'Bob'
    else:
        even_odd = 'Alice'
    return even_odd

def test():
    assert(solution(4) == 'Bob')
    assert(solution(3) == 'Alice')
    assert(solution(0) == 'Bob')
    print("All test cases passed!", file=sys.stderr)

def main():
    test() # Test my solution for a few test cases

    print("Enter a number: ", file=sys.stderr)

    num = int(input())

    even_odd = solution(num)

    print(even_odd)

# If I'm the main program and not an import, run me
if __name__ == "__main__":
    main()