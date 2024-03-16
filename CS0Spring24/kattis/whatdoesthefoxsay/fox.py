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

phrase = list(input().split())

line=input()
sounds = []
while(line != "what does the fox say?"):
    line = line.split()
    sounds.append(line[-1]) # add sound to list of known sounds
    line=input()

print(sounds)
for word in sounds:
    while(word in phrase):
        phrase.remove(word)

print(' '.join(phrase))