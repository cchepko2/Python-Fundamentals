# loops within loops
# find the first character that is repeated

word = input("Enter a word: ")

# Lets print the first character in word
print(f"{word[0]=}")
# Lets print the 3rd character in word
print(f"{word[2]=}")
# Lets print the last character in word
print(f"{word[len(word)-1]=}")
# Lets print the last character in word
print(f"{word[-1]=}")
# Lets print the 2nd to last character in word
print(f"{word[-2]=}")
# If index is bigger then len(word), we will get an "index out of range" error
# print(f"{word[-20]=}")


# first, let's just print each letter in the word
for character in word:
    print(character)

print()
# another way, using a range loop, where i is the index of the character
for i in range(len(word)):
    print(i, word[i])

# after this loop i=len(word)-1
# short way to make something happen x amount of times, without an index variable
i=0
x=2
for __ in range(x):
    print(word[i])

# floating point arithmatic can be weird
#print(2.3 + 5.6)

print()
# Onto the solution
found = False
for i in range(len(word)-1):
    char_a = word[i]
    print(f"{char_a=}", end = '\t')
    for j in range(i+1,len(word)):
        char_b = word[j]
        print(f"{char_b=}", end='')

        if(char_a == char_b): # we've found matching characters
            print(f"The character {char_a} is repeated indexes {i} and {j}.")
            # Victory! We found a repeated character, how do we get out of the loops?
            found = True
            break # Found a match, break the inner loop

    if(found): # If a we found a match, break the outter loop
        break
    print()

for i in range(len(word)):
    char_a = word[i]
    j = word.find(char_a, i+1)
    if( j != -1):
        print(f"{char_a} is repeated at indexex {i} and {j}")
    

    
    

