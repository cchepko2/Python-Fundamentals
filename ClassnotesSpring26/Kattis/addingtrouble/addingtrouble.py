'''
Corin Chepko
2/24/26
Program: Kattis Problem - https://open.kattis.com/problems/addingtrouble
Algorithm:
    input integers a, b, and c separated by a space
    convert to int
    check if a+b == c
    if equal
        print "correct!"
    else:
        print "wrong!"
'''

import sys

def main():
    a, b, c = map(int, input().split())

    answer = solution(a, b, c)

    print(answer)

def solution(a, b, c):
    if(a + b == c):
        answer = "correct!"
    else:
        answer = "wrong!"

    return answer

def test():
    assert(solution(1, 1, 2) == "correct!")
    assert(solution(1, 1, 1) == "wrong!")
    assert(solution(10,0, 10) == "correct!")
    print("All test passed!", file=sys.stderr)

if __name__ == "__main__":
    test()
    main()