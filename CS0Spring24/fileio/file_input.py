import pathlib
import random

my_path = pathlib.Path(__file__).parent.resolve()

with open(f'{my_path}/words.txt', 'r') as fr:
    words = fr.readlines()
    for i in range(len(words)):
        words[i] = words[i].strip()
    word = random.choice(words)
    print(word)

with open(f'{my_path}/out.txt', 'w') as fo:
    fo.write("The third word is '" + words[2]+"'")

print(words)
print(' '.join(words))
