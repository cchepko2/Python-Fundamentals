import sys

print("Enter a message: ", file=sys.stderr)
message = input()

translated = ""
vowels = 'aeiouy'
for word in message.split():
    if word[0] in vowels:
        translated += word + 'yay' + ' '
    else:
        index = 0
        for c in word:
            if c in vowels:
                new_word = word[index:] + word[0:index] + 'ay'
            index+=1

        translated += new_word + ' '

print(translated)
