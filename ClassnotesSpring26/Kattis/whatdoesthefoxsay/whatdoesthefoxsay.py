'''
Corin Chepko
3/30/26
Kattis Problem - What does the fox say - https://open.kattis.com/problems/whatdoesthefoxsay
Algorithm Steps:
    input number of test cases
    for each test:
        input line of recorded animal sounds and split() into a list
        input lines of known sounds until line="what does the fox say"
            add third word from the split() of the line into list of known_sounds
        remove known sounds the recorded sounds
        join recorded sounds into solution
'''

import sys
from typing import List

def main():
    num_tests = int(input())

    for i in range(num_tests):

        recorded_sounds = input().split()
        
        known_sounds = []
        
        while(True):
            line = input()
            if(line == "what does the fox say?"):
                    break
            
            # append third word onto the know_sounds list
            line_split = line.split()
            known_sounds.append(line_split[2])

        answer = solution(recorded_sounds, known_sounds)
        print(answer)

def solution(recorded_sounds: List[str], known_sounds: List[str]) -> str:
    
    answer = []
    for sound in recorded_sounds:
        if sound not in known_sounds:
                answer.append(sound)

    # join the fox sounds list into a string
    return " ".join(answer)

def test():
      recorded = ["toot", "woof", "bang"]
      known = ["woof"]
      assert solution(recorded, known) == "toot bang"
      print("All test passed!", file=sys.stderr)


if __name__ == '__main__':
        test()
        main()