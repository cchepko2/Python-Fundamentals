import string

print(f"{string.whitespace=}")
print(f"{string.punctuation=}")
print(f"{string.ascii_letters=}")
print(f"{string.ascii_lowercase=}")
print(f"{string.digits=}")

phrase = 'Well, "I never did!", said Alice'
phrase = 'no puntuation'

for punct in string.punctuation:
    if punct in phrase:
        print("You have punctuation!")
        break
# Made it through the loop without breaking
else:
    print("no punctuation you heathen")

def hasSymbols(phrase):
    symbols = '!@#$%'
    for c in symbols:
        if c in phrase:
            return True
    return False

