import string

phrase = "What does the fox say?"

print(phrase[11])
print(len(phrase))

num_letters = len(phrase)
for i in range(num_letters):
    print(phrase[i], end=' ')

print()

i = 0
for ch in phrase:
    print(ch, end='_')
    i+=1
print()

names = ["Corin","Sam","Sarag","Alice"]

for name in names:
    print(name)

