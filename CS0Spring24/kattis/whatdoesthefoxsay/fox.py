'''
Corin Chepko
3/15/24
Kattis Problem: What does the fox say 
https://open.kattis.com/problems/whatdoesthefoxsay
Algorithm Steps (for one test case):
    read in phrase of sounds
    read line while line != "what does the fox say?"
    split line
    last, or third word is sound - add this to list of known sounds
    remove all instances of sound from phrase
    print(modified phrase)
'''

import sys

def whatdoesfoxsay(phrase: list, sounds: list)-> str:
    for word in sounds:
        while(word in phrase):
            phrase.remove(word)

    return ' '.join(phrase)

def collect_input()->tuple:
    phrase = list(input().split())

    line=input()
    sounds = []
    while(line != "what does the fox say?"):
        line = line.split()
        sounds.append(line[-1]) # add sound to list of known sounds
        line=input()
    
    return phrase, sounds

def test():
    phrase = ["toot", "boop", "caw"]
    sounds = ["toot", "boop"]
    assert whatdoesfoxsay(phrase, sounds) == "caw"
    print("All tests passed!", file=sys.stderr)

def main():
    num_tests = int(input())
    for _ in range(num_tests):
        phrase, sounds = collect_input()
        print(whatdoesfoxsay(phrase, sounds))

if __name__ == "__main__":
    test()
    main()