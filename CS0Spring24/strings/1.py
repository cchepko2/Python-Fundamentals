full_name = "Corin Chepko"

print(full_name.split())

first, last = full_name.split()

last_first = last + ', ' + first  # All these statements do the same thing
last_first = f"{last}, {first}" # All these statements do the same thing
last_first = "{}, {}".format(last, first)   # All these statements do the same thing
last_first = "{0}, {1}".format(last, first) # All these statements do the same thing

print(last_first)

for character in last_first:    #both these loops do the same thing
    print(character, end = ' ')
print()
for i in range(len(last_first)): #both these loops do the same thing
    print(last_first[i], end = ' ')

pirates_phrase = "The pirates of the Caribbean"

index = pirates_phrase.lower().find("the")

print('\nIndex of "the" is at ', index)

index = pirates_phrase.lower().find("the", index+1)

print('\nIndex of 2md "the" is at ', index)
print(pirates_phrase[15])


print("\n\n\n")

pirates_phrase = "The pirates of the Caribbean"
pirates_phrase = pirates_phrase.lower() # convert to lowercase
index = pirates_phrase.find("the")

print('\nIndex of "the" is at ', index)

index = pirates_phrase.rfind("the")
print('\nIndex of 2md "the" is at ', index)