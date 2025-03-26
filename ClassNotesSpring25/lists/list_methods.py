import string
phrase = "Spring is coming!"

# Make a list of each character in string
phrase_characters = list(phrase)
print(phrase_characters)

# Make a list of each word in string
phrase_words = phrase.split()
print(phrase_words)

# sort methods will try to sort list in ascending order
# sort method operates over the list itself, the original list is lost
phrase_words.sort()
print(phrase_words)
phrase_words.sort(reverse=True)
print(phrase_words)

phrase_words.append("soon...")
print(phrase_words)

print( phrase_words.count('Spring') )

phrase_words.insert(0, "Yoda says")
print(phrase_words)

removed_word = phrase_words.pop(-1)
print(removed_word)
print(phrase_words)