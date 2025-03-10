'''
Script to capitalize all 'r's in phrase
'''

answer = ""

phrase = "little red riding hood"
phrase = phrase

list_chars = []

# string traversal using index and range function
'''for i in range(len(phrase)):
    print(phrase[i], end=' ')'''

print()

# string traversal using range-based-loop
for character in phrase:
    #print(character, end = ' ')
    if( character == 'r'):
        answer += 'R'
        list_chars += 'R'
    else:
        answer += character
        list_chars += character

print()
print(answer)
print(list_chars)
print(",".join(list_chars))

