last_first = "A bi2g strin3g with occasion5al interup7ting numb3ers"

print(last_first)

for character in last_first:    #both these loops do the same thing
    print(character, end = ' ')

print(character)

print()
for i in range(len(last_first)): #both these loops do the same thing
    print(last_first[i], end = ' ')

print()

for c in last_first:
    if(not c.isdigit()):
        print(c, end='')

print()