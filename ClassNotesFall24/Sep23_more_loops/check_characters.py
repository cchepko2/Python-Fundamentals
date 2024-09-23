import string

print(string.hexdigits)
print(string.punctuation)
print(string.ascii_lowercase)

print('a' in string.punctuation)

phrase = "What does the fox say?"
print('a' in phrase)

for character in phrase:
    if character not in string.punctuation and character in string.ascii_lowercase or character == ' ':
        print(character, end = '')
print() #print a new line after last line