'''
Programmer: Corin Chepko
Date: 10/29/25
Program: Kattis Problem - What Does the Fox Say: https://open.kattis.com/problems/whatdoesthefoxsay
Algorithm:
    Input number of test cases
    for each test:
        input line of recorded sounds
        input lines of animal sounds until line="what does the fox say?"
        remove animal sounds from recorded sounds
        print remaining recorded sounds
'''

import sys
from typing import List

def main():
    num_tests = int(input())
    for __ in range(num_tests):
        
        recorded_sounds = input().split()

        #print(f"{recorded_sounds=}")

        line = input()
        sounds = []
        while(True):
            sound_lst = line.split()
            sounds.append(sound_lst[2]) # Add the third word, which is the sound to the sounds list
            
            line = input()
            if(line == "what does the fox say?"):
                break

        #print(f"{sounds=}")

        fox_says = solution(recorded_sounds, sounds)
        print(fox_says)

def solution(recorded_sounds: List[str], animal_sounds: List[str]) -> str:
    fox_says = []
    for sound in recorded_sounds:
        if sound not in animal_sounds:
            fox_says.append(sound)
    fox_says = ' '.join(fox_says)
    return fox_says

def test():
    animal_sounds = ['toot', 'blub']
    recorded = ['pow', 'cry', 'toot', 'pa', 'blub', 'blub']
    assert solution(recorded, animal_sounds) == "pow cry pa"

    print("All tests passed!", file=sys.stderr)

if __name__ == '__main__':
    test()
    main()