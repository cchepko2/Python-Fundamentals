# loops within loops
# find the first character that is repeated

word = input("Enter a word: ")

# first, let's just print each letter in the word
for character in word:
    print(character)

# another way, using a range loop, where i is the index of the character
for i in range(len(word)):
    print(word[i])

# floating point arithmatic can be wierd
#print(2.3 + 5.6)

