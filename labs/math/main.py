# create empty dictionary
translation = {}

list_vals = ["sheep", "spanish"]

# add some keys and values
translation["pig"] = "igpay"
translation["latin"] = "atinlay"
translation["sheepsay"] = list_vals

# shallow copy, the list inside is shallow 
# copied, so a change in the list affects 
# both dictionarys
new_translation = translation.copy()

list_vals[0] = "Lamb"

print(translation)
print()

print(new_translation)

# .keys() method returns a list of the keys in the dictionary
print(translation.keys())

phrase = "I like pig latin sheepsay"
phrase = phrase.split()

print(phrase)
print()

for word in phrase:
    if word in translation.keys():
        print(translation[word])
    else:
        print(word)


#print(translation["Goat"])