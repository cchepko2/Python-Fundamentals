'''
Corin Chepko
3/2/26
Program - Kattis Problem: Sith - https://open.kattis.com/problems/sith
Algorithm:
    input name
    input a -> convert to int
    input b -> convert to int
    input reported a-b -> convert to int
    compute a-b
    check if a-b is negative
    if negative:
        check to a-b == abs(a-b)
        if True:
            SITH
        else:
            JEDI
    else:
        VEIT EKKI
'''

import sys

def main():
    name=input()
    a = int(input())
    b = int(input())
    a_minus_b = int(input())

    ans = solution(a, b, a_minus_b)

    print(ans)

def solution(a, b, a_minus_b):
    if a-b < 0:
        if a-b != a_minus_b:
            ans = "SITH"
        else:
            ans = "JEDI"
    else:
        ans = "VEIT EKKI"

    return ans

def test():
    a = 5
    b = 2
    a_minus_b = 3
    assert(solution(a, b, a_minus_b) == "VEIT EKKI")

    a = 2
    b = 5
    a_minus_b = -3
    assert(solution(a, b, a_minus_b) == "JEDI")

    a = 2
    b = 5
    a_minus_b = 3
    assert(solution(a, b, a_minus_b) == "SITH")

    print("All tess passed!", file=sys.stderr)

if __name__ == "__main__":
    test()
    main()