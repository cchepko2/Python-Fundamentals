message = "K number of characters."
i=0

for ch in message:
    print(f'{ch}', end=' ')
    print(f'{i}', end=' ')
    i+=1

# enumeration
for index, value in enumerate(message):
    print(f"Index: {index}, Value: {value}")

# find first vowel in message
i=0
for ch in message:
    if(ch.upper() == 'A' or ch.upper() == 'E' or ch.upper() == 'I' or ch.upper() == 'O' or ch.upper() == 'U'):
        print("First vowel is:", ch, " At index:", i)
        break
    i+=1
