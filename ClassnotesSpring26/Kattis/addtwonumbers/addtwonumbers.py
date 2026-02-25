'''
Kattis: addtwonumbers
'''


import sys

def main():
    a, b = input().split()
    a = int(a)
    b = int(b)

    ans = solution(a, b)

    print(ans)

def solution(n1, n2):
    return n1+n2

def test():
    assert solution(1, 2) == 3.0
    print("All tests passed!", file=sys.stderr)

test()
main()