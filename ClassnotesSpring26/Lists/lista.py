import string

print(string.ascii_letters)

list_Alpha = list(string.ascii_letters)

print(list_Alpha)

for char in string.ascii_letters:
    print(char, end=' ')
print()

for char in list_Alpha:
    print(char, end=' ')
print()

alphabet = ','.join(list_Alpha)
print(alphabet)

