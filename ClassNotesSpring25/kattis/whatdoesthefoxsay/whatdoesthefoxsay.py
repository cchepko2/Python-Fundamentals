'''
Corin Chepko
3/31/25
Kattis Problem - https://open.kattis.com/problems/whatdoesthefoxsay
Algorithm Steps:
    Collect input:
        input number test case
        for each test case:
            input list of sounds
            input lines of known sounds
            when line is "What does the fox say", compute what the fox said
'''

import sys
from typing import List

def solution(sounds: List, known_sounds: List):
    for sound in known_sounds:
        while(True):
            try:
                sounds.remove(sound)
            except ValueError:
                break
    
    fox_said = ' '.join(sounds)      

    return fox_said

def test():
    swamp_sounds = ["crazy", "meow", "ribbit", "blub", "pow!"]
    known_sounds = ["meow", "ribbit", "blub"]
    assert( solution(swamp_sounds, known_sounds) == "crazy pow!")
    print("All tests passed!", file=sys.stderr)

def main():
    num_tests = int(input())
    for i in range(num_tests):
        sounds = input().split()
        known_sounds = []
        while(True):
            line = input()
            if line == "what does the fox say?":
                break
            else:
                # append the third word from the line into the list
                # of known sounds
                known_sounds.append(line.split()[2])

        fox_said = solution(sounds, known_sounds)
        print(f"{sounds=}", file=sys.stderr)
        print(f"{known_sounds=}", file=sys.stderr)
        print(fox_said)

if __name__ == '__main__':
    main()
    test()