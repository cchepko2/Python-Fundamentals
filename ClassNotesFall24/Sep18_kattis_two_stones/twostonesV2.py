'''
Author: Corin Chepko
Date: 9/19/24
Program Info: kattis problem - https://open.kattis.com/problems/twostones
Algorithm Steps:
    input a number
    convert to int
    if( even ):
        print("Bob")
    else:
        print("Alice")
'''

def main():

    stones = int(input())
    answer = solution(stones)
    #print(solution(stones))
    print(answer)


def solution(stones: int) -> str:
    if(stones%2 == 0):
        answer = "Bob"
    else:
        answer = "Alice"

    return answer

if __name__ == "__main__":
    main()